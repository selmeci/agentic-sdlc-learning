# Deep-dive modal UX: full-width layout, section navigator, reading progress

**Date:** 2026-07-15
**Status:** approved (design forks confirmed by user)
**Scope:** the in-page deep-dive overlays (`.e1ov`) in `workbook/agentic-development-study.html`.
Applies generically to **all** overlays (H1, H2, D1, E1–E8, P1–P5, SDLC) — 17 content overlays.

## Problem

Opening a deep dive (e.g. H1) shows a 1000px-capped panel, but every content block
(`p`, `.callout`, `.io`, `table.map`, `.reading`) is capped at `max-width:74ch` (~600–690px),
so on desktop the right ~40% of the panel is dead space. There is also no way to see the
section structure or jump around inside the modal (the standalone files have a TOC sidebar;
the overlay has none), and no sense of reading progress.

## Goals (from the user)

1. **Use the available surface.** Text and blocks should fill the panel instead of clustering
   in a narrow left column.
2. **Section navigator.** Clicking the black `H<n> · DEEP DIVE` tag in the top bar opens a
   list of the page's sections; clicking one scrolls to it inside the modal.
3. **Reading progress.** As the user scrolls and reads, record which sections they have already
   seen; surface this in the top bar (before the ✕ close button) and in the navigator.

## Confirmed design decisions

- **Width:** prose (`p`, `.lead`) keeps a comfortable reading measure (~80ch); structural blocks
  (`.callout`, `.io`, `table.map`, `.reading`, `.comp`, figures) span the full content width;
  panel widened 1000 → 1180px. (Rejected: stretching prose to full width — long lines hurt reading.)
- **Persistence:** seen-section state persists across reopens via the **existing `store`
  backend** (key namespace under `agentic-study-v1` state), same mechanism as topic progress.
- **Scope:** one generic implementation keyed off the currently-open `.e1ov`, so all overlays
  get the features at once. No per-overlay wiring.

## Architecture

Single-file HTML artifact, zero build. All changes live in the workbook's `<style>` and the
trailing app `<script>`. No new files, no dependencies. Two moving parts:

### A. Layout (CSS only, scoped to `.e1ov`)

- `.e1ov .panel` → `max-width:1180px`.
- Introduce reading-measure var on the body; prose caps at it, structural blocks do not:
  - keep `.e1ov .body p{max-width: <~80ch>}` (bump from 74ch), `.lead` inherits.
  - remove `max-width:74ch` from `.e1ov .callout`, `.e1ov .io`, `.e1ov table.map`,
    `.e1ov .reading` → they become full content width.
  - `.e1ov .callout p` gets the reading measure so callout prose stays readable while the box
    is full width.
- Mobile (`max-width:760px`) rules unchanged (single-column already).

### B. Navigator + progress (JS module + CSS), generic

New init function `initDeepDiveNav()` run once at startup, after overlays exist in the DOM.
For **each** `.e1ov[role="dialog"]` that has a `.body` with `h2` sections (skip `#verov`):

1. **Section model.** Collect `.body h2`. For each, ensure a stable `id`
   (`<overlayId>-s<index>`, e.g. `h1ov-s0`) — assigned only if missing, never colliding with
   existing ids. Label = the `.n` number + the heading's text.
2. **Bar controls (injected, not hand-edited per overlay):**
   - Make the existing `.tag` a `<button class="tag secnav-toggle">` (keep text) that toggles
     a popover; the `<h3>` title also becomes part of the toggle affordance (click target).
   - Append a **progress chip** `.secprog` (`seen N/T`) immediately before the `.x` close button.
   - Append a thin **progress line** under the sticky bar (reuse the `.rprog`/`i` fill idiom).
3. **Popover** `.secnav` (absolutely positioned under the tag, inside `.bar`): a scrollable list
   of sections; each row = number chip + title + a "seen" tick. Current section highlighted.
   Click a row → smooth-scroll the `.panel` so the heading lands just under the sticky bar;
   close the popover. Closes on Escape, on outside click, and when the overlay closes.
4. **Tracking.** On `.panel` scroll (rAF-throttled, matching the existing scroll-spy pattern):
   - compute the "current" section = last heading whose top is above a threshold line
     (~bar height + a margin);
   - mark current and everything above it as **seen**;
   - update the chip count, the fill width (current index / total), and the popover ticks;
   - persist the seen set (debounced) to `store`.
   Uses panel scroll, not window scroll (the panel is the `overflow:auto` scroller).
5. **Open/close integration.** The per-overlay open handlers already scroll the panel to top and
   set `body.overflow`. On open, `initDeepDiveNav` state for that overlay is refreshed from the
   persisted set (ticks + chip shown immediately); a fresh scroll pass sets the current section.

### Persistence shape

Extend the in-memory `state` with `state.seen = { <overlayId>: [sectionIndex, …] }`, saved
through the existing `saveState()`/`store.set` path and hydrated in `loadState()`. Backward
compatible: absent `seen` → treated as empty. No topic `id`s touched (golden rule 1 safe).

## Accessibility & motion

- Toggle button: `aria-expanded`, `aria-controls`; popover `role="menu"`/list with focusable rows;
  Escape closes and returns focus to the toggle.
- Respect `prefers-reduced-motion` for the smooth-scroll and the fill transition (the codebase
  already has this pattern for `.backtop`/`.rprog`).
- Progress chip has an accessible label (`seen 3 of 10 sections`).

## Non-goals

- No change to the standalone deep-dive files' layout — they already have a TOC sidebar and
  back-to-top; the reading measure there is fine (sidebar consumes the width). (Optional later:
  add the same "seen" ticks to their sidebar TOC — tracked as follow-up, not in this pass.)
- No dark mode, no content changes, no new topics, no per-overlay hand-wiring.
- No change to the main workbook page's existing scroll-spy/back-to-top (those stay for the
  outer page).

## Verification

- `python3 scripts/validate.py` green (JS parses, HTML balanced, SVGs, CSS-class coverage,
  deep-dive wiring, topic count 52, CONTENT-MAP).
- Behavioural check in a real browser (chrome-devtools MCP) at 1440px and ~700px:
  panel fills surface; tag opens the navigator; clicking a row scrolls to the section; scrolling
  marks sections seen and updates the chip; closing and reopening restores the seen ticks.

## Coordination note

A parallel session added H2 (v1.20) concurrently. This work must be applied on top of the
current file state (now 17 content overlays) and rebased if the file moves again before commit.
The generic approach means H2 is covered automatically with no extra wiring.
