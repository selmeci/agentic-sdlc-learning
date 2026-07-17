# Cross-device Progress Sync Implementation Plan (Yjs)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an opt-in, local-first backend sync so a reader's study progress travels between devices via a 4-character pairing code — using Yjs (a CRDT) for conflict-free merge, with no hand-rolled merge logic.

**Architecture:** A Hono Worker on Cloudflare stores each reader's state as an encoded Yjs document in KV and merges pushes server-side with `Y.applyUpdate`. The single-file workbook keeps its existing plain-JSON `localStorage` as the canonical local store (unchanged, Yjs-independent) and, only when sync is enabled, maintains a parallel Y.Doc mirrored from `state`, syncing its binary updates to the Worker.

**Tech Stack:** Cloudflare Workers, Hono.js, `hono-rate-limiter` (native Cloudflare Rate Limiting binding), Yjs (pure-JS CRDT, browser + Worker), Cloudflare KV, Vitest, pnpm; vanilla in-HTML JS (client), Python validator + in-browser visual checks.

## Global Constraints

- **Local-first, Yjs-independent.** The existing `store` backend + plain-JSON `state` under `agentic-study-v1` is the canonical local store and is NOT changed. Yjs is additive: used only for the optional sync layer. If Yjs fails to load (claude.ai CSP / offline), local save must work exactly as today.
- All local persistence (including the encoded Y.Doc and the sync code) goes through the existing single `store` backend — never raw `localStorage`/`window.storage`. (CLAUDE.md golden rule #5)
- The workbook stays a **single-file, zero-build HTML artifact**. Yjs loads from a CDN via a `<script type="module">` (same spirit as the existing `marked.min.js` at line 5380). Worker source lives in `sync-worker/`.
- Client sync JS stays inside the **last bare `<script>` block** and passes `node --check`. The Yjs module loader is a separate `<script type="module">` (attributed → not the app-parse target).
- **No new CSS class in workbook markup unless styled in `<style>` or referenced by a JS `querySelector`/`closest`/`matches`.** Reuse existing modal classes (`.e1ov`, `.panel`, `.bar`, `.body`, `.tag`, `.x`, `.kicker`, `.mono`); the only new class is `.syncchip`, which must be styled.
- **Never** change or renumber topic ids; they remain the keys inside the Yjs `progress`/`notes` maps. Topic count unchanged (validator expects 52).
- `python3 scripts/validate.py` must exit 0 after every task that touches the workbook.
- Cloudflare account id: `fb0866add4b7bc5813b01a16ce090bfc`. Use the user's logged-in `wrangler`.
- **Tooling: pnpm** (not npm). Keep the user's dependency versions in `sync-worker/package.json`; add `yjs`.
- Pairing code: 4 chars, alphabet `abcdefghijklmnopqrstuvwxyz0123456789`.
- **No custom merge.** Convergence is Yjs's `applyUpdate` on both client and Worker. Tests assert the CRDT apply-order-independence property; they do not re-implement merge rules.
- **Bindings are generated, not hand-written.** `wrangler types` produces `sync-worker/worker-configuration.d.ts` (global `Env` from `wrangler.toml` bindings); the Hono app is typed `Hono<{ Bindings: Env }>`. tsconfig uses the generated runtime types (`types: []` + include the `.d.ts`); `pnpm typecheck` regenerates first. The generated file is committed so the repo reflects the deployed config.
- Sync wire format: raw Yjs binary updates (`application/octet-stream` request/response bodies); `/new` returns the code in an `X-Sync-Code` response header. localStorage stores the encoded doc base64-encoded.
- Local keys: `agentic-study-v1` (canonical JSON, unchanged), `agentic-study-ydoc-v1` (base64 encoded Y.Doc, sync vehicle), `agentic-study-sync-v1` (`{code,lastSyncAt}`).
- Version: bump to the **next free** version (verify the current footer version first — a parallel session may have taken v1.39 for B1).

---

### Task 1: Worker scaffold + Yjs merge helper (TDD)

Scaffold `sync-worker/` and the tiny Yjs merge wrapper. The merge is `Y.applyUpdate`; the test asserts apply-order-independent convergence.

**Files:**
- Create: `sync-worker/.gitignore`
- Modify: `sync-worker/package.json` (add `yjs`; keep the user's other versions)
- Create: `sync-worker/tsconfig.json`
- Create: `sync-worker/src/sync.ts`
- Create: `sync-worker/test/sync.test.ts`
- Delete: `sync-worker/src/merge.ts`, `sync-worker/test/merge.test.ts` (superseded custom merge)

**Interfaces:**
- Produces: `mergeUpdate(stored: Uint8Array | null, incoming: Uint8Array): Uint8Array` — applies `incoming` (and `stored` if present) into a fresh `Y.Doc` and returns the encoded merged state.

- [ ] **Step 1: Remove the superseded custom-merge files**

Run: `cd sync-worker && git rm src/merge.ts test/merge.test.ts`
Expected: both files staged for deletion.

- [ ] **Step 2: Create `sync-worker/.gitignore`** (if not already present)

```
node_modules/
.wrangler/
dist/
```

- [ ] **Step 3: Ensure `sync-worker/package.json` matches this (add `yjs`; keep the existing versions)**

```json
{
  "name": "agentic-study-sync",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy",
    "cf-typegen": "wrangler types",
    "typecheck": "wrangler types && tsc --noEmit",
    "test": "vitest run"
  },
  "dependencies": {
    "hono": "^4.12.30",
    "hono-rate-limiter": "^0.5.3",
    "yjs": "^13.6.31"
  },
  "devDependencies": {
    "@cloudflare/workers-types": "^5.20260717.1",
    "typescript": "^7.0.2",
    "vitest": "^4.1.10",
    "wrangler": "^4.112.0"
  }
}
```

- [ ] **Step 4: Create `sync-worker/tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "moduleResolution": "Bundler",
    "lib": ["ES2022"],
    "types": [],
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["src", "test", "worker-configuration.d.ts"]
}
```

> Bindings are typed from the `Env` interface in `worker-configuration.d.ts`, generated by
> `wrangler types` (run in Task 2/3 and committed). `pnpm typecheck` regenerates it first.

- [ ] **Step 5: Install with pnpm**

Run: `cd sync-worker && pnpm install`
Expected: `yjs`, `hono`, etc. installed; `pnpm-lock.yaml` created/updated.

- [ ] **Step 6: Write the failing test**

Create `sync-worker/test/sync.test.ts`:

```ts
import { describe, it, expect } from "vitest";
import * as Y from "yjs";
import { mergeUpdate } from "../src/sync";

function update(fn: (d: Y.Doc) => void): Uint8Array {
  const d = new Y.Doc();
  fn(d);
  return Y.encodeStateAsUpdate(d);
}
function progressOf(bytes: Uint8Array): Record<string, unknown> {
  const d = new Y.Doc();
  Y.applyUpdate(d, bytes);
  return d.getMap("progress").toJSON();
}
function seenOf(bytes: Uint8Array): Record<string, unknown> {
  const d = new Y.Doc();
  Y.applyUpdate(d, bytes);
  return d.getMap("seen").toJSON();
}

describe("mergeUpdate", () => {
  it("round-trips a single update", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "done"));
    expect(progressOf(mergeUpdate(null, a))).toEqual({ "eng-1": "done" });
  });

  it("merges two updates and converges regardless of apply order", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "done"));
    const b = update((d) => d.getMap("progress").set("eng-2", "studying"));
    const ab = progressOf(mergeUpdate(mergeUpdate(null, a), b));
    const ba = progressOf(mergeUpdate(mergeUpdate(null, b), a));
    expect(ab).toEqual({ "eng-1": "done", "eng-2": "studying" });
    expect(ab).toEqual(ba);
  });

  it("unions grow-only seen-set keys", () => {
    const a = update((d) => d.getMap("seen").set("e1ov:0", true));
    const b = update((d) => d.getMap("seen").set("e1ov:1", true));
    expect(seenOf(mergeUpdate(mergeUpdate(null, a), b))).toEqual({ "e1ov:0": true, "e1ov:1": true });
  });

  it("treats a null/empty stored doc as a fresh doc", () => {
    const a = update((d) => d.getMap("progress").set("eng-1", "studying"));
    expect(progressOf(mergeUpdate(new Uint8Array(0), a))).toEqual({ "eng-1": "studying" });
  });
});
```

- [ ] **Step 7: Run the test to verify it fails**

Run: `cd sync-worker && pnpm test`
Expected: FAIL — `Cannot find module "../src/sync"`.

- [ ] **Step 8: Implement `sync-worker/src/sync.ts`**

```ts
import * as Y from "yjs";

// Merge an incoming Yjs update onto the stored encoded state and return the new
// encoded state. Merge is Yjs's applyUpdate — commutative, idempotent, associative.
export function mergeUpdate(stored: Uint8Array | null, incoming: Uint8Array): Uint8Array {
  const doc = new Y.Doc();
  if (stored && stored.byteLength) Y.applyUpdate(doc, stored);
  if (incoming && incoming.byteLength) Y.applyUpdate(doc, incoming);
  const out = Y.encodeStateAsUpdate(doc);
  doc.destroy();
  return out;
}
```

- [ ] **Step 9: Run the test + typecheck**

Run: `cd sync-worker && pnpm test && pnpm run typecheck`
Expected: all tests pass; typecheck clean.

- [ ] **Step 10: Commit**

```bash
git add sync-worker/.gitignore sync-worker/package.json sync-worker/pnpm-lock.yaml sync-worker/tsconfig.json sync-worker/src/sync.ts sync-worker/test/sync.test.ts
git rm --cached sync-worker/src/merge.ts sync-worker/test/merge.test.ts 2>/dev/null || true
git commit -m "feat(sync): worker scaffold + Yjs merge helper (replaces custom merge)"
```

---

### Task 2: Code gen + Hono app (Yjs binary routes, route-tested)

Add code minting and the three endpoints with server-side Yjs merge, CORS, and the global rate limiter. Route tests use `app.request()` with an in-memory fake KV (byte values) and a fake rate-limit binding.

**Files:**
- Create: `sync-worker/src/code.ts`
- Create: `sync-worker/src/index.ts`
- Create: `sync-worker/test/code.test.ts`
- Create: `sync-worker/test/routes.test.ts`
- Create: `sync-worker/wrangler.toml` (kv id filled in Task 3)

**Interfaces:**
- Consumes: `mergeUpdate` from `./sync` (Task 1).
- Produces: default-exported Hono `app`; `makeCode(len?: number): string`. Bindings `{ SYNC_KV: KVNamespace; RATE_LIMITER: { limit(o:{key:string}): Promise<{success:boolean}> } }`. KV keys `"r:"+code` hold the encoded doc bytes. `/new` returns the code in header `X-Sync-Code`; all state bodies are `application/octet-stream`.

- [ ] **Step 1: Write the failing code test**

Create `sync-worker/test/code.test.ts`:

```ts
import { describe, it, expect } from "vitest";
import { makeCode } from "../src/code";

describe("makeCode", () => {
  it("is 4 chars from the allowed alphabet by default", () => {
    for (let i = 0; i < 200; i++) expect(makeCode()).toMatch(/^[a-z0-9]{4}$/);
  });
});
```

- [ ] **Step 2: Run to verify it fails**

Run: `cd sync-worker && pnpm test -- code`
Expected: FAIL — cannot find `../src/code`.

- [ ] **Step 3: Implement `sync-worker/src/code.ts`**

```ts
const ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789";

// Slight modulo bias (256 % 36) is negligible for a low-stakes study-tool code.
export function makeCode(len = 4): string {
  const bytes = new Uint8Array(len);
  crypto.getRandomValues(bytes);
  let out = "";
  for (let i = 0; i < len; i++) out += ALPHABET[bytes[i] % ALPHABET.length];
  return out;
}
```

- [ ] **Step 4: Run to verify it passes**

Run: `cd sync-worker && pnpm test -- code`
Expected: PASS.

- [ ] **Step 5: Implement `sync-worker/src/index.ts`**

```ts
import { Hono } from "hono";
import { cors } from "hono/cors";
import { rateLimiter } from "hono-rate-limiter";
import { mergeUpdate } from "./sync";
import { makeCode } from "./code";

// Bindings from `wrangler types` (worker-configuration.d.ts, global `Env`) —
// regenerate with `pnpm cf-typegen` after wrangler.toml changes.
const app = new Hono<{ Bindings: Env }>();

app.use("*", cors({
  origin: "*",
  allowMethods: ["GET", "POST", "OPTIONS"],
  allowHeaders: ["Content-Type"],
  exposeHeaders: ["X-Sync-Code"],
  maxAge: 86400,
}));

app.use("*", rateLimiter<{ Bindings: Env }>({
  binding: (c) => c.env.RATE_LIMITER,
  keyGenerator: (c) => c.req.header("cf-connecting-ip") ?? "anon",
}));

const bin = (u: Uint8Array) =>
  new Response(u, { headers: { "Content-Type": "application/octet-stream" } });

app.post("/new", async (c) => {
  const incoming = new Uint8Array(await c.req.arrayBuffer());
  const state = mergeUpdate(null, incoming);
  let code = "";
  for (let i = 0; i < 6; i++) {
    const cand = makeCode(4);
    if (!(await c.env.SYNC_KV.get("r:" + cand))) { code = cand; break; }
  }
  if (!code) return c.json({ error: "code space exhausted" }, 500);
  await c.env.SYNC_KV.put("r:" + code, state);
  const res = bin(state);
  res.headers.set("X-Sync-Code", code);
  return res;
});

app.get("/r/:code", async (c) => {
  const code = c.req.param("code").toLowerCase();
  const stored = await c.env.SYNC_KV.get("r:" + code, "arrayBuffer");
  if (!stored) return c.json({ error: "not found" }, 404);
  return bin(new Uint8Array(stored));
});

app.post("/r/:code", async (c) => {
  const code = c.req.param("code").toLowerCase();
  const stored = await c.env.SYNC_KV.get("r:" + code, "arrayBuffer");
  if (!stored) return c.json({ error: "not found" }, 404);
  const incoming = new Uint8Array(await c.req.arrayBuffer());
  const merged = mergeUpdate(new Uint8Array(stored), incoming);
  await c.env.SYNC_KV.put("r:" + code, merged);
  return bin(merged);
});

export default app;
```

- [ ] **Step 6: Write the failing route tests**

Create `sync-worker/test/routes.test.ts`:

```ts
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
```

- [ ] **Step 7: Run tests + typecheck**

Run: `cd sync-worker && pnpm test && pnpm run typecheck`
Expected: all pass (sync + code + routes); typecheck clean.

- [ ] **Step 8: Create `sync-worker/wrangler.toml`** (`id` filled in Task 3; `namespace_id` under `[[ratelimits]]` is an arbitrary account-unique integer, not a KV id)

```toml
name = "agentic-study-sync"
main = "src/index.ts"
compatibility_date = "2026-07-01"
account_id = "fb0866add4b7bc5813b01a16ce090bfc"

[[kv_namespaces]]
binding = "SYNC_KV"
id = "REPLACE_IN_TASK_3"

[[ratelimits]]
name = "RATE_LIMITER"
namespace_id = "1001"
simple = { limit = 60, period = 60 }
```

- [ ] **Step 9: Commit**

```bash
git add sync-worker/src/code.ts sync-worker/src/index.ts sync-worker/test/code.test.ts sync-worker/test/routes.test.ts sync-worker/wrangler.toml sync-worker/pnpm-lock.yaml
git commit -m "feat(sync): hono app with server-side Yjs merge, code gen, cors, rate limit"
```

---

### Task 3: Provision on Cloudflare and deploy (inline)

Create the KV namespace, wire its id, deploy, and smoke-test the live Worker.

**Files:**
- Modify: `sync-worker/wrangler.toml` (KV `id`)

**Interfaces:**
- Produces: the deployed base URL `SYNC_URL` (`https://agentic-study-sync.<subdomain>.workers.dev`), consumed by Task 5.

- [ ] **Step 1: Confirm wrangler auth / account**

Run: `cd sync-worker && wrangler whoami`
Expected: account id `fb0866add4b7bc5813b01a16ce090bfc` present. If not, stop and ask the user to `wrangler login`.

- [ ] **Step 2: Create the KV namespace**

Run: `cd sync-worker && wrangler kv namespace create SYNC_KV`
Expected: prints an `id = "..."`. Copy it.

- [ ] **Step 3: Wire the KV id into `wrangler.toml`** — replace `REPLACE_IN_TASK_3`.

- [ ] **Step 4: Deploy**

Run: `cd sync-worker && wrangler deploy`
Expected: prints `https://agentic-study-sync.<subdomain>.workers.dev`. Record it. If `[[ratelimits]]` is rejected by this wrangler version, check the current schema in the error text (may be `[[unsafe.bindings]]` `type="ratelimit"`); adjust and redeploy. Do not fall back to a KV-based limiter without asking.

- [ ] **Step 5: Smoke-test with curl (binary bodies via a Yjs update built in node)**

```bash
cd sync-worker
BASE="https://agentic-study-sync.<subdomain>.workers.dev"   # from Step 4
# build a small Yjs update and drive the API through node (yjs is installed):
node --input-type=module -e '
import * as Y from "yjs";
const base = process.env.BASE;
const d = new Y.Doc(); d.getMap("progress").set("eng-1","done");
const up = Y.encodeStateAsUpdate(d);
const r = await fetch(base+"/new",{method:"POST",body:up});
const code = r.headers.get("X-Sync-Code");
const state = new Uint8Array(await r.arrayBuffer());
const d2 = new Y.Doc(); Y.applyUpdate(d2, state);
console.log("code=",code,"progress=",JSON.stringify(d2.getMap("progress").toJSON()));
const miss = await fetch(base+"/r/zzzz"); console.log("unknown GET status=",miss.status);
' BASE="$BASE"
```
Expected: prints a 4-char `code`, `progress={"eng-1":"done"}`, and `unknown GET status= 404`.

- [ ] **Step 6: Commit**

```bash
git add sync-worker/wrangler.toml
git commit -m "chore(sync): provision KV namespace + deploy worker"
```

---

### Task 4: Workbook — Yjs loader + Y.Doc model helpers

Add the CDN Yjs loader and the pure helpers that mirror `state`⇄`Y.Doc` and persist the encoded doc. No network and no UI yet; the canonical JSON persistence is untouched.

**Files:**
- Modify: `workbook/agentic-development-study.html` — add a `<script type="module">` Yjs loader near line 5380 (next to `marked`); add doc helpers + base64 + `stateBlob`/`refreshAll` in the app `<script>` near the `state` declaration (~line 5820).

**Interfaces:**
- Produces (in-file): `window.Y` (async, from CDN) + a `yjs-ready` event; `yReady()`; `ydoc` (a `Y.Doc` or null); `DOCKEY`; `stateBlob()`; `refreshAll()`; `b64(u)`/`unb64(s)`; `seenKeys(seenObj)`; `mirrorToDoc()` (state→doc); `materializeFromDoc()` (doc→state); `persistDoc()`; `initYjsDoc()` (async: build doc, restore from `DOCKEY`, seed from `state`).

- [ ] **Step 1: Add the Yjs CDN loader**

Immediately after the `marked` script tag (line 5380), add:

```html
<script type="module">
  try {
    const Y = await import('https://cdn.jsdelivr.net/npm/yjs@13/+esm');
    window.Y = Y;
    window.dispatchEvent(new Event('yjs-ready'));
  } catch (e) { /* sync stays disabled; local save is unaffected */ }
</script>
```

- [ ] **Step 2: Add doc helpers after the `state` declaration**

After line 5820 (`let state={...}`), insert (match the file's `var`/`function` style):

```js
/* Sync layer (Yjs). Additive: the canonical local store is still the JSON `state`
   above via `store` (agentic-study-v1). The Y.Doc exists only when sync is used. */
var ydoc=null, DOCKEY='agentic-study-ydoc-v1', applyingRemote=false;
function yReady(){return typeof window.Y!=='undefined'&&!!window.Y;}
function stateBlob(){return{progress:state.progress,notes:state.notes,seen:state.seen,highlights:state.highlights,updatedAt:state.updatedAt};}
function refreshAll(){syncFromState();updateCounts();updateNotesCount();renderTopicHls();applyFilter();}
function b64(u){var s='';for(var i=0;i<u.length;i++)s+=String.fromCharCode(u[i]);return btoa(s);}
function unb64(str){var s=atob(str),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return u;}
function seenKeys(sn){var out=[];Object.keys(sn||{}).forEach(function(ov){(sn[ov]||[]).forEach(function(i){out.push(ov+':'+i);});});return out;}
function mirrorToDoc(){
  if(!ydoc)return;
  var P=ydoc.getMap('progress'),N=ydoc.getMap('notes'),S=ydoc.getMap('seen'),H=ydoc.getMap('highlights');
  ydoc.transact(function(){
    Object.keys(state.progress).forEach(function(k){if(P.get(k)!==state.progress[k])P.set(k,state.progress[k]);});
    Object.keys(state.notes).forEach(function(k){if(N.get(k)!==state.notes[k])N.set(k,state.notes[k]);});
    seenKeys(state.seen).forEach(function(k){if(S.get(k)!==true)S.set(k,true);});
    var have={};(state.highlights||[]).forEach(function(h){if(h&&h.id){have[h.id]=1;if(JSON.stringify(H.get(h.id))!==JSON.stringify(h))H.set(h.id,h);}});
    Array.from(H.keys()).forEach(function(id){if(!have[id])H.delete(id);});
  });
}
function materializeFromDoc(){
  if(!ydoc)return;
  var P=ydoc.getMap('progress'),N=ydoc.getMap('notes'),S=ydoc.getMap('seen'),H=ydoc.getMap('highlights');
  state.progress=P.toJSON();state.notes=N.toJSON();
  var sn={};Array.from(S.keys()).forEach(function(k){var i=k.lastIndexOf(':'),ov=k.slice(0,i),n=parseInt(k.slice(i+1),10);if(!sn[ov])sn[ov]=[];sn[ov].push(n);});
  Object.keys(sn).forEach(function(ov){sn[ov].sort(function(a,b){return a-b;});});
  state.seen=sn;
  state.highlights=Array.from(H.values());
}
function persistDoc(){if(!ydoc)return;try{store.set(DOCKEY,b64(window.Y.encodeStateAsUpdate(ydoc)));}catch(e){}}
async function initYjsDoc(){
  if(ydoc||!yReady())return ydoc;
  ydoc=new window.Y.Doc();
  try{var r=await store.get(DOCKEY);if(r&&r.value)window.Y.applyUpdate(ydoc,unb64(r.value));}catch(e){}
  mirrorToDoc();persistDoc();
  return ydoc;
}
```

- [ ] **Step 3: Run the validator**

Run: `python3 scripts/validate.py`
Expected: `RESULT: all checks passed.` (The module loader is attributed, so it isn't the app-parse target; the app `<script>` still parses; no new markup classes.)

- [ ] **Step 4: Sanity-check Yjs loads (browser console)**

Open the workbook on a served origin (not strictly needed for `file://`, but jsDelivr requires http/https — use `python3 -m http.server` in the repo root and open `http://localhost:8000/workbook/agentic-development-study.html`). In the console: `yReady()` → `true` shortly after load; `await initYjsDoc(); ydoc.getMap('progress').toJSON()` reflects your current progress. Confirm normal saving still works.

- [ ] **Step 5: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(workbook): Yjs CDN loader + state<->Y.Doc mirror helpers"
```

---

### Task 5: Workbook — sync engine

Wire the network layer on top of the Y.Doc: constant, sync metadata, enable/link/unlink/push/pull, hooked into the existing `saveNow` choke-point plus load and window focus.

**Files:**
- Modify: `workbook/agentic-development-study.html` (app `<script>`)

**Interfaces:**
- Consumes: `SYNC_URL` (Task 3), the Task 4 helpers, existing `store`/`KEY`/`saveNow`/`setSave`, the init block.
- Produces (in-file): `sync={code,status,lastSyncAt}`; `setSyncStatus(st)`; `loadSyncMeta()`; `saveSyncMeta()`; `schedulePush()`; `afterRemote(bytes)`; `syncPush()`; `syncPull()`; `enableSync()→Promise<string|null>`; `linkSync(code)→Promise<{ok,err?}>`; `unlinkSync()`.

- [ ] **Step 1: Add the sync constant + state near `const KEY=`**

After line 5817 (`const KEY='agentic-study-v1';`) insert (URL from Task 3, Step 4):

```js
const SYNC_URL='https://agentic-study-sync.<subdomain>.workers.dev';
const SYNCKEY='agentic-study-sync-v1';
var sync={code:null,status:'off',lastSyncAt:null};
var pushTimer=null;
```

- [ ] **Step 2: Add the engine after `saveNow` (after line 5866)**

`setSyncStatus` targets a chip Task 6 adds; guard the element so this task stands alone.

```js
function setSyncStatus(st){sync.status=st;var el=document.getElementById('syncchip');if(!el)return;var map={off:'',syncing:'syncing…',ok:'synced · '+(sync.code||''),error:'sync error'};el.textContent=map[st]||'';el.className='syncchip'+(st==='error'?' err':'');}
async function loadSyncMeta(){try{var r=await store.get(SYNCKEY);if(r&&r.value){var m=JSON.parse(r.value);sync.code=m.code||null;sync.lastSyncAt=m.lastSyncAt||null;}}catch(e){}}
function saveSyncMeta(){try{return store.set(SYNCKEY,JSON.stringify({code:sync.code,lastSyncAt:sync.lastSyncAt}));}catch(e){return Promise.resolve(false);}}
function schedulePush(){if(!sync.code||!ydoc)return;clearTimeout(pushTimer);pushTimer=setTimeout(syncPush,900);}
function afterRemote(bytes){
  applyingRemote=true;
  try{
    window.Y.applyUpdate(ydoc,bytes);
    materializeFromDoc();persistDoc();
    store.set(KEY,JSON.stringify(stateBlob()));
    refreshAll();
  }finally{applyingRemote=false;}
}
async function syncPush(){
  if(!sync.code||!ydoc)return;
  setSyncStatus('syncing');
  try{
    mirrorToDoc();persistDoc();
    var res=await fetch(SYNC_URL+'/r/'+encodeURIComponent(sync.code),{method:'POST',body:window.Y.encodeStateAsUpdate(ydoc)});
    if(res.status===404){unlinkSync();setSave('err','sync link broken');return;}
    if(!res.ok)throw 0;
    afterRemote(new Uint8Array(await res.arrayBuffer()));
    sync.lastSyncAt=Date.now();saveSyncMeta();setSyncStatus('ok');
  }catch(e){setSyncStatus('error');}
}
async function syncPull(){
  if(!sync.code||!ydoc)return;
  setSyncStatus('syncing');
  try{
    var res=await fetch(SYNC_URL+'/r/'+encodeURIComponent(sync.code));
    if(res.status===404){unlinkSync();setSave('err','sync link broken');return;}
    if(!res.ok)throw 0;
    afterRemote(new Uint8Array(await res.arrayBuffer()));
    sync.lastSyncAt=Date.now();saveSyncMeta();setSyncStatus('ok');
  }catch(e){setSyncStatus('error');}
}
async function enableSync(){
  if(!yReady())return null;
  await initYjsDoc();
  setSyncStatus('syncing');
  try{
    mirrorToDoc();persistDoc();
    var res=await fetch(SYNC_URL+'/new',{method:'POST',body:window.Y.encodeStateAsUpdate(ydoc)});
    if(!res.ok)throw 0;
    sync.code=res.headers.get('X-Sync-Code');sync.lastSyncAt=Date.now();await saveSyncMeta();
    afterRemote(new Uint8Array(await res.arrayBuffer()));setSyncStatus('ok');return sync.code;
  }catch(e){setSyncStatus('error');return null;}
}
async function linkSync(code){
  if(!yReady())return{ok:false,err:'Sync is unavailable here.'};
  await initYjsDoc();
  code=(code||'').trim().toLowerCase();
  if(!/^[a-z0-9]{4}$/.test(code))return{ok:false,err:'A code is 4 letters/numbers.'};
  setSyncStatus('syncing');
  try{
    var res=await fetch(SYNC_URL+'/r/'+encodeURIComponent(code));
    if(res.status===404)return{ok:false,err:'No data found for that code.'};
    if(!res.ok)throw 0;
    sync.code=code;sync.lastSyncAt=Date.now();await saveSyncMeta();
    afterRemote(new Uint8Array(await res.arrayBuffer()));setSyncStatus('ok');schedulePush();return{ok:true};
  }catch(e){setSyncStatus('error');return{ok:false,err:'Network error. Try again.'};}
}
function unlinkSync(){sync.code=null;sync.lastSyncAt=null;saveSyncMeta();setSyncStatus('off');}
```

- [ ] **Step 3: Hook auto-push into `saveNow`**

In `saveNow` (line 5859-5866), after the successful `setSave('ok', …)` line, add:

```js
    if(sync.code&&!applyingRemote)schedulePush();
```

- [ ] **Step 4: Hook load + focus into init**

Read the file around the existing `loadState()` call (~line 6770-6790). After the first render, add:

```js
loadSyncMeta().then(function(){
  if(!sync.code)return;
  function go(){initYjsDoc().then(function(){setSyncStatus('ok');syncPull();});}
  if(yReady())go(); else window.addEventListener('yjs-ready',go,{once:true});
});
window.addEventListener('focus',function(){if(sync.code&&ydoc)syncPull();});
```

- [ ] **Step 5: Run the validator**

Run: `python3 scripts/validate.py`
Expected: `RESULT: all checks passed.`

- [ ] **Step 6: Verify the engine from the console (two contexts)**

Serve the repo (`python3 -m http.server`) and open the workbook in a normal and an incognito window.
1. A console: `await enableSync()` → 4-char code; mark a topic mastered; see a POST to `/r/<code>`.
2. B console: `await linkSync("<code>")` → `{ok:true}`; `location.reload()`; A's mastered topic present.
3. Change a topic in B; focus A; A picks up B's change.
4. Throttle A to offline, mark a topic → local save chip still says saved (local-first holds).

- [ ] **Step 7: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(workbook): Yjs sync engine (enable/link/unlink/push/pull)"
```

---

### Task 6: Workbook — sync modal, sidebar button, status chip

Add the user-facing UI, reusing the existing `.e1ov` modal pattern. Disable actions when Yjs isn't available. Verified visually (light + dark).

**Files:**
- Modify: `workbook/agentic-development-study.html` (CSS `<style>`, sidebar Data group ~line 475-481, header savebox ~line 453, a new `#syncov` modal before `<footer>` ~line 4680, event wiring in app `<script>` near the `verov` wiring ~line 6063).

**Interfaces:**
- Consumes: `enableSync/linkSync/unlinkSync/sync/yReady` (Task 5); the modal open/close pattern (`.e1ov.show`, `data-*open`/`data-*close`, Escape, backdrop).
- Produces (in-file): `renderSyncModal()`, `#syncov`, `#syncbtn`, `#syncchip`.

- [ ] **Step 1: Add the status-chip CSS**

Next to the `.savebox` rules (~line 45-47), add (the only new class):

```css
.syncchip{font-family:var(--mono);font-size:10.5px;color:var(--soft);margin-left:10px}
.syncchip.err{color:#B3362B}
```

- [ ] **Step 2: Add the status chip to the header** — modify line 453:

```html
    <div class="savebox" id="savebox"><span class="dot"></span><span id="savetxt">loading…</span><span class="syncchip" id="syncchip"></span></div>
```

- [ ] **Step 3: Add the sidebar button** — after line 479 (the `my notes` button):

```html
      <button id="syncbtn" type="button" data-syncopen title="Sync progress across devices with a short code">sync across devices</button>
```

- [ ] **Step 4: Add the modal before `<footer>`** (line 4680), reusing existing modal classes only:

```html
<div class="e1ov" id="syncov" role="dialog" aria-modal="true" aria-label="Sync across devices">
  <div class="panel">
    <div class="bar"><span class="tag">DEVICE SYNC</span><h3>Sync across devices</h3><button class="x" type="button" data-syncclose>✕ close</button></div>
    <div class="body" id="syncbody"><p class="kicker">Loading…</p></div>
  </div>
</div>
```

- [ ] **Step 5: Add `renderSyncModal()` + open/close wiring** near the `verov` wiring (~line 6063). Uses only existing classes (`kicker`, `mono`) plus ids.

```js
function renderSyncModal(){
  var b=document.getElementById('syncbody');if(!b)return;
  if(!yReady()){
    b.innerHTML='<p class="kicker">Device sync needs the sync engine, which could not load here (it is blocked inside the Claude preview and offline). Open the workbook on its normal web address and it will work. Your progress is still saved locally.</p>';
    return;
  }
  if(sync.code){
    var when=sync.lastSyncAt?new Date(sync.lastSyncAt).toLocaleString():'—';
    b.innerHTML='<p class="kicker">This device is synced. Enter this code on another device to pull your progress there.</p>'
      +'<p>Your code: <strong id="synccode" class="mono" style="font-size:22px;letter-spacing:3px">'+sync.code+'</strong> <button type="button" id="synccopy">copy</button></p>'
      +'<p class="kicker">Last synced: '+when+'</p>'
      +'<p><button type="button" id="syncunlink">unlink this device</button></p>'
      +'<p class="kicker">Unlinking stops sending changes; your local progress stays.</p>';
  }else{
    b.innerHTML='<p class="kicker">Sync keeps your progress and notes on a small server so you can continue on another device. No account — just a 4-character code.</p>'
      +'<p><button type="button" id="syncenable">Enable sync &amp; get my code</button></p>'
      +'<p class="kicker">Already have a code from another device?</p>'
      +'<p><input id="synccodein" type="text" maxlength="4" placeholder="abcd" autocomplete="off" style="font-family:var(--mono);letter-spacing:3px;text-transform:lowercase"> <button type="button" id="synclink">link this device</button></p>'
      +'<p class="kicker" id="syncmsg"></p>';
  }
}
var syncov=document.getElementById('syncov');
if(syncov){
  document.addEventListener('click',function(e){
    if(e.target.closest('[data-syncopen]')){renderSyncModal();syncov.classList.add('show');document.body.style.overflow='hidden';syncov.querySelector('.panel').scrollTop=0;return;}
    if(e.target.closest('[data-syncclose]')||e.target===syncov){syncov.classList.remove('show');document.body.style.overflow='';return;}
    if(e.target.id==='syncenable'){e.target.disabled=true;enableSync().then(function(c){renderSyncModal();if(!c){var m=document.getElementById('syncmsg');if(m)m.textContent='Could not reach the sync server. Try again.';}});return;}
    if(e.target.id==='synclink'){var inp=document.getElementById('synccodein'),msg=document.getElementById('syncmsg');if(msg)msg.textContent='linking…';linkSync(inp?inp.value:'').then(function(r){if(r.ok){renderSyncModal();}else if(msg){msg.textContent=r.err;}});return;}
    if(e.target.id==='syncunlink'){unlinkSync();renderSyncModal();return;}
    if(e.target.id==='synccopy'){var code=sync.code||'';if(navigator.clipboard){navigator.clipboard.writeText(code);}e.target.textContent='copied';setTimeout(function(){e.target.textContent='copy';},1200);return;}
  },true);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&syncov.classList.contains('show')){syncov.classList.remove('show');document.body.style.overflow='';}});
}
```

- [ ] **Step 6: Run the validator**

Run: `python3 scripts/validate.py`
Expected: `RESULT: all checks passed.` If it flags a class "used but never styled/referenced", only `.syncchip` should be new — add its rule.

- [ ] **Step 7: Verify the full flow in-browser (visual, light + dark)**

Serve the repo; two independent contexts:
1. A: sidebar → `sync across devices` → `Enable sync & get my code` → code shown; `copy` works.
2. B: open modal → paste code → `link this device` → flips to linked view; B shows A's progress.
3. Change on each side → converge on focus; header chip reads `synced · <code>`.
4. Invalid code → "No data found for that code."; bad format → "A code is 4 letters/numbers."
5. Dark mode: reopen modal; code/buttons/chip legible.
Screenshot the modal (linked + unlinked). Prefer chrome-devtools-mcp hit-testing to confirm the chip/buttons are not occluded.

- [ ] **Step 8: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(workbook): device-sync modal, sidebar button, status chip"
```

---

### Task 7: Version bump, changelog, architecture note, finish

**Files:**
- Modify: `workbook/agentic-development-study.html` (`#verov` first `.vitem` ~line 2106; footer version line ~line 4681)
- Modify: `docs/CHANGELOG.md`, `docs/ARCHITECTURE.md`

- [ ] **Step 1: Determine the next free version**

Run: `grep -n "<b>v1\." workbook/agentic-development-study.html | head -1` and read the first `.vitem` version in `#verov`.
Pick the next unused version (if the footer already reads v1.39 from B1, use **v1.40**; otherwise v1.39). Use that number `vNEXT` and date `2026-07-17` throughout this task.

- [ ] **Step 2: Prepend a `.vitem` to `#verov`** (immediately after line 2105, before the current top item)

```html
      <div class="vitem"><span class="vv">vNEXT</span><span class="vd">2026-07-17</span><p><strong>NEW — cross-device sync.</strong> Progress and notes were device-local; you can now opt in to sync them across devices with no account. From the sidebar <span class="mono">Data → sync across devices</span>, "Enable sync" uploads your current state and returns a random <strong>4-character code</strong>; every change from then on syncs automatically. On another device, enter the code to pull and merge that state in. Merging is handled by <strong>Yjs</strong>, a conflict-free replicated data type (CRDT), on both the browser and a small Cloudflare Worker — so concurrent edits on two devices reconcile correctly with no data loss and no custom merge logic. <strong>Local storage stays primary</strong>: the sync engine loads from a CDN and is best-effort; if it is blocked (e.g. inside the Claude preview) or offline, saving still works exactly as before, and the header shows a <span class="mono">synced · CODE</span> / <span class="mono">sync error</span> status. Rate-limited server-side. No topic-id or content changes.</p></div>
```

- [ ] **Step 3: Update the footer version line** (~line 4681) to `<b>vNEXT</b> · 2026-07-17 · …` (keep the rest of the line identical).

- [ ] **Step 4: Mirror to `docs/CHANGELOG.md`** — read the top, prepend a `vNEXT` entry in the existing format.

- [ ] **Step 5: Add a "Sync layer" section to `docs/ARCHITECTURE.md`** — read it, then add: the local-first invariant (JSON `store` never depends on network/Yjs); the additive Y.Doc and its schema (progress/notes maps, seen grow-only set, highlights-by-id map); the three local keys; the Hono+KV Worker with server-side `Y.applyUpdate`; Yjs chosen over Automerge/Loro for being pure-JS and tiny.

- [ ] **Step 6: Final validation**

Run: `python3 scripts/validate.py` → `RESULT: all checks passed.`
Run: `cd sync-worker && pnpm test && pnpm run typecheck` → all pass.

- [ ] **Step 7: Commit**

```bash
git add workbook/agentic-development-study.html docs/CHANGELOG.md docs/ARCHITECTURE.md
git commit -m "docs(sync): vNEXT — version bump, changelog, architecture note"
```

- [ ] **Step 8: Finish the branch**

Use the superpowers:finishing-a-development-branch skill. Summarize what shipped and the live Worker URL.

---

## Notes for the implementer

- **Yjs everywhere = no custom merge.** Do not add per-field merge logic in the Worker or the workbook. If a merge question arises, the answer is a Yjs map/set operation.
- **Local-first is sacred.** The JSON `store` path must never depend on `window.Y`. Guard every Yjs call behind `yReady()`/`ydoc`.
- **claude.ai sandbox:** the CDN Yjs import and the Worker fetch may both be blocked by CSP there. Sync then shows disabled/`sync error`; local saving is unaffected. Primary target is GitHub Pages / local served file.
- **Don't** convert the workbook to a build step or bundle Yjs into the file; load it from CDN like `marked`.
- The stray untracked `deep-dives/B1-bootstrap-paradox-deepdive.html` is from another session — do not stage or delete it.
