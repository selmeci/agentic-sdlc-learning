# Roadmap

Where the study programme stands and what to build next. Priorities reflect the engagement
goal: be ready to walk a brownfield client from "why" through a measured pilot to a staged rollout.

## Done

- **Workbook**: 8 modules, 52 topics, 6 research reports, SDLC + Domain map sections. (v1.13)
- **Deep-dive companions (14)**: SDLC Foundations, **E1–E8** (all of M1), **P1–P5** (all of M2).
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

### 3. M3 / M4 / M5 topic deep dives
- **M3 Handoff contract** (H1–H4): the contract anatomy + EARS/Gherkin — directly reusable as
  a client template. High practical value.
- **M4 Information architecture** (I1–I7): durable/derived/disposable, write-permissions,
  agentic search vs RAG, memory.
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
