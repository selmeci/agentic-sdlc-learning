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
SVGs: one `<defs>` with a **unique** marker `id="ahP2a"`; arrows use `class="edP2"`
(or inline `style="marker-end:url(#ahP2a)"`).

House rules: dense English prose; tie back to the framework (name the E/P/D topics & reports
it connects to); separate strong evidence vs vendor claims vs synthesis; flag D1–D5 as original;
mark fast-moving tool facts as point-in-time.

## Step 2 — generate the standalone file
Reuse E1's `<head>` verbatim, then:
- retitle `<title>` and the header `<h1>`/tag;
- append to the `<style>`: `.closingnote{…}` and `svg .edP2{…marker-end:url(#ahP2a)}`;
- add a `<nav class="toc">` listing `#s0…#sn`;
- give each `<h2>` an `id="sN"` (loop, high→low so `1` doesn't match inside `10`).
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
