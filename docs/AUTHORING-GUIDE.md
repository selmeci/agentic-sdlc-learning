# Authoring guide — adding the next deep-dive companion

The recurring unit of work. It is mechanical and validated. Example below uses **P2**
(`prod-prd`); substitute the token (`p2`), title, and marker/edge names for any topic.

> Read `docs/ARCHITECTURE.md` first for the overlay pattern. Keep `scripts/validate.py` green.

## Per-topic tokens you'll pick
- **token**: short lowercase, e.g. `p2` → anchor `#p2-deepdive`, overlay id `p2ov`,
  close attr `data-p2close`, marker id `ahP2a`, edge class `edP2`.
- **standalone filename**: `deep-dives/P2-prds-with-ai-deepdive.html` (match the naming style).
- Find the topic's `id` and current `src` array in the workbook (here: `prod-prd`).

## Step 1 — write the shared body
Create `/tmp/p2body.html`: the section content only (no `<html>/<head>`). Fixed shape:
`§0 why it matters` → content sections with `.io` / `.comp` / `.callout` / `figure` (SVG) /
`table.map` → `§n takeaways` (three-sentences callout) → further reading (`.reading`) →
final `<p class="closingnote">…</p>`. Number sections `<h2><span class="n">0</span>…`.
SVGs: wrap each figure in `<figure>`, and the `<svg>` **must** carry `role="img"` + a
descriptive `aria-label`. That is the exact selector the diagram lightbox and screen readers
use — a figure SVG without `role="img"` silently ships non-zoomable, and the validator fails
it. One `<defs>` with a **unique** marker `id="ahP2a"`; arrows use `class="edP2"`
(or inline `style="marker-end:url(#ahP2a)"`).

House rules: dense English prose; tie back to the framework (name the E/P/D topics & reports
it connects to); separate strong evidence vs vendor claims vs synthesis; flag D1–D5 as original;
mark fast-moving tool facts as point-in-time.

## Step 2 — generate the standalone file
Reuse E1's `<head>` verbatim, then:
- retitle `<title>` and the header `<h1>`/tag;
- append to the `<style>`: `.closingnote{…}` and `svg .edP2{…marker-end:url(#ahP2a)}`;
- add a `<nav class="toc">` listing `#s0…#sn`;
- give each `<h2>` an `id="sN"` (loop, high→low so `1` doesn't match inside `10`). **These IDs become public deep links — preserve them when editing; never rename an existing section id, because external links point at it.**
- **keep the diagram lightbox** (since v1.69, every figure is click-to-enlarge). The reused
  `<head>` already carries the `.dlb` CSS; every standalone file also ends with the `.dlb`
  modal `<div>` + its `<script>` right before `</body>` — copy that block verbatim from any
  existing deep dive. This plus the figure `role="img"` (Step 1) is what makes diagrams
  zoomable; `scripts/validate.py` (`check_diagram_lightbox`) fails the build if either is missing.
Write to `deep-dives/P2-…-deepdive.html`.

## Step 3 — build + insert the overlay
Wrap the **same body** in:
```html
<div class="e1ov" id="p2ov" role="dialog" aria-modal="true" aria-label="P2 deep dive">
  <div class="panel">
    <div class="bar"><span class="tag">P2 · DEEP DIVE</span><h3>…</h3>
      <button class="x" type="button" data-p2close>✕ close</button></div>
    <div class="body">
… body …
    </div>
  </div>
</div>
```
Because the whole workbook page is one DOM, overlay `<h2>` ids must be unique across all overlays. Prefix each id with the overlay token in the wrapper (`<ov.id>-<standalone-id>`, e.g. `p2ov-s3`). The public workbook fragment for section 3 is therefore `#p2ov-s3`, while the standalone file keeps `#s3`. Never rename an existing id; preserve both the standalone and prefixed forms so external links keep working.

Insert into the workbook immediately **before** `<footer>`.

## Step 4 — wire the 3 remaining hooks
1. **Scoped marker CSS** — after the last `.e1ov svg .edXX{…}` rule add:
   `.e1ov svg .edP2{stroke:#57656F;stroke-width:1.3;fill:none;marker-end:url(#ahP2a)}`
2. **JS handler** — prepend to the handler chain (before the current first `var …ov=`):
   ```js
   var p2ov=document.getElementById('p2ov');
   if(p2ov){
     document.addEventListener('click',function(e){
       var open=e.target.closest('a[href="#p2-deepdive"]');
       if(open){e.preventDefault();p2ov.classList.add('show');document.body.style.overflow='hidden';p2ov.querySelector('.panel').scrollTop=0;return;}
       if(e.target.closest('[data-p2close]')||e.target===p2ov){p2ov.classList.remove('show');document.body.style.overflow='';}
     },true);
     document.addEventListener('keydown',function(e){if(e.key==='Escape'&&p2ov.classList.contains('show')){p2ov.classList.remove('show');document.body.style.overflow='';}});
   }
   ```
3. **Link** — change the topic's first `src` entry to
   `{t:"↳ P2 Deep Dive — open here (…)",u:"#p2-deepdive"}` (keep the rest of `src`).

## Step 5 (optional) — enrich the topic in the workbook
Add a `know` bullet / `concepts` / an extra `checks` `{q,a}` so the topic is useful without
opening the overlay. Keep the topic `id` unchanged.

## Step 6 — version + validate
Prepend a `.vitem` entry to the version-history modal (`#verov`), update the footer's
current-version `<b>vX.Y</b>` line (the top-bar button label updates itself from the first
`.vitem`), and mirror the entry to `docs/CHANGELOG.md`.
Run `python3 scripts/validate.py` — it must report JS OK, HTML balanced, 0 SVG errors, the new
`#p2-deepdive` wired ×2, and topic count intact. Present both changed files.

## Step 7 — register the diagram in the gallery

Every new `<figure>` in a deep-dive companion must appear in `gallery-registry.json`.

1. Run `python3 scripts/generate-gallery.py --draft-registry` to refresh the draft.
2. Copy the new/updated entry into `gallery-registry.json` and fill the `why` field.
3. Run `python3 scripts/generate-gallery.py` to regenerate `gallery.html`.
4. Run `python3 scripts/validate.py` — registry coverage failures must be green.
5. Commit `gallery-registry.json`, `gallery.html`, and the deep-dive file together.

If you edit an existing figure (caption, section, anchor), update the matching
`gallery-registry.json` entry and regenerate `gallery.html`.

## Editing an existing overlay (e.g. adding a section)
To modify a deep dive already embedded, you must swap the overlay by an **exact** string match:
1. Keep the previous body as `…_old.html` (back it up before editing).
2. Rebuild `old_ov = wrap(old_body)` byte-for-byte (same wrapper) and confirm it's present.
3. Build `new_ov = wrap(new_body)`, then `s.replace(old_ov, new_ov, 1)`.
4. Regenerate the standalone from the new body. Renumber sections + TOC if you inserted one.
Precedent: E4 (added mutation §5), E7 (DORA/METR §1 then how-to §2–§3), E8 (Superpowers/Compound
§3 + BMAD brownfield). Follow those diffs as worked examples.

## The traps (from CLAUDE.md, repeated because they bite)
- Apostrophes in Python strings/heredocs (`Fowler's`) → SyntaxError, nothing written. Reword or
  use `str_replace` on the file.
- Bash `{a,b,c}` brace expansion may be unavailable — list paths explicitly.
- Unique marker id + edge class per SVG; never reuse across the document.
- Never rename a topic `id`.

## Runbook companions (M9 playbook topics)

Runbooks are deep dives with a fixed practice shape — same two-copies recipe as above
(token `pb1` → `#pb1-deepdive`, `pb1ov`, `data-pb1close`, marker `ahPB1a`, edge `edPB1`),
plus:
- Shape: `§0 why → §1 how to run it (progress chip + persistence note) → phase sections
  with steps → evaluation §  with templates → exit gate & takeaways`.
- Each step: `.pbstep` block with `input.pbck` carrying `data-pb="<topic id>"` and a
  **frozen** `data-step="pbN-sM"` id (progress keys — same never-rename rule as topic ids;
  the validator enforces uniqueness), a `.pbwhat` label, `.pbwhy` with overlay links to the
  theory, and a `.pbdone` criterion.
- Templates: `.pbtpl` wrapper + `.pbcopy` button with `data-copy` pointing at the `<pre>` id.
  Where the underlying theory is deterministic, the template is the **real runnable
  artifact** — hook scripts, permission baselines, CI gate configs (the E5 litmus: what
  must never happen ships as enforcement, not advice). This applies above all to PB3
  Harness, whose templates are the client-facing starter kit.
- Persistence: workbook only — `state.pb` via the single store; the standalone copy ships
  the non-persistent script (live count + copy) and the `.pbnote` disclaimer.
- The `.pb*` CSS block lives in the workbook `<style>` and is copied into each standalone
  runbook head.
