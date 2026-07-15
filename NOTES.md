# Working notes

Freeform scratchpad for the project. Not authoritative — the docs/ files are.
Use this for open questions, session hand-off notes, and things to check before a client meeting.

## Open questions
- (P5/E6) Exact wording of the P1–P5 rung definitions we want to commit to for the client deck.
- (T2) What DORA data can this specific client actually produce from day 0? (unknown until we see them)
- (D-scale) Keep re-confirming D1–D5 framing reads as clearly "original synthesis", not standard.

## Re-verify before any client meeting (point-in-time facts, mid-2026)
- Tool versions / marketplace status: Superpowers, Compound Engineering, BMAD (V6+), Spec Kit, Kiro.
- CVEs and incident dates cited in E5/E7/E8 and M7 Security.
- DORA metric names (the 4th key has been renamed across report years).

## Session hand-off
- 2026-07-15: quality-review session. 4 review agents ran (content ×2, workbook, fact-currency);
  user approved 4 improvement packages (A factual fixes, B 2026 currency, C content extensions,
  D workbook UX). Package A is ~half done (E2/E3 cross-refs, E1 Devin, E8 Böckeler, E6 Faros/
  FlakyGuard/provenance — all in both copies). Remaining: E7 −17% claim, P1 Torres numbers +
  P-scale flag, E4 ~70% flag, CONTENT-MAP id fixes; then packages B, C, D and version bump.
  **Full checkpoint with the complete remaining-work list: Claude memory file
  `improvement-rollout-checkpoint.md` (project memory dir).**
- Also done this session: `.rt`/`.chead` CSS drift fixed in all deep-dives; validate.py extended
  with a CSS-class-coverage check; dead `class="main"` removed from workbook.
- Previous: P2 deep dive added (workbook v1.10). Build recipe: docs/AUTHORING-GUIDE.md.
  Gate: `python3 scripts/validate.py` (green as of this hand-off).
