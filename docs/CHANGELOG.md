# Changelog

Version history of the workbook (`workbook/agentic-development-study.html`). Mirrors the
in-app version-history modal (top-bar button). Dates are when the work was done in-session.

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
