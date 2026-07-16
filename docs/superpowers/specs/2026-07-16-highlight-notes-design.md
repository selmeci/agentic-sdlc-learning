# Highlight-notes on deep dives — design

**Date:** 2026-07-16
**Status:** approved (design), pending implementation plan
**Target file:** `workbook/agentic-development-study.html` (only)
**Version bump:** v1.28 → v1.29

## Problem

Readers study the deep-dive companions but have no way to capture a specific
passage that matters to them together with their own reaction to it. Today the
only note affordance is a free-text "My notes" textarea per *topic* — coarse,
detached from the exact wording, and not linkable back to a source location.

We want: select text in a deep dive → save it as a note → optionally attach the
reader's own thought → find all such notes in one place on the main page → click
one to jump back to the exact passage it came from, with the passage still
visibly highlighted.

## Scope decision (settled)

The feature lives **entirely in the workbook** (`workbook/agentic-development-study.html`).

Why not the standalone `deep-dives/*.html` files: they carry **no storage
backend** (verified — 0 matches for `store` / `window.storage` / the storage
key) and each is served from its own origin, so highlights made there could
never travel to a central list without a large cross-file sync mechanism we are
deliberately not building. The workbook is the only surface that has the shared
`store` *and* renders every deep dive (as in-page `.e1ov` overlays). So:

- Highlighting works inside the **in-page deep-dive overlays** only.
- The standalone files are **not modified**. (This does not violate the
  "two copies stay in sync" golden rule: we are not changing any deep-dive
  *body content* — we are adding a workbook-level interaction layer.)

## User-facing behaviour

### Capture (inside a deep-dive overlay)
1. User selects text inside an open deep-dive overlay (`.e1ov.show`, excluding
   the version-history modal `#verov` and the notes modal itself).
2. A small floating **"+ save as note"** button appears near the selection,
   positioned from the selection's bounding rect.
3. Clicking it **saves the highlight immediately** with an empty `thought`, and
   shows a brief transient confirmation ("saved — add your thought in notes").
   No popover, no modal, no interruption to reading.
4. Selections that are whitespace-only or shorter than 3 characters are ignored
   (button does not appear). Text inside `<svg>` figures is excluded from
   selection anchoring.

### Central notes modal (main page)
- A new top-bar button **`notes (N)`** (next to export/import) opens a modal
  reusing the existing `.e1ov` overlay shell — same open/close/Escape/backdrop
  behaviour as the version-history modal (`#verov`).
- Notes are **grouped by deep dive** (by `title`), newest first within a group.
- Each note card shows:
  - the **quoted passage** (blockquote styling),
  - an **editable "your thought" textarea** (saves on input via the existing
    debounced `scheduleSave`),
  - an **"open in deep dive →"** button,
  - a **delete ✕** button.
- Empty state: a prompt telling the reader to select text in a deep dive and
  choose "save as note".
- The button label count `(N)` reflects `state.highlights.length` and updates
  live on add/delete.

### Return trip
- "open in deep dive →" closes the modal, opens the correct overlay, scrolls the
  passage into view, and **briefly flashes** it (a fading background pulse).
- The passage stays **persistently tinted** every subsequent time that deep dive
  is opened (all saved highlights for that deep dive are re-applied on open).

## Data model

A new array on the existing `state` object, persisted through the **same `store`
backend** under key `agentic-study-v1`, saved via the existing debounced
`scheduleSave` / `saveNow`:

```js
state.highlights = [
  {
    id,            // unique: "h_" + Date.now() + "_" + short random (browser runtime — Date.now OK here)
    ov,            // overlay token, e.g. "i4" (derived from the overlay id "i4ov")
    title,         // display label captured at save, e.g. "I4 · Memory Systems"
    quote,         // the selected text (stored up to a sane cap, e.g. 600 chars)
    prefix,        // ~32 chars of visible text immediately before the quote
    suffix,        // ~32 chars of visible text immediately after the quote
    occ,           // occurrence index of quote in the overlay's visible text (disambiguator)
    thought,       // reader's own comment; "" at save time, editable in the modal
    created        // ISO timestamp
  }
]
```

- `loadState` reads `p.highlights || []` into `state.highlights` (mirrors how
  `progress`/`notes`/`seen` load today).
- `exportData` adds `highlights` to the payload.
- `importData` **merges** imported highlights into the current array,
  **de-duped by `id`** (append any whose `id` is not already present). Guard
  updated so a file containing only `highlights` still validates as an export.

## Anchoring & persistent re-highlight

Content is stable and hand-authored, so we use **text-quote anchoring**
(quote + short prefix/suffix + occurrence index), not fragile DOM paths.

### On save
Map the current selection's start/end (text-node container + offset) to global
character offsets over the overlay panel's visible text (built by a TreeWalker
that skips `<svg>`, `<script>`, `<style>`). From that:
- `quote = fullText.slice(gStart, gEnd)`
- `prefix = fullText.slice(max(0, gStart-32), gStart)`
- `suffix = fullText.slice(gEnd, gEnd+32)`
- `occ = ` index of this occurrence among all occurrences of `quote`.

### On overlay open — `applyHighlights(overlay)`
- A single **MutationObserver** watches every `.e1ov` for `class` attribute
  changes; when one gains `.show`, it calls `applyHighlights` for that overlay.
  This **decouples the feature from the ~20 existing per-overlay open handlers**
  and automatically covers any future deep dive.
- `applyHighlights`:
  1. Unwraps any existing `mark.hl-note` in the overlay (replace with text node,
     normalize) so re-open is idempotent.
  2. For each of `state.highlights` whose `ov` matches this overlay, **locates**
     the passage: find all occurrences of `quote` in the current visible text;
     score each by how well the surrounding text matches `prefix`/`suffix`;
     tie-break by `occ`; fall back to the `occ`-th occurrence, then the first.
  3. **Wraps** each located `[gStart, gEnd)` range in
     `<mark class="hl-note" data-note-id="…">`, splitting across element
     boundaries by wrapping each intersected text node's portion separately
     (per-text-node sub-ranges via `Range.surroundContents`), so inline HTML and
     SVG structure is never broken.
  4. Ranges are applied so that earlier offsets stay valid (recompute the text
     map per range — the doc is small; a `<mark>` adds no text so global offsets
     are preserved).

### Runtime-only marks
All `<mark>` elements are inserted **at runtime by JS** — never written to the
HTML file. Therefore `scripts/validate.py` (which checks the *static* file:
JS parses, tags balance, SVGs parse, deep-dive anchors appear twice, topic count)
is **unaffected** by the marks. Only the static additions (modal HTML, CSS,
top-bar button, JS block) must keep tags balanced and JS parsing.

## Edge cases

- **Passage not found** (content later changed): the note still appears in the
  list with its stored `quote`. "Open in deep dive" opens the overlay, scrolls to
  top, and shows a quiet inline "couldn't locate the exact passage" note. No
  exception, no broken DOM.
- **Overlapping highlights**: ranges applied right-to-left; minor nesting is
  tolerated (a mark inside a mark renders as a slightly darker tint). Acceptable
  for a study tool. **Known limitation**, documented, not engineered around.
- **Selection crossing a figure/SVG**: anchoring uses text-only offsets; SVG text
  is skipped, so a selection spanning a figure anchors on its text portions.
- **No persistence available** (`store` null): the warnbar already shows; the
  save button still appears but saving is a no-op beyond the current session,
  consistent with existing progress/notes behaviour.

## CSS

Added near the existing `.note` / `.e1ov` rules, reusing design tokens:
- `mark.hl-note` — subtle tint (amber/cobalt accent, low alpha), no layout shift.
- `mark.hl-note.flash` — brief fading pulse animation on arrival.
- floating `#hlSave` button — small, mono, fixed-positioned.
- notes-modal card styles — reuse `.note textarea` styling for the thought field.

## Housekeeping

- **Version bump v1.29**: prepend a `.vitem` to `#verov`, update the footer
  current-version line, mirror the entry to `docs/CHANGELOG.md`.
- Add `state.highlights` to the storage description in `docs/ARCHITECTURE.md`.
- Run `python3 scripts/validate.py` — must pass (green).

## Out of scope (YAGNI)

- Highlighting in standalone deep-dive files.
- Cross-origin / cross-file note sync.
- Rich-text thoughts, tags, colours, or note categories.
- Engineering away overlapping-highlight nesting.
- Surfacing the existing per-topic "My notes" textareas in the central modal
  (they remain a separate, unchanged feature).
