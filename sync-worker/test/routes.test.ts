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
