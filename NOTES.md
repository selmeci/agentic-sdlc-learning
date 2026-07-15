# Working notes

Freeform scratchpad for the project. Not authoritative — the docs/ files are.
Use this for open questions, session hand-off notes, and things to check before a client meeting.

## Open questions
- (P5/E6) Exact wording of the P1–P5 rung definitions we want to commit to for the client deck.
- (T2) What DORA data can this specific client actually produce from day 0? (unknown until we see them)
- (D-scale) Keep re-confirming D1–D5 framing reads as clearly "original synthesis", not standard.

## Re-verify before any client meeting (point-in-time facts)
- Tool versions / status: verified 2026-07-15 against primary sources (Kiro GA Nov 2025,
  Spec Kit v0.11, Superpowers v5.x, BMAD v6.8, Claude Code 2026 surface) — re-verify if
  older than a month at meeting time.
- DORA: 2025 report incorporated (Rework Rate 5th metric, AI Capabilities Model); the 2026
  report is expected fall 2026 — check for it before any meeting after that.
- METR: Feb-2026 follow-up incorporated (self-flagged "very weak evidence"); watch for the
  redesigned experiment's results.
- CVEs and incident dates cited in E5/E7/E8 and M7 Security (all checked out on 2026-07-14).
- Still unverified: Superpowers "Anthropic marketplace, Jan 2026" claim (softened in E8);
  the Anthropic −17% comprehension RCT (no primary source located — softened in E7);
  Uber FlakyGuard exact numbers (attributed + re-verify flag in E6);
  Storybook MCP benchmark figures +12.8%/2.76×/−27% (no published source found 2026-07-15 —
  reframed as unquantified vendor claim in M6 notes, D3 topic and the D1 deep dive);
  Meta Astryx details (13k apps, component counts — vendor press coverage only, flagged in D1).
- Verified 2026-07-15 for D1 (primary sources): Krebs slop audit numbers, NN/g State of UX 2026
  exact quote, Design2Code 49%/64% (GPT-4V-specific), DTCG 2025.10 status (CG deliverable, not
  W3C REC), CodeA11y CHI 2025, Code Connect frameworks, Frost quotes ("natural design system
  consumer" 2023; "machine-readable infrastructure" Dec 2025 — "AI is a new user" is NOT his).

## Session hand-off
- 2026-07-15 (later session): **D1 deep dive added (v1.15)** — outline → 3 research teammates
  (2 fact-verification, 1 discovery) → write → assemble per AUTHORING-GUIDE. Fact corrections
  applied workbook-wide (Storybook figures, Frost quote, CodeA11y). New sources adopted:
  Indeed/Wolosin, Meta Astryx, arXiv:2603.13036, shadcn-as-default. Validator green.
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
