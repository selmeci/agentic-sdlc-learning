---
title: Gallery Review Findings Fixes - Plan
type: fix
date: 2026-07-20
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
product_contract_source: ce-plan-bootstrap
execution: code
---

## Goal Capsule

Close every open finding from the ce-code-review of `feature/gallery` (run `20260720-162358-05426287`). Six of seven findings were already applied and committed in `8cf17d0`; this plan covers what remains: finding #5 (workbook relative gallery link vs. CLAUDE.md golden rule 3) and the two agent-native gaps (gallery step missing from the CLAUDE.md recipe, un-gitignored draft registry scratch file). Stop conditions: `python3 scripts/validate.py` stays green, no behavior change to any HTML artifact, no new untracked files from the documented draft workflow.

## Product Contract

### Summary

Amend CLAUDE.md so the workbook's existing gallery link is legal and the deep-dive recipe names the gallery step, and gitignore the draft-registry scratch file. Documentation/config only — no generated artifact changes.

### Problem Frame

The gallery branch shipped with three loose ends the review could not auto-fix. The workbook footer link to `../gallery.html` contradicts golden rule 3 as written, leaving the standing prompt in conflict with shipped behavior. The CLAUDE.md "typical next task" recipe still ends at `validate.py`, so an agent following it produces deep dives without gallery registration (recovered only by the validator going red later). And the documented `--draft-registry` workflow leaves an untracked scratch file in the repo root.

### Requirements

**Standing prompt (CLAUDE.md)**

- R1. Golden rule 3 gains an explicit, narrowly-scoped exemption for site-level navigation links to root pages (e.g. `gallery.html`), resolving review finding #5 while keeping the workbook footer link in place.
- R2. The "typical next task" recipe includes registering new figures in `gallery-registry.json` and regenerating `gallery.html`, consistent with `docs/AUTHORING-GUIDE.md` Step 7.

**Repo hygiene**

- R3. `gallery-registry-draft.json` is covered by `.gitignore`, so the documented draft workflow leaves no untracked scratch file.

## Planning Contract

### Key Technical Decisions

- KTD1. Resolve #5 by **amending rule 3, not by delinking**. `gallery.html` is a site-level index page; `index.html` already navigates by relative links; GitHub Pages is the primary consumption surface. The exemption is scoped to site-level navigation (header/footer links to root pages) — deep-dive cross-references inside the workbook stay overlay-only, preserving rule 3's original intent (the single-file hosted preview must not 404 on sibling deep dives).
- KTD2. **No validator check for relative links in this plan.** project-standards suggested one, but a deterministic check would have to encode KTD1's exemption precisely; premature now, revisited if site-level links proliferate. Deferred (see Scope Boundaries).

### Assumptions

- A1. The user accepts KTD1 as the resolution of #5 (keep the link, amend the rule). If they prefer delinking instead, U1's rule-3 edit is dropped and the workbook footer anchor becomes a plain-text mention — see Open Questions, OQ1.

### Open Questions

- OQ1 (deferred; default chosen in KTD1/A1): keep the workbook `../gallery.html` link with a rule-3 exemption, or delink. Non-blocking because the review validated the link works on GitHub Pages and the plan's default preserves shipped behavior.

## Implementation Units

### U1. Amend CLAUDE.md rule 3 exemption and recipe gallery step

**Goal:** Make the standing prompt consistent with the shipped gallery feature.
**Requirements:** R1, R2
**Dependencies:** none
**Files:** `CLAUDE.md`
**Approach:** Edit golden rule 3 (currently lines 23-25) to state the exemption in one sentence: deep-dive cross-references remain overlay-only; site-level navigation to root pages (`gallery.html`, `index.html`) may use relative links. Extend "The typical next task" (lines 60-69) with the gallery registration step, pointing at `docs/AUTHORING-GUIDE.md` Step 7 rather than duplicating it. Match the file's existing dense, numbered style. No other rules touched.
**Patterns to follow:** The existing rule 3 wording and recipe format in `CLAUDE.md`; the gallery step wording in `docs/AUTHORING-GUIDE.md` Step 7.
**Test scenarios:**
- Rule 3 as edited permits `workbook/agentic-development-study.html`'s `<a href="../gallery.html">` while still prohibiting relative links between deep dives (read-back check).
- The recipe text names `gallery-registry.json` and `gallery.html` regeneration.
- `python3 scripts/validate.py` passes (docs edit must not break any gate).
**Verification:** A reader can no longer find a contradiction between rule 3 and the workbook footer link; an agent following the recipe registers diagrams in the gallery without being told separately.

### U2. Gitignore the draft registry scratch file

**Goal:** The documented `--draft-registry` workflow leaves the repo clean.
**Requirements:** R3
**Dependencies:** none
**Files:** `.gitignore`
**Approach:** Add a single `gallery-registry-draft.json` entry, following the file's existing grouping/comment style. The generator's `--draft-registry` output path (`scripts/generate-gallery.py`, repo root) is unchanged — this is hygiene, not behavior.
**Test scenarios:**
- `git check-ignore gallery-registry-draft.json` exits 0.
- Run `python3 scripts/generate-gallery.py --draft-registry`, confirm `git status --porcelain` shows no new untracked entry, then delete the scratch file.
- `python3 scripts/validate.py` passes.
**Verification:** The draft workflow documented in AUTHORING-GUIDE Step 7 produces no untracked noise.

## Verification Contract

- `python3 scripts/validate.py` — must pass after every unit (the repo's deterministic gate).
- `git check-ignore gallery-registry-draft.json` — exits 0 after U2.
- `git status --porcelain` — no untracked `gallery-registry-draft.json` after exercising `--draft-registry`.
- Read-back of edited CLAUDE.md sections against R1/R2 wording above.

## Definition of Done

- R1-R3 implemented in `CLAUDE.md` and `.gitignore`.
- `python3 scripts/validate.py` green; no HTML artifact modified; `gallery.html` untouched (freshness check stays green).
- Work committed on `feature/gallery` (docs/chore commits per repo convention).
- No abandoned-attempt edits left in the diff.

## Scope Boundaries

### Deferred to Follow-Up Work

- Python unit-test harness for `generate-gallery.py` pure functions (`prefix_svg_ids`, `scope_edge_css`, `inject_missing_markers`) — the repo has no Python test runner today; introducing one is a separate decision.
- Validator self-tests proving each gallery check fails when it should (verified manually during the review).
- Structural DOM checks on generated `gallery.html` (id uniqueness, `url(#...)` resolution) beyond the byte-compare freshness gate.
- Deterministic validator check for cross-artifact relative links (KTD2 — blocked on the exemption settling in practice).
- Capturing gallery patterns into a future `docs/solutions/` corpus (learnings-researcher recommendation; no corpus exists yet).
- `docs/CONTENT-MAP.md` hardcodes "all 74 diagrams" — prose count will drift; no mechanism proposed in this plan.

## Sources & Research

- ce-code-review run `20260720-162358-05426287` on `feature/gallery` — finding #5 (project-standards, validated), agent-native gaps 1 and 3; fixes #1-#4, #6, #7 already applied in commit `8cf17d0`. (Agent-native gap 2 — the workbook relative-link observation — is the same issue as finding #5, covered by R1/KTD1.)
- `docs/superpowers/plans/2026-07-20-gallery.md` — original gallery plan (Task 6 requested the workbook link #5 questions).
- `docs/AUTHORING-GUIDE.md` — Step 7 gallery maintenance workflow.
