# Deep-dive link presentation — design

**Date:** 2026-07-16
**Status:** approved (brainstorming complete)
**Scope:** `workbook/agentic-development-study.html` only (topic-card renderer + CSS + version bump)

## Problem

In each topic's "Go deeper" section, deep-dive links open an **in-page overlay** (via a JS
click handler that calls `preventDefault()`), but they are rendered identically to genuine
external references:

- Every item in `<ul class="srcs">` gets the same `↗` bullet (`.srcs li::before`, ~line 124),
  a glyph that means "you're leaving this page."
- The deep-dive `<a>` even carries `target="_blank" rel="noopener"` (~line 5477) — literally
  "open in a new tab" — neutralised only by the JS interceptor. The DOM says "external nav."
- The sole distinguishing signal today is textual: a leading `↳` and the words
  "Deep Dive — open here", buried in a list item that looks like a citation.

Users cannot tell that clicking opens a specific in-page content panel rather than navigating away.

## Chosen direction

**Dedicated "deep dive" panel button** (chosen over "restyle within one list" and
"two labelled sub-groups"). A button affordance reads as a control that acts *here*, not a link
that navigates. External references remain a clean citation list below it.

## Design

### Detection & data — no data changes
All 26 `src` arrays stay untouched (respects stable-ID / minimize-risk golden rules).
In the renderer, split each topic's `src`:
- **Deep dives:** `s.u && s.u.charAt(0)==='#'` — bulletproof; verified that the *only* in-page
  `#` anchors in any src list are the 26 `#*-deepdive` links (no false positives).
- **References:** everything else (external `http` links + plain-text notes).

Title/description parsed at render time from the uniform string
`↳ <CODE> Deep Dive — open here (<description>)` via
`/^↳\s*(.*?)\s*—\s*open here\s*\((.*)\)$/` → title `"E1 Deep Dive"`,
desc `"seven components, inputs/outputs, SDLC map"`. If a future entry does not match, fall
back to the raw text (minus a leading `↳`) as the title, no description.

### Markup (single render block, ~line 5477)
```html
<div class="sec"><div class="lab">Go deeper</div>
  <a class="ddgo" href="#e1-deepdive" aria-haspopup="dialog">
    <span class="ddgo-ic" aria-hidden="true"><svg…panel-with-lines…></span>
    <span class="ddgo-txt">
      <span class="ddgo-title">E1 Deep Dive</span>
      <span class="ddgo-desc">seven components, inputs/outputs, SDLC map</span>
    </span>
    <span class="ddgo-act">Open panel <svg…chevron…></span>
  </a>
  <div class="srclab">References</div>          <!-- only when references exist -->
  <ul class="srcs"> …external items only… </ul>  <!-- only when references exist -->
</div>
```

**Hard constraint:** the element stays `<a href="#<code>-deepdive">`. The JS overlay handlers
match `a[href="#e11-deepdive"]` exactly, and `validate.py` checks every `#*-deepdive` link is
wired. Only styling + attributes change.

### Correctness fixes folded in
- Drop `target="_blank" rel="noopener"` from the deep-dive `<a>` (keep it on external refs).
- Add `aria-haspopup="dialog"` so the affordance is announced as opening a dialog, not a link.

### Styling (reuses existing theme vars → dark-mode-ready)
`.ddgo` = full-width flex button-card: 1px border + 3px cobalt left-accent, `var(--card)` bg,
rounded, hover lightens + border→cobalt, subtle `:active` press. Icon = a **panel-with-text-lines**
SVG (a "page of content", deliberately not a diagonal ↗). Title in `--disp`, description in
`--soft`, a mono "Open panel →" affordance on the right. Colors via existing
`--cobalt / --card / --line / --ink / --soft / --disp / --mono`. `≤480px` media rule hides the
"Open panel" text (keeps the chevron) so it never crowds on mobile.

Net effect: the deep dive reads as an interactive control that expands content here; the `↗`
glyph now appears only on genuinely external citations. The two are unmistakable.

## Validation & versioning
- `python3 scripts/validate.py` must stay green (link-wiring, tag balance, SVG well-formedness).
- Workbook-render-only; standalone deep-dive files have no such src list → **no two-copies sync**.
- Bump v1.33 → **v1.34**: prepend `.vitem` to `#verov`, update footer current-version line,
  mirror to `docs/CHANGELOG.md`.

## Out of scope
- The SDLC deep dive (referenced only in prose, not in any topic src list).
- Any change to overlay content or the standalone deep-dive files.
