# Design: Cross-device progress sync (Yjs CRDT)

**Date:** 2026-07-17
**Status:** Approved for planning (revised — Yjs, replacing an earlier hand-rolled merge)
**Scope:** Add an optional, local-first backend sync so a reader's progress/notes can
travel between devices, using an established CRDT (Yjs) for conflict-free merge.

## Problem

Progress (topic status, notes, seen-set, highlights) is stored only in the browser
(`localStorage`, key `agentic-study-v1`, with the claude.ai `window.storage` wrapper as
fallback). Storage is per-origin and per-device: a reader who continues on another device
starts fresh. Manual JSON export/import exists but is clumsy.

## Goal

Let a reader opt in to device sync with no accounts and no complex login:

1. The reader requests a sync. Their local state is uploaded to the server.
2. On first sync the reader receives a **4-character random code** (`a–z0–9`).
3. From that moment, every local change is pushed to the server automatically.
4. On another device the reader enters the code; the server state is merged in, and that
   device becomes linked (auto-pushes from then on).

Non-goals: authentication, real-time presence, live cursors.

## Why Yjs (design decision)

An earlier iteration hand-rolled a per-field merge. That was the wrong instinct: merge
is a solved problem, and a hand-written algorithm drifts into ad-hoc tie-breaks because
a plain-JSON schema lacks the metadata a correct merge needs. We instead adopt a
**CRDT** — conflict-free by construction — and let the schema be the CRDT.

- **Yjs** — 18 kB gzipped, **pure JavaScript, no WASM**, ~920K weekly downloads, the
  production default. Runs in **both** the browser and a Cloudflare Worker.
- Automerge (320 kB Rust→WASM, ~50 ms init) and Loro (WASM) are also correct but too
  heavy for a hand-authored single-file artifact, and would need WASM wiring in the
  Worker. History-as-a-feature (Automerge's edge) is not a goal here.

Merge becomes a library call — `Y.applyUpdate` — on both ends. No custom merge code.

## Constraints (from CLAUDE.md)

- **Local persistence stays local-first and Yjs-independent.** The existing `store`
  backend + plain-JSON `state` under `agentic-study-v1` is unchanged and remains the
  canonical local store. Yjs is **additive**, used only for the optional sync layer, so
  if Yjs fails to load (e.g. claude.ai CSP) the app still saves locally exactly as today.
- The workbook stays a **single-file, zero-build HTML artifact**. Yjs loads from a CDN
  (same pattern as the existing `marked.min.js`). Worker source lives in `sync-worker/`.
- `scripts/validate.py` must stay green. Client sync JS lives in the last `<script>`
  block and must pass `node --check`; any new markup CSS class must be styled/referenced.
- **No topic-id changes.** Topic ids remain the keys inside the Yjs `progress`/`notes`
  maps.
- Version bump ritual; **verify the next free version number** (a parallel session may
  have taken v1.39 for B1 — pick the next unused).
- Tooling: **pnpm** (not npm) in `sync-worker/`; keep the user's latest dep versions.

## Architecture

```
Workbook (single-file HTML; GitHub Pages / local file / claude.ai)
  state {progress,notes,seen,highlights,updatedAt}  ── canonical LOCAL store (JSON, unchanged)
     store.set(agentic-study-v1)                        works with or without Yjs
        │
        │  (only when sync enabled AND Yjs loaded)
        ▼
  Y.Doc  ── built/kept from state; persisted encoded under agentic-study-ydoc-v1
     progress:Y.Map  notes:Y.Map  seen:Y.Map(set)  highlights:Y.Map(byId)
        │  Y.encodeStateAsUpdate / Y.applyUpdate (merge = library call)
        ▼
Cloudflare Worker (Hono, *.workers.dev), account fb0866add4b7bc5813b01a16ce090bfc
  POST /new      -> new code; apply client update into a fresh doc; store; return state
  GET  /r/:code  -> return encoded doc state (base64) or 404       (load/focus pull)
  POST /r/:code  -> Y.applyUpdate(stored, client); store; return merged state  (push)
  imports yjs (pure JS — runs in Workers); merges server-side
  SYNC_KV      : code -> base64(Y.encodeStateAsUpdate(doc))
  RATE_LIMITER : native [[ratelimits]] binding (hono-rate-limiter, global middleware)
```

**Local-first invariant:** the JSON `store` path never depends on the network or on Yjs.
Sync is best-effort; failures show a status chip and never block saving.

**Self-healing convergence:** because Yjs merge is commutative/idempotent/associative, a
concurrent double-push (KV get→put is not atomic) cannot cause permanent loss — the
"losing" device still holds its changes in its own Y.Doc and re-merges them on its next
sync. Durable Objects would fully serialize writes but are unnecessary at this scale.

## Yjs document schema

One `Y.Doc` with four top-level maps:

| Map (`ydoc.getMap(...)`) | Keys → values | Materializes to `state.*` |
|---|---|---|
| `progress` | topicId → status string (`none`/`studying`/`done`) | `state.progress` (LWW per topic) |
| `notes` | topicId → note string | `state.notes` (whole-text LWW per topic) |
| `seen` | `"<ovId>:<idx>"` → `true` (grow-only set) | grouped into `state.seen = {ovId:[idx…]}` |
| `highlights` | highlightId → highlight object | `state.highlights` array; delete via `Y.Map.delete` |

- `progress`/`notes`: `Y.Map` gives last-write-wins per key — standard and sufficient.
- `seen`: modelled as a **grow-only set** of `ov:idx` keys — union is automatic and
  "once seen, stays seen" falls out for free.
- `highlights`: keyed by their existing id; upsert (create/edit-thought) = `set` the whole
  object (LWW), remove = `delete`. Union-by-id is automatic.

## Client behaviour

- **Yjs loader:** a `<script type="module">` imports Yjs from CDN and sets `window.Y`,
  firing a `yjs-ready` event. If it never loads, `window.Y` stays undefined and the sync
  UI is shown disabled with a one-line explanation; local save is unaffected.
- **state ↔ Y.Doc mirror:** at the single existing `saveNow` choke-point, when linked,
  mirror the current `state` into the Y.Doc (set changed keys; add seen keys; upsert/delete
  highlights), persist the encoded doc, and schedule a push. On a remote update, apply it
  into the Y.Doc, materialize back into `state`, persist JSON + doc, and re-render. A
  re-entrancy flag prevents mirror↔materialize loops.
- **enable:** `POST /new` with the encoded doc → receive code → persist code → apply
  server state → linked.
- **link with a code:** `GET /r/:code` (404 → invalid) → apply into local doc →
  materialize → persist code → push local up (idempotent) → linked.
- **auto-push:** debounced after `saveNow` when linked → `POST /r/:code` → apply merged
  server reply back into the local doc.
- **refresh:** on page load and on window focus, `GET /r/:code` → apply → materialize.
  No continuous polling.
- **unlink:** clear the local sync-code key; stop pushing; local data untouched.
- **status:** the existing save indicator gains `synced · CODE` / `syncing…` /
  `sync error` (local still saved).

### Local keys
- `agentic-study-v1` — unchanged canonical JSON state.
- `agentic-study-ydoc-v1` — base64 of the encoded Y.Doc (sync vehicle; only written when
  syncing). On first enable, seeded from current `state` (migration of existing progress).
- `agentic-study-sync-v1` — `{code, lastSyncAt}` (device linkage; never uploaded).

## Backend (Cloudflare Worker)

### Stack
- **Hono.js** router; **hono-rate-limiter** with Cloudflare's native Rate Limiting API
  (`binding` option, `[[ratelimits]]`), applied globally, keyed on `cf-connecting-ip`.
- **yjs** (pure JS) imported in the Worker for server-side merge.
- One KV namespace `SYNC_KV`. Source in `sync-worker/`: `package.json` (pnpm; `hono`,
  `hono-rate-limiter`, `yjs`), `wrangler.toml`, `src/*.ts`. Bundled by `wrangler deploy`.

### Endpoints (payloads are base64 of Yjs binary updates)
- `POST /new` — body `{update}`. New `Y.Doc`; `Y.applyUpdate(doc, decode(update))`;
  generate a unique 4-char code (`a–z0–9`, retry on KV collision); store
  `base64(Y.encodeStateAsUpdate(doc))`; return `{code, update}` (server state).
- `GET /r/:code` — return `{update}` (base64 server state) or `404`.
- `POST /r/:code` — body `{update}`. `404` if code unknown (a typo cannot create junk).
  Else load stored doc, `applyUpdate`, store, return `{update}` (merged state).
- CORS `*` (GET/POST/OPTIONS, `Content-Type`); data is protected by the code, not origin;
  no cookies. Covers GitHub Pages, `file://`, claude.ai.

## Merge

**There is no custom merge.** Convergence is Yjs's `applyUpdate`, exercised on both the
client and the Worker. Tests assert the CRDT property we rely on (apply-order
independence) rather than re-implementing merge rules.

## Error handling

- Any `fetch` failure / `429` / `5xx`: local save already succeeded; set sync status
  `error`; retry on the next change or focus. Never fatal.
- `POST /r/:code` `404` (record vanished): surface once, drop to unlinked; local intact.
- Yjs unavailable (CSP/offline): sync UI disabled with a note; local unaffected.

## Provisioning (user's logged-in wrangler, account `fb0866add4b7bc5813b01a16ce090bfc`)

1. Scaffold `sync-worker/` (pnpm; `hono`, `hono-rate-limiter`, `yjs`; `wrangler.toml`
   incl. `[[ratelimits]]`; `src/`).
2. `wrangler kv namespace create SYNC_KV`; wire the id into `wrangler.toml`.
3. `pnpm install`, then `wrangler deploy`; capture the `*.workers.dev` URL.
4. Hard-code that URL into the workbook `SYNC_URL` constant.

## Testing

- **Worker (pnpm + vitest):** unit — the sync helper: applying two client updates to a
  stored doc converges regardless of order; a fresh doc round-trips. Routes (via
  `app.request` + fake KV): `POST /new` mints a 4-char code and stores; `GET` returns /
  404s; `POST /r/:code` merges two updates and 404s on unknown; CORS header present.
- **Client (in-browser, verified visually):** two storage contexts as two devices —
  enable → code → link second → change on each → converge on focus. Screenshot the modal
  (light + dark). Verify local save still works with Yjs blocked (offline/CSP).
- `python3 scripts/validate.py` green.

## Version / docs

- Bump to the next free version (verify current first), update `#verov`, footer,
  `docs/CHANGELOG.md`.
- Add a "Sync layer" section to `docs/ARCHITECTURE.md`: Yjs doc schema, the local-first
  invariant, the additive Y.Doc, the Worker's server-side `applyUpdate`, and the three
  local keys.

## Open questions

None. Yjs + server-side merge + whole-text-LWW notes approved during brainstorming.
