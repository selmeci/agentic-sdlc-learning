---
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
product_contract_source: ce-plan-bootstrap
execution: code
---

# feat: Add stable, externally linkable anchors to every section

## Goal Capsule

Make every section of the study workbook and deep-dive companions directly referenceable via URL fragment. A visitor opening `.../workbook/agentic-development-study.html#eng-context` must land on that topic; opening `.../deep-dives/E2-context-engineering-deepdive.html#s3` must scroll to section 3. Preserve the existing zero-build, hand-authored HTML architecture and keep `scripts/validate.py` green.

**Authority hierarchy:** User request (linkable reference source) > `CLAUDE.md` zero-build invariant > `docs/AUTHORING-GUIDE.md` > existing overlay/section-nav code.

**Stop conditions:** Stop and report if a change would require a build step, break existing progress storage keys, or cause `validate.py` to fail unrecoverably.

---

## Product Contract

### Problem Frame

The site is already used as a learning resource, but it cannot yet be used as a citation source. Sections inside the workbook are rendered from JavaScript without stable `id` attributes, and deep-dive overlay sections receive positional generated IDs (`e1ov-s0`) that change if sections are reordered. Standalone deep dives have inconsistent IDs—some semantic (`#why`), some numeric (`#s3`)—and there is no visible affordance to copy a link to a section.

### Requirements

- **R1.** Every major section (`h2`) in every standalone deep-dive file has a stable, unique `id`.
- **R2.** Every major section (`h2`) inside every workbook overlay has a stable, unique `id` that matches its standalone counterpart so the same fragment works in both contexts.
- **R3.** Every workbook module and every topic is reachable by a stable fragment (`#<module-id>` and `#<topic-id>`).
- **R4.** Visiting a URL with a fragment scrolls to and reveals the target: standalone files scroll naturally; the workbook opens the correct overlay and scrolls to the section, or scrolls to a module/topic.
- **R5.** A lightweight anchor-link affordance lets users copy the current URL plus fragment for any `h2` section in standalone files and overlays.
- **R6.** `scripts/validate.py` enforces the new anchor contract (unique IDs, no missing `h2` IDs in deep-dive bodies).
- **R7.** The authoring guide documents how to assign stable IDs when adding or editing deep dives.

### Scope Boundaries

#### In scope
- Standalone deep-dive files in `deep-dives/*.html`.
- Embedded overlays in `workbook/agentic-development-study.html`.
- Module/topic rendering code in the workbook trailing `<script>`.
- `scripts/validate.py`.
- `docs/AUTHORING-GUIDE.md` anchor conventions.

#### Deferred to follow-up work
- Pretty URL routing or server-side redirects (site is static, zero-build).
- Anchor history/back-button integration beyond default browser behavior.
- Linking to individual paragraphs or list items below `h2` granularity.

---

## Planning Contract

### Key Technical Decisions

- **KTD1. Preserve existing IDs.** Standalone files already use a mix of semantic (`#why`) and numeric (`#s3`) IDs. Keep existing IDs to avoid breaking existing links; only backfill missing IDs.
- **KTD2. Overlay IDs must mirror standalone IDs.** The same body content appears twice (standalone + overlay). The overlay `h2` IDs must equal the standalone IDs so a fragment is portable between the two views. Where the standalone body already has IDs, copy them into the overlay body verbatim.
- **KTD3. Use data IDs for workbook modules/topics.** Module `id` values (`eng-…`, `prod-…`, etc.) and topic `id` values are frozen stable keys already used for progress storage; reuse them as DOM `id` attributes. This avoids inventing a second namespace.
- **KTD4. Client-side fragment routing only.** No build step or server rewrite. Intercept `hashchange` and initial `location.hash` in the workbook script to open overlays and scroll; standalone files rely on native fragment scrolling.
- **KTD5. Anchor links injected by JS, not duplicated markup.** To keep the hand-authored body clean and avoid authoring-guide churn, add the copy-link affordance at runtime for overlay `h2` elements. For standalone files, inject at runtime as well so the authoring recipe stays unchanged.

### Assumptions
- The standalone and overlay bodies are kept in sync by the existing authoring recipe; overlay bodies are exact copies of standalone bodies except for wrapper markup.
- `id` collisions within a page are accidental, not intentional.
- Browser `localStorage` progress keys remain unchanged; this work only adds DOM IDs, it does not rename topic/module IDs.

---

## Implementation Units

### U1. Audit existing anchors

**Goal:** Produce an inventory of all existing IDs in standalone deep-dives and workbook overlays, identifying missing `h2` IDs and duplicates.

**Requirements:** R1, R2

**Files:** `deep-dives/*.html`, `workbook/agentic-development-study.html`

**Approach:**
- Run a small ad-hoc script (Python or Node) that parses each standalone deep-dive and the workbook overlay bodies.
- List every `h2` and its `id`, flag missing IDs, and flag duplicate IDs within a document.
- Note which overlays already have hardcoded `h2` IDs and which rely on the runtime `ov.id+'-s'+i` fallback.

**Test scenarios:**
- Audit reports zero missing `h2` IDs in standalone files after U2 is complete.
- Audit reports zero duplicate IDs within any single file after fixes.

**Verification:** Audit script output is saved as a temporary note; the final state has no missing `h2` IDs.

---

### U2. Stabilize IDs in standalone deep-dive files

**Goal:** Ensure every `h2` in every standalone deep-dive has a stable, unique `id`.

**Requirements:** R1

**Dependencies:** U1

**Files:** `deep-dives/*.html`

**Approach:**
- Keep existing semantic IDs unchanged.
- For missing IDs, assign a numeric `id="sN"` matching the visible section number (the `<span class="n">N</span>`), because the authoring guide already expects this convention and the user explicitly references "bod 3".
- Fix any duplicate IDs by appending a disambiguating suffix only when duplication cannot be resolved by renumbering.

**Patterns to follow:** Existing `E2-context-engineering-deepdive.html` uses `id="s0"`…`id="s7"`; follow this pattern for consistency.

**Test scenarios:**
- Happy path: every `h2` in every standalone deep-dive has a non-empty `id`.
- Edge case: two `h2` elements with identical generated slugs are disambiguated without breaking visible numbering.
- Error path: validate.py fails if any standalone deep-dive `h2` lacks an id after this unit.

**Verification:** `python3 scripts/validate.py` passes the new anchor check.

---

### U3. Stabilize IDs in workbook overlays

**Goal:** Ensure every overlay `h2` has a stable `id` matching its standalone counterpart, and stop the runtime generator from overriding stable IDs.

**Requirements:** R2

**Dependencies:** U2

**Files:** `workbook/agentic-development-study.html`

**Approach:**
- Copy the updated standalone bodies (with stable IDs) back into the matching workbook overlays using the existing byte-for-byte replacement recipe from `docs/AUTHORING-GUIDE.md`.
- Modify the section-nav builder (around line 11866) so it only generates a fallback ID when an `h2` has no id: `if(!h.id) h.id = ov.id+'-s'+i;`.
- Add a validation-time check that no overlay `h2` ends up with a generated positional ID after this work.

**Patterns to follow:** Existing overlay close/open handlers and section-nav builder.

**Test scenarios:**
- Happy path: `workbook/agentic-development-study.html#e2ov-s3` scrolls to E2 section 3 in the overlay.
- Edge case: reordering sections in a future edit does not change existing semantic IDs.
- Error path: `validate.py` flags any overlay `h2` whose id starts with `<ov.id>-s` after U3.

**Verification:** Audit shows no generated positional IDs on overlay `h2` elements.

---

### U4. Add fragment routing to the workbook

**Goal:** Visiting a fragment URL in the workbook opens the right overlay or scrolls to the right module/topic.

**Requirements:** R3, R4

**Dependencies:** U3

**Files:** `workbook/agentic-development-study.html`

**Approach:**
- In the trailing `<script>`, add a `handleFragment()` function that runs on `DOMContentLoaded` and on `hashchange`.
- If the hash matches an overlay section id (`#<overlay-id>-<section-id>` or simply `#<section-id>` when the overlay is already identifiable), open the overlay and scroll its panel to the section.
- If the hash matches a module id (`#<module-id>`), scroll to that module and ensure it is rendered.
- If the hash matches a topic id (`#<topic-id>`), scroll to the topic and expand it.
- Reuse existing `goTo` logic from the section-nav builder where possible.

**Test scenarios:**
- Happy path: `.../workbook/agentic-development-study.html#e2-s3` opens E2 overlay and scrolls to section 3.
- Happy path: `.../workbook/agentic-development-study.html#eng-context` scrolls to the Context topic and expands it.
- Edge case: fragment refers to a hidden topic (filtered out by search) — scroll to it and clear the filter or fail gracefully.
- Error path: unknown fragment is ignored; page loads normally.

**Verification:** Manual browser check on at least one overlay fragment, one module fragment, and one topic fragment.

---

### U5. Add anchor-link copy affordance

**Goal:** Let users copy a direct link to any section.

**Requirements:** R5

**Dependencies:** U3

**Files:** `workbook/agentic-development-study.html`, `deep-dives/*.html`

**Approach:**
- Add a small CSS rule for `.anch` (anchor link) that shows a link icon on hover/focus next to `h2` elements.
- In the workbook script, after section nav is built, prepend an anchor link to each overlay `h2` that sets `location.hash` and copies the URL to clipboard on click.
- In standalone files, inject the same affordance with a small script block at the bottom of each file (or a shared inline snippet) so the authoring recipe stays consistent.

**Test scenarios:**
- Happy path: hovering over an `h2` reveals a clickable link icon.
- Happy path: clicking the icon updates the URL fragment and copies the full URL.
- Accessibility path: anchor link has an `aria-label` like "Copy link to this section".

**Verification:** Visual/manual check in a browser; no console errors.

---

### U6. Extend validation and update authoring guide

**Goal:** Make the anchor contract enforceable and documented.

**Requirements:** R6, R7

**Dependencies:** U2, U3, U5

**Files:** `scripts/validate.py`, `docs/AUTHORING-GUIDE.md`

**Approach:**
- Extend `validate.py` to:
  - Check every `h2` in standalone deep-dive bodies has an `id`.
  - Check every `h2` in workbook overlay bodies has an `id` and that it is not a generated positional ID (`<ov.id>-sN`).
  - Check `id` uniqueness within each document.
  - Keep existing checks (JS parse, HTML balance, SVG well-formed, `#*-deepdive` wiring ×2, topic count).
- Update `docs/AUTHORING-GUIDE.md` Step 2 to state: "give each `<h2>` an `id="sN""`, and add a note that stable IDs must be preserved when editing an existing deep dive.

**Test scenarios:**
- Happy path: `validate.py` passes after all units.
- Failure path: temporarily removing an `id` from an `h2` causes `validate.py` to report the file and line.

**Verification:** `python3 scripts/validate.py` passes.

---

## Verification Contract

Run after every unit and at the end of the branch:

```bash
python3 scripts/validate.py
```

Expected output: JS OK, HTML balanced, 0 SVG errors, all `#*-deepdive` anchors wired ×2, topic count intact, plus the new anchor checks green (no missing `h2` IDs, no duplicate IDs, no generated positional IDs in overlays).

Manual verification in a browser:
1. Open a standalone deep dive with `#s3` fragment — page scrolls to section 3.
2. Open the workbook with `#e2-s3` fragment — E2 overlay opens and scrolls to section 3.
3. Open the workbook with `#eng-context` fragment — page scrolls to and expands the Context topic.
4. Hover over any section heading and click the anchor icon — URL updates and clipboard contains the link.

---

## Definition of Done

- [ ] All standalone deep-dive `h2` elements have stable, unique `id` attributes.
- [ ] All workbook overlay `h2` elements have stable `id` attributes matching their standalone counterparts.
- [ ] Workbook modules and topics are reachable by fragment (`#<module-id>`, `#<topic-id>`).
- [ ] Fragment URLs scroll/open the correct target in both workbook and standalone files.
- [ ] Anchor-link affordance is present and functional on section headings.
- [ ] `scripts/validate.py` passes, including the new anchor checks.
- [ ] `docs/AUTHORING-GUIDE.md` documents the anchor convention.
- [ ] No build step, no new dependencies, no change to progress-storage keys.
