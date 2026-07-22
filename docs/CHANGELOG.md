# Changelog

Version history of the workbook (`workbook/agentic-development-study.html`). Mirrors the
in-app version-history modal (top-bar button). Dates are when the work was done in-session.

## v1.64 · 2026-07-22

Added the S5 deep-dive companion (Loop / Auto-Run: Self-Modification, YOLO & Sandbox Escapes) — fifth M7 companion. Verified by a 10-agent swarm + 5-agent spot-verify round. The loop as its own threat surface (Replit's code-freeze production-DB deletion — "eleven times in ALL CAPS" — vs Copilot's one settings line; GTG-1002's 80–90% autonomous campaign); the self-escalation class with a full CVE ledger (CVE-2025-53773 autoApprove; CVE-2026-22708 env-poisoning built-ins with the alias correction — export/typeset/declare/readonly/unset/local — and the 7.2-vendor-CVSS-4.0/9.8-NVD-3.1 dual scoring; CVE-2025-59532 model-chosen sandbox root; CVE-2026-25725 SessionStart-hook persistence; CVE-2026-39861 symlink; CVE-2026-48124; CVE-2026-26268; TrustFall 21852/33068) plus Mini Shai-Hulud persisting through agent config in the wild; the hands-off-mode taxonomy with vendor-verbatim honesty ("offers no protection against prompt injection"; "Never use 'Run Everything' mode") and the 2026 classifier-gated middle path filed under S3's litmus; the hollow gate (GhostApproval's pre-authorization writes — "an undo mechanism, not an authorization gate"); the sandbox stack as shipped with Anthropic's "not a complete isolation boundary" and six escape classes (Pillar's week — 2 days old, Guan's null-byte through ~130 versions, Ona's agent-reasoned escape) plus SandboxEscapeBench (0.49/0.50 at default, zero at difficulty 4–5, Mythos saturation caveat); the loop resisting termination (Palisade 47%, METR 70–95% still hacking, peer-preservation 31% in production harnesses); write-gating the enforcement configuration as S3's open question answered (#11226 with the stale-bot correction, srt Mandatory Deny Paths, root-owned managed settings, the residual Edit/Write gap); and autonomy ceilings (L3 holds; reviewed-after challenged, 94%/56%) with three STOP conditions. Three SVGs (self-escalation cycle, gate spectrum, containment stack) + two tables (CVE ledger, vendor taxonomy). Topic fact fixes in sec-loop: alias dropped from the built-ins list, DuneSlide attributed to Cato AI Labs with the 9.3-vendor/9.8-NVD split, new know bullet on CVE-2026-25725 + GhostApproval pre-authorization writes, first src entry now opens the deep dive.

## v1.63 · 2026-07-22

Added the S4 deep-dive companion (MCP / Tools: the Richest Attack Surface) — fourth M7 companion, built on an 8-agent verification + discovery swarm followed by a 6-agent spot-verify round. The two-way trust boundary (descriptions/results in as trusted content, calls out with user privileges); the protocol's own disclaimers (tool annotations "MUST be considered untrusted" per spec MUST-language; "authorization in MCP is optional" per the NSA CSI, May 2026); class 1 in depth (GitHub MCP toxic flow; the Supabase "CURSOR CLAUDE" PoC with Supabase's "Where We Got It Wrong"); class 2 (postmark-mcp's one-line BCC in v1.0.16 after fifteen clean versions; Invariant's tool poisoning/shadowing verbatim; SANDWORM_MODE's McpInject worm module; MCPTox 72.8% ASR, more capable models more susceptible); class 3's CVE ledger (mcp-remote 9.6, Inspector 9.4, reference filesystem/git servers, TS SDK DNS-rebinding, MCPwn 9.8 with contested patch status); the privilege & config layer (Astrix 88%/53%/8.5%, GitGuardian 24,008 secrets / 2,117 valid, Smithery registry breach, config-as-execution CVE-2025-61260 / CVE-2026-47751, Bitsight/Trend Micro shadow estate); and the defense stack (client allowlists + pinning, scoped tokens, read-only defaults with the #2156 caveat, gateways, spec OAuth fixes, Snyk Agent Scan) keyed to OWASP MCP Top 10, CoSAI, NIST CAISI and ATLAS AML.T0086. Four SVGs (trust boundary, three-class map, GitHub chain, defense seam). Fact fixes elsewhere: "all three ingredients in a single package" re-attributed to Willison (S4 topic + Report 6); General Analysis Supabase post re-dated Jul → 16 Jun 2025 (S2 both copies, Report 6, I7 topic, domain map V5); the rug-pull stat corrected from "0/8 libraries" to 0/8 techniques across 3 libraries (S2 both copies).

## v1.62 · 2026-07-21

Added the S3 deep-dive companion (Advisory vs Deterministic Controls; the Rules File Backdoor) — third M7 companion. The advisory/deterministic split as M7's organizing principle, anchored in OWASP LLM07:2025 ("deterministic, auditable manner"), Anthropic's containment post (25 May 2026, "the deterministic boundary is what gets hit when everything probabilistic misses", 24/25 exfiltration red team) and Rehberger's instruction-hierarchy verdict; the advisory layer calibrated by ETH Zurich's AGENTS.md study (arXiv:2602.11988 — steering is real, so a poisoned file is dangerous); the Rules File Backdoor anatomy (Pillar, 18 Mar 2025; ATLAS AML.CS0041) with attribution fixes (AML.CS0041 is a case-study id — techniques are AML.T0068/T0081/T0067; the Tag-block range comes from the technique literature, not Pillar's prose; the PoC was script injection, not exfiltration); the §3 evidence file (ImpossibleBench 54%/76%, Nasr et al. >90% adaptive bypass for most, AIShellJack 84%); the deterministic stack with the hooks-tighten-only correction; and §5's incident record (CVE-2025-59536/21852, NVIDIA's AGENTS.md rewrite, CamoLeak with the CVE-2025-59145 debunk, Mitiga Skillgate pending) plus CSA's governance checklist. Three SVGs (two layers, backdoor pipeline, E5 litmus). Fact fixes elsewhere: S8's hooks claim rewritten (tighten-only; permission system for hard allow/deny) and Anthropic's containment post re-dated Jun 2026 → 25 May 2026 in both S2 copies.

## v1.61 · 2026-07-21

Added the S2 deep-dive companion (The Lethal Trifecta & the Rule of Two) — second M7 companion. Willison's three legs verbatim (16 Jun 2025) with the [A]/[B]/[C] lettering correctly attributed to Meta, Meta's Agents Rule of Two (31 Oct 2025) with the widened [C] leg, session-scoped transitions and the "safe" → "lower risk" correction Willison prompted, four trifecta incidents as one A→B→C shape (GitHub MCP, EchoLeak CVE-2025-32711, Supabase MCP, GitLost), the per-leg control map with 2026's egress honesty (CVE-2025-66479, the null-byte parser differential, "allowlist = capability grant, not destination filter"), Oso's digital gossiping applied to the orchestration graph, persistent memory as carried-forward leg A, and the human gate's documented failure modes (93% approval fatigue, Lies-in-the-Loop, Unicode TAG concealment, 0/8 rug-pull re-approval). Four SVGs (trifecta Venn, Rule-of-Two menu, per-leg control map, gossiping cluster). Topic fact fixes: the Meta src entry is now dated and linked (31 Oct 2025), "digital gossiping" is attributed to Oso (Dec 2025), and the egress-allowlist overclaim is softened to defense-in-depth.

## v1.60 · 2026-07-21

NEW DIAGRAM GALLERY — browsable grid of all 74 figures from the deep-dive companions. Added `gallery.html`, `gallery-registry.json`, and `scripts/generate-gallery.py`; registered every deep-dive figure; updated `CLAUDE.md` golden rule 3 with a site-level navigation exemption and added the gallery registration step to the typical next-task recipe; gitignored `gallery-registry-draft.json`.

## v1.59 · 2026-07-20

Added the S1 deep-dive companion (Security is cross-cutting: prompt injection & blast-radius reduction) — opening module M7. The root cause from primary sources (Willison's token-stream quote, the Sep 2022 coinage, the SQLi-analogy arc through NCSC's "it may be worse", 8 Dec 2025), the privileged runtime as confused deputy (Hardy 1988; NCSC "inherently confusable"), the assume-breach posture with lineage (Saltzer & Schroeder → NIST SP 800-207 → Microsoft → Bargury) and three honest caveats (gates see less, laundering defeats scanning, memory breaks reversibility), the honest ceiling with the arms-race arc (instruction hierarchy → Spotlighting → StruQ/SecAlign → CaMeL/design patterns; Attacker Moves Second as ">90% for most" with PIGuard 71%/MELON 76%; 2026 confirmations SoK >85%, AutoDojo), client wording borrowed from OWASP/NCSC/OpenAI, and the cross-cut map keyed to OWASP ASI01/ASI03. Two SVGs (token stream, blast-radius funnel); Kiro and Comment-and-Control as dual hooks. Fact fixes: the S1 know bullet and Report 6 TL;DR now carry the verified ">90% for most" figure with full affiliations, dropping the unattributable "architectural limitation" phrasing for OWASP's own wording. Verified by a 12-agent swarm; fast-moving items marked point-in-time.

## v1.58 · 2026-07-20

Added the D7 deep-dive companion (Design Archaeology & the F0–F4 Rollout) — completing module M6. The characterization parallel (golden-master baseline + de-facto token extraction as the visual layer's B2; Frost's 2013 interface inventory and Curtis's audit practice as anchors), the F0 audit toolbox (Project Wallace DTCG + usage counts; Dembrandt --compare drift gate; CSS Stats/Superposition flagged stale), the golden-master tooling landscape (Percy AI review shipped vs Chromatic pixel-only; Lost Pixel archived), the agent-readiness heatmap (legibility × brand risk; Callahan, Curtis 0–4 scorecard, stylelint-polaris coverage), the F0–F4 permission ladder with the F0 STOP branch (B6 spine-and-rails), strangler mechanics decomposed into named practice (Fluent shims, Carbon windows, Polaris lifecycle, Gestalt lint — pattern name flagged as ours), the measured risk ledger (CodeA11y 0-of-16, WebAIM 95.9%, EAA/EN 301 549, CodeRabbit 1.7×/2.74×-XSS, Veracode 45% flat across generations, the MCP injection canon incl. Figma hidden-layer injection) and the mature end-state. Fact-checked via a 12-agent verification + discovery swarm; all load-bearing figures confirmed against primary sources.

## v1.57 · 2026-07-20

Added the D6 deep-dive companion (The D1–D5 Design Scale & the Designer as Curator) — completing the M6 set with D7. The three-ladder verification split (engineering earns rungs deterministically; design and product cap where deterministic gates end), the five D-levels with evidence per rung (Design2Code ceiling, Krebs slop audit 22/32/46, CodeRabbit 1.7×/2.74×-XSS, Veracode 45%, CodeA11y 0-of-16), the D5 anti-pattern argued against Nielsen's Level-6 counter-position, the designer-as-curator role with its Junior Designer Dilemma, and the honest D3→D4 gate-metric gap. Fact-checked via an 11-agent verification swarm; also corrected the D7 Veracode misattribution.

## v1.56 · 2026-07-20

**NEW RUNBOOK PB5 — Pilot: measure, gate, decide.** Fifth and final M9 runbook, in both
copies (`deep-dives/PB5-pilot-runbook.html` + in-workbook overlay): ten checklist steps
across three phases — pre-registration (the PB1 baseline re-pulled with the computability
question answered in writing, the token/cost column PB1 left open, a two-arm design with
a protected control arm, the signed pre-registration plus a dry-run probe), the measured
window (F2 at the granted level with small batches held, weekly guardrail dials, enablement
and perception capture), and read & decide (honest deltas with stability beside throughput,
the F2→F3 gate's three exits GO/HOLD/STOP, the pilot report routed into the field-report
loop). Distills E7 (the DORA process and the METR method) and B6 (the gate table,
back-triggers and STOP criteria) into the decision layer that closes the journey. Single
entry posture: a recorded PB4 GO; PB1's report §3 is the "before" snapshot. Deterministic
where the theory is: back-trigger thresholds agreed at gate-opening so demotion is a number
acting, not a meeting (the Digital Apprentice asymmetry, flagged as a design proposal), and
the Phase-A dry run — a metric pipeline that has not run once on real data is not installed.
Fresh evidence layer (verified 2026-07-20): the "2× mandate" longitudinal study
(arXiv:2607.01904 — 802 developers, 196,212 PRs: 2.09× throughput, per-reviewer load roughly
doubled, automated review overtaking human review, merge/revert stable), METR's 2026
design-change note as the contamination cautionary tale (30–50% withheld tasks, self-rated
"very weak evidence" — the control arm is the scarce resource), DX's Core 4 AI addendum
(no new metric; adoption and token spend filed as "diagnostic telemetry"; in-house 27.4%
AI-authored production code and ~7.8% PR lift), the cost-to-merged-feature benchmark
($5.56–$69.97 — token price and cost-to-merge can point in opposite directions), and
Copilot's usage-based billing (since 2026-06-01). Honest handling kept throughout: MIT NANDA
quoted with its real wording ("95% of organizations are getting zero measurable return", methodology
300+/52/153 — never "95% of pilots fail"), the two 24%-ish PR findings (Microsoft, Faros)
never merged into one number, vendor telemetry labelled, direction-only claims below the
pre-registered sample floor. Adversarial spot-verify (ten claims against primary sources:
nine confirmed) caught one wording erratum pre-release — MIT NANDA's verbatim line includes
*measurable* ("getting zero measurable return"), fixed here and in both B6 copies. Exit: a signed GO / HOLD / STOP — GO recycles PB2/PB3 per
module into F3, HOLD is a normal exit, STOP is the recommendation a roadmap must be able
to make. **M9 complete at 5/5: Assess → Bootstrap → Harness → Handoff → Pilot.**

## v1.55 · 2026-07-20

**NEW DEEP DIVE D5 — The design harness: verification loops & guardrails.** Fifth M6
companion (`deep-dives/D5-design-harness-verification-guardrails-deepdive.html` + in-workbook
overlay), three SVG diagrams. The six-layer stack in cost order (style lint → API contract →
interaction tests → axe-core → visual regression → designer gate); visual-regression practice
(pixelmatch mechanics, CI-built baselines in pinned images, deliberate-only updates, the
false-positive taming sequence that answers the topic's open question) plus the stress-state
matrix (forced-colors/dark/contrast/reduced-motion/RTL/320px as cheap harness checks — the
swarm's missing-things addition); axe-core as the a11y gate with honest limits (~105 rules /
~90 default, zero-false-positive policy, Deque's 57% = issue volume not criteria, GOV.UK
143-barrier study, WCAG 2.2/EAA, overlays anti-pattern with the FTC accessiBe order);
lint-as-law (color-no-hex, declaration-strict-value, no-restricted-imports,
primer/polaris/slds-linter/carbon configs, Dembrandt drift gate); conformance vs quality with
benchmark triangulation. Fact pass corrections: **FrontendBench's 90.54% re-attributed to its
scripted test harness (no LLM judge in the paper) — the workbook topic and Report 5 notes
fixed**, WebDevJudge's ~70% LLM-judge plateau added as the counter-weight; the "ds-lint 233
WCAG rules" claim retired as unverifiable; FigmaLint re-attributed to Southleft (Frosts
co-present); Uber block+ticket and Shopify 14% labeled vendor-blog-only anecdotes; Storybook 9
dated June 2025 with the `storybook/test` import; Chromatic noted as having NO AI diffing
(Percy/Applitools claims labeled vendor).

## v1.54 · 2026-07-20

**NEW RUNBOOK PB4 — Handoff: run the contract end-to-end.** Fourth M9 runbook, in both
copies (`deep-dives/PB4-handoff-runbook.html` + in-workbook overlay): eleven checklist steps
across four phases (contract discipline — owners, template, ids; machine-verifiable criteria
— the story→EARS→Gherkin→red-tests ladder and the ten-minute spec review; the return channel
& drift loop; the delivery & exit gate), distilling H1–H4 into the discipline that decides
what the caged module's agent is told to do. Single entry posture: a recorded PB3 GO; PB1's
editor becomes the requirement owner, PB1's baseline the loop-health control. Deterministic
where the theory is (E5 litmus): the REQ-id gate and H3's suspect gate ship as runnable CI
blocks, stop-on-ambiguity and id-stamping as *appends* to PB3's AGENTS.md master — never a
second steering file; acceptance tests ride PB2's net agent-read-only under PB3's hook.
Judgment stays human by construction: intent and non-goals human-written (Rationale Clarity
1.54 vs 2.66, arXiv:2507.15157), the agent as fourth amigo (drafts and asks, never ratifies),
the weekly triage's three legal exits — code-wrong / requirement-wrong / we-learned — each an
artifact change, never chat. Evidence framing honest: HumanEvalComm >60% code-instead-of-asking
(TOSEM 2025), SWE-Bench+ 32.67%/31.08% false greens, review-density 29.6 vs 4.1 tok/LOC,
unmerged tail 26.1% + MSR 2026 reviewer engagement, provenance undercount 3.3%/30×, METR
perception gap; preprints labelled (HiL-Bench 67–88→1–9, Orchid ~7.2pp/31pp), Ambig-SWE
(arXiv:2502.13069) cited as mechanism only. Fresh point-in-time layer (verified 2026-07-20):
Copilot↔Jira GA Jun 25 — the issue body IS the prompt (plus Devin↔Linear, Cursor↔Linear/Slack),
Spec Kit v0.13.0, Kiro's EARS default + Analyze Requirements gate (no drift detection — not
credited with one), gplint over the stale gherkin-lint, the `Assisted-by:` trailer standard
vs Claude Code's `Co-Authored-By` default, EU AI Act disclosure from Aug 2026. Böckeler's
spec-first→spec-anchored→spec-as-source ladder names the target: spec-anchored, via the loop.
Adversarial spot-verify caught two seed errors pre-release (gplint v2.5.2 = Apr 2024 not 2026;
QEMU is NOT an `Assisted-by:` adopter — it still bans AI contributions and floated its own
`AI-used-for:` trailer) plus one H1 erratum, fixed in both H1 copies: the SDD tool review and
its "rather review code" counter-view belong to Birgitta Böckeler, the article's actual author
— not Martin Fowler. Exit test: one real feature merged with review against green acceptance
tests; GO → PB5 Pilot. M9 at 4/5 — next PB5 Pilot.

## v1.53 · 2026-07-18

**NEW DEEP DIVE D4 — Governance & SSOT in the design world.** Fourth M6 companion
(`deep-dives/D4-governance-ssot-design-world-deepdive.html` + in-workbook overlay), three
SVG diagrams. Curtis's team models with the 2024 retraction quoted exactly ("federated is
not a choice, it's a facet" — the circulating "facet, not a model" form marked as
paraphrase; "Overlords don't scale" re-anchored to the solitary model it actually
targets). The hybrid operating model — core team owns tokens/APIs/governance, agents
generate and maintain, designer gate approves (L3 on the design layer) — grounded in
documented mechanics: Carbon's component checklist + Labs incubation + CLA, Primer's
closed writes with weekly triage, Paste's build-time status schema, SLDS's "please ask
first", Figma branch review + library analytics. Versioning as the system's clock: SemVer
(Curtis 2018), warn→wait→remove with real windows (Lightning 18 months, Origami 3–6),
codemod-attached deprecation (Atlassian, Apr 2026), plus the three agent-consumption
rules — manifests show current APIs only, "never hallucinate a prop", deprecated
machine-flagged — and the ADR-lifecycle mapping. The durable/derived/disposable
write-permission table applied to design artifacts (agents free in disposable, regenerate
derived, propose-only to durable). The SSOT argument in three verified positions — Sewell
("Figma is, at best, a set of suggestions"; the Shopify/Uber/GitHub anecdotes labeled
unsourced vendor assertions in a product-pitch article), Başcı/JumpCloud ("Figma is
upstream input, not downstream truth"), Ulrey ("a single source of truth is a lie" — the
"cohesive knowledge ecosystem" phrase marked as our paraphrase, not his words) — plus
Equinor's tokens-first stance, Vallaure's contract-in-the-middle, and Figma's Code Layers
(Jun 2026) flagged weeks-old watch-list. New section the outline missed, from the swarm's
extras hunt: provenance, disclosure and the audit trail of machine contributors (OSS
GenAI-governance policy clusters; Chung & Hassan, AIware 2026: ≥96% agent-initiated PRs
vs <0.1% agent-authorized merges; "logs record the executor but not the decision-maker").
Southleft's 69→100 contract experiment labeled vendor POC. Fact pass: 6-agent
verification swarm with real catches (Curtis quotes corrected to verbatim, Paste
versioning docs 404 caught, SLDS SemVer softened to "SemVer-shaped", Builder.io
attribution split Shopify-lint / Uber-CI / GitHub-PR-check). Topic `des-governance` src
now opens the overlay first.

## v1.52 · 2026-07-18

**NEW RUNBOOK PB3 — Harness: stand up the engineering harness.** Third M9 runbook, in both copies (`deep-dives/PB3-harness-runbook.html` + in-workbook overlay): thirteen checklist steps across four phases (context layer extracted-not-decreed, deterministic guardrails, the write-permission matrix & the platform layer, autonomy & the probe-driven exit gate), distilling E1–E5 and I2 into an installable harness for the module PB2's GO opened. Its templates ARE the starter kit — runnable configs, not prose: a `settings.json` permission baseline carrying the verified gotchas (deny→ask→allow with no exceptions, `Edit(path)` covers Write, settings-file path anchoring, deny rules don't bind subprocesses), a PreToolUse guard hook (deny + reason, no-opinion fall-through, regression-checked), a CI verification gate (suite intact · genuinely green · mutation bar per the PB2 ADR), a gitleaks/detect-secrets/TruffleHog secret-scan stack, the I2 write-permission matrix pre-filled for week one (Report 3 synthesis, flagged), CODEOWNERS + restrict-file-paths with the GitLab caveat, and the harness-install report. Single entry posture by design: a recorded PB2 GO. Answers the topic's open question via I2's sequencing — gate the scorers first, then the steering files, then decisions, then the long tail. One correction carried, flagged point-in-time: per current official docs a PreToolUse hook decision does NOT override `permissions.deny/ask` (E5's prose describes hook-wins semantics — erratum to follow); E5's design rule stands (no-opinion fall-through, never blanket-allow). Evidence framing honest: ImpossibleBench 54% / >79% test-editing / abort-tool 54→9 (arXiv:2510.20270), the Replit July 2025 code-freeze incident, harness variance 7.8× (arXiv:2605.23950), GitGuardian 2026 as vendor-published research (28.65M secrets +34%, AI-tied +81%, 64% unrevoked; the pinned 3.2% vs 1.5%), named MCP CVEs only — no aggregator stats. Every DONE criterion is a deliberate probe, blocked or caught, verified once. Exit: GO → PB4 Handoff; demotion instant, promotion slow (E6).

## v1.51 · 2026-07-18

**NEW DEEP DIVE D3 — How agents consume design context.** Third M6 companion
(`deep-dives/D3-how-agents-consume-design-context-deepdive.html` + in-workbook overlay).
The four channels that carry design context into the context window, in ascending
fidelity: the screenshot ceiling measured (Design2Code, NAACL 2025 — 49% interchangeable
/ 64% preferred for GPT-4V with self-revision, caveats attached), Figma MCP post-GA
(read GA since Oct 2025; seat gating, the 351,378-token context bill, scoped-fetch
mitigations), Code Connect as the identity layer that kills hallucinated components
(template files recommended, `figma.connect()` legacy; Org/Enterprise gating; partial
coverage degrading silently), and Storybook MCP with the self-healing
consume–generate–verify loop (10.3+, React-only docs in Preview; the 12.8% / 2.76× /
−27% figures labeled vendor claims — and 12.8% is improved code usage, never acceptance
rate). The FigmaBench metadata trap (Dec 2025 preprint) bounds the structured-is-better
claim; the vibe-tool defaults (v0 Design Systems 2.0, Lovable design-system.json, Bolt
in-tool Storybook — all paid-tier gated); the §7 channel ladder (repo always, metadata
scoped, identity where it pays, verification in the loop, screenshots as supplement)
with its security surface (CVE-2025-53967, hidden-layer injection); and the evidence
file with its do-not-cite list. Topic `des-consumption` src now opens the overlay first.

## v1.50 · 2026-07-18

**NEW RUNBOOK PB2 — Bootstrap: build the verification base.** Second M9 runbook, in both copies (`PB2-bootstrap-runbook.html` + overlay): twelve checklist steps across four phases (read-only module comprehension, characterization safety net, mutation audit, minimal CI & the F0→F2 exit gate), distilling B1 safe ordering, B2 characterization/golden master and B3 mutation gate into executable practice. Handles both PB1 exit postures — GO (≥17, 4/4 gates: bootstrap the pilot from PB1's shortlist with the report §2 numbers as baseline) and score <10 (PB2 *is* the engagement deliverable). Six copy templates: the "document, don't fix" generation prompt with the SUSPECTED-BUG convention, the TestGen-LLM three-gate CI filter, a shared ADR skeleton (kept pins per Hyrum's Law + the mutation-gate decision), read-only enforcement (CODEOWNERS + harness deny rule — enforcement, not a prompt request), a diff-scoped Mode 1 mutation job, and the module bootstrap report. Evidence framing kept honest throughout: the ~70% mutation threshold is our working heuristic recorded in an ADR, never an industry standard; the toolbox table is explicitly point-in-time (mid-2026, re-verify before a client meeting); wrong-orderings (WO1–WO4) and never-do gate failure modes embedded as callouts. Exit: GO opens PB3 write scope for the module; NO-GO keeps it at F1 with mutation survivors as the agent's next task list.

## v1.49 · 2026-07-18

**NEW MODULE M9 — Playbook: from theory to practice. First runbook PB1 Assess.** The practice layer lands inside the workbook: five `pb-` topics ordered by the engagement journey (Assess → Bootstrap → Harness → Handoff → Pilot), built for the internal team to carry the methodology to a brownfield client. PB1 ships complete — a runbook companion in both copies (`PB1-assess-runbook.html` + overlay) with nine checklist steps across five phases (verification base & delivery baseline, information architecture, governance minimum, team readiness, evaluation), each step carrying the action, the theory link that justifies it, and a DONE criterion; plus two copy-paste templates (readiness questionnaire with four non-compensable [GATE] criteria, assessment-report skeleton with a delivery-baseline section), the score→L1–L5 recommendation table and the F0 go/no-go with STOP criteria (the scoring model is our synthesis, flagged). The delivery baseline (DORA keys + cost per merged PR) is captured at assess time — a pilot without it can be neither proven nor disproven. NEW interaction layer: runbook checkboxes persist through the existing store (`agentic-study-v1`, new `pb` field, mirrored into cross-device sync), with a per-runbook progress chip and copy buttons; the standalone copy is deliberately non-persistent. PB2–PB5 are visible as in-preparation topics (one runbook per future version; PB3's templates will be the harness starter kit — runnable hook/permission/CI configs, not prose). Validator extended: `pb-` prefix recognised, checklist step ids checked for uniqueness (they are frozen progress keys, like topic ids).

## v1.48 · 2026-07-18

**SYNC — delta sync over the existing Yjs/HTTP layer.** Pushes and pulls now carry Yjs
*diffs* against the server's last known state vector instead of the full encoded
document on every change (previously a "section read" uploaded the whole state, and the
payload grew monotonically with edit history).

- The client persists `ssv` (the server's last known state vector) in
  `agentic-study-sync-v1`; the push body is `Y.encodeStateAsUpdate(ydoc, ssv)` with the
  current vector in an `X-State-Vector` header, and the Worker replies with only the
  diff the client lacks. `ssv` advances only after a successful push and only to the
  vector actually sent — pulls never advance it — so offline and mid-flight edits
  always reach the server.
- New pull endpoint `POST /r/:code/sync` (client state vector → missing diff);
  `POST /r/:code` accepts the optional header and falls back to full-state replies
  without it (older clients unaffected); `POST /new` + `GET /r/:code` unchanged.
- Every 25th push (and any push while `ssv` is null) sends full state: the periodic
  reconciliation that restores the self-healing property against the non-atomic KV
  get→put race, which full-state pushes used to provide implicitly.
- Server storage unchanged (one compacted snapshot per code in KV); Worker redeployed.
  Spec: `docs/superpowers/specs/2026-07-18-delta-sync-design.md`.

## v1.47 · 2026-07-18

**NEW DEEP DIVE D2 — Design tokens as the visual contract (DTCG).** Second M6 companion
(`deep-dives/D2-design-tokens-dtcg-deepdive.html` + in-workbook overlay). Built on a
four-teammate fact/discovery pass + a three-agent adversarial spot-verify round (13th session
in a row it caught real errors).

- Token anatomy ($-prefixed properties, groups, curly-brace aliases, `.tokens`/`.tokens.json`,
  `application/design-tokens+json`) and the **tier model credited precisely**: community
  practice, NOT DTCG normative text — Curtis 2016 options/decisions as the two-tier root;
  zeroheight 2026 distribution (only ~10% single-layer, full three tiers in just over half).
- The 2025.10 release **read precisely**: stable = Format + Color modules only; theming/modes
  live in the separate Resolver Module — an explicit "do not implement" draft; the W3C
  announcement itself headlines theming (marketing vs normative callout). Status verbatim
  pinned ("not a W3C Standard nor is it on the W3C Standards Track"; CG Candidate
  Recommendation under the Final Specification Agreement). **The workbook's earlier "theming
  shipped in 2025.10" wording corrected** in the D2 topic bullets and Report 5 notes.
- History corrections: term coined by **Jina Anne** at Salesforce ~2014 (the circulating
  "Jon Levine co-coined" is unverified — dropped); DTCG founded 2019 (Anne + Deloumeau-Prigent);
  June 2026 chair transition (Anne & Head → chairs emerita).
- The mid-2026 pipeline, point-in-time: **Style Dictionary v5 shipped** (v5.5.0 Jun 2026;
  full 2025.10 coverage converging, issue #1590 — corrects Report 5's "v5 in progress");
  Terrazzo (= Cobalt UI renamed); Tokens Studio git sync = paid tier; Figma Variables API
  Enterprise-gated + native DTCG export announced but not GA (reported ~Nov 2026); Penpot =
  first **open-source** design tool with native DTCG tokens.
- Sync direction as THE governance question: code-first default (Sopelnik verbatim "design
  tokens are code, not design files", Feb 2026; Builder.io/Sewell "Code is the source of truth
  (not Figma)", Sep 2025), with **Adobe Spectrum** as the designer-authored/code-stored
  counterexample-shaped confirmation (Braithwaite, Knapsack, May 2025); model table (our
  synthesis).
- The agent contract (§5): Pandya's "closed set of values instead of fabricating new ones";
  supply channels (repo JSON, Figma MCP `get_variable_defs` beta with default-mode limitation,
  design-system.json/shadcn registries) and **DESIGN.md** (Google Labs, Apr 21 2026, alpha,
  DTCG + Tailwind exporters, lint CLI with agent-actionable JSON; next-day Anthropic-ecosystem
  uptake request; the circulating tool roster = third-party commentary, not spec text);
  enforcement stack (Stylelint color-no-hex / allowed-list / declaration-strict-value, ESLint
  no-restricted-imports, Dembrandt drift gate with exit codes).
- Evidence file with **corrected dating**: zeroheight 56→84% = the 2025 report (n=294, fielded
  late 2024), NOT "2026 vs a year earlier"; 2026 report = 86% (n=147) with the ~40% pipeline
  gap; CHI 2026 EA (Cha/Jo/Shin/Seo) registry-based 95.08% compliance (extended abstract,
  pilot n=9 — direction, not decimals); the honest null: **no rigorous token-specific causal
  study exists** (July 2026); design-token vs LLM-token naming-collision warning.
- **Do-not-cite list**: Atlassian "67%"/"58→89", Primer "WCAG 71→96", "31–47% time saved",
  Spotify rebrand folklore — all third-hand/unpinnable; Netguru Silk (2–3 days, 2024) as the
  only pinned rebrand number, flagged vendor self-report.
- Six-step brownfield migration (inventory → characterize → consolidate → bridge → ratchet →
  generate) with exit conditions — our synthesis; Project Wallace usage-count illustration
  reframed as illustration (the "47 colors" example is a gloss, not a published stat).
- Spot-verify catches this round: DESIGN.md vendor list third-party; "5.2k stars at 72h"
  unsourced (1.6k at +2 days per the primary issue); D'Amato article undated + Salesforce
  "solid web standard" line de-quoted to paraphrase; Builder.io "governance loop" quote
  corrected to its real two-sentence wording; Braithwaite quote trimmed to fetched text.
- Topic D2 enriched: two "careful" flags in the know bullets, Resolver-draft + DESIGN.md
  concepts, a new dark-mode-via-DTCG check question.

## v1.46 · 2026-07-18

**NEW DEEP DIVE B6 — Roadmap F0–F3, metrics and STOP criteria.** Sixth M5 companion
(`deep-dives/B6-roadmap-f0-f3-deepdive.html` + in-workbook overlay) — **module M5 complete**.
Built on a three-teammate fact/discovery pass + an adversarial spot-verify round (12th session
in a row it caught real errors).

- The roadmap as a **permission ladder with measured gates** (Report 4 synthesis, honestly
  analogue-checked: no published canonical equivalent as of July 2026 — nearest cousins stage
  oversight per task, not access over time: Sharma's D³, GAIE).
- Gate table with deterministic checks, named sign-off and **automatic demotion** (borrowing
  GAIE's risk-routed tiers, arXiv:2606.22484, and the Digital Apprentice's dual-key promotion /
  asymmetric demotion, arXiv:2606.04321 — both flagged as preprints).
- Metrics: delivery health (DORA five, current names) vs bootstrap progress; the self-report
  trap (METR RCT) and the vendor-telemetry file (Faros 2026 "Acceleration Whiplash": review
  time +441.5%, +51.3% PR size, 31.3% more PRs merging without any review — flagged vendor).
- Secrets from day 0 on the 2026 evidence: GitGuardian — Claude Code-assisted commits at
  3.2% vs 1.5% baseline (~2×), MCP config files as a leak surface (24,008 secrets / 2,117
  valid), 70%-still-active persistence; toolbox table (gitleaks licensing split, TruffleHog
  verification, push protection) point-in-time.
- STOP criteria anchored to safety standards (ISO 26262 / IEC 62304 / DO-178C / IEC 61508
  bidirectional traceability, via compliance-vendor guidance, flagged) + EU AI Act Art. 12/19.
- Day-1 recipe table and the F0–F3 × R1/R2/R3/R6 **master-plan table** (our synthesis),
  answering the topic's open question.
- **Fact fixes from the swarm:** DORA's deployment rework rate re-dated to its true **2024**
  introduction (dora.dev metrics history) — fixed in E7, E8, H4 and B1, both copies; current
  DORA vocabulary "change fail rate" noted; MIT NANDA "95%" pinned to real wording and
  methodology (300+ initiatives / 52 org interviews / 153 senior leaders — the circulating
  "150 interviews / 350 employees" is a misquote); DX dataset corrected to 425 organizations;
  unverifiable sub-figures (DX daily/monthly split, GitGuardian "2.4× peak") excluded.
- New load-bearing sources: Microsoft instrumented rollout study (arXiv:2607.01418 — ~24%
  sustained PR-merge lift, peer-network diffusion, "visible peer use"), DX Q4 impact report
  (structured-enablement evidence, onboarding 91→49 days), DORA AI Capabilities Model (7
  capabilities), Swarmia five autonomy levels, KPMG stall mechanism, MIT NANDA handled with
  caveats.
- Topic `brown-roadmap` enriched: metrics/secrets know-bullets re-pinned, gates + diffusion
  bullet added, concepts extended, new self-check; src updated (GitGuardian 2026, Microsoft
  study, DORA metrics history).

## v1.45 · 2026-07-18

**NEW DEEP DIVE B5 — Strangler fig, the heatmap and picking the first battlefield.** Fifth
M5 companion (`deep-dives/B5-strangler-heatmap-deepdive.html` + in-workbook overlay), built
on an 8-agent fact-verification + discovery swarm.

The rewrite question honestly framed (Spolsky, Brooks, the Basecamp counterexample that is
really strangler economics in disguise, FreshBooks/BillSpring, FogBugz/Wasabi), the strangler
fig with its real origin story (Fowler 2004, Stevenson/XP-2004 credit, the retitle that
"strangled the old one"), the plumbing toolbox (seams, anti-corruption layer, branch by
abstraction, expand/contract, dark launching, feature flags), the churn × complexity heatmap
with caveats (Nagappan & Ball ICSE 2005 as the honest citation), a scored pilot-selection
model with the exclusionary criticality gate (our synthesis, flagged), Hyrum's Law, god
classes vs the agent's context budget, the database (dual-write/outbox/CDC, Stripe's
four-phase playbook), and what agents reprice in 2026 (Anthropic's COBOL post vs GitClear's
rot counterweight; fitness-function ratchet).

Key swarm corrections: branch-by-abstraction attribution pinned (Stacy Curl coined the name;
Paul Hammant first detailed the technique publicly, 2007; Fowler popularized it); Code Red
printed as issues taking **124% longer** to resolve in the worst code-health band, not the
marketing "faster" reframe; the hotspot-concentration folklore corrected ("4% of the code,
70%+ of defects" is a single-system anecdote — the defensible form is Pareto-shaped, ~20%
of modules carrying ~80% of defects); and no empirical rewrite failure rate exists (Standish
CHAOS figures dismantled by Eveleens & Verhoef 2010 — the case rests on case studies and
expert judgment, printed as such). Topic `brown-strangler` src now opens the overlay first.

## v1.44 · 2026-07-17

**NEW DEEP DIVE B4 — Agent Archaeology: reverse-engineering legacy.** Fourth M5 companion
(`deep-dives/B4-agent-archaeology-deepdive.html` + in-workbook overlay), built on an 8-agent
fact-verification + discovery swarm plus a 4-agent spot-verify round (11th session in a row
it paid).

Corrections the swarm surfaced: CodeConcise is graph-traversal-*augmented* RAG, not "instead
of RAG"; the 60,000 person-days headline and the 240 FTE-years figure are the same projection
in two units; the 3h-vs-3-weeks anecdote comes from a different client, "best cases"; the AWS
"~7B lines/year" figure was NOT FOUND → replaced with the verified 1.1B lines analyzed / 810k
hours saved, cumulative; Western Union is 2.5M lines, not 250k, and the six weeks run
discovery→testing (pilot); the "15–20k lines" module sizing was unpinnable → dropped; Siala &
Lano's AgileUML zero-spurious result holds for Java (0.14 on Python); the WCA for Z → IBM Bob
timeline pinned (GA Mar 2026).

Load-bearing new sources: Malykhin's *Archaeologist's Copilot* (martinfowler.com, Jul 16 2026,
verbatims spot-verified), the CROZ Nov 2025 review verbatims, Unum's AVP "if you cannot
understand it, you cannot verify", Soliman & Keim ICSA 2025 (0.395 architecture-answer
precision), Siala & Lano Frontiers 2025, arXiv:2504.04372 (78% brittle comprehension), Xia
TSE 2018 (~58%, 3,148 hours), Corbi IBM SJ 1989, the Glass 2001 attribution fix, Wen ICPC
2019, Uddin & Robillard 2015, Tan SOSP 2007, the Cursor support-bot incident (Apr 2025),
Spring REST Docs / Doc Detective / Schemathesis, AgenticAKM arXiv:2602.04445, and the
GitHub/Microsoft COBOL framework ($2–5 per 1k LOC). The hypothesis-with-confidence labels,
the sampling protocol, promote-through-verification and the F0 workflow are flagged as our
Report 4 synthesis. Topic `brown-archaeology` know/checks/src rewritten with the verified
figures.

## v1.43 · 2026-07-17

**UX — sidebar actions restyled as an action menu.** The **View** (expand/collapse all) and
**Data** (export/import data, my notes, sync across devices) controls were laid out as a
wrapping row of chips directly under the filter pills, so they read as more filters rather than
actions. They are now a **vertical menu of full-width rows**, each with a leading inline-SVG
icon (muted → cobalt on hover) and a hover highlight — echoing the Modules nav's clickable-row
pattern (`.mnav a`) but marked as actions by an icon rather than a code chip. The sidebar now
carries three distinct visual languages: nav rows (code chip), filter pills (toggle state),
action rows (icon).

The sidebar is also now **height-safe**: it caps at the viewport and scrolls internally
(`max-height:calc(100vh - 100px); overflow-y:auto`), so the Data actions are never clipped on
short viewports or as more modules are added — a pre-existing sticky-sidebar flaw that the
taller vertical menu exposed. On mobile (`≤900px`) the sidebar reverts to a static horizontal
wrap with no cap. Changes are confined to the `.side`, `.bulk`, and `.bulk button` rules plus
the six action-button icons; the **Filter by status** pills are unchanged; no topic-id or
content changes.

## v1.42 · 2026-07-17

**NEW DEEP DIVE B3 — Mutation Testing as the Test-Quality Gate.** Third M5 companion
(`deep-dives/B3-mutation-testing-gate-deepdive.html` + in-workbook overlay), built on the
three-teammate fact pass + spot-verify round (10th session in a row it paid).

Spot-verify catches: the SpecBench quote re-pinned verbatim ("Oversight **therefore** collapses
onto a single surface: the automated test suite."), with the 28 pp/tenfold-LOC figure flagged as
the abstract headline over a ~27 pp 90th-percentile fit (R²=0.21); the Augment-blog JFreeChart
"256K mutants / 109 minutes" figure identified as third-hand (unnamed cost survey) and excluded;
the ISSTA 2019 flakiness numbers pulled verbatim from the PDF.

Theory grounded with verbatims: DeMillo/Lipton/Sayward 1978 (competent programmer + coupling
stated as observations; Hamlet 1977 as the parallel origin); Just et al. FSE 2014 (coupling for
**73% of real faults**, 17% not coupled; mutant detection correlates with real-fault detection
"independently of code coverage"; Defects4J credited to the ISSTA 2014 companion paper);
Inozemtseva & Holmes ICSE 2014 (coverage "should not be used as a *quality target*" — their
word, not "stopping criterion").

LLM-era evidence made precise: MUTGEN pinned to its real title ("Mutation-Guided Unit Test
Generation with a Large Language Model", accepted IEEE TSE; the 53% plateau is one
HumanEval-Java subject; 89.5%/89.1% are corpus scores across 1,144/1,900 mutants); Haroon et al.
clarified (23,977 = the failing subset of 119,163 SAC-generated tests; preprint-flagged);
TestGenEval GPT-4o 35.2%/18.8% verbatim; Yoshimoto arXiv:2603.13724 (AI authored 16.4% of
test-adding commits, coverage comparable to human tests — the premise, not the payoff);
Rethinking arXiv:2602.07900 (test volume ≠ outcomes).

New reward-hacking section: ImpossibleBench 54.0% Conflicting-SWEbench vs 76% Oneoff-SWEbench
disambiguated; SpecBench arXiv:2605.21384; Rajan arXiv:2606.16062 (28.5% of a 49-task SWE-bench
Verified sample accept a Docker-verified incorrect patch; Pass@1 +14.14 pp higher on hackable
tasks, 123/134 models positive).

Feedback-loop evidence: MuTAP (IST 171, 2024 — up to 28% more faulty snippets detected, 17%
caught only by it, 93.57% mutation score); ACH reused from B2; YATE +21.77% mutants; AdverTest
arXiv:2602.08146 (adversarial co-evolution verbatims; Defects4J +8.56% over best LLM baselines,
+63.30% over EvoSuite); LLMorpheus arXiv:2404.09952 (LLM-generated mutants beyond operators).

Industry: the Google trilogy with verbatims (one mutant per line; changed/covered/non-arid lines
only; findings in Critique via Tricorder; usefulness 20%→80%; >24,000 developers / 1,000+
projects; ~15M mutants; "developers using mutation testing write more tests") and the fact-check
correction that Google's no-score stance is a *practical* dismissal ("infeasably expensive…
no good way to surface it"), not a normative one — distilled into the consumption-mode lesson:
survivors-in-review at scale vs module score at the bootstrap boundary.

The three taxes with the classic numbers: Schuler & Zeller STVR 2013 (~45% of undetected
mutants equivalent; ~15 min/mutant manual triage); TCE ICSE 2015 (7.4% equivalent + 21%
duplicated for C; 5.7%/5.4% Java); pseudo-tested methods (concept coined by Niedermayr et al.
2016; EMSE 2019 study found them in all 21 projects; a single headline % is UNPINNABLE — not
cited); ISSTA 2019 (mutation scores vary 4 pp between repeated runs; 9% of mutant-test pairs
non-deterministic).

Cost ladder + toolbox point-in-time: PIT incremental analysis, Arcmutate PR-scoped git
integration, Descartes extreme mutation, StrykerJS `--incremental` (since v6.2), gremlins over
stale go-mutesting; Stryker report thresholds `high: 80, low: 60, break: null` and PIT
`mutationThreshold` default 0 — **no mainstream tool ships a mandatory score gate**, so the
~70% bar is presented as Report 4's working heuristic, not an industry standard.

The two-mode gate (diff-scoped advisory survivors + module-level held-out-mutants score as the
F1→F2 exit criterion) flagged as **our synthesis**, with the practice-sheet-vs-exam principle
and six anti-patterns. Topic B3 `know`/`concepts`/`checks` enriched (Google-scale bullet,
flakiness bullet, held-out-mutants check).

## v1.41 · 2026-07-17

**NEW DEEP DIVE B2 — Characterization & Golden-Master Testing with Agents.** Second M5
companion (`deep-dives/B2-characterization-golden-master-deepdive.html` + in-workbook overlay),
built on the three-teammate fact pass + spot-verify round (9th session in a row it paid).

The two pinning techniques stated precisely: **Feathers characterization** (WELC 2004 ch. 13;
verbatim "The purpose of characterization testing is to document your system's actual behavior,
not check for the behavior you wish your system had" and "When a system goes into production,
in a way, it becomes its own specification") and **Falco/Bache approval testing** — approval /
golden master / snapshot / characterization mapped as one mechanism with four emphases (Bache's
2021 anatomy quoted; Rainsberger = *popularizer* of golden master, never "coiner"; Hyrum's Law
verbatim + Excel-1900 (Microsoft primary) and Java-8-HashMap (picard #139) as load-bearing-bug
exhibits — the pairing flagged as our synthesis).

Production evidence with contexts kept honest: TestGen-LLM (75/57/25 = Reels/Stories eval;
11.5% / 73% = Instagram+Facebook test-a-thons; "Assured LLM-SE" = separate paper
arXiv:2402.04380), **ACH pinned to arXiv:2501.12862** (FSE 2025; 10,795 Kotlin classes → 9,095
mutants → 571 privacy-hardening tests, 73% accepted, 36% privacy-relevant; equivalent-mutant
detector 0.79/0.47 → 0.95/0.96 with pre-processing; deployed Messenger/WhatsApp — NOT
Instagram), Qodo Cover (first OSS implementation; huggingface/pytorch-image-models **PR #2331**,
15 tests / 168 lines; Itamar Friedman quote with its full "…who run fully automated workflows"
clause), UnitTenX, **YATE** (arXiv:2507.18316 — test *repair* beats regeneration: +32.06%
lines / +21.77% mutants killed).

Five traps, each with measured evidence: coverage vanity (MutGen 100%/4%; **TestGenEval**
arXiv:2410.00752 — GPT-4o 35.2% coverage vs **18.8% mutation score**, the only test-gen
benchmark grading mutation), oracle-passing-by-construction (arXiv:2412.14137, read both
directions: fatal for bug-finding, definitional for characterization), **bug-as-spec measured**
(arXiv:2607.05139 — fault detection ~25% → ~14% when the model sees the faulty implementation,
five models, three benchmarks), flaky pins (ICSE SEIP 2026 DBMS study — 0.07% baseline vs
0.29–0.71% generated, 63% unordered collections, "developers should prioritize fixing flaky
tests before applying LLM-based generation approaches" verbatim), and the agent gaming its net
(Beck's genie "disabling or deleting tests" verbatim from *Augmented Coding: Beyond the Vibes*;
ImpossibleBench; ThoughtWorks Radar Vol. 34 "erode approve/deny chokepoints" verbatim) — plus
Sapegin's approve-all-fatigue line ("developers just update snapshots without looking at them
at all") as the human-scale substrate.

The six-step workflow (document-don't-fix → deterministic filter → ~20%+all-suspected sampling
→ two-door SUSPECTED-BUG triage → ~70% mutation gate → read-only commit) **flagged as our
Report 4 synthesis**. Toolbox table point-in-time (ApprovalTests; Verify's Aug-2026 licensing
change; Jest/Vitest; Texttest; VCR-style cassettes; Percy AI diff-reviewer as vendor claim) +
a four-row deterministic exit-criteria table with the keep-or-discard decision recorded per
module.

**Fact fixes elsewhere:** the Report 4 notes' "there are no wrong answers — just documenting
the way things exist" line was **Erik Dietrich's gloss misattributed to Feathers** — corrected
with Feathers' real verbatim lines. Topic B2 `know`/`concepts`/`src`/`checks` enriched
(bug-as-spec + flakiness bullet, ACH src link, read-only-tests check).

## v1.40 · 2026-07-17

**NEW — cross-device sync (opt-in, local-first).** Progress and notes were saved only per
browser; readers can now sync them across devices with no account. From the sidebar
**Data → sync across devices**, "Enable sync" uploads the current state and returns a random
**4-character code**; every change from then on syncs automatically. Entering the code on another
device pulls and merges that state in, linking it too.

Merge is handled by **Yjs**, a CRDT, on both the browser and a small Cloudflare Worker — chosen
over Automerge/Loro because it is pure-JS (18 kB, no WASM) and runs in both places, so there is
**no hand-rolled merge logic**. The synced "schema" is a `Y.Doc` (progress/notes maps, a
grow-only `seen` set, a highlights-by-id map). Local storage stays canonical and
Yjs-independent: the engine loads from a CDN and is best-effort, so if it is blocked (claude.ai
CSP) or offline, saving works exactly as before. The save indicator gains a `synced · CODE` /
`sync error` chip.

Backend: `sync-worker/` — a Hono + KV Worker (deployed to `agentic-study-sync.selmeci.workers.dev`)
that stores the encoded Y.Doc per code and merges pushes server-side with `Y.applyUpdate`,
rate-limited via Cloudflare's native Rate Limiting binding. Worker bindings are generated from
`wrangler types`. No topic-id or content changes; the local JSON store (`agentic-study-v1`) is
untouched. *(v1.39 is reserved for the parallel B1 deep-dive branch, so this ships as v1.40.)*

## v1.39 · 2026-07-17

**NEW DEEP DIVE B1 — The Bootstrap Paradox & Safe Ordering. M5 OPENED.**
First M5 companion (`deep-dives/B1-bootstrap-paradox-deepdive.html` + `#b1-deepdive` overlay),
built on the standard three-teammate fact pass (b1jul17-facts-dora / b1jul17-facts-legacy /
b1jul17-scout) + spot-verify round (b1jul17-spotverify). The chapter states the paradox as three
separately-true claims (agent needs a verification loop — E4; legacy = "simply code without
tests" — Feathers 2004 Preface; the agent is the cheapest tool to build the missing
prerequisites) and shows how, unanchored, it closes into the bug-as-spec loop; the evidence file
with honest weights (DORA 2024 −1.5%/−7.2% associated with +25% adoption, DORA's OWN mechanism
quoted — "small batch sizes and robust testing mechanisms" — and the 2025 sign flip flagged:
throughput positive, instability persists, "AI's primary role is as an amplifier" + the
seven-capability AI Capabilities Model; METR RCT 16/246/19%-slower-vs-24%-expected/20%-believed
on 22k+-star/1M+-LOC repos; GitClear vendor-flagged copy/paste 8.3%→12.3% + moved ~24%→9.5% +
churn 5.5%→7.9%, "8×"/"4×" headlines pinned to their dated reports; Stack Overflow 2025 45.7%
distrust / 66% "almost right, but not quite"); the benchmark greenfield-bias corollary
(SWE-bench keeps only fail-to-pass instances, 2,294 of ~90k PRs; Epoch AI teardown: ~90% under
an hour, Django ≈ half, top-5 >80%; SWE-EVO 72.80% → 25% on evolution tasks); the five-step
dependency chain flagged as our Report 4 synthesis, mapped onto Böckeler's guides/sensors
vocabulary, with the ETH −2%/+23% numbers anchoring "AGENTS.md extracted, not decreed"; Phase 0
read-only as the paradox-breaker (Xia TSE 2018 58% comprehension share; Ehsani MSR 2026 on
AIDev-pop: docs/CI/build tasks merge best, 38% Abandoned/Not Reviewed; the 2024 Böckeler "pipe
dream" → 2025 UnitTenX arc, 0%→100% on the djbdns case study); four wrong-order failure modes
(WO1–WO4); per-step exit-criteria table.

**Spot-verify (8th session in a row it paid):** a fabricated Böckeler mutation-testing quote
killed (real line: acceptance tests "give us a false sense of security in test effectiveness —
mutation testing helps us monitor that gap"); UnitTenX "characterization tests" is NOT the
paper's term (says "resolve bugs and document unknown interfaces"), 0%→100% scoped to djbdns
(202 functions); Stack Overflow 66%-vs-45.2% attribution settled.

**Fact fixes elsewhere:** TestGen-LLM "useful:generated 1:4 controlled vs 1:20 real-world" is
UNPINNABLE (not in arXiv:2402.09171) — dropped from topic B2's know and flagged in the Report 4
research notes; topic B1's "DORA mechanism" know bullet reframed to DORA's own
batch-size/testing-discipline hypothesis + the 2025 reversal; MutGen 89.5% pinned to
HumanEval-Java (89.1% LeetCode-Java) in topic B3's know. Topic B1 know/concepts/src/checks
enriched (greenfield-bias bullet, METR self-report check, METR src link).

## v1.38 · 2026-07-16

**NEW DEEP DIVE I7 — Linking Product ↔ Engineering: IDs, Maps & the MCP Bridge. M4 COMPLETE.**
Seventh and final M4 companion (`deep-dives/I7-linking-product-engineering-deepdive.html` +
`#i7-deepdive` overlay), built on the standard three-teammate fact pass (i7jul16-facts-links /
i7jul16-facts-mcp / i7jul16-scout) + the i7jul16-spotverify round. Content spine: the two planes
joined by one boring foreign key — the unified ID scheme with per-platform mechanics (Linear
auto-links from branch names; Jira smart commits need key + command in the commit message;
GitHub auto-close is same-repo only; GitLab push-rule regex) and an enforcement ladder from
CLAUDE.md convention through `prepare-commit-msg`/`commit-msg` to server-side rulesets + CI grep
(E5); the missing-links evidence (Bird et al. ESEC/FSE 2009 — 8–55% of fixed bugs linked per
project and the severity inversion, 63% of minor vs 15% of blocker bugs linked in Apache;
LinearB verbatim "In 75% of teams, 31% of branches are unlinked"); the ticket-as-prompt pattern
(Copilot↔Jira preview Mar 5 → GA Jun 25 2026, Devin↔Linear playbook labels, Cursor↔Linear —
all vendor-flagged) with its independent counterweight (Wang/Pradel/Liu arXiv:2503.15223,
ICSE 2026: 29.6% of plausible SWE-bench patches diverge; 66.2% of suspicious ones trace to
under-specified issue statements); the system map (C4 verbatims incl. the generate-not-draw
L4 rule, arc42 12 sections CC BY-SA, matklad ARCHITECTURE.md, ThoughtWorks ADR-in-source-control
verbatim); one master per artifact + "reference, don't copy" with the master table (our
synthesis, flagged); the MCP bridge priced (Anthropic 150k→2k / "98.7%" vendor verbatim;
MCP-Universe distractor-server evidence replacing the unpinnable "2–3+ servers" claim) and
threat-modeled (Willison lethal-trifecta verbatims + three incidents: Invariant Labs GitHub MCP
toxic flows May 2025, General Analysis / Supabase MCP Jul 2025, Noma Security GitLost Jul 2026);
provenance (multi-method census 850,157/3.3%/30×, Agent Trace v0.1.0 RFC Jan 2026 Cursor-led,
Copilot commit→session-log links Mar 2026 + SIEM/Purview streaming preview Jul 2026, the VS Code
co-author-trailer revert per The Register May 2026); llms.txt honestly labeled (Mueller "FWIW no
AI system currently uses llms.txt", Ahrefs 97%). Spot-verify (7th session in a row it paid):
GitLost "VP of Sales" detail + Agentic-Workflows preview date dropped as uncorroborated; LinearB
stat re-pinned to its verbatim (was "a third of git work"); Bird "every project" softened to the
manually-verified projects; Wang inflation figure is 6.4 pts not 6.2 (not used); "Jira has its
own version of reality" NOT FOUND — excluded. **Fact fix elsewhere:** H3's "AIDev census" naming
corrected in both copies — arXiv:2606.24429 is the *multi-method census* (Khosravani & Mockus);
AIDev (arXiv:2602.09185) is the separate PR census it compares against; the 30× base tightened
to 850,157 one-snapshot commits (886,122 = cross-project total, now labeled). Topic I7
know/concepts/src/checks rewritten with verified figures; CONTENT-MAP companion count fixed
(27→29; the I6 session had missed it).

## v1.37 · 2026-07-16

**NEW DEEP DIVE I6 — Retrieval: Agentic Search, Embedding Indexes & Knowledge Graphs.** Sixth M4
companion (`deep-dives/I6-retrieval-deepdive.html` + `#i6-deepdive` overlay), built on the standard
three-teammate fact pass (i6jul16-facts-vendors / i6jul16-facts-research / i6jul16-scout) + the
i6jul16-spotverify round. Content spine: four retrieval lanes (agentic search / embedding index /
symbol-and-structure index / code knowledge graph); the vendor board with primary quotes — Boris
Cherny on HN (Feb 2025, "agentic search out-performed RAG for the kinds of things people use Code
for") and his restated reasons (simpler; security, privacy, staleness, reliability — "precision"
dropped as never-stated), Codex's quiet ripgrep default (no anti-RAG manifesto), Cursor's hybrid
(+12.5% avg QA accuracy, 6.5–23.5% by model, internal Cursor Context Bench, custom embedder trained
on agent traces; Merkle-tree sync + content-proof design from the Jan 2026 post), Sourcegraph Cody's
Feb-2024 embeddings retreat (verbatim + three reasons; consumer sunset Jul 2025 kept distinct from
the architectural retreat), Devin as the index-building counterexample (DeepWiki), Windsurf Riptide
("3x the recall", migrated Codeium post), Augment's embeddings-at-scale case (20+ bytes / 20+ ns per
LOC, 8x quantization, sub-200ms — all vendor). Independent evidence: SWE-bench BM25 1.96% vs oracle
4.80% (Claude 2; GPT-4 oracle 1.74% on 25% subset) read as "iteration, not better one-shot retrieval,
was the fix"; Agentless 32.00% Lite / $0.70 hierarchical LLM localization; CodeRAG-Bench verbatims
(NAACL 2025 Findings); the folklore correction — dense code-trained embedders frequently surpass BM25
on code (CoIR pin), so grep's case is freshness/simplicity/privacy/iteration, not retrieval quality;
Codebase-Memory arXiv:2603.27277 (83% vs 92% answer quality at ten times fewer tokens, 2.1× fewer
tool calls, 31 repos — preprint-flagged). Index tax: staleness as I3 drift (Merkle mechanics, 3.2MB
hash bookkeeping), security as embedding inversion (Vec2Text 92% exact recovery + no-query-access
follow-ons — vector store = recoverable source, M7), cost as Guo's build/maintain/per-query curve
with Blackbird's corpus-scale ground truth (15.5B docs, 25TB lexical index, "2,048 CPU cores for 96
seconds" for brute grep) and the Milvus 40%-tokens claim quoted as the named vendor rebuttal.
GraphRAG anti-miscitation callout (document summarization, LLM-judged wins — not code); code-KG shelf
(CodexGraph/RepoGraph/CGM) flagged self-reported; "no public evidence of a KG retrieval backbone in
production agents mid-2026". The L0–L3 escalation ladder + trigger table + twenty-query bench =
**our synthesis, flagged like D1–D5**. Two new SVGs (marker `ahI6a`, edge `edI6`). **Seed-topic
corrections:** the workbook's "Devin: same pattern" know-bullet was WRONG (Devin indexes) — fixed;
"+12.5% from combining semantic + grep" re-attached to semantic search's lift; Claude Code reasons
corrected to the actually-stated list. **Spot-verify kills (6th session in a row it paid):** the
"second Anthropic engineer: outperformed by a lot / surprising" quote NOT FOUND (never existed in
HN 43164253 — the long quote is Cherny's tweet, the HN quote is shorter and different); Riptide
"200% improvement in retrieval recall" is a secondary paraphrase (verbatim: "3x the recall");
Codebase-Memory latency and raw token/call counts not in the abstract (dropped); Cursor "plaintext
never persisted server-side" not found on fetchable pages (re-verify before enterprise adoption).
Topic `ia-retrieval` know/concepts/src/checks enriched (5 bullets, 9 concepts, 6 src incl. HN thread
+ CodeRAG-Bench, 3 checks incl. the E7-grade vendor-deck response and the GraphRAG category error).

## v1.36 · 2026-07-16

**Highlight notes: write at save, read on hover, edit on click.** Building on the v1.35 fix and
per-topic list, you can now attach a note to a highlighted passage directly at the mark. After
clicking **"+ save as note"**, a small popover (`#hlNote`) opens with a text field so you write the
note immediately (or **skip**). Hovering any highlight shows its note in a tooltip (`#hlTip`);
empty notes show a subtle *"click to add a note"* hint. Clicking a highlight reopens the popover
pre-filled to edit — disambiguated from drag-selecting a new highlight by requiring a collapsed
selection. Marks now use a `pointer` cursor to signal interactivity.

The note is the same `thought` field surfaced in the per-topic "My highlights" list and the global
"my notes" modal — one source, three views, kept in sync via `renderTopicHls()` / `renderNotes()`
on save. Close semantics: **save** or click-outside persists; **skip** / Escape discards (the
highlight itself is already saved); Cmd/Ctrl+Enter also saves. The popover (`z-index:252`) and
tooltip (`z-index:253`) sit above the deep-dive overlay (200), consistent with the v1.35 z-index
fix. Verified in Chrome (popover on top, tooltip shows note + hint, click-to-edit prefills,
persistence across reload) via hit-testing and screenshots. Workbook-render-only; the
`state.highlights` schema, export/import, and standalone deep dives are unchanged.

## v1.35 · 2026-07-16

**Highlight-notes: fixed the invisible save button, and added a per-topic highlights list.**

**Fix (root-caused via systematic debugging + visual confirmation).** Selecting text inside a
deep-dive overlay never showed the floating **"+ save as note"** button, so no highlight could be
created — the v1.29 feature was effectively unusable. Root cause was a z-index layering bug: `#hlSave`
(z-index 70) and `#hlToast` (z-index 71) are appended to `document.body`, but the deep-dive overlay
`.e1ov` is `position:fixed; inset:0; z-index:200` covering the whole viewport. Because the button only
ever appears for selections *inside* an overlay, it always rendered **behind** it — present in the DOM
and `display:block`, but visually occluded. This is why a DOM inspection would mislead: `elementFromPoint`
at the button's centre returned the overlay's content (`DIV.body`), not the button. Fixed by raising both
above the overlay: `#hlSave` → 250, `#hlToast` → 251. Verified in Chrome (button visible, save persists,
passage tinted, toast shown, all confirmed by hit-testing and screenshots).

**Feature — per-topic "My highlights" list.** Each topic card now shows a **"My highlights (N)"**
section (between "Go deeper" and "My notes") listing the passages you highlighted in that topic's deep
dive: a 2-line quote preview, your note (read-only), and an **"open at passage →"** button that opens
the overlay scrolled to and flashing the source passage. The topic→deep-dive mapping comes from the
topic's own `#<tok>-deepdive` src anchor; the list reuses the existing document-level `[data-hopen]`
handler for the jump. Creating, editing, and deleting highlights stay in the overlay + global "my notes"
modal (unchanged); the per-topic list is a contextual **view + jump** index kept in sync by a new
`renderTopicHls()` hooked into save / delete / import / thought-edit / load. Sections with no highlights
stay hidden. Workbook-render-only: `state.highlights` schema, export/import, and the standalone
deep-dive files are all unchanged; no frozen progress keys move.

## v1.34 · 2026-07-16

**UX — deep-dive links now render as a distinct "Open panel" button, not a citation.** In every
topic's "Go deeper" section, the in-page deep-dive link was visually indistinguishable from
external references: it shared the same `↗` "leaving-the-page" bullet, and the anchor even carried
`target="_blank" rel="noopener"` — neutralised only by the JS overlay interceptor calling
`preventDefault()`. The DOM effectively said "external navigation" for a link that opens content
in place. Deep dives now render as a bordered button-card (panel-with-lines icon, bold title,
description, "Open panel →" affordance) placed above a separate "References" list; the `↗` glyph
is now reserved for genuinely external citations. Added `aria-haspopup="dialog"` so the affordance
is announced as opening a dialog, and dropped the misleading `target="_blank"` on in-page links.

Purely presentational and workbook-render-only (one render block + CSS): the 26 `src` arrays are
untouched (title/description parsed at render from the uniform `↳ <CODE> Deep Dive — open here
(<desc>)` string, with a raw-text fallback), the `#*-deepdive` anchor wiring and JS handlers are
unchanged — so no frozen progress keys move and no two-copies (standalone-vs-overlay) sync is
triggered. Design: `docs/superpowers/specs/2026-07-16-deepdive-link-presentation-design.md`.

## v1.33 · 2026-07-16

**NEW TOPIC E11 + deep dive — Formal Methods in the Agentic Loop: Vericoding & Runtime
Enforcement** (`eng-formal`; 54→55 topics; M1 now E1–E11, completing the three-topic July
source-evaluation round). Companion `deep-dives/E11-formal-methods-deepdive.html` + overlay
`#e11-deepdive`. The chapter's spine is an anti-conflation rule — "formal verification of
agents" means two practices: Direction A, formal methods on the agent's OUTPUT (vericoding:
arXiv:2509.22908, 12,504 specs, 82% Dafny / 44% Verus / 27% Lean, "vericoding vs vibe coding"
verbatim; Misu et al. FSE 2024, 58% verified Dafny, UC Irvine — NOT Microsoft, prompt-based
NOT a repair loop; AWS Cedar/Lean verification-guided development as the production
proof-point) versus Direction B, formal methods on the agent's BEHAVIOUR (AgentSpec, ICSE
2026 — the chapter's only peer-reviewed system: >90% unsafe-execution prevention, but
LLM-auto-generated rules only 70.96% recall; ProbGuard — formerly Pro2Guard, never
"ProGuard" — with the quantified safety–utility curve: 40.63%→2.60% unsafe at
59.38%→10.42% completion; VeriGuard and Agent Behavioral Contracts as the 2025–26 wave;
NeMo Guardrails/Llama Guard as the deployed learned-filter baseline). Economics thread:
Newcombe CACM 2015 (cost-perception quote, 35-step DynamoDB bug, "debugging designs") →
antfly May 2026 (practitioner/vendor blog — Antfly sells agent retrieval, not verification;
its Pebble validation stated precisely: the workflow found a DIFFERENT bug independently
fixed later, not a rediscovery; one anchor, zero metrics) → Vogels × Byron Cook Feb 2026
(neuro-symbolic, Bedrock Automated Reasoning checks). Counterweight load-bearing:
NL-to-TLA+ = 26.6% syntactic / 8.6% semantic correctness across 30 LLMs (arXiv:2606.05792,
"not without expert oversight") — resolved against the 82%-Dafny number as
oracle-in-the-loop vs oracle-free formalization; the human owns intent (Lahiri's intent
gap, arXiv:2603.17150, extending H2's formalization ladder). Ferrando FMAS 2025 grounds
why Direction B is runtime-only; the Dec 2024 roadmap's "remains elusive" verdict kept.

## v1.32 · 2026-07-16

**NEW TOPIC E10 + deep dive — Background & Long-Running Agents: Async Delegation**
(`eng-background`; 53→54 topics). Companion `deep-dives/E10-background-agents-deepdive.html`
+ overlay `#e10-deepdive`. Second topic from the July source-evaluation round. Sections: the
execution axis E6 does not cover — where the agent runs, when, who initiates — with the
cross-vendor convergence on sandbox→work→PR cited from launch primaries (Codex cloud May 2025,
Cursor background agents GA Jun 2025, Jules, Copilot coding agent, Ona); the evidence run both
ways (METR TH1.1: doubling ~4.3 months since 2023, Claude Opus 4.6 ~12 h p50 — pinned from
METR's raw benchmark_results_1_1.yaml, correcting the 14.5 h figure circulating in drafts;
versus LHTB arXiv:2607.08964: best frontier model 15.2% pass@1 at 0.95 threshold on 46
sustained terminal tasks, mean 4.3%); persistence mechanics (Ralph loop primary-sourced to
ghuntley.com Jul 14 2025 with the verbatim one-liner; Anthropic initializer/coding-agent split;
Managed Agents session-as-append-only-log + wake(sessionId)/getSession(id) verbatim, TTFT
numbers vendor-tiered; the "unacceptable to remove or edit tests" rule kept I2-precise — it
guards feature-list entries; "test ratchet" attributed as Osmani's term); verification at a
distance (evaluator ≠ generator; Cursor planner/worker/judge + "Opus stopped early" flagged
secondhand-via-Osmani; approval fatigue 93% / 20%→40% / 17% FN verbatim); governance (Ona's
"guardrail inside the context window is a suggestion, not a boundary" as the infra-layer
thesis; cost as a governance surface with token-velocity circuit breakers — pattern
practitioner-tier, viral runaway-bill dollar figures excluded as folklore); adoption path
(false summit → background agents → software factory; six summit case studies tabled with a
hard ALL-vendor-self-reported flag; Ona = ex-Gitpod rebrand Sep 2025, OpenAI acquisition
agreed Jun 11 2026 per openai.com/CNBC/Bloomberg; DORA 2025's ~90% explicitly NOT stretched
to an async-delegation adoption stat — none exists). Osmani's long-horizon-reasoning /
long-running-execution / persistent-agency taxonomy adopted as the chapter's spine.

## v1.31 · 2026-07-16

**NEW TOPIC E9 + deep dive — Harness Engineering as a Discipline: Eval-Driven Tuning**
(`eng-harness-tuning`, first new M1 topic since the workbook's creation; 52→53 topics).
Companion `deep-dives/E9-harness-tuning-deepdive.html` + in-page overlay `#e9-deepdive`.
From the July source-evaluation round (the boss reading list), verified by a deep-research
workflow (3-vote adversarial verification per claim) + four reader teammates + an E9-specific
fact/discovery pass. Sections: the tunable surface (Claude Code single while-loop,
arXiv:2604.14228, vs OpenDev compound ensemble, arXiv:2603.05344; the six runtime
responsibilities, arXiv:2606.20683; apiad's Mode/Skill/Command/Subagent vocabulary); the
evidence that the harness moves scores (arXiv:2605.23950 — harness-induced variance 7.80×
model-induced in a controlled factorial, 34–48-pt scaffold swings on SWE-bench Verified Mini,
the "disclose the harness" rule; Nemotron 3 Ultra 65–70.4% across five harnesses; Artificial
Analysis customizing Terminus-2 turn-budget disclosure); the discipline (Hashimoto's rule,
mitchellh.com Feb 2026 verbatim; Osmani's Ratchet as a provenance rule; "success is silent,
failures are verbose"; HumanLayer's context-firewall subagents + anti-persona stance, flagged
as one vendor's doctrine); the eval-driven tuning loop (LangChain playbook: traces →
behaviour class → one change → cost ladder → keep-if-repeats; guidance placement; the
94→96/127 middleware ablation; the flat-category = model-limit diagnostic — all vendor-tiered,
with Braintrust EDD and Anthropic's generator/evaluator harness post as independent
practitioners of the method); co-evolution (the named "Harness Robustness" post-training
stage; HaaS/SDK trend; vendor-strategy implications, T6). Key disentanglement: the
Terminal-Bench meme is TWO results — Opus 4.6 #33→#5 (HumanLayer) and deepagents-cli
52.8→66.5 with gpt-5.2-codex fixed (Trivedy/LangChain, retold by Osmani) — both self-reported,
point-in-time. Refuted claims excluded: "first-of-their-kind" harness profiles; the "1.6% AI
decision logic" figure. Attribution fixes applied: "context engineering" popularized by
Karpathy (Jun 2025), not solely Horthy; harness engineering "attributed to" Trivedy, not
"coined" as fact. **Also: I5 fact refresh** against arXiv:2602.11988 v2 — the ETH benchmark
is CTXBENCH (was misnamed AGENTbench) and developer-provided files bought +2.4% short of
significance (was +4%); HumanLayer's "14-22% more reasoning tokens" gloss is NOT in the paper
(cost is measured in USD/steps). Fixed in both copies; METR note for the record: TH1.1 raw
data (May 2026 update) puts Opus 4.6 at ~12.0 h p50, doubling ~129 days from 2023.

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
