# Changelog

Version history of the workbook (`workbook/agentic-development-study.html`). Mirrors the
in-app version-history modal (top-bar button). Dates are when the work was done in-session.

## v1.15 · 2026-07-15
**Added the D1 deep-dive companion** (The design system as the third handoff artifact) —
opening the M6 design-harness set (embedded overlay `#d1-deepdive` + standalone
`deep-dives/D1-design-system-artifact-deepdive.html`):
- The third-artifact thesis (contract = what, codebase+harness = how/prove, design system =
  what it must look like), explicitly flagged as Report 5's original synthesis.
- Machine-readable infrastructure with verified primary-source Frost quotes; the Coverage +
  Validation pillars cited precisely as spoken remarks (Storybook/Chromatic webinar, Dec 2025).
- AI slop: Krebs audit (all numbers re-verified against adriankrebs.ch, Apr 2026) + the
  design-homogenization review (Shin et al., arXiv:2603.13036) as the academic backbone.
- The five layers of the artifact (tokens / APIs / mappings / stories / direction), each with
  its deterministic gate; evidence table incl. the new Indeed/Wolosin machine-readable
  benchmark (1,056 prompts × 8 MCP configs) and Meta Astryx + shadcn/ui exhibits.
- Conformance-vs-judgment as the thesis's precise scope; CodeA11y (CHI 2025) correctly cited.

**Fact re-verification pass** (3 research agents, primary sources, 2026-07-15) applied
workbook-wide:
- Storybook MCP benchmark figures (+12.8% / 2.76× / −27%) could not be traced to any published
  source — reframed as an unquantified vendor claim in the M6 research notes and D3 topic.
- Brad Frost "AI is a new user" corrected to the verified "AI is a natural design system
  consumer" (Feb 2023) / "machine-readable infrastructure" (Dec 2025); NN/g State of UX 2026
  quote tightened to the exact wording.
- CHI 2025 a11y finding precisely attributed: CodeA11y (Mowar et al.), "routinely omit
  accessibility features", not "systematically generate inaccessible markup".

## v1.14 · 2026-07-15
**Quality-review pass** across the workbook + all deep dives (four parallel review agents +
a web fact-currency sweep), followed by four approved improvement packages:
- **Factual fixes**: stale "memory (E4)" cross-refs in E2/E3 → E1 memory component / M4;
  E1 Devin phrasing (completed 3/20, not "3/20 failures"); E8 SDD critique attributed to
  **Birgitta Böckeler** (martinfowler.com), not Fowler; Faros AI flagged as vendor telemetry
  (E6/E7); scale provenance made honest (L1–L5 adapted from industry ladders; P1–P5 + D1–D5
  original synthesis); unsourced hard numbers softened to practitioner estimates (Torres
  20–40%/~5%, Anthropic −17%, the ~70% mutation bar); CONTENT-MAP topic ids corrected (8).
- **2026 currency**: E7 gains DORA 2025 (Rework Rate as official 5th metric, AI Capabilities
  Model, "faster but not safer" reversal) and the METR Feb-2026 follow-up (−4% CI −15…+9,
  self-flagged selection effects — used as a teaching example); E8 refreshed (Kiro GA +
  property-based spec testing, Spec Kit v0.11 workflow-as-dependency, Superpowers v5 reversal);
  E3 gains the skills/plugins/agent-teams surface + the ICSE 2026 harness-engineering paper;
  E5 gains OWASP Agentic Skills Top 10 + "prompts become shells" + CI/CD supply-chain notes.
- **New content**: E4 §6 "Verification beyond the unit-test oracle" (property-based, agentic
  E2E, rubric-anchored LLM-judge as advisory-only) + fail-fast ladder + flakiness protocol;
  E5 harness-agnostic five-layer control table + credentials callout + config artifact;
  E6 operational rubric, circuit-breaker ("a dial, not a ratchet"), staffing arithmetic;
  E2 cache economics + tool-schema sprawl + empirical rot framing; E8 worked 15-line spec;
  P1 eval checklist, privacy/consent callout, P1–P5 mini-ladder, synthetic-users caveat.
- **Workbook UX**: export/import of progress+notes (JSON), suggested study paths, SDLC in the
  sidebar nav, research-priority badges on T1–T4, second self-checks for the thinnest topics.
- **Toolchain**: `validate.py` now also checks CSS-class coverage (markup vs stylesheet/JS)
  and CONTENT-MAP↔workbook topic-id drift; fixed the `.rt`/`.chead` CSS drift in all
  standalone deep dives.

## v1.13 · 2026-07-15
Added the **P5** deep-dive companion (The P1–P5 assistance scale in the product layer) —
**completing the M2 deep-dive set**. The five levels with per-rung evidence ratings, the
verification asymmetry vs engineering L1–L5 (anchored by the Nature Human Behaviour 2024
meta-analysis: human+AI worse than best alone on decision tasks, g=−0.23), why P5 is the
anti-pattern (Klarna's 2025 reversal, Mitchell et al. 2025, EU AI Act Art. 14 human-oversight
mandate from Aug 2026), AI evals as the emerging partial verification loop (Torres, Husain &
Shankar, criteria drift), and per-artifact level assignment with downshift triggers. P1–P5
flagged as **our synthesis** with named ancestors (Parasuraman/Sheridan/Wickens 2000, Feng et
al. 2025) after a search confirmed no published product-layer equivalent. Also tightened
Bashir/ClarifyGPT citations workbook-wide (Alstom/Westermo datasets; +11.52% is relative;
3.84/5 is a four-criteria average; F1 67–76% by dataset).

## v1.12 · 2026-07-15
Added the **P4** deep-dive companion (The PM: from author to editor and curator) — Cagan's
vulnerable-vs-empowered distinction with verbatim sourcing (A Vision For Product Teams,
Feb 2025), the automation-bias evidence base (Mosier 1998: 55% expert omission errors;
Parasuraman & Manzey 2010: training does not prevent it; Lee et al. CHI 2025: confidence in
GenAI ↔ less critical thinking; Budzyń et al. Lancet 2025: −6 pp clinician deskilling),
**corrected Torres attributions** (the "generating summaries" line is a webinar write-up
paraphrase; her primary figure is ~30% fabricated quotes, Product Talk Oct 2025), the
structural editor toolkit (accountability, spot-checks, kill-rate), and the curator role
(flagged as our synthesis; editor frame credited to Rachitsky 2024).

## v1.11 · 2026-07-15
Added the **P3** deep-dive companion (Decomposition into agent-ready work items) — INVEST
re-read for agents, right-sizing against the METR reliability horizon (80% horizon ~5× below
the headline 50%), the GitLab Duo controlled evidence (splitting helps as a completeness
check, estimating fails at 16% vs 60%; 2026 follow-up: ~59% of AI tasks shipped), the
agent-ready checklist as a lintable refinement gate, and Spec Kit/Kiro task mechanics.
Also **corrected the GitLab Duo citation** everywhere from "Nier et al." to
Pavlič, Saklamaeva & Beranič, Applied Sciences 2024, 14(24):12006.

## v1.10 · 2026-07-14
**Version history moved into a modal** — opened from a version button in the top bar (label
auto-derives from the newest entry) or a footer link. The footer keeps only the current
version + artifact registry; the full v0.1 → current changelog lives in the modal (`#verov`).

## v1.9 · 2026-07-14
Progress and notes now **persist locally in the browser** — the storage layer prefers
`localStorage` (key `agentic-study-v1` unchanged, so artifact-side data is unaffected) and
falls back to the claude.ai `window.storage` wrapper where `localStorage` is blocked.
The save indicator shows the active backend (`loaded · local` / `loaded · artifact`).

## v1.8 · 2026-07-14
Added the **P2** deep-dive companion (PRDs & requirements with AI) — the junior-PM jobs vs
the rationale gap (Quattrocchi et al.), the PR/FAQ kill discipline, requirements red-teaming
as a backlog-refinement gate, and the no-follow-up-questions handoff metric.

## v1.7 · 2026-07-13
Started the **M2 (Product harness)** deep-dive set with an embedded companion for **P1**
(AI-assisted discovery) — two-perspectives method, the lazy-synthesis anti-pattern, AI evals
as the product-layer verification loop.

## v1.6 · 2026-07-13
Expanded **E8 BMAD** coverage (deep dive §2 + topic) — what BMAD is (V6, docs-as-source,
12+ agent roles) and its brownfield path (`*document-project`, respect-conventions, mandatory
Test Architect regression gate), with what to borrow for an existing-system engagement.

## v1.5 · 2026-07-13
Added two how-to sections to **E7** (deep dive §2–§3) — using **DORA** (measurement process,
what to collect, baseline checklist) and **METR** (RCT-style pilot method + prep kit).

## v1.4 · 2026-07-13
Promoted **SDLC** to a full inline section (parallel to the Domain map) with three tabbed
views — stages & components, process-models spectrum, when-to-use-which decision lens.

## v1.3 · 2026-07-13
Added an **SDLC Foundations** intro block (embedded deep dive + standalone file) — what SDLC
means, the process models (Waterfall → DevOps), agentic fit per model, and a decision lens.

## v1.2 · 2026-07-13
Added a **DORA & METR explainer** to E7 (deep dive §1 + topic) — what each is, the four keys,
and whether/how we can use them.

## v1.1 · 2026-07-13
Extended **E8** with the two plugin methodologies — **Superpowers** (within-task discipline)
and **Compound Engineering** (between-task learning loop) — compared on planning, execution,
feedback learning.

## v1.0 · 2026-07-12
Added embedded deep-dive companion for **E8** (Spec-driven development) — completing the full
**E1–E8** engineering-harness deep-dive set.

## v0.6 – v0.11 · 2026-07-12
Added embedded deep-dive companions for **E1–E7** (one or two per version), each openable
in-page from its "Go deeper".

## v0.5 and earlier · 2026-07-11/12
Built the workbook itself: 8 modules / 52 topics, 6 embedded research reports, the Domain map
(5 SVG views incl. security), the M7 Security module, and the P1–P5 / L1–L5 / D1–D5 scales.
Original Slovak v0.1 (`archive/agenticky-vyvoj-studium.html`) preceded the English rebuild.
