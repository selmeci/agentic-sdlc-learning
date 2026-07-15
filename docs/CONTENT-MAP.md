# Content map

The complete catalog of the workbook (`workbook/agentic-development-study.html`, v1.13):
8 modules, 52 topics, 6 research reports, 2 inline map sections, 14 deep-dive companions.

> Module **display code** (M1…M8) differs from the internal **data id** in a couple of cases
> for historical reasons — the ids are frozen to preserve user progress. Both are listed.

## Inline map sections (top of the workbook, before the modules)

- **SDLC Foundations** (`#sdlc-sec`) — 3 tabbed SVG views: S1 stages & components,
  S2 process-models spectrum, S3 when-to-use-which decision lens. Links to the SDLC deep dive.
- **Domain map** (`#dmap`) — 5 tabbed SVG views: V1 ArchiMate-style motivation/domains,
  V2 DDD context map, V3 operating loop with gates, V4 lethal trifecta & defense-in-depth,
  V5 per-component threat map.

## Modules & topics (52)

### M1 · Engineering harness (id `m1`) — Report 1; 6 research-note sections
| Topic | id | Deep dive |
|---|---|---|
| E1 Agent = Model + Harness: the seven-component framework | `eng-framework` | ✅ embedded + standalone |
| E2 Context engineering & context rot | `eng-context` | ✅ |
| E3 Harness engineering in practice (Anthropic patterns) | `eng-harness` | ✅ |
| E4 Verification-first: TDD as the loop, protecting the tests | `eng-verification` | ✅ (incl. mutation-testing §5) |
| E5 Governance: hooks, permissions, the lethal trifecta | `eng-governance` | ✅ |
| E6 The L1–L5 autonomy taxonomy | `eng-autonomy` | ✅ |
| E7 Metrics & anti-patterns: what the hard data says | `eng-metrics` | ✅ (incl. DORA/METR explainer + how-to) |
| E8 Spec-driven development (Spec Kit, Kiro, BMAD) | `eng-sdd` | ✅ (incl. Superpowers/Compound + BMAD brownfield) |

### M2 · Product harness (id `m2`) — Report 2; 2 research-note sections
| Topic | id | Deep dive |
|---|---|---|
| P1 AI-assisted discovery | `prod-discovery` | ✅ embedded + standalone |
| P2 PRDs and requirements with AI | `prod-prd` | ✅ |
| P3 Decomposition into agent-ready work items | `prod-decomposition` | ✅ |
| P4 The PM: from author to editor and curator | `prod-pm-role` | ✅ |
| P5 The P1–P5 assistance scale in the product layer | `prod-scale` | ✅ |

### M3 · Handoff contract (id `m3`) — Report 2 (contract portion); 5 research-note sections
| Topic | id |
|---|---|
| H1 Anatomy of the handoff contract | `hand-anatomy` |
| H2 EARS & Gherkin: machine-verifiable AC | `hand-ears-gherkin` |
| H3 Traceability & spec modes | `hand-traceability` |
| H4 Feedback loop & handoff anti-patterns | `hand-feedback` |

### M4 · Information architecture (id `m4`) — Report 3; 5 research-note sections
| Topic | id |
|---|---|
| I1 Artifact taxonomy: durable / derived / disposable | `ia-taxonomy` |
| I2 Lifecycle & write-permissions as governance | `ia-lifecycle` |
| I3 Consistency, drift & documentation debt | `ia-consistency` |
| I4 Memory systems for agents | `ia-memory` |
| I5 Progressive disclosure: Skills, nested files, indexes | `ia-disclosure` |
| I6 Retrieval: agentic search vs RAG vs knowledge graphs | `ia-retrieval` |
| I7 Linking product ↔ engineering | `ia-linking` |

### M5 · Brownfield bootstrap (id `m5`) — Report 4; 5 research-note sections
| Topic | id |
|---|---|
| B1 The bootstrap paradox and safe ordering | `brown-paradox` |
| B2 Characterization & golden-master testing with agents | `brown-characterization` |
| B3 Mutation testing as the test-quality gate | `brown-mutation` |
| B4 Agent archaeology: reverse-engineering legacy | `brown-archaeology` |
| B5 Strangler fig, the heatmap and picking the first battlefield | `brown-strangler` |
| B6 Roadmap F0–F3, metrics and STOP criteria | `brown-roadmap` |

### M6 · Design harness (id `m7`) — Report 5; 6 research-note sections
> **D1–D5 is an original synthesis, not an industry standard — flag it wherever it appears.**

| Topic | id |
|---|---|
| D1 Design system as the third handoff artifact | `des-artifact` |
| D2 Design tokens as the visual contract (DTCG) | `des-tokens` |
| D3 How agents consume design context | `des-consumption` |
| D4 Governance & SSOT in the design world | `des-governance` |
| D5 The design harness: verification loops & guardrails | `des-harness` |
| D6 D1–D5 scale & the designer as curator | `des-scale` |
| D7 Design archaeology & the F0–F4 rollout | `des-brownfield` |

### M7 · Security — cross-cutting (id `m8sec`) — Report 6; 8 research-note sections
| Topic | id |
|---|---|
| S1 Security is cross-cutting: prompt injection & blast-radius reduction | `sec-crosscut` |
| S2 The lethal trifecta & the Rule of Two | `sec-trifecta` |
| S3 Advisory vs deterministic controls; the rules-file backdoor | `sec-advisory` |
| S4 MCP / tools: the richest attack surface | `sec-mcp` |
| S5 Loop / auto-run: self-modification, YOLO & sandbox escapes | `sec-loop` |
| S6 Memory poisoning & multi-agent risk | `sec-memory` |
| S7 Contract & brownfield surfaces; the secrets problem | `sec-surfaces` |
| S8 Configuring rules for maximum practical safety | `sec-config` |

### M8 · Study trajectory (id `m6`, `plan:true`) — backlog, no research pass yet
| Topic | id |
|---|---|
| T1 Economics & the business case | `traj-economics` |
| T2 Measurement & pilot design | `traj-measurement` |
| T3 Change management & people | `traj-change` |
| T4 Compliance, legal & the EU context | `traj-compliance` |
| T5 The harness as an internal product | `traj-platform` |
| T6 Vendor strategy & lock-in | `traj-vendor` |
| T7 Organizational governance | `traj-governance` |

## The six research reports (embedded, rendered from Markdown)

1. **Report 1** — Engineering harness: `Agent = Model + Harness`; the 7 components; L1–L5.
2. **Report 2** — Two-layer: product harness assists (P1–P5); the handoff contract (6 parts).
3. **Report 3** — Information architecture: durable/derived/disposable; write-permissions; ADRs.
4. **Report 4** — Brownfield bootstrap: read-only → characterization → mutation-verify → writes.
5. **Report 5** — Design system as the third handoff artifact; DTCG; the D1–D5 scale (original).
6. **Report 6** — Security as the cross-cutting dimension; prompt injection; lethal trifecta;
   per-component threat map with real 2025–26 incidents/CVEs.

## Deep-dive companions (14)

Embedded as in-page overlays **and** shipped as standalone files in `deep-dives/`:

`SDLC-foundations` · `E1-agent-model-harness` · `E2-context-engineering` ·
`E3-harness-in-practice` · `E4-verification-first` · `E5-governance` ·
`E6-autonomy-levels` · `E7-metrics-anti-patterns` · `E8-spec-driven-development` ·
`P1-ai-assisted-discovery` · `P2-prds-with-ai` · `P3-decomposition` · `P4-pm-role` ·
`P5-assistance-scale`

Overlay anchors wired in the workbook: `#sdlc-deepdive`, `#e1-deepdive` … `#e8-deepdive`,
`#p1-deepdive` … `#p5-deepdive` (each appears exactly twice: the "Go deeper" link + the JS
open handler).
