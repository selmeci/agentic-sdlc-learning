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
- Verified 2026-07-15 for I1 (primary sources): Ahrefs llms.txt study (137,210 domains, 97%
  zero traffic May 2026, 1.1% AI-retrieval fetches — point-in-time, re-verify), AGENTS.md
  stewardship (Agentic AI Foundation / Linux Foundation; "60k+ repos" self-reported,
  fast-moving), Anthropic memory tool GA (memory_20250818, six ops), Solmaz SimpleDoc
  (Dec 22 2025), Kiro .kiro/specs + Spec Kit .specify/memory/constitution.md layouts
  (fast-moving), Tan/Wagner/Treude 28.9%/4.7yr (top-1000 scope), Nygard ADR Nov 15 2011
  (four statuses incl. Deprecated), Cline Memory Bank six files (official docs).
- I5 tension to resolve in its session: workbook says CLAUDE.md "under ~300 lines"; official
  Claude Code docs say "Target under 200 lines. Longer files still load in full but may
  reduce adherence." Reconcile + attribute when I5's deep dive is written.
- Verified 2026-07-15 for D1 (primary sources): Krebs slop audit numbers, NN/g State of UX 2026
  exact quote, Design2Code 49%/64% (GPT-4V-specific), DTCG 2025.10 status (CG deliverable, not
  W3C REC), CodeA11y CHI 2025, Code Connect frameworks, Frost quotes ("natural design system
  consumer" 2023; "machine-readable infrastructure" Dec 2025 — "AI is a new user" is NOT his).

## Next scoped initiative — DARK MODE (evaluated in v1.16, deliberately deferred)
Research backs dark mode as an **opt-in** (light stays default for a reading-heavy artifact;
NN/g + a 2025 tablet study find no fatigue win, and extended-reading legibility slightly favours
light). It was deferred in v1.16 because a *correct* build is a sizeable, higher-regression pass,
not because it lacks merit. When picking it up, do it token-first — do NOT `filter:invert()`:
1. **Tokenize the hardcoded colour.** ~34 unique hex (78 occurrences) live outside `:root` in the
   workbook `<style>` (e.g. `.gbar #DDE4EA`, `.seg #DCE3E9`, `.check #F7F9FB`, `.rc pre #10161C`,
   `.tid #EBEFFA/#D6DDF3`, the `.dmap`/`.e1ov` SVG fill classes `.fA/.fC/.fK/.fG/.fW`,
   `.bxC/.bxA/...`). Promote each to a semantic var on `:root` (`--surface`, `--surface-2`,
   `--code-bg`, `--diagram-*` …). Component CSS already mostly uses vars — this closes the gap.
2. **Add the dark block.** Redefine the token *values* under `@media (prefers-color-scheme:dark)`
   AND `:root[data-theme="dark"]` / `[data-theme="light"]` (toggle must beat the media query both
   ways). Non-pure-black surface (#121212–#1E1E1E, lighter with elevation); desaturate + lighten
   cobalt/amber/pine or they read neon. Verify body ≥4.5:1 (WCAG 2.2 AA), sanity-check with APCA
   (Lc 60–75), 3:1 for large text / UI / focus rings.
3. **Diagrams.** The 74 inline SVG `fill=/stroke=` in body markup are the ragged edge; the arrow
   `marker path` fills (#57656F) can be overridden in CSS (`svg marker path{fill:var(--…)}` beats
   the presentation attribute). The `.dmap`/`.e1ov` fill classes are already CSS — just add dark
   values. Budget for re-checking every diagram in dark.
4. **Toggle + persistence.** A header toggle (near the version button), persisted through the
   existing `store` backend (key `agentic-study-v1`, add a `theme` field) — never scatter raw
   localStorage. Set `data-theme` on `<html>` early (inline head script) to avoid a flash.
5. **×16 files.** Workbook + 15 standalones share the `<head>` tokens — script the token/dark-block
   insertion (mind the Python-apostrophe + brace-expansion build gotchas in CLAUDE.md) and re-run
   `scripts/validate.py`. Screenshot both themes at desktop + mobile before shipping.

## Session hand-off
- 2026-07-15 (I1 session): **I1 deep dive added (v1.24) — M4 opened.** Outline → 3 teammates
  (2 fact-verify + 1 discovery) → spot-verification on discovery sources (caught a fabricated
  ".claudeignore"; two path/mechanism corrections). Load-bearing: the I1 src entry
  "Anthropic: memory typology (in-context/external/in-weights/cache)" **retired as
  unpinnable** (no primary source — third-party blogs only; replaced in src). Triad confirmed
  as Report-3 synthesis → flagged like D1–D5 (precedents: Majors durable/disposable code,
  records-management retention classes, never-hand-edit tooling conventions). I2 wording
  fixed: ADR statuses + Deprecated; feature_list.json → "JSON feature-list pattern".
  **Real bug fixed:** H2/H3/H4 *standalones* lacked `<main>` → desktop grid zigzagged content
  into the 210px TOC column (verified + fixed in-browser; overlays/mobile were fine, hence
  unnoticed). New re-verify items below. Validator green.
- 2026-07-15 (H4 session): **H4 deep dive added (v1.23) — M3 complete.** Outline → 3 teammates
  (2 fact-verify + 1 discovery) → spot-verification round on discovered sources (caught a
  misattributed ClarifyCodeBench figure — numbers kept out) → write → assemble per
  AUTHORING-GUIDE. Retired the unpinnable "30-min→3h" line in all copies; Kiro RA 60% figure
  relabelled as AWS-internal-via-The-New-Stack; reqproof quotes pinned to Bugaev May 2026.
  New re-verify items: HiL-Bench/Orchid/fix-PR/MSR-2026 arXiv preprints (point-in-time),
  Devin 2.1 confidence UX, Copilot/Codex plan-mode asking. CONTENT-MAP companion count fixed
  (15→19, had drifted since H1). Validator green.
- 2026-07-15 (design/responsive session): **v1.16 responsive & wayfinding pass.** Design skill +
  1 research teammate (2025–26 study-material/mobile/dark-mode best practice). Rendered the
  workbook at 390px → confirmed the dense SVG diagrams were squished to illegibility (the headline
  problem). Fix: JS wraps every diagram SVG in `.figwrap>.figscroll`; <760px they keep a legible
  min-width and scroll horizontally (fade + scrollbar cue), captions stay outside. Added scroll-spy
  nav highlight, top reading-progress line, back-to-top; bigger mobile tap targets; fluid `clamp()`
  headings. Mirrored diagram-fix + back-to-top into all 15 standalones. Validator green; desktop
  pixel-unchanged (min-width only engages on narrow screens). Dark mode evaluated & deferred (see
  the scoped initiative above).
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
