# S1 deep-dive outline — "Security is cross-cutting: prompt injection & blast-radius reduction"

Working outline for the S1 deep-dive companion (M7 opener, topic `sec-crosscut`, token `s1`,
anchor `#s1-deepdive`, overlay `s1ov`, marker `ahS1a`, edge class `edS1`).
Status: **outline + fact list, pending swarm verification — no prose written yet.**

Sources already in-repo: S1 topic `know`/`checks` (workbook line 9534), Report 6 notes
(TL;DR, framing, honest-ceiling sections), E5 governance deep dive (owns mechanisms —
S1 must reference, not re-teach), domain map V4/V5 (trifecta + threat map SVGs already exist).

## Positioning (avoid duplication)

- **E5** owns enforcement mechanisms (hooks/permissions/sandbox, advisory-vs-deterministic litmus).
- **S2** owns the lethal trifecta & Rule of Two in depth. S1 may only *preview* them.
- **V4/V5 domain maps** own the visual threat map. S1 diagrams must not re-draw the threat map.
- **S1's unique job:** the mindset shift — one unsolved root cause (prompt injection), a privileged
  runtime as the defended asset, blast-radius reduction as the posture, the honest ceiling
  (unsolved, >90% bypass), and how to say this to a client without killing the engagement.

## Section plan

- **§0 Why it matters** — security is not an eighth component; it lands on all seven + the two
  contract surfaces. Module opener framing; hooks into S2–S8.
- **§1 The root cause: one token stream, no trust separation** — trusted instructions and
  untrusted data are concatenated into the same token stream (Willison). The SQL-injection
  analogy: classic injection was solved by parameterized queries; LLMs have no equivalent —
  data and instructions are the same medium. Direct vs indirect injection (indirect = the
  delivery vector for nearly every real incident).
  **Diagram A:** token-stream figure — [system prompt][user instruction][untrusted retrieved
  content] → one stream → model → privileged tools (shell/files/network/credentials).
- **§2 What we are actually defending: a privileged developer runtime** — not a chatbot
  (worst case: bad answer) but shell + file write + network + credentials ≈ securing a shell,
  package manager and CI runner combined. Inventory of what a compromised coding agent can do
  (exfiltrate secrets, modify code/CI, self-escalate config — forward refs to S4/S5 incidents).
- **§3 The posture: assume breach → blast-radius reduction** — bounded, observable, reversible.
  Why prevention-first fails (see §4); what each blast-radius property means concretely;
  deterministic controls as the only enforcement (advisory ≠ control, ref E5).
  **Diagram B:** layered blast-radius funnel — attack enters → each deterministic layer
  (least privilege → sandbox → egress allowlist → human gates → audit) shrinks reachable damage;
  contrast "prevention wall" (breached once = total loss) vs "bounded blast radius".
- **§4 The honest ceiling: unsolved, and say so** — "The Attacker Moves Second"
  (arXiv 2510.09023): all 12 tested defenses bypassed >90% by adaptive attackers; prompt
  injection as "architectural limitation"; Willison 2.5+ years "no convincing mitigations".
  Architectural defenses reduce but do not eliminate: Rule of Two (preview → S2),
  CaMeL / Dual-LLM (arXiv 2503.18813), design-patterns paper (arXiv 2506.08837).
  Client communication: "complete security is a different, much harder, unsolved problem" —
  every control reduces likelihood and blast radius, none prevents injection.
- **§5 How S1 lands on the whole framework** — cross-cut map: one row per framework component
  (prompt, context, memory, tools/MCP, loop, verification, governance, contract surfaces) →
  threat class → owning S-topic. Table, not diagram (V5 already has the SVG threat map).
- **§6 Takeaways** (three-sentence callout) + further reading + closing note.

## Facts to verify via swarm (with in-repo claims to check)

1. "The Attacker Moves Second" — arXiv 2510.09023, Oct 2025; authors Nasr, Carlini, Tramèr et al.;
   joint OpenAI/Anthropic/DeepMind; bypassed all 12 tested defenses with >90% success.
   Check exact title, author list, institution claim, the 12-defenses and >90% figures.
2. Willison "the lethal trifecta" post dated 16 Jun 2025; quote: trusted prompts and untrusted
   text "concatenated together into the same token stream" — exact wording/source post.
3. Willison coined "prompt injection" ~Sep 2022 — date and original post.
4. CaMeL — "Defeating Prompt Injections by Design", arXiv 2503.18813 (DeepMind, Apr 2025);
   builds on Willison's 2023 Dual-LLM proposal; privileged/quarantined LLM split + DSL claim.
5. Design-patterns paper — Beurer-Kellner et al., arXiv 2506.08837; six patterns list
   (action-selector, plan-then-execute, map-reduce, dual-LLM, code-then-execute,
   context-minimization).
6. OWASP LLM Top 10 — prompt injection as LLM01 in the 2025 list; and whether OWASP/vendors
   use the phrase "architectural limitation" (attribution needed).
7. SQL-injection analogy framing — who made it publicly (Willison? NCSC "prompt injection is
   not SQL injection" Dec 2023/2025?); verify before leaning on it.
8. Any post-Oct-2025 state-of-the-art shift: new model-layer defenses, updates to the
   "unsolved" verdict, notable 2026 prompt-injection incidents involving coding agents that
   belong in S1 (not S4/S5).

## Discovery briefs for the swarm (things the outline may have missed)

- D1: Other high-quality framings for "why LLMs can't separate instructions from data"
  (instruction hierarchy — OpenAI 2024, Spotlighting — Microsoft, structured queries /
  StruQ, ICL markers) — worth one mention each in §1/§4?
- D2: "Assume breach" / blast-radius lineage in classic security (Microsoft assume-breach,
  zero trust, NIST) — good grounding for §3.
- D3: Client-communication precedents — how vendors/OWASP/regulators phrase "unsolved"
  (NCSC, Gartner, OpenAI safety pages) to borrow honest, non-alarmist wording for §4.
- D4: Anything else the swarm judges high-quality and relevant to S1's scope
  (root cause, privileged runtime, blast-radius posture, honest ceiling) that the outline missed.

---

# Swarm results (2026-07-20) — 12 agents, all completed

## Fact verification outcomes

1. "The Attacker Moves Second" — **mostly confirmed, three fixes.** arXiv 2510.09023, v1 10 Oct 2025,
   Nasr … Carlini … Tramèr (14 authors). Affiliations broader than "OpenAI/Anthropic/DeepMind":
   also HackAPrompt, Northeastern, ETH Zürich, MATS. The 12 defenses span jailbreak AND prompt
   injection. Figure is **">90% for most"** — PIGuard 71%, MELON 76%; most defenses originally
   reported near-zero ASR. Human red-teamers (500+) beat automation 100% vs 69%.
2. Willison trifecta post — **title corrected** ("The lethal trifecta for AI agents: private
   data, untrusted content, and external communication", 16 Jun 2025). The token-stream quote in
   our notes is a paraphrase; verbatim: "Everything eventually gets glued together into a
   sequence of tokens and fed to the model." Also: "I coined the term prompt injection… I named
   it after SQL injection, which has the same underlying problem."
3. Coinage — **confirmed**: "Prompt injection attacks against GPT-3", 12 Sep 2022; Goodside
   demonstrated, Willison coined; the SQLi analogy was Willison's own, with the "parameterized
   prompts" hope retracted 13 Apr 2023 ("extremely difficult, if not impossible").
4. CaMeL — **fixes**: v1 24 Mar 2025 (publicized Apr); Google / Google DeepMind / ETH Zurich;
   the paper's term is "custom Python interpreter" executing pseudo-Python (not "DSL");
   published IEEE SaTML 2026; AgentDojo **77% vs 84%** undefended (v2). The "once an LLM agent
   has ingested untrusted input…" quote belongs to the **Design Patterns paper**, not CaMeL.
5. Design Patterns — **confirmed**: Beurer-Kellner et al. (alphabetical order; Tramèr
   corresponding), arXiv 2506.08837, v1 10 Jun 2025; pattern 3 is "**LLM** map-reduce"; the
   trade-off is phrased as utility vs security; "unlikely that general-purpose agents can
   provide meaningful and reliable safety guarantees".
6. OWASP — LLM01:2025 Prompt Injection is #1 (also #1 in 2023). **"Architectural limitation"
   is secondary commentary — do not attribute to OWASP.** OWASP's wording: "it is unclear if
   there are fool-proof methods of prevention"; "mitigate the impact". OpenAI (Atlas hardening
   post, Dec 2025): "unlikely to ever be fully 'solved'". OpenAI CISO Stuckey (Oct 2025, via
   The Register): "a frontier, unsolved security problem".
7. SQL-injection analogy — **the NCSC piece is 8 Dec 2025** (not 2023): "Prompt injection is not
   SQL injection (it may be worse)", David C (NCSC Technical Director for Platforms Research).
   Verbatims: parameterized queries fix SQLi "at its root"; under an LLM "there is only ever
   'next token'"; prompt injection "may never be totally mitigated"; it "will remain a residual
   risk, and cannot be fully mitigated with a product or appliance"; "Beware any [product] that
   claim they can 'stop' prompt injection"; LLMs as "inherently confusable"; advice aligned to
   ETSI TS 104 223.
8. SOTA check (Jul 2026) — **the "unsolved" verdict stands**; no defense survived adaptive
   attack. New: SoK "Prompt Injection Attacks on Agentic Coding Assistants" (arXiv 2601.17548,
   78 studies, >85% adaptive ASR); AutoDojo (arXiv 2606.15057: a filter at 0% static ASR → 28%
   recovered, 64% on action-open tasks); "Defenses… Learn Surface Heuristics" (arXiv 2601.07185);
   role-confusion paper (arXiv 2603.12277, MIT CSAIL / ICML 2026: "destyling" cuts ASR 61%→10%;
   injection defense "a perpetual whack-a-mole game"). Willison, Jun 2026 (softening, not
   reversal): frontier-model training makes naive attacks "much harder to pull off", but "I
   still wouldn't recommend deploying a production system where a prompt injection attack could
   cause irreversible damage". 2026 coding-agent incidents: **Clinejection** (Mar 2026: issue
   title → cache poisoning → cline@2.3.0 published with stolen npm secrets); **Comment and
   Control** (Apr 2026, Guan et al.: a PR title made Claude Code Security Review, Gemini CLI
   Action AND Copilot Agent post their own API keys; CVSS 9.4; silently patched, no CVEs);
   **Claude Code GitHub Action** (Microsoft Threat Intelligence, Jun 2026: injection → Read of
   /proc/self/environ → unscrubbed ANTHROPIC_API_KEY; fixed in Claude Code 2.1.128; in-the-wild
   HTML-comment payloads observed); Unit 42 (Mar 2026): 22 distinct injection techniques found
   in live web pages. OpenAI "Lockdown Mode" (~Jun 2026): deterministic egress limiting —
   vendor validation of the posture, explicitly not an injection cure.

## Discovery results — accepted into the section

- **D1 (instruction/data separation attempts)** — the arms-race arc for §4: Instruction
  Hierarchy (OpenAI, arXiv 2404.13208 — NOT an ICML paper; Rehberger bypassed GPT-4o-mini's
  hierarchy within 3 days, Jul 2024) → Spotlighting (Microsoft, arXiv 2403.14720; claimed
  >50%→<2% ASR; prompt-layer only, defense-in-depth by its own framing) → StruQ
  (arXiv 2402.06363, USENIX Security 2025; broken whitebox at 85–95%, arXiv 2507.07417) →
  SecAlign (CCS 2025; Meta SecAlign++ 70B open weights, arXiv 2507.02735) → CaMeL (the only
  provable approach, at ~7pp utility cost). Each raises the bar; none eliminates.
- **D2 (classic lineage for §3)** — Saltzer & Schroeder 1975 least privilege ("Primarily, this
  principle limits the damage that can result from an accident or error"); NIST SP 800-207
  (Aug 2020: attacker assumed present + least privilege per session); Microsoft Zero Trust
  ("Assume breach… controls focus on limiting breach impact"); Bargury (Aug 2024, "Assume
  Breach When Building AI Apps": "AI jailbreaks are not vulnerabilities; they are expected
  behavior").
- **D3 (client wording for §4)** — NCSC residual-risk wording; OpenAI's scam/social-engineering
  analogy (a permanent risk category you manage, like phishing); OWASP mitigate-the-impact;
  NCSC "beware any product that claims to 'stop' prompt injection" (anti-silver-bullet line).
- **D4 (gaps — all accepted)**:
  - **Confused deputy** (Hardy 1988; Willison dual-LLM post Apr 2023; NCSC "inherently
    confusable"; arXiv 2606.28679 formalizes it for agent frameworks) — the classic name for
    the privileged runtime; anchors §2.
  - **Kiro incident** (Dec 2025, reported by FT Feb 2026: an agent with operator-level
    permissions deleted & recreated an environment → ~13h AWS Cost Explorer outage; **no
    attacker involved**) — blast-radius controls are dual-purpose; hook for §0/§3.
  - **Human-gate visibility caveat** (Invariant tool-poisoning, Apr 2025: Cursor's approval
    dialog hid the SSH key being exfiltrated; HTML-comment payloads invisible in rendered
    view) — the human sees less than the model.
  - **Tool descriptions as an injection channel** (Invariant: tool poisoning, rug pulls,
    shadowing — one sentence; S4 owns the depth).
  - **"Reversible" caveat** — memory poisoning persists across sessions (Microsoft Defender
    research, Feb 2026; one sentence; S6 owns the depth).
  - **"Observable" caveat** — output laundering: "cut the first 7 chars" of an sk-ant- key
    defeated GitHub Secret Scanning; EchoLeak (CVE-2025-32711) exfiltrated via reference-style
    Markdown images past link redaction — justifies deterministic egress over output scanning.
  - **OWASP Top 10 for Agentic Applications 2026** (ASI01 Agent Goal Hijack — "LLMs can't
    reliably tell instructions from data"; ASI03 confused deputies) — key the cross-cut map
    to ASI IDs.
  - Discarded: CurXecute CVE-2025-54135 (already covered), Kiro "6.3M orders" claim
    (unverifiable), Nx s1ngularity (off-scope), Aim Security EchoLeak link (dead — cite MSRC
    + arXiv 2509.10540 instead).

## Final section plan (post-verification)

- **§0 Why it matters** — module opener; security is not an eighth component; one unsolved
  root cause; the Kiro incident as the "no attacker needed" hook + Comment and Control as the
  adversarial one (one injection, three vendors, API keys posted as PR comments).
- **§1 The root cause: one token stream, no trust separation** — Willison verbatim ("glued
  together into a sequence of tokens"); coinage 12 Sep 2022; the SQLi-analogy arc (Willison's
  2022 hope → Apr 2023 retraction → NCSC Dec 2025 "it may be worse"); direct vs indirect;
  the tool-metadata channel (one sentence); NCSC "only ever next token".
  **Diagram A:** token-stream figure: [system prompt][user task][untrusted content: tickets,
  web, tool output, tool descriptions] → one stream → model → privileged tools.
- **§2 What we are defending: a privileged runtime (a confused deputy)** — Hardy 1988; NCSC
  "inherently confusable"; inventory: shell, files, network, credentials ≈ shell + package
  manager + CI runner; Willison: sneaked-in tokens = "complete control over what happens next".
- **§3 The posture: assume breach → blast-radius reduction** — lineage chain
  (Saltzer & Schroeder → NIST 800-207 → Microsoft → Bargury); bounded/observable/reversible
  with the three honest caveats (gates see less / laundering defeats scanning / memory breaks
  reversibility); dual-purpose vs Kiro-style error; deterministic controls only (ref E5);
  OpenAI Lockdown Mode as vendor validation.
  **Diagram B:** blast-radius funnel — injected instruction enters → least privilege → sandbox
  → egress allowlist → human gate → audit/rotate; residual damage shrinks per layer; contrast
  "prevention wall: one breach = everything".
- **§4 The honest ceiling: unsolved — and how to say it** — the arms-race arc (D1 works →
  Attacker Moves Second >90%-for-most + 2026 confirmations: SoK >85%, AutoDojo); CaMeL &
  design patterns reduce-but-don't-eliminate (77/84; the "impossible… consequential actions"
  quote correctly attributed to Beurer-Kellner et al.); Willison Jun 2026 nuance; client
  wording from D3 (NCSC / OpenAI / OWASP quotes; the anti-silver-bullet line).
- **§5 The cross-cut map** — table: framework component → threat class → owning topic, keyed
  to OWASP ASI IDs (ASI01/02/03/06…) and S2–S8; pointer to domain map V4/V5.
- **§6 Takeaways + further reading + closing note.**

## House notes for the writer

Token `s1`: anchor `#s1-deepdive`, overlay `s1ov`, close attr `data-s1close`, marker `ahS1a`,
edge class `edS1`. Standalone: `deep-dives/S1-security-crosscutting-deepdive.html`.
Body shape per AUTHORING-GUIDE (`§0 why` → `.io`/`.comp`/`.callout`/figures/`table.map` →
takeaways callout → `.reading` → `p.closingnote`). Step-5 fixes in passing: the S1 topic
`know` bullet 4 (">90%" → ">90% for most"; drop the OWASP-flavoured "architectural
limitation" attribution) and the matching Report 6 TL;DR bullet.
