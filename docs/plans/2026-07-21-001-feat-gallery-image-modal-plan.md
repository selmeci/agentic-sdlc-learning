---
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
execution: code
product_contract_source: ce-plan-bootstrap
created: 2026-07-21
---

# feat: Gallery diagram lightbox modal

## Goal Capsule

Clicking a diagram preview in `gallery.html` opens a modal overlay showing the same diagram enlarged, so a reader can inspect fine detail without leaving the gallery. Closing (Esc, backdrop click, close button) returns to the gallery.

## Summary

The gallery is a fully generated static page (`scripts/generate-gallery.py` → `gallery.html`). Each card already inlines a complete SVG with per-card prefixed ids. The cheapest correct modal is therefore client-side only: a single shared modal container in the generated template; on click of a `.gallery-preview`, JS clones that card's SVG into the modal and opens it. No new build tooling, no per-card markup, no changes to the registry or to deep-dive files.

## Problem Frame

Diagram previews are capped at `max-height:180px` (`.gallery-preview svg`), which makes dense figures unreadable. Today the only way to see detail is "Open in deep dive →", which leaves the gallery and loses the browsing context. Users need a quick in-place zoom.

## Requirements

- R1. Clicking a card's diagram preview opens a modal overlay above the gallery showing that card's diagram at near-viewport size.
- R2. The modal closes via: close button, click on the backdrop, and the Esc key.
- R3. While the modal is open, background page scroll is locked; on close, scroll position is unchanged.
- R4. Opening the modal for a different card replaces the modal content (no stacking, no leftover state).
- R5. The modal respects `prefers-reduced-motion` (no animated transitions for users who opt out).
- R6. `gallery.html` remains a generated artifact: all changes live in `scripts/generate-gallery.py`, and `python3 scripts/validate.py` (incl. the gallery freshness check) passes.

Non-goals / deferred:
- Zoom/pan controls inside the modal (Deferred to Follow-Up Work).
- Deep-linking to an open modal via URL hash.
- Changes to deep-dive pages themselves.

## Key Technical Decisions

- **KTD1 — Clone-on-open, single shared modal.** One modal element in the page template; on open, the clicked preview's `<svg>` is `cloneNode(true)`'d into it. Rationale: 78 cards already inline their SVGs; duplicating every SVG into per-card modal markup would roughly double page weight (~100 KB → ~200 KB) for no benefit. Trade-off accepted: the clone duplicates SVG ids in the DOM. This is safe here because ids are prefixed per card (`g-<n>-...`) and the clone's referenced `<defs>` are identical to the original's, so `url(#...)` resolution renders correctly regardless of which duplicate the browser picks.
- **KTD2 — Sizing via the existing `viewBox`.** All gallery SVGs carry a `viewBox`, so in the modal `svg{width:100%;height:auto}` (bounded by `max-width`/`max-height` of the viewport minus padding) scales them losslessly. No per-figure sizing logic.
- **KTD3 — Everything in the generator template.** CSS goes into `GALLERY_CSS`, the modal container into the static HTML shell, and behavior into the existing inline `<script>` in `scripts/generate-gallery.py`. `gallery.html` is regenerated, never hand-edited (the validator's freshness check enforces this).
- **KTD4 — No dependencies.** Vanilla JS/CSS, matching the existing gallery filter script pattern.

## Implementation Units

### U1. Modal shell and styles in the generator template

- **Goal:** Add the modal DOM container and its CSS to the generated page.
- **Requirements:** R1, R2 (markup for close button/backdrop), R5, R6
- **Dependencies:** none
- **Files:** `scripts/generate-gallery.py` (template sections: `GALLERY_CSS`, HTML shell before the closing `<script>`)
- **Approach:** Add a hidden container (e.g. `<div class="gallery-modal" role="dialog" aria-modal="true" aria-label="Enlarged diagram" hidden>`) containing a backdrop, a content box with a close button (`×`, with `aria-label="Close"`), and an empty body slot for the cloned SVG. CSS in `GALLERY_CSS`: fixed-position full-viewport overlay (semi-opaque `rgba(26,36,48,.72)`, matching the `--ink` palette), centered content box (`max-width:min(1100px,94vw)`, `max-height:90vh`, `overflow:auto`, `background:var(--card)`), modal SVG rule `width:100%;height:auto` (no `max-height:180px` cap), close button positioned top-right. A `.open` class (or removing `hidden`) toggles visibility; a short opacity/transform transition guarded by `@media (prefers-reduced-motion:reduce)` which disables it.
- **Patterns to follow:** existing `GALLERY_CSS` custom-property palette and `@media (prefers-reduced-motion:reduce)` usage already present in the page template.
- **Test scenarios:**
  - `Test expectation: none (automated) — presentational shell;` behavior is verified in U2's scenarios and the U3 smoke pass.
  - Static check: generated `gallery.html` contains exactly one modal container and the modal CSS rules.
- **Verification:** Regenerating `gallery.html` succeeds and the modal container is present, hidden by default.

### U2. Modal open/close behavior

- **Goal:** Wire clicks to open the modal with the cloned SVG, and all close paths.
- **Requirements:** R1, R2, R3, R4, R5
- **Dependencies:** U1
- **Files:** `scripts/generate-gallery.py` (inline `<script>` block, alongside the existing filter IIFE)
- **Approach:** A second IIFE. Event delegation on `.gallery-grid`: a `click` on (or inside) a `.gallery-preview` opens the modal — clear the modal body slot, `cloneNode(true)` the preview's `<svg>`, append, remove `hidden`/add `.open`, set `document.body.style.overflow='hidden'`, move focus to the close button. Close paths: close-button click, backdrop click (click target is the modal element itself, not its children), and `keydown` Escape (listener active only while open). On close: re-hide, restore `body.style.overflow`, return focus to the preview that opened it. Cursor hint: `.gallery-preview{cursor:zoom-in}` in CSS (U1 or here, whichever keeps the diff small).
- **Patterns to follow:** the existing gallery filter IIFE (vanilla JS, `querySelector`, no libraries).
- **Test scenarios:**
  - Happy path: clicking card A's preview opens the modal containing an SVG equal to card A's (same prefixed id namespace, e.g. `g-<a>-`), visibly larger than the 180px preview cap.
  - Close via × button: modal hidden, body scroll restored, focus back on the originating preview.
  - Close via backdrop click: same expectations.
  - Close via Escape: same expectations.
  - Switching cards: open card A, close, open card B — modal shows only card B's SVG (no duplicate/stale content).
  - Scroll lock: with a tall page, opening the modal does not change `scrollY`; wheel/touch scroll of the background is suppressed while open.
  - Reduced motion: with `prefers-reduced-motion:reduce` emulated, opening/closing involves no transition delay.
- **Verification:** All scenarios above confirmed in a real browser run (headless Chrome is acceptable) against the regenerated `gallery.html`.

### U3. Regenerate artifact and run repo gates

- **Goal:** Produce the final `gallery.html` and prove the repo's own quality gate passes.
- **Requirements:** R6
- **Dependencies:** U1, U2
- **Files:** `gallery.html` (regenerated only, via `python3 scripts/generate-gallery.py`)
- **Approach:** Run the generator, then `python3 scripts/validate.py` (covers gallery freshness, registry coverage, SVG well-formedness of deep dives, JS parse of the workbook). Additionally smoke-render the regenerated page in headless Chrome and confirm the modal opens on a synthetic click and the rendered modal shows the diagram (pixel-level sanity: modal region is not blank/black).
- **Execution note:** This is static-site work; prefer runtime smoke verification (headless browser) over unit coverage — no JS test framework exists in this repo.
- **Test scenarios:**
  - `validate.py` exits 0.
  - Headless render of `gallery.html` shows all 78 cards (no regression of the black-square fix from earlier today).
  - Headless render with a dispatched click on the first `.gallery-preview` shows the modal overlay with a legible enlarged SVG.
- **Verification:** Validator green; smoke screenshots inspected.

## Scope Boundaries

### Deferred to Follow-Up Work
- Zoom/pan inside the modal.
- URL-hash deep links to a specific open diagram.
- Prev/next keyboard navigation between diagrams inside the modal.

## Open Questions

None blocking. (Modal max width of ~1100px is a judgment call consistent with the site's `1200px` content width; trivially adjustable in `GALLERY_CSS`.)

## Sources & Research

- Repo-local only: `scripts/generate-gallery.py` (template, `GALLERY_CSS`, card rendering), `gallery.html` (generated output), `scripts/validate.py` (gates incl. gallery freshness). Local patterns are strong; no external research needed.
