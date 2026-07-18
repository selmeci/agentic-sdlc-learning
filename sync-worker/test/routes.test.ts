import { describe, it, expect } from "vitest";
import * as Y from "yjs";
import app from "../src/index";

function makeEnv() {
  const m = new Map<string, Uint8Array>();
  return {
    SYNC_KV: {
      get: async (k: string, type?: string) => {
        if (!m.has(k)) return null;
        const v = m.get(k)!;
        if (type === "arrayBuffer") return v.buffer.slice(v.byteOffset, v.byteOffset + v.byteLength);
        return v;
      },
      put: async (k: string, v: unknown) => {
        m.set(k, v instanceof Uint8Array ? v : new Uint8Array(v as ArrayBuffer));
      },
    },
    RATE_LIMITER: { limit: async () => ({ success: true }) },
    _map: m,
  } as any;
}
function update(fn: (d: Y.Doc) => void): Uint8Array {
  const d = new Y.Doc();
  fn(d);
  return Y.encodeStateAsUpdate(d);
}
function progressOf(bytes: ArrayBuffer): Record<string, unknown> {
  const d = new Y.Doc();
  Y.applyUpdate(d, new Uint8Array(bytes));
  return d.getMap("progress").toJSON();
}

describe("routes", () => {
  it("POST /new returns a 4-char code header and stores state", async () => {
    const env = makeEnv();
    const res = await app.request("/new", { method: "POST", body: update((d) => d.getMap("progress").set("eng-1", "done")) }, env);
    expect(res.status).toBe(200);
    const code = res.headers.get("X-Sync-Code");
    expect(code).toMatch(/^[a-z0-9]{4}$/);
    expect(progressOf(await res.arrayBuffer())).toEqual({ "eng-1": "done" });
    expect(env._map.has("r:" + code)).toBe(true);
  });

  it("GET /r/:code returns stored state, 404 when unknown", async () => {
    const env = makeEnv();
    const created = await app.request("/new", { method: "POST", body: update(() => {}) }, env);
    const code = created.headers.get("X-Sync-Code")!;
    expect((await app.request("/r/" + code, undefined, env)).status).toBe(200);
    expect((await app.request("/r/zzzz", undefined, env)).status).toBe(404);
  });

  it("POST /r/:code merges the update into the stored doc", async () => {
    const env = makeEnv();
    const created = await app.request("/new", { method: "POST", body: update((d) => d.getMap("progress").set("a", "studying")) }, env);
    const code = created.headers.get("X-Sync-Code")!;
    const res = await app.request("/r/" + code, { method: "POST", body: update((d) => d.getMap("progress").set("b", "done")) }, env);
    expect(res.status).toBe(200);
    expect(progressOf(await res.arrayBuffer())).toEqual({ a: "studying", b: "done" });
  });

  it("POST /r/:code 404s for an unknown code (no junk records)", async () => {
    const env = makeEnv();
    const res = await app.request("/r/zzzz", { method: "POST", body: update((d) => d.getMap("progress").set("a", "done")) }, env);
    expect(res.status).toBe(404);
    expect(env._map.size).toBe(0);
  });

  it("sets permissive CORS headers", async () => {
    const env = makeEnv();
    const res = await app.request("/new", { method: "POST", body: update(() => {}) }, env);
    expect(res.headers.get("access-control-allow-origin")).toBe("*");
  });
});

function b64(u: Uint8Array): string {
  let s = "";
  for (let i = 0; i < u.length; i++) s += String.fromCharCode(u[i]);
  return btoa(s);
}
function diffOmits(reply: Uint8Array, known: Uint8Array): boolean {
  const replyClients = new Set(Y.decodeStateVector(Y.encodeStateVectorFromUpdate(reply)).keys());
  for (const id of Y.decodeStateVector(Y.encodeStateVectorFromUpdate(known)).keys()) {
    if (replyClients.has(id)) return false;
  }
  return true;
}

describe("delta wire format", () => {
  it("push with X-State-Vector replies only the missing diff", async () => {
    const env = makeEnv();
    const updA = update((d) => d.getMap("progress").set("a", "studying"));
    const created = await app.request("/new", { method: "POST", body: updA }, env);
    const code = created.headers.get("X-Sync-Code")!;
    // another device pushes b
    await app.request("/r/" + code, { method: "POST", body: update((d) => d.getMap("progress").set("b", "done")) }, env);
    // our device knows only a; it pushes with its state vector
    const client = new Y.Doc();
    Y.applyUpdate(client, updA);
    const res = await app.request("/r/" + code, {
      method: "POST",
      headers: { "X-State-Vector": b64(Y.encodeStateVector(client)) },
      body: new Uint8Array(0),
    }, env);
    expect(res.status).toBe(200);
    const reply = new Uint8Array(await res.arrayBuffer());
    expect(diffOmits(reply, updA)).toBe(true);
    Y.applyUpdate(client, reply);
    expect(client.getMap("progress").toJSON()).toEqual({ a: "studying", b: "done" });
  });

  it("push without the header keeps returning full state (old clients)", async () => {
    const env = makeEnv();
    const updA = update((d) => d.getMap("progress").set("a", "studying"));
    const created = await app.request("/new", { method: "POST", body: updA }, env);
    const code = created.headers.get("X-Sync-Code")!;
    await app.request("/r/" + code, { method: "POST", body: update((d) => d.getMap("progress").set("b", "done")) }, env);
    const res = await app.request("/r/" + code, { method: "POST", body: new Uint8Array(0) }, env);
    const client = new Y.Doc();
    Y.applyUpdate(client, new Uint8Array(await res.arrayBuffer()));
    expect(client.getMap("progress").toJSON()).toEqual({ a: "studying", b: "done" });
  });

  it("push with a garbage header falls back to full state", async () => {
    const env = makeEnv();
    const created = await app.request("/new", { method: "POST", body: update((d) => d.getMap("progress").set("a", "done")) }, env);
    const code = created.headers.get("X-Sync-Code")!;
    for (const bad of ["!!!not-base64!!!", b64(new Uint8Array([1, 2, 3]))]) {
      const res = await app.request("/r/" + code, {
        method: "POST",
        headers: { "X-State-Vector": bad },
        body: new Uint8Array(0),
      }, env);
      expect(res.status).toBe(200);
      expect(progressOf(await res.arrayBuffer())).toEqual({ a: "done" });
    }
  });

  it("stores the full merged state when a pusher sends X-State-Vector", async () => {
    const env = makeEnv();
    const updA = update((d) => d.getMap("progress").set("a", "studying"));
    const created = await app.request("/new", { method: "POST", body: updA }, env);
    const code = created.headers.get("X-Sync-Code")!;
    // another device that already knows A pushes update B with its state vector
    const pusher = new Y.Doc();
    Y.applyUpdate(pusher, updA);
    const updB = update((d) => d.getMap("progress").set("b", "done"));
    const pushRes = await app.request("/r/" + code, {
      method: "POST",
      headers: { "X-State-Vector": b64(Y.encodeStateVector(pusher)) },
      body: updB,
    }, env);
    expect(pushRes.status).toBe(200);
    // a fresh device pulls with an empty state vector and must receive the full merged state
    const res = await app.request("/r/" + code + "/sync", { method: "POST", body: new Uint8Array(0) }, env);
    expect(res.status).toBe(200);
    expect(progressOf(await res.arrayBuffer())).toEqual({ a: "studying", b: "done" });
  });

  it("POST /r/:code/sync returns the diff the requester is missing", async () => {
    const env = makeEnv();
    const updA = update((d) => d.getMap("progress").set("a", "studying"));
    const created = await app.request("/new", { method: "POST", body: updA }, env);
    const code = created.headers.get("X-Sync-Code")!;
    await app.request("/r/" + code, { method: "POST", body: update((d) => d.getMap("progress").set("b", "done")) }, env);
    const client = new Y.Doc();
    Y.applyUpdate(client, updA);
    const res = await app.request("/r/" + code + "/sync", { method: "POST", body: Y.encodeStateVector(client) }, env);
    expect(res.status).toBe(200);
    const reply = new Uint8Array(await res.arrayBuffer());
    expect(diffOmits(reply, updA)).toBe(true);
    Y.applyUpdate(client, reply);
    expect(client.getMap("progress").toJSON()).toEqual({ a: "studying", b: "done" });
  });

  it("POST /r/:code/sync 404s for an unknown code", async () => {
    const env = makeEnv();
    const res = await app.request("/r/zzzz/sync", { method: "POST", body: new Uint8Array(0) }, env);
    expect(res.status).toBe(404);
  });

  it("preflight allows the X-State-Vector header", async () => {
    const env = makeEnv();
    const res = await app.request("/r/ab12", {
      method: "OPTIONS",
      headers: {
        Origin: "https://example.com",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "x-state-vector",
      },
    }, env);
    expect(res.headers.get("access-control-allow-headers") || "").toContain("X-State-Vector");
  });
});
