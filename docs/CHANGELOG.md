# Changelog

Version history of the workbook (`workbook/agentic-development-study.html`). Mirrors the
in-app version-history modal (top-bar button). Dates are when the work was done in-session.

## v1.18 · 2026-07-15
**Table responsiveness follow-up** (consistency with the v1.16 pass): the five `table.map`
tables in E7 (2) and E8 (3) are now wrapped in the same `.figscroll` container the diagrams
use, so below 760px they scroll horizontally in their own box instead of overflowing the page —
matching how the H1 deep dive ships its tables. Applied in both copies (standalone files and
the workbook overlays). No content changes. Remaining bare tables in E1–E6, P1–P5, D1, SDLC
and the workbook map sections are noted as a possible follow-up sweep. Validator green.

## v1.17 · 2026-07-15
**H1 deep-dive companion — Anatomy of the handoff contract** (opens the M3 deep-dive set):
- New deep dive, embedded overlay + standalone `deep-dives/H1-handoff-contract-anatomy-deepdive.html`:
  the amnesia test, the six components with per-component failure modes and owners, the spec-review
  gate (with the 10-minute / seven-question review checklist), three-amigos ownership, the T0–T2
  contract sizing tiers (answering the topic's minimal-contract open question), and the annotated
  TASK-042 walkthrough. Two new SVG figures (marker `ahH1a`, edge class `edH1`).
- **Fact verification pass behind it** (three research agents, 2026-07-15):
  - The six-part anatomy is explicitly flagged as **Report 2's synthesis** — re-verification showed
    Spec Kit v0.12.x dropped its dedicated non-goals/out-of-scope section (checklists moved to
    `/speckit.checklist`), so "converging across tools" was reworded; **amux retired** as a
    reference (it is a parallel-agent multiplexer, not a contract format) in the M3 research note.
  - The unattributable **"BDD's second chance" quote retired**; replaced with Gojko Adzic's verified
    framing ("Specification by Example taken to a new level — or the revenge of Waterfall").
  - The 29.6-vs-4.1 tokens/line review-density figures now carry their correct source:
    **arXiv:2603.15911** (2026; 278,790 review conversations, 300 OSS projects; ARA cluster 11.3).
  - Kiro timeline split precisely: GA (Nov 17, 2025) = property-based testing; the LLM+SMT
    **Requirements Analysis** contradiction prover is a 2026 addition (~60% of 1,400+ first-draft
    AC needed refinement, vendor-reported).
  - DoD provenance corrected to "since the first Scrum Guide (2010); 2020 makes it the Increment's
    commitment".
- New sources adopted: Sean Grove's *The New Code* (AI Engineer World's Fair, Jun 2025), Cognition's
  Devin task guidance, Addy Osmani's three-tier boundaries (always/ask-first/never), the SWE-Bench+
  weak-oracle audit (arXiv:2410.06992), Fowler's SDD counter-view, agents.md disambiguation.
- Topic `hand-anatomy` enriched: new know bullet (synthesis provenance + T0–T2 tiers), new concept,
  deep-dive link as first source.
- Also repaired five double-encoded UTF-8 characters left over from v1.15 (four em dashes, ×, −).

Validator green: JS parse, HTML balance, all SVGs well-formed, CSS-class coverage, `#h1-deepdive`
wired ×2 (+1 handler), topic count 52, CONTENT-MAP id match.

## v1.16 · 2026-07-15
**Responsive & wayfinding pass** (design-led review of the whole artifact set — no content
or topic-id changes; desktop layout unchanged):
- **Mobile diagram legibility (the headline fix).** The dense inline SVG diagrams (viewBox
  860–980 units wide) were being squished to ~350px on phones, rendering their labels at
  ~3–4px — illegible. Each diagram SVG is now wrapped (via JS) in a `.figwrap > .figscroll`
  pair: below 760px it keeps a legible min-width (700px for the SDLC/Domain maps, 560px for
  deep-dive figures) and scrolls horizontally, with a right-edge fade + thin styled scrollbar
  as the affordance. Captions/prose stay outside the scroller and wrap to the viewport, so the
  page body never scrolls sideways. Applied in the workbook (map sections + embedded overlays)
  and mirrored into all 15 standalone deep-dives.
- **Orientation / wayfinding.** Intersectionless scroll-spy (rAF scroll handler) highlights the
  module currently in view in the sidebar `.mnav`; a 2.5px reading-position line sits at the top
  of the sticky header; a floating back-to-top button (46px, reduced-motion aware) appears past
  640px of scroll. Standalone deep-dives get the back-to-top too.
- **Touch targets & fluid scale.** Mobile tap targets enlarged toward WCAG 2.2 target-size
  (status toggles, filter chips, view/data buttons, map tabs); the largest headings
  (`.mod-head h2`, overlay `.body h2`, standalone `h2`) are now fluid via `clamp()` with
  `text-wrap:balance`.
- **Storage / IDs / persistence:** untouched (`agentic-study-v1`, all topic ids frozen).
- **Dark mode — evaluated, deferred (deliberate).** Research (NN/g, WCAG 2.2, APCA, 2025 studies)
  supports dark mode as an *opt-in*, with light remaining the right default for a reading-heavy
  artifact. A *correct* implementation would touch ~150 colour points in the workbook alone
  (78 CSS + 74 inline SVG fills) plus recolour every diagram, ×16 files — a sizeable, higher-
  regression initiative. Rather than ship a half-themed diagram set, it is scoped as the next
  dedicated pass: tokenize the ~34 hardcoded hex into semantic vars, add a `[data-theme]` +
  `prefers-color-scheme` block (non-pure-black surfaces, desaturated cobalt/amber/pine), a
  header toggle persisted through the existing `store`, and dark overrides for the diagram
  CSS classes + `marker path` fills. Tracked in `NOTES.md`.

Validator (`scripts/validate.py`) green: HTML balance, 30 well-formed SVGs, CSS-class coverage,
deep-dive wiring, topic count 52, CONTENT-MAP id match.

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
