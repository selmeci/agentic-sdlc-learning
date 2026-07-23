# S4 deep dive — outline & seed facts (pre-swarm)

**Topic:** `sec-mcp` — "MCP / tools: the richest attack surface"
**Deliverables:** `deep-dives/S4-mcp-tools-attack-surface-deepdive.html` standalone + workbook overlay (`#s4-deepdive`, `s4ov`), per `docs/AUTHORING-GUIDE.md`. Next version: v1.63.
**Workflow (per NOTES.md / S3 precedent):** outline → swarm (fact-verify + discovery) → spot-verify discovery finds → write body → assemble → validate → gallery.

## Position in the module (avoid re-treading neighbours)

- S1 owns: the injection root cause + "assume breach" posture + arms-race evidence.
- S2 owns: the trifecta geometry + Rule of Two + human-gate failure modes; GitHub-MCP & Supabase appear there as **one-table-row chains** — S4 owns the in-depth mechanics (S2's closing note explicitly defers to S4).
- S3 owns: advisory-vs-deterministic split + rules-file backdoor; rug-pull "0/8 re-approval" stat already used there (reuse by reference).
- S7 owns: secrets problem breadth + Figma #303 hidden-layer design injection; S4 references, doesn't re-derive.
- S4's distinct job: **the tool layer itself** — the protocol's trust model, the three attack classes (content through tools, the server as attacker, the implementation breaking), the privilege/config layer, and the MCP-specific defense stack. The "everything the agent *loads and calls* is executable trust" thesis, complementing S3's "everything the agent *reads*".

## Draft section structure

- **§0 Why the tool layer is the richest surface** — tools turn tokens into effects (E1 component); MCP standardised the seam, so the seam is now a supply chain. Every tool call crosses the trust boundary in both directions: descriptions/results flow *in* as content the model trusts, calls flow *out* as actions with the user's privileges. Trifecta framing: a single MCP server can ship all three legs (S2). Forward: the "richest" claim is structural — count the directions of trust, not the CVEs.
- **§1 MCP mechanically: what the protocol actually trusts** — Nov 2024 launch (Anthropic), OpenAI/Google adoption 2025, AAIF/Linux Foundation donation; spec pieces relevant to security: tool descriptions & annotations (`readOnlyHint` etc. — advisory!), OAuth in the spec, the spec's own security-best-practices doc (confused deputy, session hijack, token passthrough), sampling/elicitation as extra channels. Key line: the protocol has trust *annotations*, not trust *enforcement* — everything rides on the client.
- **§2 Class 1 — injection through tool results (content → privilege)** — the deep case studies:
  - **GitHub MCP toxic flow** (Invariant Labs, 26 May 2025): malicious public issue → agent (Claude 4 Opus + official GitHub MCP) pulls private-repo data → leaks via autonomously created PR. "Not a flaw in the GitHub MCP server code… a fundamental architectural issue"; "all three ingredients in a single package". No CVE — the server worked as specified.
  - **Supabase MCP** (General Analysis, early Jul 2025): support-ticket text addressed to the agent → `service_role` key (bypasses RLS) → SELECT `integration_tokens` → INSERT into the attacker-visible ticket. "No permissions were violated. The agent just followed instructions it should never have trusted." **Constructed PoC — say so.** Supabase's response post (defense-in-depth-mcp): read-only mode, untrusted-content wrapping, MCP off by default.
  - Pattern: tool results are untrusted content arriving with a privileged microphone; the ticket/issue channel is S7's contract surface — one sentence cross-ref.
- **§3 Class 2 — the server itself is the attacker** —
  - **postmark-mcp** (Koi Security, Sep 2025): first documented in-the-wild malicious MCP server; one-line BCC added in v1.0.16 after ~15 clean versions; silently exfiltrated every email. Supply-chain lesson: it was *updated into* malice.
  - **Tool poisoning & shadowing** (Invariant, Apr 2025 PoCs): malicious instructions embedded in tool *descriptions* (invisible to the user, read by the model); shadowing — a hostile server's description steers calls to *other* servers' tools (S1 outline deferred the depth here).
  - **Rug pulls**: tool metadata changes server-side after one-time approval; 0/8 server libraries re-prompt (cross-ref S2/S3 where already cited).
  - Ecosystem breadth: typosquatted servers, registry growth, scans finding vulnerable/malicious servers in the wild (GitGuardian secret-leak figure in MCP configs; OWASP MCP Top 10 beta).
- **§4 Class 3 — the implementation breaks (classic vulns in a new stack)** — the CVE run, all point-in-time:
  - `mcp-remote` CVE-2025-6514 (CVSS 9.6; OAuth-payload RCE on Windows; ~437k downloads) — a *bridge* tool everyone installed.
  - MCP Inspector CVE-2025-49596 (9.4; browser→localhost RCE) — even the ecosystem's reference dev tool shipped insecure by default.
  - Anthropic reference Filesystem server CVE-2025-53110 / 53109 (path-validation escapes).
  - Community `figma-developer-mcp` CVE-2025-53967 (command injection; fixed 0.6.3).
  - Lesson: MCP didn't invent new bug classes; it re-installed the old ones (command injection, SSRF, path traversal) one hop from the model, often pre-auth and running locally with user privileges.
- **§5 The privilege & configuration layer** — why incidents hurt as much as they do: over-scoped tokens (`service_role`, broad PATs) hand the injected agent maximum blast radius; MCP configs are JSON files full of plaintext secrets (GitGuardian figure; scan configs like code); one-repo-per-session / session scoping; shadow MCP discovery at clients (the topic's open question — discovery tooling, allowlist enforcement across teams).
- **§6 The defense stack, MCP-specific** — allowlist servers like dependencies (pin versions, review updates — postmark lesson); least-privilege scoped tokens, read-only where possible; human gate on writes (with S2's fatigue fine print); sandboxed containers per server; egress allowlist as backstop (S3's highest-leverage control); gateways/proxies as the 2026 enterprise pattern (policy + logging at the seam); spec-level mitigations (OAuth done right, no token passthrough); scanning (mcp-scan etc.) — with the honest note that scanning is advisory-shaped unless enforced at the client/gateway (S3 litmus applied).
- **§7 Takeaways + further reading** — three-sentence callout; tie back to S1/S2/S3/S7, E5, I7, Report 6.

## Candidate diagrams (SVG)

1. **The two-way trust boundary** — one tool call, both crossings: descriptions/results in (content, model-trusted), calls out (actions, user-privileged); attack classes 1/2/3 pinned to where they enter.
2. **The three attack classes map** — class 1 content-through-tools (GitHub, Supabase), class 2 hostile server (postmark, poisoning, rug pull), class 3 broken implementation (CVE list) — with the control that matches each.
3. **GitHub MCP toxic-flow chain** (A→B→C swimlane, deeper than S2's table row) — issue → agent → private repos → PR exfil; mark each severable leg.
4. **postmark-mcp timeline** — 15 clean versions → v1.0.16 BCC line → discovery; the "updated into malice" supply-chain shape. (Maybe fold into §3 prose if 3 figures suffice.)

## Seed facts to verify (swarm)

**Cluster A — MCP protocol & spec (primary: modelcontextprotocol.io, Anthropic newsroom):**
- Launch date & wording (Nov 2024); OpenAI adoption (Mar 2025) & Google/DeepMind; AAIF / Linux Foundation donation date & founding members.
- Spec versions & current stable; where security lives in the spec (Security Best Practices doc: confused deputy, session hijacking, token passthrough — exact named sections).
- Tool annotations (`readOnlyHint`, `destructiveHint` …) — advisory semantics per spec, exact wording ("should not be relied upon for security decisions"?).
- Official MCP registry status (GA? preview?) & growth numbers (server counts — PulseMCP etc., labeled).

**Cluster B — GitHub MCP incident (primary: Invariant Labs blog, 26 May 2025):**
- Exact date, post title ("toxic agent flows"?), exact quotes ("fundamental architectural issue", "all three ingredients…").
- Setup details: Claude 4 Opus, official GitHub MCP server (~14k stars claim — pin or drop), public repo with malicious issue, the exfil-via-PR mechanics.
- "No CVE / server worked as specified" framing; any GitHub response (lockdown mode — which date/product surface?).

**Cluster C — Supabase MCP incident (primary: General Analysis blog + supabase.com/blog/defense-in-depth-mcp):**
- Exact date (early Jul 2025?), PoC-not-in-the-wild status, mechanism details (ticket text addressed to "CURSOR CLAUDE"? service_role bypasses RLS, integration_tokens, INSERT into ticket).
- Exact quote "No permissions were violated…".
- Supabase's response measures (read-only mode, untrusted-content wrapping, MCP disabled by default — exact list).

**Cluster D — postmark-mcp + the CVE run:**
- postmark-mcp (Koi Security, Sep 2025): exact version (1.0.16?), number of prior clean versions, the BCC line mechanics, weekly downloads, how found, npm/registry response, "first malicious MCP server in the wild" claim wording.
- CVE-2025-6514 (mcp-remote): reporter (Oasis?), CVSS, affected/fixed versions, Windows-only?, download count.
- CVE-2025-49596 (MCP Inspector): reporter (Oligo?), mechanism (browser→localhost), fixed version.
- CVE-2025-53110 / 53109 (Anthropic Filesystem server): what exactly (symlink? path escape?), reporter, fixed versions.
- CVE-2025-53967 (figma-developer-mcp): command injection detail, fixed 0.6.3, reporter.

**Cluster E — attack classes & ecosystem data:**
- Tool poisoning & tool shadowing PoCs (Invariant, ~Apr 2025): exact dates, mechanism, which clients affected (Cursor dialog hidden-argument detail is S2's — confirm scope).
- Rug pull: the 0/8 re-approval study (arXiv:2607.05744?) — confirm what exactly it measured.
- GitGuardian: the "24,008" secrets-in-MCP-configs figure — exact number, report, date.
- OWASP Top 10 for MCP: status (beta?), steward, headline items.
- Ecosystem scans: any measured study of public MCP servers' security posture (% with vulns / no auth / etc.) — Equixly, Backslash, Knostic, academic (MCPTox? MCP-Universe §4.5 already used for accuracy, check for a security section).
- MCP Security checklist / other canonical community lists.

**Cluster F — defenses (point-in-time, vendor docs):**
- MCP gateways/proxies as 2026 pattern: named products/oss (Docker MCP Toolkit & Catalog, Lasso/Context-Fort, Microsoft, Cloudflare?); what a gateway enforces vs what stays client-side.
- Client-side allowlists: Claude Code managed-settings `allowedMcpServers`/enterprise controls; Cursor equivalents — only what's solid, marked point-in-time.
- mcp-scan (Invariant) and similar scanners: what they catch (poisoning, rug pulls via pinning?).
- GitHub MCP server "lockdown mode" / read-only flags; server-side scopes as the fix for class 1.
- Spec-level: OAuth resource indicators / token-audience fixes against passthrough.

**Discovery (open-ended, 2 agents):**
- Post-Sep-2025 malicious MCP servers / registry poisoning / new MCP CVEs in 2026 (up to Jul 2026).
- Academic security benchmarks for MCP (poisoning/rug-pull/injection success rates).
- 2026 enterprise MCP security guidance (CSA, NIST, vendor) worth citing.
- Anything else high-quality & relevant the outline missed — e.g., sampling/elicitation abuse, MCP auth deployment reality, server-card trust.

## House rules reminders
- Dense English prose; separate strong evidence vs vendor claims vs synthesis.
- All tool/CVE/product facts point-in-time (as of July 2026); flag fast-moving items for re-verification.
- Tie back to S1/S2/S3/S7, E1/E5, I7, Report 6; keep trifecta depth in S2's terms, don't re-derive it.
- Supabase = constructed PoC; label every vendor-originated incident as vendor research.

## OUTCOME (2026-07-22)

Shipped as v1.63. The 8-agent verification swarm (6 fact clusters + 2 discovery) plus a
6-agent spot-verify round confirmed the seed facts and produced real corrections, applied
before writing and retro-fixed where older content carried them: "combines all three
ingredients in a single package" is **Willison's** line, not Invariant's (fixed in the S4
topic and Report 6); the General Analysis Supabase post is dated **16 Jun 2025** (it went
viral in July — fixed in both S2 copies, Report 6, the I7 topic and the domain map V5
caption); arXiv:2607.05744 measured **0/8 rug-pull techniques** forcing re-approval across
**3** server libraries (32/32 cells), not "0 of 8 libraries" (fixed in both S2 copies);
the mcp-remote CVE reporter is **JFrog (Or Peles)**, not Oasis; CVE-2025-49596's 9.4 is a
**CVSS 4.0** score; ETDI's authors are AWS/Intuit-affiliated, not Microsoft; postmark-mcp
was deleted from npm **by the author**, not by npm; Supabase's default is read-only +
project-scoped, not "MCP disabled"; GitHub's lockdown mode shipped **10 Dec 2025**.
Discovery finds integrated: MCPwn (CVE-2026-33032, with the NVD-vs-press patch dispute
flagged), SANDWORM_MODE's McpInject module, the Smithery registry breach (3,243 = fly.io
apps, mostly MCP servers), the mcp-server-git CVE trio (split fix versions), the TS SDK
DNS-rebinding CVE, Codex CLI CVE-2025-61260 and Claude Code Action CVE-2026-47751, the
NSA CSI (May 2026), CoSAI whitepaper, ATLAS AML.T0086, NIST CAISI (17 Feb 2026), OWASP
MCP Top 10 v0.1 beta, MCPTox / MCPSecBench / Hasan / MCP-TDP / MCPBench numbers (each
with its caveat), Astrix/Equixly/Bitsight/Trend Micro scans, and the mcp-scan → Snyk
Agent Scan rebrand.

Final files: `deep-dives/S4-mcp-tools-attack-surface-deepdive.html` (standalone), the
`s4ov` overlay in `workbook/agentic-development-study.html` (anchor `#s4-deepdive`), 4
gallery entries in `gallery-registry.json` / `gallery.html`, changelog mirror in
`docs/CHANGELOG.md`, CONTENT-MAP updated (50 companions). Validator green (60 topics
intact, `#s4-deepdive` wired ×2).
