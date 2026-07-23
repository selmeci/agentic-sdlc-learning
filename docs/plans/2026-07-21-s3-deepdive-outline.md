# S3 deep dive — outline & seed facts (pre-swarm)

**Topic:** `sec-advisory` — "Advisory vs deterministic controls; the rules-file backdoor"
**Deliverables:** `deep-dives/S3-…-deepdive.html` standalone + workbook overlay (`#s3-deepdive`, `s3ov`), per `docs/AUTHORING-GUIDE.md`. Next version: v1.62.
**Workflow (per NOTES.md precedent):** outline → swarm (fact-verify + discovery) → spot-verify discovery finds → write body → assemble → validate → gallery.

## Draft section structure

- **§0 Why it matters** — the organizing principle of M7: every control is either advisory (model-interpreted) or deterministic (harness-executed). Only the deterministic layer is a security boundary. Same split as E1/E5 (engineering) and D5 (design), now the security lens.
- **§1 The advisory layer, mechanically** — what rules files are (CLAUDE.md, AGENTS.md, .cursor/rules, copilot-instructions.md, .windsurf/rules …): auto-loaded into context each session, interpreted by the model. Valuable for steering, but (a) injection can override them, (b) they compete with untrusted content in context (E2), (c) they are writable files — an attack surface themselves.
- **§2 The Rules File Backdoor** — Pillar Security (Mar 2025), MITRE ATLAS AML.CS0041: hidden Unicode (zero-width joiners/spaces, bidi override markers, Tag codepoints) in `.cursor/rules` / `copilot-instructions.md`; "virtually invisible to developers"; affects GitHub Copilot & Cursor; survives forking/templates → supply-chain propagation.
- **§3 Evidence that advisory fails** — models disobey system-prompt/rules under injection and pressure: AgentDojo / injection benchmarks; the V4 caption's ">90% bypass in adaptive tests" claim (needs pinning); reward-hacking evidence (frontier agents rewrite tests against explicit instructions — I2's "roughly half of trials").
- **§4 The deterministic stack** — permissions & deny-lists, PreToolUse hooks, OS sandbox, network egress allowlist, managed settings, CI gates — executed by the harness regardless of model output. The E5 litmus: "what must never happen" → hook/permission; "what the model should know" → prompt.
- **§5 Rules files as governed artifacts** — since rules steer agents, treat them like code: PR review, CI scanning for invisible Unicode, provenance controls, no auto-loading of session-written rules (the topic's open question), AGENTS.md stewardship, detection tooling.
- **§6 The cross-framework pattern** — same advisory→deterministic move in E5, I2 (write-permissions), H2/H3 (EARS linting, REQ-id greps), D5 (design gates). Flag as framework synthesis.
- **§7 Takeaways + further reading**

## Candidate diagrams (SVG)

1. **The two-layer stack / strength ladder** — advisory (rules files, system prompt, "please don't") vs deterministic (permissions, hooks, sandbox, egress, CI) — what holds under injection. (V4 bottom band already sketches this; S3 needs the focused version.)
2. **Rules File Backdoor attack flow** — attacker template/PR → rules file with invisible Unicode → agent auto-loads into context → hidden directive executes (exfil / weakened code) → propagates via fork.
3. **The litmus decision flow** — "must never happen?" → deterministic mechanism; "should the model know?" → advisory text. Maybe fold into §4 prose instead.

## Seed facts to verify (swarm)

**Cluster A — Rules File Backdoor (primary: Pillar Security blog, Mar 2025):**
- Date, affected tools (GitHub Copilot, Cursor), exact techniques named (zero-width joiners? bidi markers? Unicode Tag codepoints U+E0000–E007F?)
- Exact "virtually invisible" quote wording
- Supply-chain claim (survives forking, spreads via templates/rules-sharing)
- What the hidden directives did in their PoC (exfil? weaken generated code?)
- Disclosure/mitigation response from vendors
- MITRE ATLAS AML.CS0041 — exact technique name & description

**Cluster B — advisory-fails evidence:**
- The V4 caption claim ">90% bypass in adaptive tests" — pin to a source or soften
- AgentDojo / prompt-injection benchmark numbers on instruction override
- Reward-hacking: agents rewriting tests despite explicit CLAUDE.md prohibition (I2 deep dive cites "roughly half of trials" — which paper?)
- Any peer-reviewed work on models deprioritizing system instructions under conflicting injected content

**Cluster C — deterministic-layer facts (vendor docs, point-in-time):**
- Claude Code: hooks override permission rules (S8 claim); PreToolUse deny mechanics; managed settings precedence (enterprise → user → project → local)
- sandbox.credentials blocking secret reads (E3 v1.3x claim)
- Vendor docs stating rules/memory files are not security boundaries (if such statements exist)
- Cursor/Windsurf/Copilot equivalents (allowlists, yolo-mode gates) — only what's solid

**Cluster D — Unicode steganography background:**
- Tag codepoints U+E0000–E007F as prompt-smuggling channel (Embrace The Red "ASCII smuggling", ~Jan 2024?)
- Invisible-character classes (ZWJ U+200D, ZWSP U+200B, bidi controls U+202A–E / U+2066–9)
- Trojan Source (CVE-2021-42574, Boucher & Anderson 2021) as the adjacent prior art for code
- Detection: existing linters/scanners for invisible Unicode in text files

**Discovery (open-ended):**
- Later (post-Mar-2025) instances of rules-file poisoning / malicious cursor-rules repos / AGENTS.md injection research
- Copilot-instructions exfiltration research (e.g. CamoLeak/Legit Security, if real)
- Studies measuring how well agents follow repo rules files (adherence rates)
- Anything else high-quality & relevant to "advisory vs deterministic; rules-file backdoor"

## House rules reminders
- Dense English prose; separate strong evidence vs vendor claims vs synthesis.
- Tool facts point-in-time; flag fast-moving items for re-verification.
- Tie back to E1/E5, E2, I2, D5, S1/S2/S8, Report 6.

## OUTCOME (2026-07-21)

Shipped as v1.62. The 6-agent verification swarm (4 fact clusters + 2 discovery) confirmed the
seed facts; a 2-agent spot-verify round then caught real errors that were corrected before
writing: Anthropic's containment post "How we contain Claude across products" is dated
**25 May 2026** (not "Jun 2026" — fixed in the S3 draft and retro-fixed in both S2 copies);
Check Point's "Caught in the Hook" is **25 Feb 2026**; NVIDIA's AGENTS.md post is **Apr 2026**
(with Jul–Aug 2025 disclosure); GitHub issue #11226 was **closed not-planned**; arXiv:2602.11988
(ETH AGENTS.md study) has **no venue** yet; CamoLeak has **no CVE** (the CVE-2025-59145 seen in
press coverage is the unrelated npm color-name takeover — debunked in §5 and the closing note).
Attribution fixes applied per the fact pass: AML.CS0041 is a case-study id (techniques
AML.T0068/T0081/T0067), the Tag-block range is credited to the technique literature not Pillar's
prose, and the PoC is described as script injection, not exfiltration. S8's "hooks override
permission rules" claim was rewritten (hooks tighten-only; permission system for hard
allow/deny).

Final files: `deep-dives/S3-advisory-vs-deterministic-rules-backdoor-deepdive.html` (standalone),
the `s3ov` overlay in `workbook/agentic-development-study.html` (anchor `#s3-deepdive`),
gallery entries in `gallery-registry.json` / `gallery.html`, changelog mirror in
`docs/CHANGELOG.md`, session hand-off in `NOTES.md`. Validator green.
