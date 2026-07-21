# Gallery Feature Design

## Overview

Add a standalone **Gallery** page that collects every diagram/image from the deep-dive companions, displays them in a browsable grid, and links each one back to the originating deep dive together with the section context and the reason it appears there.

## Goals

- Give readers a single place to discover all visual material in the study programme.
- Surface the *why* of each diagram, not just the caption.
- Make the gallery cheap to maintain by auto-discovering figures while keeping human-curated metadata in a registry.
- Enforce the registry via the existing validator so new diagrams cannot be added without gallery metadata.

## Non-goals

- Replace deep-dive pages or inline map sections.
- Host original image assets outside the repository.
- Add a runtime framework or build pipeline.

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Page type | Standalone HTML file (`gallery.html`) | Requested by the user; easy to host on GitHub Pages and share. |
| Image scope | Only figures in `deep-dives/*.html` | Inline workbook maps (SDLC, domain map) are not deep-dive companions and would need separate handling. |
| Metadata strategy | Hybrid: auto-discover figures, manual registry for context | Captions and section headings can be extracted automatically, but the *why* requires human curation. |
| Figure identification | `{deepDive, figureIndex}` | Least invasive; no changes to existing HTML. Index shifts are caught by validation. |
| Generator | `scripts/generate-gallery.py` | Keeps the project zero-build; the generated file is committed. |
| Validation | Extend `scripts/validate.py` | Reuses the existing gate; fails if a figure lacks a registry entry or an entry is orphaned. |

## Files Added/Modified

### New files

- `gallery-registry.json` — curated metadata for each gallery entry.
- `scripts/generate-gallery.py` — generator script.
- `gallery.html` — generated output (committed).

### Modified files

- `scripts/validate.py` — registry/figure consistency checks + schema checks.
- `index.html` — link to the gallery.
- `workbook/agentic-development-study.html` — link to the gallery.
- `docs/AUTHORING-GUIDE.md` — step for adding figures to the gallery.
- `docs/CONTENT-MAP.md` — mention the gallery.

## Data model

### `gallery-registry.json`

```json
{
  "entries": [
    {
      "deepDive": "E1-agent-model-harness",
      "figureIndex": 0,
      "title": "Seven-component harness",
      "section": "2 · The seven components",
      "sectionAnchor": "map",
      "why": "Shows why the model is only one of seven enforceable components; prevents treating the agent as 'just the LLM'."
    }
  ]
}
```

Field semantics:

- `deepDive` (string, required) — deep-dive filename without the `.html` extension, e.g. `E1-agent-model-harness-deepdive` or `PB1-assess-runbook`.
- `figureIndex` (int, required) — zero-based order of the `<figure>` inside that deep-dive file.
- `why` (string, required) — human-curated explanation of why the diagram matters in its section.
- `title` (string, optional) — display title; falls back to the extracted `<figcaption>` text.
- `section` (string, optional) — display name of the containing section; falls back to the nearest preceding `<h2>` text.
- `sectionAnchor` (string, optional) — `id` of the section heading used for the deep-dive link; falls back to the nearest preceding `<h2 id="...">`.

## Generator behavior

`scripts/generate-gallery.py`:

1. Load `gallery-registry.json`.
2. Iterate `deep-dives/*.html` in alphabetical order.
3. For each file, parse all `<figure>` elements in DOM order and record:
   - `figureIndex`
   - `<figcaption>` text (fallback if missing: `"Diagram"`)
   - nearest preceding `<h2>` text and `id`
4. Match each figure to a registry entry by `{deepDive, figureIndex}`.
   - The registry is the source of truth for which figures appear in the gallery. Missing or invalid registry entries are skipped; the validator is the hard gate that prevents them.
5. Render `gallery.html`:
   - Reuse the workbook/deep-dive CSS (design tokens, card styles, SVG base rules) for visual consistency.
   - Prefix every `id` inside an inlined SVG with `g-<card_index>-` so that many diagrams can share a single page without id collisions. All internal references (`url(#id)`, `href="#id"`, `xlink:href="#id"`) are rewritten to match.
   - Collect SVG edge-class CSS per source file and emit scoped rules for each card (e.g. `.g-card-31 svg .ed { ... marker-end:url(#g-31-ah-e2) }`). Edge styles are keyed by `(file_stem, class_name)` so a file like `E2-context-engineering-deepdive.html` that uses a custom marker URL is not overwritten by another file's generic rule.
   - Copy any referenced markers that live in a different SVG of the same deep-dive file into the selected SVG before prefixing ids, so cross-SVG marker references keep working after only one SVG is inlined per card.
   - Do not include deep-dive overlay scripts or runbook handlers.
   - Header with "GALLERY" tag and title "Diagram Gallery".
   - Intro paragraph.
   - Text filter for title/section/why.
   - Responsive card grid:
     - SVG preview (max-height ~180px, preserved aspect ratio).
     - Title.
     - Section tag.
     - Why text (2–3 lines).
     - "Open in deep dive →" link (`deep-dives/<file>.html#<sectionAnchor>` or file-only if no anchor).
   - Empty state when filter matches nothing.
6. Cards follow the order of `gallery-registry.json` entries. The registry is the source of truth; the validator is the hard gate that ensures complete coverage.

## Validation

Extended `scripts/validate.py` checks:

1. **Registry coverage (FAIL)** — every `<figure>` in `deep-dives/*.html` must have a matching `{deepDive, figureIndex}` entry.
2. **Orphaned entries (FAIL)** — every registry entry must point to an existing deep-dive file and a `<figure>` at the given index.
3. **Schema (FAIL)** — required fields present and typed correctly; duplicate keys forbidden.
4. **sectionAnchor (FAIL)** — if a registry entry has a non-empty `sectionAnchor`, that value must exist as an `id="…"` in the corresponding deep-dive file.
5. **SVG id uniqueness (FAIL)** — ids must be unique both within each deep-dive file and across all deep-dive files, because every inlined SVG is prefixed but the original ids must not collide.
6. **Gallery freshness (FAIL)** — `gallery.html` must match the output of `scripts/generate-gallery.py`. If they differ, the validator fails with `gallery.html is stale; run python3 scripts/generate-gallery.py`.

Example error messages:

- `E1-agent-model-harness-deepdive.html figureIndex 1 has no gallery-registry entry`
- `gallery-registry.json entry {E1-agent-model-harness-deepdive, 5} points to missing figure`
- `gallery.html is stale; run python3 scripts/generate-gallery.py`

## UI/UX

- Cards use the existing paper/card/rounded styling.
- SVG previews are inline (not external images) so they work offline and on GitHub Pages.
- Filter input is a plain text box that filters on title, section and `why`.
- Each card is an `<article>`; the deep-dive link is a regular anchor for accessibility.
- Each card's deep-dive link has a descriptive text; the SVG preview is decorative and relies on the surrounding card context. (Deep-dive SVGs that already include their own `role`/`aria-label` keep those attributes.)

## Authoring workflow

When adding a new figure to a deep dive:

1. Add the `<figure>` to the deep-dive HTML as usual.
2. Add the corresponding entry to `gallery-registry.json`.
3. Run `python3 scripts/generate-gallery.py`.
4. Run `python3 scripts/validate.py` — must pass.
5. Commit the deep-dive change, the registry change, and the regenerated `gallery.html`.

## Open questions / future work

- Should the gallery also expose a plain list view? Deferred until requested.
- Should generated SVG previews be simplified/stripped of interactivity? Keep as-is initially; revisit if performance becomes an issue.
