# Roadmap

Where the study programme stands and what to build next. Priorities reflect the engagement
goal: be ready to walk a brownfield client from "why" through a measured pilot to a staged rollout.

## Done

- **Workbook**: 8 modules, 55 topics, 6 research reports, SDLC + Domain map sections. (v1.33 —
  M1 grew to E1–E11 in the July 2026 source-evaluation round: E9 harness tuning, E10 background
  agents, E11 formal methods, each with a deep-dive companion.)
- **Deep-dive companions (36)**: SDLC Foundations, **E1–E11** (all of M1), **P1–P5** (all of M2),
  **D1–D2** (M6), **H1–H4** (all of M3), **I1–I7** (all of M4), **B1–B6** (all of M5).
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
- ~~**D2** `des-tokens` — design tokens as the visual contract (DTCG)~~ — **done (v1.47)**,
  with a four-teammate fact/discovery pass + a three-agent adversarial spot-verify round
  (13th session in a row it caught real errors: theming is NOT in stable 2025.10 — it lives in
  the "do not implement" Resolver Module draft, and the W3C announcement's theming headline is
  marketing overreach; the 56→84% adoption stat re-dated to zeroheight's 2025 report n=294
  (86% n=147 in 2026); Style Dictionary v5 shipped, not "in progress"; "Jon Levine co-coined"
  unverified → credit Jina Anne alone; DESIGN.md's circulating vendor roster = third-party
  commentary; two paraphrases de-quoted). Load-bearing new sources: DESIGN.md (Google Labs,
  Apr 2026, alpha) + Anthropic-ecosystem uptake issue, CHI 2026 EA registry-based 95.08%
  (plus the honest null: no token-specific causal study), D'Amato dissent, Dembrandt drift
  gate, Adobe Spectrum/Braithwaite designer-authored/code-stored, Sopelnik + Builder.io/Sewell
  verbatims, Penpot first open-source native-DTCG tool. The tier reading, sync-direction table
  and six-step SCSS→DTCG migration flagged as our synthesis.
- Next: **D5** (the design harness — the remaining most-concrete one), then D3/D4/D6/D7.

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
    Bank; a fabricated ".claudeignore" caught).
  - ~~**I2** `ia-lifecycle` — lifecycle & write-permissions as governance~~ — **done (v1.25)**,
    with the three-teammate fact pass + spot-verify round (the Anthropic "unacceptable to
    remove or edit tests" quote re-anchored to the feature list, not test files; Radar
    Adopt = Nov 2017; MADR 4.0 "Architectural" + Rejected; ASI06 canonical name) and new
    load-bearing sources (ImpossibleBench arXiv:2510.20270, Anthropic reward-hacking 12%,
    Replit DB incident, Copilot coding-agent guardrails, restrict-file-paths rulesets,
    GitLab CODEOWNERS porosity, Rovo/Atlassian MCP identity model, Lore arXiv:2603.15566).
    The write-permission matrix + ADR code-seam grep test flagged as our synthesis.
  - ~~**I3** `ia-consistency` — consistency, drift & documentation debt~~ — **done (v1.26)**,
    with the three-teammate fact pass + spot-verify round (4th catch: scout's context-file
    population stats materially wrong — corrected to Galster et al.'s 4,768 files /
    2,586-of-2,853 repos, CLAUDE.md leading 34.4%; Tan 28.9%/4.7yr pinned to
    arXiv:2212.01479, 265/918; DORA "2.4×" folklore excluded as unpinnable; DocPrism
    98%→14% relabelled flag rate). Load-bearing new sources: Treude & Baltes
    arXiv:2606.09090 (context rot in agent config files, 23.0% of repos, two-snapshot CI
    grep), Lulla JAWs 2026 (AGENTS.md ↔ ~29% lower runtime), DocPrism, DORA 2022 docs
    quality + DORA 2025 AI-accessible internal data, SWE-at-Google ch.10 freshness,
    Docs as Tests / Doc Detective, Schemathesis/Specmatic + the tool graveyard
    (Dredd/Optic/driftctl/DeepDocs/Swimm-pivot) flagged point-in-time. The per-category
    freshness policy flagged as our synthesis.
  - ~~**I4** `ia-memory` — memory systems for agents~~ — **done (v1.28)**, with the
    three-teammate fact pass + spot-verify round (spot-verify: 8/8 discovery finds
    survived — a first; two usage corrections: Momento dated May/June 2026, the Mem0
    6,900-vs-26,000-token contrast dropped as per-call vs per-conversation). Durable
    terminology catch: "core/recall/archival memory" is Letta product vocabulary — the
    MemGPT paper says main/external context with working context + recall/archival
    *storage* (know bullet + Report 3 corrected). Load-bearing new sources: CoALA
    (arXiv:2309.02427), Copilot Memory docs (citation re-verification + 28-day TTL),
    Devin Knowledge (org→enterprise promotion), Momento arXiv:2606.00832 (over-trusting
    stale memory), memory-poisoning SoK arXiv:2606.04329 (4 channels/9 vulns/6 classes,
    MPBench), cache economics arXiv:2601.06007, OWASP Agent Memory Guard, Mem0-vs-Zep
    LoCoMo dispute (vendor-claims lesson), Sandelin coding-memory benchmark (own-tool
    caveat). The promotion path (session note → memory file → steering file via PR)
    flagged as our synthesis. ASI06 entry mitigations verbatim-UNPINNABLE — defenses
    attributed to Anthropic docs + Agent Memory Guard, never quoted as the Top 10 entry.
  - ~~**I5** `ia-disclosure` — progressive disclosure: Skills, nested files, indexes~~ —
    **done (v1.30)**, with the three-teammate fact pass + spot-verify round (seed corrections:
    L1 metadata ~100 tokens not ~80, SKILL.md body 500 lines not "5k words", official
    CLAUDE.md target 200 lines not ~300 — the NOTES.md tension resolved in favour of the
    official docs; @imports four hops and NOT lazy; CLAUDE.local.md not deprecated;
    spot-verify catches: matklad quote paraphrase, −2%/+23% is AGENTbench-specific, aider
    "personalized PageRank" not in the 2023 post). Load-bearing new sources: ETH Zurich
    arXiv:2602.11988 (the −2%/+23% pin), McMillan arXiv:2605.10039 (structural null,
    within-session decay), Anthropic advanced-tool-use + code-execution-with-MCP (tool-layer
    disclosure, vendor-flagged), HumanLayer CLAUDE.md guide, matklad ARCHITECTURE.md, aider
    repo map, Windsurf hard caps, agentskills.io cross-vendor roster. The core/map/leaves
    three-tier framing flagged as our synthesis. Fact fix: Galster re-pointed to
    arXiv:2602.14690 ("Harness Engineering…").
  - ~~**I6** `ia-retrieval` — retrieval: agentic search vs RAG vs knowledge graphs~~ —
    **done (v1.37)**, with the three-teammate fact pass + spot-verify round (seed corrections:
    the "Devin: same pattern" claim was WRONG — Devin indexes via DeepWiki, recast as the
    counterexample; Cursor's +12.5% re-attached to semantic search's lift on internal Context
    Bench; "precision" dropped from Claude Code's stated reasons — the Cherny quotes pinned to
    HN 43164253 + his restatement tweet; spot-verify kills: a fabricated "second Anthropic
    engineer" quote, Riptide "200%" paraphrase → verbatim "3x the recall"). Load-bearing new
    sources: SWE-bench BM25-vs-oracle (1.96%/4.80%), Agentless, CodeRAG-Bench + CoIR (dense
    code-trained embedders frequently beat BM25 — folklore correction), Codebase-Memory
    arXiv:2603.27277 (83% vs 92% at 10× fewer tokens), Vec2Text embedding inversion (92%),
    GitHub Blackbird, Augment quantized vectors, Cody retreat + consumer sunset, GraphRAG
    anti-miscitation callout. The L0–L3 escalation ladder + twenty-query bench flagged as
    our synthesis.
  - ~~**I7** `ia-linking` — linking product ↔ engineering~~ — **done (v1.38)**, completing
    M4. Three-teammate fact pass + spot-verify round (7th session in a row it paid: GitLost
    "VP of Sales" + preview-date details dropped; LinearB stat re-pinned verbatim "In 75% of
    teams, 31% of branches are unlinked"; a "Jira has its own version of reality" quote NOT
    FOUND → excluded). Load-bearing evidence: Bird et al. ESEC/FSE 2009 (8–55% linked, the
    severity inversion 63%-minor vs 15%-blocker), Wang/Pradel/Liu arXiv:2503.15223 ICSE 2026
    (29.6% plausible-patch divergence; 66.2% traced to under-specified issues), the
    ticket-as-prompt roster (Copilot↔Jira GA Jun 2026, Devin↔Linear, Cursor↔Linear — vendor),
    lethal trifecta + three incidents (GitHub MCP May 2025, Supabase Jul 2025, GitLost
    Jul 2026), MCP-Universe distractor evidence (replaced the unpinnable "2–3+ servers"
    claim), Agent Trace RFC + Copilot session-log links + Purview streaming, multi-method
    census 3.3%/30× (fact fix applied to H3: it is NOT "the AIDev census" — AIDev is the
    separate PR census it compares against). Enforcement ladder + master-per-artifact table
    flagged as our synthesis. **M4 complete.**
- **M5 Brownfield bootstrap** (B1–B6): the safe ordering, characterization/golden-master,
  mutation gate (B3 already cross-referenced from E4), strangler-fig + heatmap.
  - ~~**B1** `brown-paradox` — the bootstrap paradox and safe ordering~~ — **done (v1.39)**,
    with the three-teammate fact pass + spot-verify round (8th session in a row it paid: a
    fabricated Böckeler mutation-testing quote killed; UnitTenX "characterization tests" =
    paraphrase + 0%→100% scoped to djbdns; TestGen-LLM 1:4/1:20 retired as UNPINNABLE — fixed
    in topic B2 + Report 4 notes; DORA 2024 mechanism reframed to its own "small batch sizes
    and robust testing mechanisms" wording + the 2025 throughput sign flip). Load-bearing new
    sources: METR RCT arXiv:2507.09089 (19% slower vs 20% believed faster), SWE-EVO
    arXiv:2512.18470 (72.80% → 25%), Epoch AI SWE-bench-Verified teardown (Jun 13 2025),
    Böckeler guides/sensors trilogy (Aug 2024 / Apr 2026 / May 2026), UnitTenX
    arXiv:2510.05441, Ehsani et al. arXiv:2601.15195 (MSR 2026, AIDev-pop failure taxonomy:
    38% Abandoned/Not Reviewed; docs/CI/build merge best), Xia TSE 2018 (58% comprehension),
    DORA 2025 AI Capabilities Model (7 capabilities). The five-step dependency chain flagged
    as our synthesis.
  - ~~**B2** `brown-characterization` — characterization & golden-master testing~~ — **done
    (v1.41)**, with the three-teammate fact pass + spot-verify round (9th session in a row it
    paid: the "no wrong answers — just documenting the way things exist" line = Erik Dietrich's
    gloss, NOT Feathers — misattribution fixed in the Report 4 notes; Beck's "immutable tests"
    idea UNVERIFIED → dropped; the "after the third bulk approval" fatigue line = scout
    paraphrase → replaced with Sapegin's real 2019 sentence; ICSE SEIP 2026 venue + "Berndt et
    al." authorship unverified → name dropped; Bache's golden-master objection re-pinned to her
    exact wording). Load-bearing new sources: Feathers' blog verbatims ("it becomes its own
    specification"), Bache 2021 terminology anatomy, ACH arXiv:2501.12862 (FSE 2025,
    Messenger/WhatsApp), Qodo PR huggingface/pytorch-image-models#2331, YATE arXiv:2507.18316
    (repair beats regeneration), TestGenEval arXiv:2410.00752 (35.2% coverage vs 18.8% mutation),
    Mathews & Nagappan arXiv:2412.14137 (oracle-by-construction, read both directions),
    Konstantinou et al. arXiv:2607.05139 (bug-as-spec measured: ~25% → ~14%), DBMS flakiness
    arXiv:2601.08998 (0.07% vs 0.29–0.71%, 63% unordered collections), Beck "Beyond the Vibes"
    genie verbatim, Radar Vol. 34 chokepoints verbatim. Six-step workflow + two-door triage +
    exit-criteria table flagged as our synthesis.
  - ~~**B3** `brown-mutation` — mutation testing as the test-quality gate~~ — **done (v1.42)**,
    with the three-teammate fact pass + spot-verify round (10th session in a row it paid:
    SpecBench quote re-pinned verbatim + 28 pp flagged as abstract headline over R²=0.21 fit;
    Augment-blog JFreeChart cost figure identified as third-hand → excluded; ISSTA 2019
    numbers pulled verbatim). Theory verbatims: DeMillo/Lipton/Sayward 1978 + Hamlet 1977;
    Just FSE 2014 (73% coupling, coverage-independent correlation; Defects4J = ISSTA 2014
    companion); Inozemtseva & Holmes ("quality target", not "stopping criterion"). Fact
    corrections: MUTGEN real title + TSE acceptance, 53% plateau = single subject; Haroon
    23,977 = failing subset of 119,163; Google's no-score stance = practical ("infeasably
    expensive"), not normative; gremlins over stale go-mutesting; pseudo-tested % UNPINNABLE.
    Load-bearing new sources: the Google trilogy (ICSE-SEIP 2018 / ICSE 2021 / TSE 2021),
    MuTAP (IST 2024), LLMorpheus, AdverTest arXiv:2602.08146, SpecBench arXiv:2605.21384,
    Rajan arXiv:2606.16062, Yoshimoto arXiv:2603.13724, Rethinking arXiv:2602.07900,
    Schuler & Zeller STVR 2013, TCE ICSE 2015, Descartes/EMSE 2019, Shi/Bell/Marinov ISSTA
    2019, Stryker/PIT default thresholds (no tool ships a mandatory gate). Two-mode gate +
    held-out-mutants principle + ~70% heuristic flagged as our synthesis. Next: **B4**
    (agent archaeology) or **B5** (strangler fig + heatmap).
  - ~~**B4** `brown-archaeology` — agent archaeology: reverse-engineering legacy~~ — **done
    (v1.44)**, with an 8-agent fact + discovery swarm and a 4-agent spot-verify round (11th
    session in a row it paid: CodeConcise is graph-traversal-AUGMENTED RAG, not "instead of
    plain RAG"; the 60,000 person-days and 240 FTE-years are the SAME projection in two units;
    the 3h-vs-3-weeks fix is "best cases", a ThoughtWorks pair, a different client; AWS
    "~7B lines/year" NOT FOUND → replaced with the verified 1.1B lines analyzed / 810k hours
    cumulative; Western Union is 2.5M lines not 250k, six weeks = discovery→testing, ongoing
    pilot; the "15–20k lines" sizing UNPINNABLE → dropped; Siala & Lano's zero-spurious holds
    for Java, 0.14 on Python; Soliman & Keim affiliation split Paderborn/KIT; Willison title
    "least dangerous" vs body "least harmful" pinned). WCA for Z → IBM Bob timeline pinned
    (unveiled Oct 2025, GA Mar 2026, global availability Apr 28 2026; WCA supported with
    adoption path). Load-bearing new sources: Malykhin's Archaeologist's Copilot
    (martinfowler.com, Jul 16 2026 — "structural lie", Tourist-vs-Archaeologist prompts, time
    capsule, lying tests; every quote spot-verified verbatim), CROZ Nov 2025 review verbatims,
    Unum AVP "if you cannot understand it, you cannot verify" (re:Invent 2025), GitHub/Microsoft
    COBOL framework ($2–5/1k LOC), Soliman & Keim ICSA 2025 (0.395 precision), Siala & Lano
    Frontiers 2025, arXiv:2504.04372 (78% brittle comprehension), Xia TSE 2018 (~58% measured,
    3,148 hours), Minelli ICPC 2015, Corbi IBM SJ 1989 ("part historian, part detective, and
    part clairvoyant"), Glass 2001 attribution fix for the 40–80% factoid, Sim & Holt ICSE 1998,
    Rastogi ESEM 2015, Uddin & Robillard 2015, Wen ICPC 2019 (13–20% comment co-evolution),
    Tan SOSP 2007, Cursor support-bot incident Apr 2025, Spring REST Docs / Doc Detective /
    Schemathesis, AgenticAKM arXiv:2602.04445 (validation-agent convergence), HADAS
    arXiv:2404.01588. Discovery finding: confidence-labeled generated docs = unclaimed
    territory → hypothesis-with-confidence labels + sampling + promote-through-verification +
    F0 workflow flagged as our synthesis. Next: **B5** (strangler fig + heatmap). *(Done — see below.)*
  - ~~**B5** `brown-strangler` — strangler fig, the heatmap and the first battlefield~~ — **done
    (v1.45)**, shipped by the parallel session on 2026-07-18 with an 8-agent fact + discovery
    swarm; see the v1.45 CHANGELOG entry for the corrections and new sources.
  - ~~**B6** `brown-roadmap` — roadmap F0–F3, metrics and STOP criteria~~ — **done (v1.46)**,
    **completing M5**. Three-teammate fact/discovery pass + adversarial spot-verify (12th
    session in a row it caught real errors: DORA deployment rework rate re-dated to its true
    2024 introduction — fixed in E7/E8/H4/B1 both copies; MIT NANDA "95%" pinned to real
    wording + methodology 300+/52/153, the circulating "150/350" is a misquote; DX = 425
    organizations; Faros 2026 exact 441.5%/31.3%; DORA 2025 strong conditional belongs to
    user-centric focus, not platform quality). Honest analogue check: F0–F3 has NO published
    canonical equivalent (July 2026) — nearest cousins stage oversight per task (Sharma's D³
    Discover–Define–Deliver n=52 self-report; GAIE's HITL/HOTL/AWM tiers), so it stays flagged
    as Report 4 synthesis. Load-bearing new sources: GitGuardian 2026 (Claude Code commits
    3.2% vs 1.5% secret-leak baseline; MCP configs 24,008 secrets/2,117 valid), Microsoft
    instrumented rollout study arXiv:2607.01418 (~24% sustained PR-merge lift, peer-network
    diffusion), DX Q4 impact report (structured enablement, onboarding 91→49 days), DORA AI
    Capabilities Model, Digital Apprentice automatic-demotion asymmetry, Swarmia five levels,
    KPMG stall mechanism, safety-standards traceability anchor (ISO 26262/IEC 62304/DO-178C).
    Gate table + back-triggers + F0–F3 × R1/R2/R3/R6 master-plan table = our synthesis.

### M9 — Playbook module (the practice layer)
Decided 2026-07-18 (spec: docs/superpowers/specs/2026-07-18-playbook-module-design.md):
the theory→practice layer lives inside the workbook as runbooks ordered by the
engagement journey; the harness starter-kit templates and hands-on labs derive from
these runbooks later — no separate repo.
- ~~Module skeleton (pb- topics, store-backed checklists) + **PB1 Assess** runbook~~ — **done (v1.48)**.
- ~~**PB2 Bootstrap** (B1–B3 distilled)~~ — **done (v1.50)**.
- ~~**PB3 Harness** (E1–E5, I2 — templates ship as runnable configs: hook scripts,
  permission baselines, CI gates, per the E5 litmus)~~ — **done (v1.52)**.
- ~~**PB4 Handoff** (H1–H4)~~ — **done (v1.54)**, with a two-teammate research pass (repo
  distillation + web fact-verification, 2026-07-20): eleven steps / four phases; REQ-id +
  suspect gates as runnable CI blocks, stop-on-ambiguity + stamping as appends to PB3's
  AGENTS.md; fresh point-in-time layer (Copilot↔Jira GA Jun 25, Spec Kit v0.13.0, Kiro EARS
  + Analyze Requirements, gplint, Assisted-by trailer standard); Ambig-SWE cited as mechanism
  only, Reqnroll version deliberately unpinned (conflicting sources).
- ~~**PB5 Pilot** (E7, B6 — converges with T2's pilot playbook; compares against the
  delivery baseline captured in PB1)~~ — **done (v1.56)**, with a two-teammate research pass
  (repo distillation + web fact-verification, 2026-07-20): ten steps / three phases
  (pre-register → measured window → read/gate/decide); GO/HOLD/STOP against pre-registered
  criteria, guardrails as automatic dials (Digital Apprentice asymmetry), the token/cost
  column added to PB1 §3; fresh layer: METR 2026 contamination note, the 2×-mandate study
  (arXiv:2607.01904), DX Core 4 AI addendum, cost-to-merged-feature benchmark. **M9 complete
  (5/5)** — the module's backlog items (field-report loop, team-level tracking) remain.
- Backlog (deliberately deferred):
  - **Field-report loop** — a completed client runbook feeds an anonymized results entry
    back into the relevant deep dive; the corpus is currently 100% externally cited, and
    pilot outcomes are the first first-party evidence. The persisted checklist data in
    `store` is the hook for it.
  - **Team-level tracking** — `store` is per-browser/per-device; aggregating progress
    across a Sudo team at a client would need shared state. Deferred: adding it would
    reopen the rejected "engagement mode" app-creep.

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
