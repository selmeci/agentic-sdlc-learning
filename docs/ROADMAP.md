# Roadmap

Where the study programme stands and what to build next. Priorities reflect the engagement
goal: be ready to walk a brownfield client from "why" through a measured pilot to a staged rollout.

## Done

- **Workbook**: 8 modules, 52 topics, 6 research reports, SDLC + Domain map sections. (v1.15)
- **Deep-dive companions (20)**: SDLC Foundations, **E1–E8** (all of M1), **P1–P5** (all of M2),
  **D1** (first of M6), **H1–H4** (all of M3), **I1** (first of M4).
- Cross-cutting **M7 Security** module + two security domain-map views.
- Three autonomy scales in place: **L1–L5**, **P1–P5**, **D1–D5** (D-scale flagged as original).

## Next (in suggested order)

### 1. ~~Finish M2 — Product harness deep dives (P3–P5)~~ — **DONE**
- ~~**P2** `prod-prd` — PRDs & requirements with AI~~ — **done (v1.8)**.
- ~~**P3** `prod-decomposition` — decomposition into agent-ready work items~~ — **done (v1.11)**.
- ~~**P4** `prod-pm-role` — the PM from author to editor/curator~~ — **done (v1.12)**.
- ~~**P5** `prod-scale` — the P1–P5 assistance scale itself~~ — **done (v1.13)**. M2 complete:
  all five product-harness topics have deep-dive companions.

### 2. M6 — Design harness deep dives (D1–D7)
Highest-novelty area because **D1–D5 is our original synthesis** — the deep dives are where we
justify it carefully and keep flagging it as non-standard. D2 (DTCG tokens) and D5 (design
harness: Stylelint/visual-regression/axe-core) are the most concrete.
- ~~**D1** `des-artifact` — the design system as the third handoff artifact~~ — **done (v1.15)**,
  with a fact re-verification pass (Frost quotes, Krebs audit, Storybook figures unsourced →
  reframed) and new sources (Indeed/Wolosin benchmark, Meta Astryx, arXiv:2603.13036).
- Next: **D2** (tokens/DTCG) or **D5** (the harness) — the two most concrete.

### 3. M3 / M4 / M5 topic deep dives
- **M3 Handoff contract** (H1–H4): the contract anatomy + EARS/Gherkin — directly reusable as
  a client template. High practical value.
  - ~~**H1** `hand-anatomy` — anatomy of the handoff contract~~ — **done (v1.17)**, with a
    three-agent fact-verification pass (Spec Kit v0.12 template drift, amux retired,
    "BDD's second chance" → Adzic's verified framing, arXiv:2603.15911 as the 29.6/4.1 source,
    Kiro GA vs Requirements Analysis timeline split) and new sources (Grove's The New Code,
    Devin task guidance, Osmani's boundary tiers, SWE-Bench+ audit). Introduced the T0–T2
    contract sizing tiers (our synthesis).
  - ~~**H2** `hand-ears-gherkin` — EARS & Gherkin: machine-verifiable AC~~ — **done (v1.20)**,
    with a three-teammate fact pass (EARS co-authors credited, adopter roster reframed as
    creator-self-reported, GWT dated ~2004 North & Matts, SpecFlow EOL → Reqnroll, ClarifyGPT
    11.52% confirmed relative, Bashir 20.2% reframed 10-shot-vs-0-shot, Wang +23.2 pp confirmed)
    and discovery sources (Mathews & Nagappan ASE 2024 tests-in-prompt, SWE-bench Verified
    FAIL_TO_PASS oracle, AutoUAT/TestFlow, QVscribe, Automation Panda Gherkin-guidelines-for-AI).
  - ~~**H3** `hand-traceability` — traceability & spec modes~~ — **done (v1.22)**, with a
    three-teammate fact pass (the "~64% ML traceability accuracy" figure retired as unpinnable,
    "Martin Böckeler" → Birgitta Böckeler fixed in E8, Beck's Dec-2025 verbatim wording, Kiro
    Sync-Files-not-drift-detection precision, Tessl Jan-2026 pivot flagged) and discovery
    sources (AIDev census arXiv:2606.24429, ReqToCode arXiv:2603.13999, RE:FSQ 2025 RAG TLR,
    Assisted-by/Co-authored-by trailer debate, EU AI Act Art. 11). Added a provenance section
    and the five-move minimal ID scheme (our synthesis).
  - ~~**H4** `hand-feedback` — feedback loop & handoff anti-patterns~~ — **done (v1.23)**,
    completing M3. Three-teammate fact pass + a spot-verification round that caught one
    misattributed discovery figure (ClarifyCodeBench). Load-bearing new evidence: HumanEvalComm
    (TOSEM 2025, >60% code-instead-of-asking), HiL-Bench (67–88%→1–9%), Kiro Requirements
    Analysis primary source (LLM+SMT, May 2026), reqproof triage question pinned (Bugaev,
    May 2026), unmerged-fix-PR taxonomy (26.1% of 8,106), MSR 2026 reviewer-engagement study,
    DORA 2025 Rework Rate as loop-health anchor. Retired: the "30-min feature balloons to 3 h"
    line (unpinnable); Boehm 100:1 flagged folklore. Minimal return-channel protocol added
    (our synthesis). M3 complete.
- **M4 Information architecture** (I1–I7): durable/derived/disposable, write-permissions,
  agentic search vs RAG, memory.
  - ~~**I1** `ia-taxonomy` — artifact taxonomy: durable / derived / disposable~~ — **done
    (v1.24)**, with a three-teammate fact pass (the "Anthropic memory typology" source
    retired as unpinnable; triad confirmed as our synthesis and flagged; ADR statuses +
    AGENTS.md stewardship corrected) and a spot-verified discovery round (Ahrefs llms.txt
    97%-zero-traffic study, Solmaz SimpleDoc, Kiro/Spec Kit spec layouts, Cline Memory
    Bank; a fabricated ".claudeignore" caught). Next: **I2** (write-permissions — builds
    directly on I1) or **I4** (memory).
- **M5 Brownfield bootstrap** (B1–B6): the safe ordering, characterization/golden-master,
  mutation gate (B3 already cross-referenced from E4), strangler-fig + heatmap.

### 4. Trajectory research (M8, the backlog) — turn T-topics into real modules
These are the client-facing deliverables; each needs a research pass before a deep dive.
- **T2 Measurement & pilot design** — highest priority: the DORA + METR method from E7 becomes
  a concrete pilot playbook (baseline, A/B, pre-registered success, perception-gap capture).
- **T1 Economics & the business case** — the number that gets the engagement approved.
- **T7 Organizational governance**, **T3 change management**, **T5 harness as internal product**,
  **T6 vendor strategy / lock-in**, **T4 compliance / EU context**.

## Content maintenance (ongoing)
- **Re-verify fast-moving tool facts** before any client meeting: versions, marketplace status,
  star counts, CVEs, DORA metric names. All are point-in-time (mid-2026).
- Keep **honest source separation**: strong independent evidence vs vendor claims vs synthesis.
- Keep **D1–D5** flagged as an original synthesis everywhere it appears.

## Possible toolchain evolution (only if it earns its keep)
The single-file, zero-build approach is a feature (portable, hostable, no deps). If the set
grows enough that duplication hurts, consider — in this order:
1. Extract the shared `<head>` + CSS into one `assets/base.css` / template and have a small
   build step inline it (keeps outputs single-file for hosting).
2. Author deep-dive bodies as Markdown + a generator that emits both the standalone file and
   the workbook overlay from one source (removes the "two copies in sync" burden).
3. A tiny test/validate CI step wrapping `scripts/validate.py` on every commit.
Do **not** adopt a heavy SPA framework — it would trade away the portability that makes these
useful as shareable client materials.

## Definition of "done" for the engagement-readiness milestone
- All of M1–M7 have deep-dive companions (or a deliberate decision that a module doesn't need one).
- T1 + T2 promoted from trajectory to real modules (business case + pilot playbook).
- A one-page "client narrative" that threads SDLC → framework → autonomy → pilot → rollout,
  pulling from the existing sections.
