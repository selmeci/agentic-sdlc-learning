# Architecture

How the artifacts are built, so you can extend them safely. Everything is **hand-authored,
single-file, zero-build HTML** — no framework, no bundler, no npm install. That is a deliberate
choice: the files open anywhere, host anywhere, and survive tool churn.

## The workbook file

`workbook/agentic-development-study.html` is one self-contained document:

```
<head>
  <style> … design tokens + all component CSS + scoped overlay CSS … </style>
  Google Fonts: Bricolage Grotesque (display), Source Serif 4 (body), IBM Plex Mono (mono)
</head>
<body>
  intro / "how to use" (contains the SDLC + deep-dive entry links)
  <section class="dmap" id="sdlc-sec">  … SDLC Foundations: 3 tabbed SVG views …
  <section class="dmap" id="dmap">       … Domain map: 5 tabbed SVG views …
  <div id="modules"></div>               ← modules render here from JS data
  research-note <script type="text/md" data-mod="…"> blocks (the 6 reports)
  deep-dive overlays: <div class="e1ov" id="…ov"> … one per companion …
  version-history modal: <div class="e1ov" id="verov"> … one .vitem per version …
  <footer> … current version + link opening the modal + report registry …
  <script src="marked.min.js">           ← CDN, renders the text/md blocks
  <script> … the app: data model, rendering, storage, tab + overlay handlers … </script>
</body>
```

### Design tokens (CSS `:root`)
Cool light "paper" palette; accents cobalt / amber / pine. Fonts as above. The deep-dive files
reuse this exact `<head>` (copied from `E1-…`), so the whole set is visually consistent.

### The data model (in the trailing `<script>`)
Modules are JS objects: `{id, code, name, base, desc, topics:[…]}` (trajectory adds `plan:true`).
Each topic: `{id, code, title, know:[…], concepts:[…], open:[…], src:[…], checks:[{q,a}]}`.
- `id` — **frozen** stable identifier (progress key). Prefixes: `eng- prod- hand- ia- brown-
  des- sec- traj-`. **Never rename.**
- `src[]` — "Go deeper" links; a deep-dive companion is added as the **first** `src` entry with
  `u:"#<id>-deepdive"`, which opens the in-page overlay.

### Rendering
Plain JS builds the module/topic DOM from the data objects and injects into `#modules`.
`marked.js` (CDN) renders each `<script type="text/md" data-mod="…">` research block into the
matching module. Self-checks reveal on click; notes + status persist (below).

### Storage (IMPORTANT when moving to Git / hosting)
Progress + notes persist under key **`agentic-study-v1`**, debounced ~700ms, with states
`none / studying / done`, through a small `store` backend (defined next to `loadState`):
1. **`localStorage`** is preferred — progress persists locally in the browser when the file
   is opened from disk or hosted anywhere (probe-tested with a try/catch, since the claude.ai
   artifact sandbox blocks it).
2. **`window.storage` wrapper** (claude.ai artifact sandbox) is the fallback.
3. If neither exists, the warnbar shows and nothing persists.
- Go through the `store` backend for any new persistence — do not scatter raw
  `localStorage`/`window.storage` calls around the code.
- Progress is **per-origin** (and per-backend). Serving the file from a different origin
  (e.g. GitHub Pages vs the preview host) starts fresh — the data does not travel with the
  file. That's expected. The save indicator shows the active backend (`local` / `artifact`).
- **Highlights** (deep-dive annotations) persist in the same `state` under
  `agentic-study-v1` as `state.highlights` — an array of
  `{id, ov, title, quote, prefix, suffix, occ, thought, created}`. Passages are
  re-located by text-quote anchoring and wrapped in runtime-only `<mark>`
  elements on overlay open; nothing is written back to the file.

### Cross-device sync layer (Yjs CRDT — optional, additive)
Opt-in sync (v1.40) lets progress/notes travel between devices via a 4-character code,
**without** disturbing the local-first store above.
- **Local-first invariant.** The JSON `store` path (`agentic-study-v1`) stays the canonical
  local store and never depends on the network or on Yjs. Sync is a best-effort layer on top;
  if the sync engine fails to load (claude.ai CSP) or the network is down, saving works exactly
  as before. The sync UI is a modal opened from the sidebar *Data* group; a chip in the save
  indicator shows `synced · CODE` / `syncing…` / `sync error`.
- **Yjs, not a hand-rolled merge.** Merge is a `Y.applyUpdate` library call on both ends —
  chosen over Automerge/Loro because Yjs is pure-JS (18 kB, no WASM), so it runs in the browser
  (loaded from a CDN like `marked`) *and* inside the Cloudflare Worker. The "schema" is a `Y.Doc`
  with four maps: `progress` (topicId→status, LWW), `notes` (topicId→text, LWW), `seen` (a
  grow-only set of `"<ovId>:<idx>"` keys), `highlights` (id→object). It is materialized into the
  plain-JSON `state` on remote change and mirrored back on local save, at the single `saveNow`
  choke-point (guarded by a re-entrancy flag).
- **Local keys.** `agentic-study-v1` (canonical JSON, unchanged); `agentic-study-ydoc-v1`
  (base64 of the encoded Y.Doc, the sync vehicle, written only when syncing);
  `agentic-study-sync-v1` (`{code, lastSyncAt, ssv}` — device linkage plus the server's
  last known state vector, never uploaded). All go
  through the same `store` backend.
- **Delta wire format (v1.48).** Sync payloads are Yjs *diffs*, not full states: the
  client pushes `Y.encodeStateAsUpdate(ydoc, ssv)` with the current state vector in an
  `X-State-Vector` header, and the Worker replies with only the diff the client lacks.
  Pulls (`POST /r/:code/sync`) send the client's vector and return the missing diff.
  `ssv` advances only after a successful push, only to the vector actually sent; every
  25th push sends full state as reconciliation (the KV get→put race is non-atomic, and
  full-state pushes are what make a lost race self-healing). Header-less pushes get
  full-state replies, so older clients keep working; `POST /new` and `GET /r/:code`
  stay full-state (fresh devices need everything).
- **Backend** lives in `sync-worker/` (Hono + KV Cloudflare Worker, deployed to
  `agentic-study-sync.selmeci.workers.dev`). KV stores the encoded Y.Doc per code; the Worker
  merges pushes server-side with `Y.applyUpdate` (`POST /new`, `GET`/`POST /r/:code`, binary
  bodies), rate-limited via the native Cloudflare Rate Limiting binding. Bindings are typed from
  `wrangler types` (`worker-configuration.d.ts`), so they track `wrangler.toml`. This is the one
  part of the project that is **not** a zero-build single-file artifact by design — it is a
  separate deployable backend.

## The overlay pattern (how deep dives embed)

A deep dive lives in **two places from one shared body**:

1. **Standalone** `deep-dives/<name>.html` — the shared body wrapped in a full HTML document
   whose `<head>` is copied from `E1-…` (retitled, plus a `.closingnote` rule and the SVG
   marker/edge CSS for this file's diagrams), with its own `<nav class="toc">`.
2. **Embedded overlay** inside the workbook — the *same* body wrapped in
   `<div class="e1ov" id="<x>ov">…<button data-<x>close>`, inserted just before `<footer>`.

Why embed instead of link: the hosted preview serves each artifact on its own origin, so a
relative link to a sibling file **404s**. Overlays keep every cross-reference in-document.

### Wiring an overlay (4 hooks, all scoped by a per-topic token)
For a topic token like `e4` / `p1` / `sdlc`:
- **CSS**: one scoped rule `.e1ov svg .edE4{…marker-end:url(#ahE4a)}` (all overlays share the
  `.e1ov` styles; only the marker/edge differs per deep dive).
- **Overlay div**: `id="e4ov"`, close button `data-e4close`.
- **JS handler**: a small block that opens on click of `a[href="#e4-deepdive"]`, closes on
  the close button / backdrop click / Escape. Handlers are chained in the trailing script.
- **Link**: the topic's first `src` entry `u:"#e4-deepdive"`.

Each deep-dive SVG uses a **unique** marker id (`ahE1a … ahP1a`, `ahSa`) and edge class
(`edE1 … edP1`, `edS`) so no two SVGs in the document collide.

### The version-history modal (`#verov`)
The changelog lives in a modal reusing the `.e1ov` overlay shell, one
`<div class="vitem"><span class="vv">vX.Y</span><span class="vd">date</span><p>…</p></div>`
per version, newest first. It opens from any `[data-veropen]` element — the top-bar button
`#verbtn` (whose label is set at load from the first `.vitem .vv`, so it never goes stale)
and a footer link — and closes via `[data-verclose]` / backdrop / Escape. **Version bump =**
prepend a `.vitem`, update the footer's current-version line, mirror to `docs/CHANGELOG.md`.

## The map sections (`class="dmap"`)
`#sdlc-sec` and `#dmap` share `.dmap` styling and a tab switcher. Tabs (`#sdlcTabs`, `#dmapTabs`)
toggle `.sviz` / `.dviz` panels respectively via small independent JS handlers. SVGs use the
shared arrow markers (`arG/arB/arR` in a hidden defs) — except `#sdlc-sec`, which defines its
own `arSa` marker and overrides `#sdlc-sec svg .ed` to use it (self-contained, order-independent).

## Deep-dive body vocabulary (CSS classes)
`.io` (grid of `.box`, incl. `.box.sdlc`) for input/output/SDLC cards · `.comp` (with `.chead`,
`.cid`, `.role`) for component cards · `.callout` (`.amber` / `.pine` variants) · `figure` +
`figcaption` for SVGs · `table.map` for comparison tables · `.reading` (`.item`) for further
reading · `.kicker`, `.lead`, `.mono`, `.closingnote`. Match existing files exactly.

## Validation
`scripts/validate.py` is the deterministic gate. It extracts the trailing `<script>` and runs
`node --check`, balances HTML tags (ignoring void + SVG elements), parses every `<svg>` with
ElementTree, confirms each `#*-deepdive` anchor appears exactly twice, and prints the topic
count (must stay 52 unless you intentionally added topics). Run it after every change.
