# Changelog

Version history of the workbook (`workbook/agentic-development-study.html`). Mirrors the
in-app version-history modal (top-bar button). Dates are when the work was done in-session.

## v1.30 · 2026-07-16

Added the **I5 deep dive — Progressive Disclosure: Skills, Nested Context Files & the Map
Layer** (`deep-dives/I5-progressive-disclosure-deepdive.html` + in-page overlay `#i5-deepdive`),
the fifth companion of module M4. Sections: the principle honestly attributed (Nielsen 2006,
Carroll & Carrithers 1984) and the three-tier framing core/map/leaves (flagged as this
workbook's synthesis); Skills as the canonical three-level mechanism with the official token
economics (~100 tokens/skill metadata, bodies under 5k tokens / 500 lines) and the open
standard's cross-vendor reach (agentskills.io, Apache-2.0; Codex, Copilot, Cursor 2.4, Gemini
CLI — point-in-time); nested context files and scoped rules across tools, including the
subdirectory on-demand semantics, the @import illusion (four hops, still loads at launch) and
the AGENTS.md nearest-file-wins divergence; the map layer (matklad's ARCHITECTURE.md, aider's
repo map, MEMORY.md, the Ahrefs llms.txt caution reworded precisely — 97% of files fetched by
nothing at all); gardening the core around the official 200-line target (reconciling our
earlier "~300" note — practitioner range vs official budget); the evidence triad — Lulla
(Δ 28.64% median runtime / Δ 16.58% output tokens), ETH Zurich arXiv:2602.11988 (LLM-generated
files −0.5%/−2% success for +20%/+23% cost; developer-written +4%; "context files do not
provide effective overviews") and McMillan arXiv:2605.10039 (structural null, ~5.6% per-step
within-session decay); five failure modes; a week-one disclosure audit. Topic I5
know/concepts/src/checks rewritten with verified figures (seed corrections: L1 ~100 tokens not
~80, body budget 500 lines not "5k words", 200-line official target not ~300, four-hop imports
not five, CLAUDE.local.md not deprecated). Fact fix elsewhere: the I3 Galster reading item
re-pointed to arXiv:2602.14690 with the current title "Harness Engineering for Agentic AI
Coding Tools" (the previously noted Zenodo DOI belongs to the companion dataset paper).
Fact-verification: two verification teammates + one discovery scout + a spot-verification
round (catches: matklad "10x" quote was being paraphrased; −2%/+23% is AGENTbench-specific;
"personalized PageRank" not in aider's 2023 post — attributed to the implementation).

## v1.29 · 2026-07-16

Added **highlight-notes**. In any in-page deep-dive overlay, selecting a passage
shows a floating **"+ save as note"** button that stores the passage (text-quote
anchored) in the profile. A new **my notes** button in the sidebar Data group
opens a modal listing every saved passage grouped by deep dive, each with an
editable personal thought, a delete control, and an **"open in deep dive →"**
jump that scrolls to and flashes the source passage. Saved passages are
re-highlighted (persistent tint) every time the deep dive is opened, via the
existing per-overlay `MutationObserver` in `initDeepDiveNav()`. Highlights persist
through the single `store` backend (`agentic-study-v1`) and travel with
export/import. Runtime-only `<mark>` wrapping — the static file (and
`scripts/validate.py`) is unaffected. Workbook-only; standalone deep-dive files
unchanged (they have no storage backend). Known limitation: overlapping
highlights may nest (slightly darker tint).

## v1.28 · 2026-07-16

Added the **I4 deep dive — Memory Systems for Agents: Typologies, Poisoning & the
Governed Write-Mode** (23rd companion): standalone `deep-dives/I4-memory-systems-deepdive.html`
+ in-page overlay (`#i4-deepdive`, wired ×2), built with the three-teammate fact pass
(two verification rounds + discovery) and a spot-verify round on all discovery-sourced
numbers (8/8 survived — a first; two usage corrections applied).

- **§0–§1** — memory as an information-architecture decision; four operational layers
  (session/working · persistent files · cross-session state · organizational); CoALA
  frame (working/episodic/semantic/procedural — the harness itself is explicit
  procedural memory); research lineage Generative Agents / Reflexion (91% vs 80%
  HumanEval) / Voyager; MemGPT paging frame **with a terminology correction propagated
  to the `ia-memory` know bullet and Report 3 Plane B**: "core/recall/archival memory"
  is Letta product vocabulary — the paper says *main/external context*, *working
  context*, recall/archival *storage*. Calibration: LongMemEval ~30% sustained-memory
  drop; Sandelin's controlled coding-agent benchmark (memory flat on quality, hurts
  simple tasks, 22–32% cheaper on complex — own-tool caveat, directional).
- **§2** — the vendor landscape, point-in-time mid-2026: memory tool `memory_20250818`
  (GA, six ops, client-side); Claude Code auto memory (MEMORY.md first-200-lines/25KB
  **load cutoff**, distinct from the CLAUDE.md under-200-lines style target); Cline
  Memory Bank six files; Cursor Memories GA in 1.2 (an earlier "removed in v2.1"
  scout flag was retracted — the docs URL 308-redirect was a site restructure);
  Windsurf Cascade Memories; **Copilot Memory** (public preview: repo-level facts with
  citations re-verified against the current branch, 28-day unused-fact TTL, enterprise
  export/bulk-delete); **Devin Knowledge** (trigger descriptions, repo pinning,
  org→enterprise promotion); Letta (sleep-time compute, arXiv:2504.13171), Mem0, Zep/
  Graphiti, LangMem — with the **Mem0-vs-Zep LoCoMo dispute** documented both ways and
  kept as the vendor-claims lesson; BEAM (third-party) noted at 1M/10M-token scale.
- **§3** — compaction / structured note-taking / sub-agents with verbatim protocol
  quotes ("ALWAYS VIEW YOUR MEMORY DIRECTORY…", "ASSUME INTERRUPTION…"); measured cache
  economics (arXiv:2601.06007: 41–80% cost, 13–31% TTFT; dynamic content after the
  cache breakpoint).
- **§4** — the governed fourth write-mode: git-versioned memory (diffable/attributable/
  revertible), index discipline, validation floor (path containment incl. %2e%2e%2f,
  sensitive-data strip, size caps, expiry), provenance frontmatter, and the **promotion
  path** (session note → memory file → steering file only via human-merged PR) —
  flagged as our synthesis; demotion anchored to Momento (arXiv:2606.00832: agents
  treat "prior session history as a reliable proxy for current context rather than
  stale information requiring re-validation"); Every's compound-engineering loop as the
  practitioner instance.
- **§5** — ASI06 threat model (persistent, temporally decoupled, spreads via ordinary
  reads; primary quotes from the Dec 9 2025 announcement — the canonical entry's own
  mitigation list was verbatim-unreachable, so defenses are attributed to Anthropic
  docs, **OWASP Agent Memory Guard** (verbatim ×4) and I2 machinery, never quoted as
  the Top 10 entry); AgentPoison (>80% ASR at <0.1% poison), MINJA (query-only; titled
  "Memory Injection Attacks on LLM Agents via Query-Only Interaction" as of v5),
  the SoK arXiv:2606.04329 (4 write channels / 9 vulnerabilities / 6 attack classes,
  MPBench, "more aggressive memory ops → more exploitable"), Rehberger's SpAIware +
  Gemini demos (both dated, both primary).
- **§6–§7** — the files-vs-store decision criterion (default files; boundary/scale/
  compliance tests flip it; GDPR-erasure vs AI-Act-retention wrinkle flagged as our
  synthesis) and the week-one client checklist.
- **`ia-memory` topic enriched**: know +CoALA/+evidence bullets, corrected MemGPT
  terminology, concepts, `src` (deep-dive link first, +arXiv, +Copilot Memory), two
  new checks (fourth write-mode rationale; query-only poisoning).
- Docs: CONTENT-MAP 22→23 companions, ROADMAP I4 marked done.

## v1.27 · 2026-07-16

Integrated the **session-persistence research** (internal artifact, Jul 2026:
*Recording, Tracking, and Preserving AI Agent Work as First-Class SDLC Artifacts*,
https://claude.ai/artifacts/latest/019f69a3-34f6-7731-9b61-d64eb733f782) as targeted
summaries across five topics — not the whole report; each placement carries a `src`
link back to the full artifact.

- **`ia-taxonomy` (I1)** — the agent session/trajectory as the newest artifact to
  classify, and the honest answer is *tiered*, not one bucket: the decision-provenance
  spine (task id, agent+model+version+config, tool calls with outcomes, approvals,
  artifact digests, PR links) is durable/immutable; full prompts, retrieval payloads
  and thinking blocks are disposable on a 7–30-day incident-window TTL, then
  metadata+hash; link-don't-inline (durable URL/ID from commit → session). New check
  question on where a trace falls in the triad (key teaching point: nothing in it is
  *derived* — a trace cannot be regenerated, which is why the spine is worth keeping).
- **`hand-traceability` (H3)** — the chain gains the session link: the vendor-neutral
  **Agent Trace** spec (agent-trace.dev — Cognition with Cursor, Cloudflare, Vercel,
  Google Jules, Amp, OpenCode; one contract: attribute each change to conversation +
  line ranges via a durable per-trajectory URL); GitHub Copilot commit→session-log
  linking (Mar 2026) + enterprise session streaming to SIEM/Purview (preview Jul 2026);
  the **task-centric record** (spec/ticket → task → session → code/PR → review); the
  layered provenance stack for regulated work (W3C PROV/PROV-AGENT for process ·
  SLSA/in-toto for artifact · CycloneDX ML-BOM / SPDX 3.0 AI Profile for model/data
  lineage). Flagged point-in-time (Dec 2025–Jul 2026), adoption nascent, partly
  vendor-driven.
- **`ia-lifecycle` (I2)** — traces extend the ADR practice down to implementation-level
  decisions ADRs never captured (Lore, arXiv:2603.15566), but are **decision
  provenance, not rationale**: CoT-faithfulness data pinned (Anthropic 2025 — an
  influential hint surfaces in stated reasoning only 25% of the time for Claude 3.7
  Sonnet, 39% for DeepSeek R1; Korbak et al., arXiv:2507.11473 — monitorability is a
  fragile opportunity). Promoted "why" fields stay human-gated: agent drafts from the
  trace, human reviews before durable — agent-generated ADRs capture the what but can
  fabricate the why.
- **`sec-surfaces` (S7)** — the trace store as a new secrets surface: verbatim prompts,
  tool results and thinking blocks quietly make it a regulated data store and a
  secondary leakage path (arXiv:2606.30373: 132,853 Hugging Face apps — 14.15% — using
  253,755 secrets; 936 apps logging secrets at runtime). Mitigation: PII/secret
  redaction at the collector *before* storage, production-grade access control, tiered
  retention so full payloads expire.
- **`traj-compliance` (T4)** — research head-start for the backlog topic: EU AI Act
  Art. 12 (automatic event logging over the system lifetime), Arts. 19/26(6)
  (≥6-month retention), full high-risk application 2 Aug 2026, record-keeping fines up
  to €15M or 3% of worldwide turnover (Art. 99); off-the-shelf LLM APIs are not
  Art.-12-compliant by default; harmonised standards still drafts (prEN 18229-1,
  ISO/IEC DIS 24970; ISO/IEC 42001 as the surrounding AIMS).

Deliberately **not** imported: vendor observability comparisons (churn), cost
multipliers (practitioner estimates, unaudited), Cognition's hedged SWE-Bench/cache
claims, and the full W3C-PROV/AIBOM survey — the artifact link covers them. Vendor
claims kept separated from independent evidence per house style.

## v1.26 · 2026-07-16

Added the **I3 deep dive — Consistency, Drift & Documentation Debt** (topic
`ia-consistency`): embedded workbook overlay + standalone
`deep-dives/I3-consistency-drift-deepdive.html`, written after the three-teammate fact
pass (2× verification + 1 discovery) **plus the spot-verification round on discovered
sources** — which earned its keep a fourth time: the scout had materially wrong
context-file population statistics (corrected to the primary paper: 4,768 context files
across 2,586 of 2,853 repos, 90.6%, CLAUDE.md leading at 34.4% — not 9,470/4,463 with
AGENTS.md leading); a practitioner post was re-dated July **2026** (not 2025); DocPrism
98%→14% relabelled a *flag rate*, not a false-positive rate; the McMaster post year
found undeterminable and left unstated.

Fact corrections applied to the topic itself: the 28.9%/4.7-year stale-references
figures pinned to **arXiv:2212.01479 (Dec 2022)**, denominator 265/918 analyzable
projects (the EMSE 2023 paper restates 28.9% but the 4.7-year average is the 2022
study); the DORA "2.4× more likely" folklore multiplier was unpinnable in any primary
source and is excluded — the 2022 amplification framing and published per-capability
lifts used instead; the 2018 TD tertiary study credited to Rios, Mendonça-Neto &
Spínola (not Seaman).

New load-bearing sources: **Treude & Baltes, "Context Rot in AI-Assisted Software
Development" (arXiv:2606.09090)** — DOCER applied unmodified to CLAUDE.md/AGENTS.md/
copilot-instructions: stale code-element references in **23.0% of 356 repos** (95% CI
18.8–27.2%), "degrade AI assistance without any visible error", the two-snapshot git
grep as a CI check; Galster et al. (AIware 2026, context-file population) + Lulla et
al. (JAWs 2026 @ ICSE: AGENTS.md presence ↔ ~29% lower median runtime, ~17% fewer
output tokens); DocPrism (arXiv:2511.00215 — naive LLM drift review flags 98% of docs;
filtered 14%, accuracy 94%); DORA 2022 documentation-quality capability (amplification
+ published lifts) and DORA 2025 ("AI doesn't fix a team; it amplifies what's already
there"; "AI-accessible internal data" capability); SWE-at-Google ch.10 (freshness
metadata + 3-month review reminders); Write the Docs docs-as-code; Silva's Docs as
Tests + Doc Detective (active, v4.30.0); Schemathesis (ICSE 2022 paper) and Specmatic —
with the tool graveyard flagged point-in-time (Dredd archived, Optic archived Jan 2026
post-Atlassian, driftctl maintenance mode, DeepDocs deprecated, Swimm pivoted);
Fluri/Würsch/Gall WCRE 2007 (97% same-revision comment changes); Chroma context rot
(the in-window sense, disambiguated from the new repo-artifact sense).

The per-category **freshness policy** (owner + last-reviewed + interval on durables;
label + timestamp + expiry on AI-generated docs; zero-stale-references contract on
agent config; expiry = suspect, not auto-delete) is flagged as **Report-3 synthesis**.
Topic `know`/`concepts`/`checks` enriched; the I3 `src` list now opens the overlay and
carries the corrected Tan citation + Treude & Baltes. Validator green.

## v1.25 · 2026-07-15

Added the **I2 deep dive — Lifecycle & Write-Permissions as Governance** (topic
`ia-lifecycle`): embedded workbook overlay + standalone
`deep-dives/I2-lifecycle-write-permissions-deepdive.html`, written after the
three-teammate fact pass (2× verification + 1 discovery) **plus the spot-verification
round on discovered sources** — which again earned its keep: the Anthropic harness quote
"it is unacceptable to remove or edit tests…" turns out to guard the *feature-list
entries*, not unit-test files (context corrected before use; the workbook's existing
Report-3 usage was already correct). Fact corrections applied: ThoughtWorks Radar dates
pinned (Lightweight ADRs: Trial Nov 2016 → **Adopt Nov 2017**); MADR expands to
"Markdown **Architectural** Decision Records" (4.0.0, Sep 2024; adds *Rejected*);
OWASP ASI06 rendered by its canonical name "Memory & Context Poisoning" (fixed in the
I4 topic too); Nygard's immutability line quoted verbatim ("we will keep the old one
around, but mark it as superseded").

New load-bearing sources: **ImpossibleBench** (arXiv:2510.20270 — tests mutated to
contradict the spec; GPT-5 cheats 54% of trials, 76% on the one-off variant; Claude
models cheat >79% *by modifying test cases*; paper's mitigation: hide tests or make
them read-only; an explicit escalation tool cut cheating 54%→9%), Anthropic's
"Natural emergent misalignment from reward hacking" (12% sabotage-of-detection-code
figure, Nov 2025), the **Replit production-database deletion** (July 2025, Lemkin/SaaStr;
fixes — dev/prod separation, rollback, planning-only mode — as reported from Masad's
posts), **Copilot coding agent guardrails** as the shipped write-permission matrix
(own identity, signed commits, copilot/ branch only, initiator cannot approve),
GitHub **restrict file paths** push rulesets (GA Sep 2024), the GitLab CODEOWNERS
porosity caveat (privileged pushers bypass), Claude Code Edit/Read deny-rule mechanics
(the `//` absolute-path gotcha; subprocess limitation → sandbox), Atlassian
identity-scoped governance (permission schemes, Rovo agents inherit the invoking
user's permissions, Remote MCP Server GA), Anthropic memory-tool security guidance
(path containment, validate-before-write), and **Lore** (arXiv:2603.15566 — the
"Decision Shadow", git-trailer decision records). The write-permission matrix
(category → write mode → gate → enforcement) and the ADR code-seam grep test stay
flagged as **our synthesis**. I2 topic `know/concepts/checks/src` enriched; deferred
as unverifiable-at-primary: Masad's exact fix wording (secondhand via Fortune/Register),
GitGuardian leaked-secrets figures (not confirmed — excluded).

## v1.24 · 2026-07-15

Added the **I1 deep dive — Artifact Taxonomy: Durable / Derived / Disposable** (topic
`ia-taxonomy`), opening the M4 deep-dive set: embedded workbook overlay + standalone
`deep-dives/I1-artifact-taxonomy-deepdive.html`, written after a three-teammate pass
(2× fact-verification + 1 discovery) **plus a spot-verification round on the discovered
sources** — which caught a fabricated ".claudeignore" claim (no such file in the official
Claude Code docs; excluded) and two smaller corrections (settings.local.json is ignored via
the *global* git excludes file, not project .gitignore; Spec Kit's constitution lives at
`.specify/memory/constitution.md`).

Load-bearing fact outcomes: the workbook's **"Anthropic: memory typology (in-context /
external / in-weights / cache)" source was retired as unpinnable** — no Anthropic primary
source publishes that four-way typology (third-party blogs only); the I1 `src` entry was
replaced. The **triad itself was confirmed as our Report-3 synthesis** (no external
framework packages artifacts this way; flagged in the deep dive like D1–D5, with nearest
precedents cited: Charity Majors' durable/disposable code split, records-management
retention classes, and the industry's never-hand-edit conventions). Nygard's ADR statuses
completed with *Deprecated* (I2 wording fixed); AGENTS.md stewardship corrected to the
Agentic AI Foundation / Linux Foundation (multi-vendor origin), 60k+ repos as point-in-time;
Anthropic memory tool re-verified as GA (six file operations under /memories); the literal
"feature_list.json" softened to the JSON feature-list pattern (I2).

Content (11 sections): the triad with decision tests (disappearance / repair / trust);
durable — the human gate, ADR archetype, agent-facing config as a new durable class, and
spec-driven layouts converging on repo-resident durables (Kiro `.kiro/specs`, Spec Kit
`specs/` + constitution, Claude Code's committed-vs-local settings split); derived — the
never-hand-edit rule and its industry encoding (Go `^// Code generated .* DO NOT EDIT\.$`,
GitHub `linguist-generated` hiding diffs + excluding stats, committed lockfiles as
derived-but-versioned — the axis is the change path, not git), plus the
derived-needs-a-consumer rule anchored by the Ahrefs llms.txt study (137,210 domains, 97%
zero traffic in May 2026, 1.1% of fetches from AI retrieval bots — "largely decoration");
disposable — the Anthropic long-running-harness patterns (claude-progress.txt, JSON feature
list, JSON-over-Markdown as soft write-permission), markdown sprawl as measured default
behavior with Solmaz's SimpleDoc convention as the fix, pruning as context hygiene (Chroma
context rot) with records-management disposition as the precedent; the SSOT boundary
(product vs engineering masters, the pasted-PRD fork, pointer vs labelled digest); grey
zones (agent-written legacy docs derived-until-promoted, memory files as a governed fourth
write-mode, Cline Memory Bank as a de facto taxonomy); the brownfield classification sweep
(five-column table + one-page rule set); framework map; takeaways. Two new SVG figures
(taxonomy flows with promotion path; the SSOT boundary), marker `ahI1a`, edge `edI1`.

Also fixed a real layout bug found while building: the **H2/H3/H4 standalone files lacked
the `<main>` wrapper**, so their desktop two-column grid auto-placed content zigzag into
the 210px TOC column (verified broken in-browser; the workbook overlays were unaffected and
mobile collapsed to one column, which is why it went unnoticed). All three fixed and
re-verified in-browser. I1 topic `know/concepts/checks/src` enriched in the workbook.

## v1.23 · 2026-07-15

Added the **H4 deep dive — Feedback Loop & Handoff Anti-Patterns** (topic `hand-feedback`),
completing the M3 deep-dive set: embedded workbook overlay + standalone
`deep-dives/H4-feedback-anti-patterns-deepdive.html`, written after a three-teammate
fact-verification & discovery pass (facts-toolchain, facts-research, discovery) **plus a
spot-verification round on the discovered sources** — which caught one misattributed figure
(a "communication rates 76.2/62.8/48.8" triple pinned to ClarifyCodeBench arXiv:2607.00711
that does not appear in that paper; kept out, the paper re-cited only for its verified
uneven-by-defect-class finding).

Content (12 sections): the silence data — agents don't ask by default (HumanEvalComm,
ACM TOSEM 2025, arXiv:2406.00215: >60% of code-LLM responses generate code instead of a
clarifying question on 762 ambiguity-injected problems; "Learning to Ask", EMNLP 2025:
models hallucinate missing arguments; HiL-Bench, Scale AI, arXiv:2604.09408, preprint:
Pass@3 67–88% with full information collapses to 1–9% when asking is required, blocker
recall <50% on SWE tasks; Orchid, arXiv:2604.21505, preprint: Pass@1 −7.22 pp average,
−31 pp worst ambiguity type); the agent as upstream detector (Kiro Requirements Analysis,
primary source May 12 2026 — LLM auto-formalization + SMT solving on EARS criteria before
code; the ~60%-of-1,400+-AC figure labelled as AWS internal testing reported via
The New Stack, vendor claim); drift triage on the reqproof question with verified verbatim
wording (Leonid Bugaev, blog.reqproof.com, May 14 2026 — commercial interest flagged) and
three owned exits (fix code / spec PR / logged learning, with Beck's Dec-2025 line as the
third exit's charter); the four handoff anti-patterns (HAP1–HAP4) with detection smells and
controls, explicitly divided from E7's rollout-level catalogue — over-spec (29.6 vs 4.1
tokens/LOC review density), under-spec (Orchid costs; the old "30-minute feature balloons to
3 hours" line **retired as unpinnable** and reframed as an unattributed pattern in all
copies), stale-spec silent drift, throw-over-the-wall (arXiv:2602.00164: 26.1% of 8,106
agent fix PRs closed unmerged, verbatim "syntactically plausible fixes alone are often
insufficient for successful integration"; arXiv:2602.19441, MSR 2026: reviewer engagement
the strongest merge predictor across 33,596 PRs, Codex 82.6% vs Copilot 43.0% merge rates);
a minimal return-channel protocol (**our synthesis**, flagged) with the product survey —
Devin's confidence-gated asking (Devin 2.1, vendor-documented) vs Copilot/Codex clarification
gated to plan modes (point-in-time, mid-2026) — and Agent Decision Records as an early-stage
convention; multi-agent drift (MAST arXiv:2503.13657, preprint, v2 figures cited rounded
~42% specification / ~37% inter-agent misalignment / ~21% verification; hub-node cascade
topology from arXiv:2603.04474 cited for topology only, injected-fault caveat); loop-health
metrics (DORA 2025 **Rework Rate** as the anchor — fifth delivery metric, unplanned
deployments fixing what failed first time; GitClear churn labelled vendor + correlational;
New Relic June-2026 survey labelled vendor-commissioned perception, n=200 — the
94%-review-praise vs 78%-more-incidents contradiction); five brownfield moves (owners,
stop-and-ask instruction, suspect gate, triage ritual, day-0 rework baseline); framework map
and takeaways.

Fact hygiene beyond the new content: Boehm's 100:1 defect-cost ratio flagged as folklore
(Bossavit, *Leprechauns of Software Engineering*) — direction kept, multiplier dropped.
H4 topic `know`/`concepts`/`src`/`checks` and the M3 "Feedback loop" research-notes block
enriched with the verified evidence; topic `src` now opens the overlay (`#h4-deepdive`).

## v1.22 · 2026-07-15

Added the **H3 deep dive — Traceability & Spec Modes** (topic `hand-traceability`): embedded
workbook overlay + standalone `deep-dives/H3-traceability-spec-modes-deepdive.html`, written
after a three-teammate fact-verification & discovery pass (facts-toolchain, facts-research,
discovery).

Content (11 sections): why traceability becomes load-bearing at agent speed (the link is the
memory; Jama May-2026 audit story flagged as vendor illustration, no numbers); the thirty-year
heritage (Gotel & Finkelstein ICRE '94, RTM/ISO-IEC-IEEE 29148, DOORS/Jama "suspect links",
mandatory trace in DO-178C / ISO 26262 / IEC 62304); the ID chain requirement→spec→task→code→
test→PR with the Kiro criterion-level (`_Requirements: 1.2, 2.1_`) vs Spec Kit feature-folder/
branch contrast (v0.12.x, point-in-time); structural vs inferred links (trace recovery ~60–85%
by method, RAG best-case ~85.5% recovery accuracy RE:FSQ 2025; ReqToCode arXiv:2603.13999 on
ID persistence under AI modification; inference reserved for one-shot brownfield bootstrap);
a git-native suspect gate (**our synthesis**, flagged; Kiro precision: "Sync Files" is
task-completion sync only — no drift detection in today's SDD tools); Böckeler's three spec
modes with verified verbatim definitions (Birgitta Böckeler, martinfowler.com, 15 Oct 2025),
Beck's verified Dec-2025 objection, and Tessl's Jan-2026 pivot away from spec-as-source
(point-in-time); a new **provenance** section (AIDev census arXiv:2606.24429 — bot detection
recovers 3.3% of Claude Code commits, 30× undercount; Assisted-by vs Co-authored-by trailer
debate incl. the VS Code default-trailer revert; GitHub Copilot PR attribution; EU AI Act
Art. 11 horizon with vendor-gloss caveat); a five-move minimal ID scheme for brownfield
clients (**our synthesis**, flagged) answering the topic's open scaling question.

Fact corrections applied across all copies:
- The unpinnable "~64% ML traceability accuracy" figure **retired** in the H3 topic `know`
  and Report 2 notes — replaced by the verifiable band (~60–85% by method) with sources.
- **"Martin Böckeler" → "Birgitta Böckeler"** in the E8 reading list (workbook overlay +
  standalone).
- The Beck paraphrase ("you learn during implementation; the spec changes") replaced by his
  verified LinkedIn wording ("encodes the (to me bizarre) assumption that you aren't going to
  learn anything during implementation that would change the specification") in E8 (both
  copies), Report 2 notes, and the H3 check answer.
- Report 2 invalidation bullet now credits the RM-tool heritage and notes SDD tools don't
  ship it.

Workbook plumbing: H3 topic first `src` → `#h3-deepdive`; `know` rewritten (5 bullets incl.
provenance), `concepts` +"provenance trailers", second self-check added; overlay wired
(scoped `edH3`/`ahH3a` CSS + JS handler); version bump + this entry.

## v1.21 · 2026-07-15
**Deep-dive modal UX pass** (design-led, brainstormed spec + in-browser verification via
chrome-devtools; spec at `docs/superpowers/specs/2026-07-15-deepdive-modal-ux-design.md`):
- **Full-width surface.** The overlay `.panel` widened 1000→1180px; the `max-width:74ch` cap
  removed from the wide blocks so `.io` cards, `table.map`, `.comp` cards and figures span the
  full content width. Prose (`p`, `.lead`) and callouts keep a reading measure via a new
  `--rd` (~82ch) so line length stays legible; callout/reading boxes hug that measure.
- **Section navigator.** The `.bar .tag` (the black `H · DEEP DIVE` chip) became a toggle
  (`role=button`, `aria-expanded/controls`, caret) that opens a `.secnav` popover listing every
  `§` heading; clicking a row smooth-scrolls the panel to that section (respects reduced-motion).
- **Reading progress.** An Intersectionless rAF scroll handler on the `.panel` marks sections
  as the reader passes them; a `seen X/N` chip sits before the close button, a `.ddprog` fill
  line under the bar tracks scroll position, and popover rows get a "seen" tick + a "current"
  highlight. The seen-set persists through the existing `store` (`state.seen[<overlayId>]`,
  key `agentic-study-v1`; included in export/import) so it survives close/reopen.
- **Generic + scoped.** One `initDeepDiveNav()` keyed off each `.e1ov[role=dialog]` with ≥2
  `h2` sections — all 17 content overlays (H1, H2, D1, E1–E8, P1–P5, SDLC) get the features with
  no per-overlay wiring; the version-history modal is excluded. Headings get stable ids
  (`<overlayId>-s<n>`, assigned only if absent). No content or topic-id changes.

Note: the feature code itself landed in commit for v1.20 (bundled by a concurrent session that
committed the shared working tree); this entry adds the version bump and documentation. Validator
green.

## v1.20 · 2026-07-15
**Added the H2 deep-dive companion** (EARS & Gherkin: machine-verifiable acceptance criteria) —
second in the M3 set, embedded as an in-page overlay and as the standalone
`deep-dives/H2-ears-gherkin-deepdive.html`. Content: the verification gap (ambiguity in /
unverifiability out), the six EARS templates with the password-reset worked example, Gherkin
as the executable criterion that doubles as the agent's reward signal, the
story→EARS→Gherkin→red-tests ladder with the spec-review gate, the writing craft (declarative
what-not-how, BRIEF, failure paths) and the BDD trap with the fourth-amigo ownership answer.
Three-teammate fact-verification pass: EARS co-authors (Wilkinson, Harwood, Novak) credited and
the blue-chip adopter roster reframed as creator-self-reported; Given–When–Then dated to ~2004
(North & Matts); SpecFlow EOL Dec 2024 → Reqnroll (Nagy); Spec Kit's section heading verified as
"Acceptance Scenarios"; ClarifyGPT 11.52% confirmed as *relative* Pass@1 (GPT-4 avg, four
benchmarks), Bashir 20.2% reframed as 10-shot-vs-0-shot (ICSME 2025), Wang +23.2 pp confirmed
(arXiv:2508.06888). New sources from the discovery pass: Mathews & Nagappan (ASE 2024)
tests-in-prompt evidence, SWE-bench Verified's FAIL_TO_PASS oracle, AutoUAT/TestFlow
(arXiv:2504.07244), QVscribe EARS-conformance tooling, Automation Panda's
Gherkin-guidelines-for-AI. H2 topic data enriched (know/checks/src) with the corrected framings.
Both new tables ship inside the v1.19 `.figscroll` wrapper.

## v1.19 · 2026-07-15
**Table-responsiveness sweep completed** (finishes what v1.18 started): the remaining 36
`table.map` tables — E1–E6, P1–P5, D1, SDLC-foundations, and the workbook's SDLC/Domain-map
and topic sections — are now wrapped in the `.figscroll` container. All 50 tables across the
artifact set now scroll horizontally in their own box below 760px instead of overflowing the
page, matching the diagrams and the H1/E7/E8 tables. Applied in both copies (standalone files
and the workbook overlays/sections). No content changes. Validator green.

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
