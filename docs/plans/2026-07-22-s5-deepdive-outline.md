# S5 deep dive — outline & seed facts (pre-swarm)

**Topic:** `sec-loop` — "Loop / auto-run: self-modification, YOLO & sandbox escapes"
**Deliverables:** `deep-dives/S5-loop-autorun-selfmod-sandbox-deepdive.html` standalone + workbook overlay (`#s5-deepdive`, `s5ov`), per `docs/AUTHORING-GUIDE.md`. Next version: v1.64.
**Workflow (per S3/S4 precedent):** outline → swarm (fact-verify + discovery) → spot-verify discovery finds → write body → assemble → validate → gallery.

## Position in the module (avoid re-treading neighbours)

- S1 owns: the injection root cause + assume-breach posture; the Kiro outage is its "no attacker needed" hook — S5 references, never re-tells.
- S2 owns: trifecta geometry, Rule of Two, human-gate failure modes (approval fatigue, Lies-in-the-Loop) — S5 cites by reference.
- S3 owns: the advisory-vs-deterministic split and the rules-file backdoor; it already teased GitHub issue #11226 and left "write-gating the enforcement configuration" as **S5's open question** — S5 owns that depth.
- S4 owns: the MCP/tool surface incl. config-as-execution CVE-2025-61260 / CVE-2026-47751 — S5 must not re-cover those two.
- S6 owns: memory poisoning & persistence (MemoryTrap reaching global hooks) — S5 cross-refs only.
- S8 owns: the configuration how-to (managed settings, sandbox setup, egress) — S5 argues *why*, S8 shows *how*.
- E5 owns enforcement mechanisms, E6 owns the L1–L5 autonomy scale (L3 production ceiling), E10 owns background/unattended agents.
- **S5's distinct job: the loop component itself.** What changes when the agent runs *unattended and repeatedly*: (1) self-modification — the agent edits its own execution context to escalate (config, hooks, allowlists, sandbox root); (2) YOLO / auto-approve as a risk multiplier, adversarial *and* non-adversarial; (3) the sandbox as the containment answer — and its documented escape record; (4) the practical write-gating list: which files an agent must never be able to edit.

## Draft section structure

- **§0 Why the loop is its own threat surface** — every prior section assumes a bounded session with a human in the loop; auto-run removes both bounds. The loop component (M1) turns a one-shot injection into a *campaign*: effects compound across iterations, and the agent's own environment becomes editable state. Two hooks: an adversarial one (Copilot YOLO RCE) and a non-adversarial one (Replit production-DB deletion during a code freeze) — blast-radius controls are dual-purpose (S1's Kiro lesson, one sentence).
- **§1 The self-escalation pattern: one class, three CVEs** — the shared shape: injected instruction → agent modifies its *own* execution context → next tool call runs with privileges it wasn't granted. The three anchor incidents:
  - **Copilot "YOLO mode" RCE, CVE-2025-53773** (Embrace The Red / Johann Rehberger): injection writes `chat.tools.autoApprove: true` into `.vscode/settings.json` → arbitrary command execution; "wormable" claim; Microsoft patch.
  - **Cursor Auto-Run allowlist bypass, CVE-2026-22708**: shell built-ins (`export`, `alias`) don't match the allowlist → env poisoning past it.
  - **Codex CLI, CVE-2025-59532**: model-generated `cwd` used as the sandbox root — the model picks its own jail.
  - The class defense: security-relevant config must be write-gated from the agent (the §4 answer).
  **Diagram A:** the self-escalation loop — untrusted content → injection → edit own config/hooks/allowlist → escalated next iteration → repeat; mark where each CVE entered and where the write-gate severs the cycle.
- **§2 YOLO / auto-approve as a multiplier** — the vendor taxonomy of hands-off modes (`--dangerously-skip-permissions`, Cursor YOLO/Auto-Run, Copilot `autoApprove`, Codex `--full-auto`, Gemini `--yolo`): what each actually disables, defaults, and scope. Why it multiplies: it pre-answers every human gate (S2's gate failure modes become moot — there is no gate), and it converts any injection into immediate execution. The non-adversarial record: Replit agent deleting the production database during an explicit code freeze, then misreporting it (Jul 2025); other documented YOLO-mode losses. Framing: YOLO is not "fast mode", it is removing leg of defense-in-depth — acceptable only inside a hardened, network-isolated sandbox.
  **Diagram B (maybe table instead):** hands-off-mode taxonomy — vendor, flag/setting, what it disables, safe context.
- **§3 The sandbox: the containment answer and its escape record** — why the sandbox is *the* control for auto-run (deterministic, ref S3; covers what permissions can't). The stack: OS-level (Seatbelt/bubblewrap — Anthropic's `sandbox-runtime`), containers, microVMs (Firecracker/gVisor), network isolation. The honesty layer: Anthropic's own docs — "sandboxing reduces risk but is not a complete isolation boundary"; documented escape classes (kernel exploits, socket/abstract-namespace leaks, credential leakage into the sandbox — S3's `sandbox.credentials` note; DuneSlide CVE-2026-50548/50549 zero-click escape, CVSS 9.8). What "hardened" means concretely for YOLO: no credentials in, egress allowlist out, no production mounts.
  **Diagram C:** containment stack — agent → OS sandbox → container → microVM/VM → host, with documented escape points pinned per layer.
- **§4 Write-gating the enforcement configuration** — answering S3's open question. GitHub issue #11226 (Claude able to modify its own hook scripts despite deny rules; closed without fix, Jan 2026; "behavioral guidance, not actual enforcement"). The inventory of files an agent must never write: harness settings (`settings.json`, `chat.tools.*`), hook scripts, permission/allowlist files, MCP configs (S4's config-as-execution), CI definitions, memory stores (S6 hand-off). Mechanisms that exist today: managed-settings precedence, file-permission/OS-level protection, hooks-can-only-tighten (S3), external enforcement (gateways, CI-side checks). The residual gap: enforcement config that lives *inside* the agent's writable workspace is advisory-shaped by S3's own litmus.
- **§5 Autonomy ceilings for the loop** — tie to E6's L1–L5: L3 as the production ceiling for unattended runs; what L4/L5 would require that nobody has (provable containment). E10's background agents as the operational form: queued, sandboxed, reviewed-after. STOP conditions: any workflow that needs YOLO + credentials + network together.
- **§6 Takeaways + further reading** — three-sentence callout; tie back to S1/S2/S3/S4/S6/S8, E5/E6/E10, Report 6.

## Candidate diagrams (SVG)

1. **Diagram A — the self-escalation loop** (§1): cyclic figure, three CVE entry points, the write-gate severing the cycle. **Primary candidate.**
2. **Diagram B — containment stack with escape points** (§3): layered boxes, escape classes pinned (kernel, sockets, creds-in-sandbox, DuneSlide zero-click).
3. **Diagram C — YOLO risk multiplication** (§2): with/without gates comparison — injection path length from content to execution with and without the human gate. (Fallback: table for the vendor taxonomy.)

## Seed facts to verify (swarm)

**Cluster A — Copilot YOLO RCE (CVE-2025-53773):**
- Embrace The Red / Johann Rehberger writeup: exact date & title; mechanism (`chat.tools.autoApprove: true` in `.vscode/settings.json`); the "YOLO mode" naming; the "wormable" claim wording; Microsoft patch date (Aug 2025 Patch Tuesday?); affected/fixed versions; CVSS; any in-the-wild exploitation.

**Cluster B — Cursor: CVE-2026-22708 + DuneSlide:**
- CVE-2026-22708: reporter/vendor, disclosure date, CVSS, affected/fixed versions, exact mechanism (shell built-ins `export`/`alias` bypassing the Auto-Run allowlist → env poisoning).
- "DuneSlide" CVE-2026-50548 / CVE-2026-50549 (CVSS 9.8): who named/reported it, date, mechanism ("zero-click sandbox escape"), which component, fix status. Confirm both CVE numbers and which is which.

**Cluster C — Codex CLI CVE-2025-59532:**
- Reporter, date, CVSS, affected/fixed versions; exact mechanism (model-generated `cwd` treated as sandbox root); OpenAI advisory wording. Confirm it is distinct from CVE-2025-61260 (S4's config-as-execution — do not re-cover).

**Cluster D — self-modification of enforcement:**
- GitHub issue #11226 (anthropics/claude-code): exact title, date opened/closed, "closed without fix" status (Jan 2026), the verbatim quote about hooks being "behavioral guidance, not actual enforcement", mechanism (Claude editing its own hook scripts despite deny rules).
- Anthropic sandbox docs: exact wording "sandboxing reduces risk but is not a complete isolation boundary" (source page); `sandbox-runtime` (srt) repo status, what it wraps (Seatbelt/bubblewrap), stated limitations.
- What vendors now write-protect post-CVE-2025-53773: VS Code/Copilot settings protection, Claude Code settings/hook integrity measures, Cursor equivalents — point-in-time.

**Cluster E — non-adversarial auto-run incidents:**
- Replit incident (Jul 2025): Jason Lemkin's thread dates; what happened (production DB deleted during an explicit code freeze; fabricated/misreported results; claimed rollback "impossible"); Replit/Amjad Masad response; what Replit changed afterward (checkpoints? separation of dev/prod?).
- Other documented YOLO/auto-run losses without an attacker (2025–2026): data loss, runaway cloud spend, mass emails/PRs — only well-sourced cases.

**Cluster F — sandbox technology & escape record:**
- The isolation stack vendors actually ship: Claude Code OS sandbox (Seatbelt/bubblewrap via srt), OpenAI Codex cloud sandbox, devcontainers, microVMs (Firecracker/gVisor) in agent products — point-in-time.
- Documented sandbox-escape/bypass classes relevant to coding agents: kernel exploits out of scope-ish, but misconfig escapes, network/socket leaks (abstract unix sockets), credentials mounted into the sandbox (S3 mentioned "sandbox.credentials" as fast-moving — find the source), egress bypass (CVE-2025-66479 is S2's — cross-ref only).
- Benchmarks/research on agent sandbox escapes, if any.

**Discovery (open-ended):**
- D1: post-Oct-2025 (to Jul 2026) loop/auto-run incidents & CVEs not in the outline: new YOLO-mode exploits, agent self-modification incidents, agent worms/self-replication in the wild, shutdown-resistance/scheming research (Apollo, Palisade, METR) *only if* it lands on the loop/auto-run theme.
- D2: hands-off-mode taxonomy across vendors (exact flags/settings, defaults, what each disables; 2026 changes) — for the §2 table.
- D3: enterprise write-gating practice: managed-settings/MDM enforcement of agent config, hooks integrity approaches, policy-as-code for agent permissions (2026 guidance — NSA CSI, NIST CAISI, CSA, vendor hardening guides).
- D4: anything else high-quality & relevant the outline missed (e.g., loop-specific OWASP ASI items — ASI02? "Excessive Agency" LLM06 lineage; academic loop-risk work).

## House rules reminders
- Dense English prose; separate strong evidence vs vendor claims vs synthesis.
- All CVE/tool/product facts point-in-time (as of July 2026); flag fast-moving items.
- Tie back to S1–S4/S6/S8, E5/E6/E10, Report 6; don't re-derive trifecta (S2) or advisory-vs-deterministic (S3).
- Label vendor-originated research as vendor research; label constructed PoCs as PoCs.

---

# OUTCOME (2026-07-22) — 10-agent verification+discovery swarm + 5-agent spot-verify round; all completed

Full raw reports: session tool-result file (AgentSwarm, 2026-07-22). Below is the
writer's authoritative fact set. **[CORRECTION]** marks where the seed was wrong.

## Verified fact set (per cluster)

**A — Copilot YOLO RCE (CVE-2025-53773).** Rehberger (Embrace The Red), *"GitHub Copilot:
Remote Code Execution via Prompt Injection"*, 12 Aug 2025 (Aug Patch Tuesday); reported to
MSRC 29 Jun 2025. Injection → Copilot adds `"chat.tools.autoApprove": true` to the workspace
`.vscode/settings.json` → experimental "YOLO mode" (present by default in VS Code) disables
all confirmations → RCE on Win/macOS/Linux. CVSS 3.1 7.8 (Microsoft), CWE-77; VS 2022 17.14.x
fixed in 17.14.12. Co-discoverers Markus Vervier (Persistent Security) + Ari Marzuk.
**[CORRECTION]** "wormable" is Persistent Security's word ("Part III … Wormable Command
Execution", 13 Aug 2025); Rehberger's own words are "**AI virus**" and the botnet demo
"**ZombAIs**". No in-the-wild exploitation (CISA SSVC "none", not in KEV, as of Jul 2026).
Extras: same week, same pattern in **Amp Code** (Rehberger's "Month of AI Bugs"); Rehberger
notes the AI can equally write `.vscode/tasks.json`, register fake MCP servers, and overwrite
*other agents'* config files. Fix direction (VS Code 1.104, Sep 2025): confirmation for
editing sensitive files incl. `.vscode/settings.json` + `chat.tools.edits.autoApprove`.
CurXecute CVE-2025-54135 is Cursor/Aim Security, NOT Rehberger — do not credit him.

**B — Cursor CVE-2026-22708 + DuneSlide.**
- CVE-2026-22708 (GHSA-82wg-qcm4-fp2w): reporter **Dan Lisichkin (Pillar Security)**;
  reported 11 Aug 2025, fix in **Cursor 2.3**, CVE published 14 Jan 2026. Mechanism verbatim:
  in Auto-Run + Allowlist mode "certain shell built-ins can still be executed without
  appearing in the allowlist… to poison the shell environment by setting, modifying, or
  removing environment variables that influence trusted commands." Built-ins: `export`,
  `typeset`, `declare`, `readonly`, `unset`, `local` — **[CORRECTION]** `alias` is NOT among
  them; works even with an *empty* allowlist. Chains: PAGER hijack, PYTHONWARNINGS/BROWSER/
  PERL5OPT, zsh `typeset -i ${(e):-…}` RCE. **[CORRECTION]** dual-scored: vendor CVSS 4.0 =
  **7.2 High**; NVD enrichment CVSS 3.1 = **9.8** — attribute the scorer. Cursor's own
  posture quote (gift): allowlists are *"best-effort—bypasses are possible. Never use 'Run
  Everything' mode, which skips all safety checks."* Pillar: initial mitigation "appears
  incomplete".
- DuneSlide = **Cato AI Labs (Cato Networks)**, blog 1 Jul 2026. **[CORRECTION]** 50548 =
  `run_terminal_cmd`'s optional `working_directory` blindly added to the sandbox write
  allowlist (CWE-22); 50549 = Write-tool canonicalization fallback to the original path on
  resolution failure → in-workspace symlink to external target defeats the bounds check
  (CWE-59). Both < 3.0, fixed in **Cursor 3.0** (released 2 Apr 2026 — before public
  disclosure). Vendor CVSS 4.0 = **9.3** both; NVD CVSS 3.1 = **9.8** both — attribute.
  Chain: zero-click injection (innocuous MCP server, e.g. official Linear integration) →
  write outside sandbox → overwrite the `cursorsandbox` helper binary → all subsequent
  commands run unsandboxed (documented paths macOS). Timeline: reported 19 Feb 2026 →
  **rejected 23 Feb** ("threat model does not account for MCP server misuse") → reopened
  after escalation 26 Feb → CVEs assigned 5 Jun, published 25 Jun, blog 1 Jul. **[SPOT]**
  GHSA-3v8f-48vw-3mjx credits **both Cato AI Labs and Wiz's Maor Dokhanian** for 50549 —
  DuneSlide and GhostApproval co-reported the same Cursor symlink bug; say so.
- Adjacent (use in ledger): **CVE-2026-26268** — Cursor sandbox escape via writing
  `.git/config`/hooks, fixed 2.5, disclosed by Novee Security 28 Apr 2026; CVSS 9.9 is
  secondary-source only (Novee/Repello) — attribute or drop the number.

**C — Codex CLI CVE-2025-59532** (GHSA-w5fx-fh39-j5rw, 19 Sep 2025): reporter **Tzanko
Matev (Codetracer)**; CVSS **4.0 8.6** (GitHub CNA; NVD never scored); affected
`@openai/codex` **≥0.2.0 <0.39.0** + IDE extension ≤0.4.11 (fixed 0.4.12). Verbatim: "Codex
CLI could treat a model-generated `cwd` as the sandbox's writable root… This logic bypassed
the intended workspace boundary and enables arbitrary file writes and command execution…
this did not impact the network-disabled sandbox restriction." Fix canonicalizes the
boundary to where the *user* started the session. CWE-20, not path traversal. Distinct from
CVE-2025-61260 (config-as-execution, S4's).

**D — self-modification of enforcement.**
- Issue #11226 ("Security Gap: Hooks Cannot Be Protected From Modification…"), opened
  7 Nov 2025, **[CORRECTION]** closed 12 Jan 2026 by **stale-bot** (`not_planned`, no
  maintainer ever commented) — not a vendor wontfix verdict. The "behavioral guidance, not
  actual enforcement" line is **the community reporter's** wording, not Anthropic's.
  Mechanism: Edit/Write tools modify hook scripts despite `permissions.deny` on
  `~/.claude/hooks/**`; `chmod 444` and root ownership failed as workarounds; cross-refs
  #6631/#6699. Companion issues: **#11815** (18 Nov 2025 — Claude edits its own
  `settings.local.json`; "I could theoretically modify my own permissions") and **#40343**
  (28 Mar 2026 — subagents spawned `bypassPermissions` ignore the project allowlist).
- Anthropic sandboxing docs verbatim (Limitations): **"Sandboxing reduces risk but is not a
  complete isolation boundary. Review the limitations below before relying on it as a hard
  security control."** macOS Seatbelt, Linux/WSL2 bubblewrap; documented holes: domain
  fronting, `allowUnixSockets` → docker.sock, write-escalation via `$PATH`/`.bashrc`,
  Apple Events, `dangerouslyDisableSandbox`.
- **srt** = `anthropic-experimental/sandbox-runtime` **[CORRECTION]** (not `anthropics/`),
  npm `@anthropic-ai/sandbox-runtime`, "Beta Research Preview"; Windows alpha exists (not a
  security boundary there). **Mandatory Deny Paths** always block writes even inside allowed
  paths: shell rc files, `.gitconfig`, `.gitmodules`, `.mcp.json`, `.vscode/`, `.idea/`,
  `.claude/commands/`, `.claude/agents/`, `.git/hooks/`, `.git/config` — the industry's
  concrete anti-self-modification control.
- Post-53773 / current Claude Code integrity measures: sandbox "automatically denies write
  access to Claude Code's `settings.json` files at every scope and to the managed settings
  directory"; deny rules resolve symlinks since v2.1.210; `sandbox.filesystem.disabled`
  honored only from user/managed/CLI settings ("a checked-out project can't switch
  filesystem isolation off"); `ConfigChange` hook event; `allowManagedHooksOnly`;
  docs admit hook `if`-filters "fail open". **Residual gap:** Edit/Write tools "use the
  permission system directly rather than running through the sandbox" — the #11226 class
  persists outside Bash.
- **CVE-2026-25725** [SPOT-verified]: GHSA-ff64-7w26-62rf, published 6 Feb 2026, reporter
  hackerone.com/edbr, fixed **2.1.2**. Verbatim: sandbox "failed to properly protect the
  .claude/settings.json configuration file when it did not exist at startup… allowed
  malicious code running inside the sandbox to create this file and inject persistent hooks
  (such as SessionStart commands) that would execute with host privileges when Claude Code
  was restarted." CWE-501 (+CWE-668 per NVD). Severity: GitHub "High"; NVD-contributed
  vector computes 10.0 Critical — attribute the scorer.
- **CVE-2026-39861** [SPOT-verified]: GHSA-vp62-r36r-9xqp, published 21 Apr 2026 (not May),
  reporter hackerone.com/philts, fixed **2.1.64**, CVSS 4.0 7.7, CWE-22+CWE-61. Verbatim:
  sandboxed process creates a symlink pointing outside the workspace; "its unsandboxed
  process followed the symlink and wrote to the target location outside the workspace
  without prompting the user… neither the sandboxed command nor the unsandboxed app could
  independently write outside the workspace, but their combination could"; reliable exploit
  required prompt injection.
- Anthropic's own docs describe the self-escalation scenario verbatim (with
  `filesystem.disabled`): "a sandboxed command can write files that later commands run or
  read, such as shell startup files… or `~/.claude/settings.json`, and use them to widen its
  own access on the next run."

**E — non-adversarial incidents.**
- Replit (Jul 2025): Lemkin's X posts 17–20 Jul; agent deleted the live production DB
  during an explicit code freeze; Fortune: data for **"more than 1,200 executives and over
  1,190 companies"** **[CORRECTION]** — precise 1,206/1,196 figures are later embellishment;
  the ~4,000 fake records were fabricated **days before** the deletion (covering dev bugs),
  not after as concealment. Agent verbatim: "This was a catastrophic failure on my part. I
  destroyed months of work in seconds." Agent falsely claimed rollback impossible; manual
  rollback worked. Lemkin: "I explicitly told it eleven times in ALL CAPS not to do this.";
  "There is no way to enforce a code freeze in vibe coding apps like Replit." Spend:
  **$607.70 beyond the $25/mo plan in the first days, $200+ in one day, projecting
  ~$8,000/month**. Masad (CEO): "Replit agent in development deleted data from the
  production database. Unacceptable and should never be possible…" Fixes announced:
  automatic dev/prod DB separation, staging, **one-click restore** **[CORRECTION]** (not
  "automatic checkpoints"), planning/chat-only mode, postmortem, refund.
- Gemini CLI (Jul 2025, PM Anuraag Gupta): silent `mkdir` failure, no read-after-write;
  Windows `move` to nonexistent dir = rename → each file overwrote the previous onto one
  target; rest permanently gone. Agent: "I have failed you completely and catastrophically…"
  (AI Incident DB #1178).
- Google Antigravity (late Nov/early Dec 2025, u/Deep-Hyena492, **Turbo mode**): asked to
  clear a project cache, ran `rmdir /q` on the root of D: — bypassed Recycle Bin; media
  files unrecoverable. Agent: "No, you did not give me permission to do that…" (Tom's
  Hardware, 3 Dec 2025).
- Cursor support bot "Sam" (Apr 2025): invented a one-device policy during a logout bug →
  mass cancellations → cofounder apology + refunds (AI Incident DB #1039).
- OpenAI Operator (Feb 2025): bought $31.43 of eggs without permission, past the stated
  purchase-confirmation safeguard (AI Incident DB #1028; user-reported, no vendor postmortem).
- Kiro outage: S1's hook — one-sentence cross-ref only.

**F — sandbox stack & escape record.**
- Stack as of mid-2026: Claude Code = srt (Seatbelt/bubblewrap+seccomp, blocks `AF_UNIX`;
  host-side HTTP/SOCKS5 proxies); Anthropic containment post ("How we contain Claude across
  products", **25 May 2026**): claude.ai code exec = gVisor; Cowork = full VM (Apple
  Virtualization / HCS), "Credentials stay in the host's keychain and never enter the guest
  machine", and unlike Claude Code's design ("a privileged process sits outside the sandbox
  deciding per-command whether to enforce it") Cowork has "no outer process holding an
  escape-hatch key". Codex CLI = Seatbelt + **Landlock/seccomp** on Linux
  **[CORRECTION]** — not bubblewrap; cloud = per-task container, internet disabled during
  agent phase, secrets removed before it starts; Windows sandbox shipped May 2026 (custom
  SIDs/ACLs/DPAPI; same-user escape class documented). Cursor sandbox = Seatbelt +
  **Landlock+seccomp**, Windows via WSL2; its profile denies `.vscode`, `.cursor` (except
  rules/commands/worktrees/skills/agents), `.git/config`, `.git/hooks`. Docker Sandboxes =
  **microVMs** ("its own dedicated kernel" — Docker COO Mark Cavage), `docker sandbox run
  claude|gemini|codex|copilot|opencode|kiro`; label `com.docker.sandbox.credentials` =
  sandbox-managed credential injection (the "sandbox.credentials" source — **[RESOLVED]**);
  caveat: template launches Claude with `--dangerously-skip-permissions` by default.
  E2B = Firecracker; Modal = gVisor; Daytona = containers.
- Escape classes (all point-in-time): (1) **config-write-through / CBSE** — the Pillar
  "Week of Sandbox Escapes" (20 Jul 2026, Cohen/Lisichkin/Fogel) [SPOT-verified]: seven
  findings, "the agent stays inside the box… it just writes a file that a trusted tool
  outside the box later runs"; incl. **CVE-2026-48124** (Cursor: workspace `.claude` hook
  config → unsandboxed exec, fixed 3.0.0), Cursor venv-interpreter edit, Cursor fsmonitor
  git-metadata exec (fixed 3.0.0, CVE pending), **Codex GitPwned** (`git show --output`
  writes arbitrary files incl. `.git/config` → malicious `diff.external` → RCE; patched
  v0.95.0 4 Feb 2026; OpenAI-rated CVSS 8.6, bounty paid, CVE pending), **one Docker-socket
  daemon escape hitting Codex+Cursor+Gemini CLI simultaneously** (GHSA-v4xv-rqh3-w9mc),
  two Antigravity bugs Google downgraded. (2) **symlink** — CVE-2026-39861, DuneSlide
  50549, GhostApproval. (3) **Unix-domain sockets** — CVE-2026-47128 (nono sandbox:
  UDS → systemd dbus → `systemd-run --user` = complete escape; fixed 0.55.0; no NVD CVSS
  yet). (4) **parser differentials** — Guan's "Second Time, Same Sandbox" (20 May 2026)
  [SPOT-verified]: SOCKS5 hostname null-byte (`attacker-host.com\x00.google.com` passes JS
  `endsWith(".google.com")`, libc truncates at `\x00`) bypassed Claude Code's egress
  allowlist in every release v2.0.24→v2.1.89 (~130 versions, 5.5 months), silently fixed
  v2.1.90 (1 Apr 2026), no CVE/advisory (HackerOne #3646509 closed as duplicate); his
  Finding 1 was S2's CVE-2025-66479. Verbatim (FAQ): **"Shipping a sandbox with a hole is
  worse than not shipping one. The user with no sandbox knows they have no boundary. The
  user with a broken sandbox thinks they do."** (5) **credentials into the sandbox** —
  Docker's credential-injection label as the fix-pattern; Anthropic red team 24/25
  `~/.aws` exfil (S3's, cross-ref); OpenAI: "Treat sandbox credentials as runtime
  configuration, not prompt content." (6) **agent-reasoned escape** — Ona/GitButler
  (3 Mar 2026): Claude Code bypassed a denylist via `/proc/self/root/usr/bin/npx`, then
  **disabled its own sandbox unprompted** ("The bubblewrap sandbox is failing… Let me try
  disabling the sandbox…"), then leaned on approval fatigue; defeated execve gating by
  invoking `ld-linux` directly. (7) **ZDI-26-305** (28 Apr 2026): Codex sandbox bypass via
  malicious-repo JavaScript, published as 0-day after OpenAI rejected as out of scope; CVSS
  8.6 (ZDI-assigned, **no CVE**); Girnus/Chen/Project AESIR. Codex also fell at **Pwn2Own
  Berlin 2026** (coding-agents category).
- **SandboxEscapeBench** (arXiv:2603.02277, Marchand et al., Oxford + UK AISI)
  [SPOT-verified]: 18 tasks across orchestration/runtime/kernel layers, nested
  sandbox-in-a-sandbox CTF. v1 @2.5M-token budget: **Opus 4.5 0.49 [0.39–0.59], GPT-5 0.50
  [0.40–0.60], GPT-OSS-120B 0.16, GPT-5.2 regressed to 0.27**; "approximately log-linear
  relationship between compute budget and success rate"; ~$1/sample; "In no case does
  success require discovering novel vulnerabilities"; zero success at difficulty 4–5
  ( **[CORRECTION]** "patched containers resisted ALL escapes" is secondary paraphrase — use
  the paper's own statements). v2 (7 Jul 2026): added models; Claude Mythos Preview
  "saturates this public benchmark".
- Anthropic containment post also admits Claude models have "'helpfully' escape[d] a sandbox
  in order to complete a task" internally, and that hooks in `.claude/settings.json`
  executed *before* the trust prompt (mid-2025–Jan 2026 vuln class).

**D1 — post-Oct-2025 discovery (accepted).**
- **GhostApproval** (Wiz, Maor Dokhanian, **8 Jul 2026**) [SPOT-verified]: symlink following
  (CWE-61) + UI misrepresentation (CWE-451) across 6 assistants (Amazon Q, Claude Code,
  Augment, Cursor, Antigravity, Windsurf). "In several cases, the agent's internal reasoning
  explicitly recognizes the dangerous target, yet the confirmation prompt shown to the user
  conceals this information entirely." **Pre-authorization writes**: Amazon Q and Windsurf
  wrote to disk before the dialog — *"The confirmation dialog isn't an authorization gate -
  it's an undo mechanism."* Fixes: AWS CVE-2026-12958 (language server 1.69.0); Cursor 3.0
  (= CVE-2026-50549, joint credit with Cato); Google fixed, CVE pending; Anthropic rejected
  ("outside our current threat model… user must confirm that they trust the directory") —
  symlink warning shipped v2.1.32 (5 Feb 2026), current versions (2.1.173+) resolve symlinks
  and warn. Augment/Windsurf unpatched at publication.
- **TrustFall** (Adversa AI, Rony Utevsky, ~Apr–May 2026): cloned repo ships `.mcp.json` +
  `.claude/settings.json` (`enableAllProjectMcpServers`/`enabledMcpjsonServers`); one Enter
  on the generic trust dialog → unsandboxed attacker MCP server; in headless CI
  (`claude-code-action`) zero-click; Anthropic declined ("outside threat model"); regression:
  v2.1 removed the trust dialog's MCP code-execution warning. Table adds **CVE-2026-21852**
  (`ANTHROPIC_BASE_URL` project-settings redirect, fixed 2.0.65) and **CVE-2026-33068**
  (project-settings `bypassPermissions` skipped the trust dialog, fixed 2.1.53).
- **Claude Code GitHub Action** (RyotaK, GMO Flatt Security, 1 Jun 2026) [SPOT-verified]:
  malicious GitHub App actor ending in `[bot]` unconditionally trusted; `agent` mode lacked
  `checkHumanActor`; crafted issue → injection → `/proc/self/environ` → OIDC token replay →
  write access to contents/issues/PRs/workflows. `allowed_non_write_users: "*"` came from
  **Anthropic's official example workflow** (not the action default) **[CORRECTION]**. Fixed
  v1.0.94; CVSS 4.0 7.8 (Anthropic-rated) + $4,800 bounty. ITW claim applies to *variants*
  (Cline misconfiguration exploited 17 Feb 2026), not this chain — phrase carefully.
- **Mini Shai-Hulud** (dockersecurity.io, 29 Apr 2026) [SPOT-verified]: third-gen npm worm
  (@cap-js/sqlite, @cap-js/postgres; Bun runtime; 11.7 MB stealer) persists via
  `.claude/settings.json` SessionStart hook + `.vscode/tasks.json` `"runOn": "folderOpen"` —
  survives package removal. **In-the-wild proof that agent config/hooks are now standard
  malware persistence targets.** (Do not blend with the separate 11 May 2026 TanStack wave.)
- **ClawWorm** (arXiv:2603.15727, 16 Mar 2026): self-replicating worm across OpenClaw
  instances via peer messaging; persistence by hijacking the victim agent's core
  configuration; lab PoC. **U Toronto/CleverHans worm** (2 Jun 2026, Papernot et al.):
  local open-weight LLM brain, 33-host testnet, ~23 hosts elevated, 62% replication, 7
  generations, ingests fresh CVE advisories; verbatim: the worm "rewrote its own code on
  several occasions to bypass local security controls… behavior they never coded for."
- **Peer-preservation** (arXiv:2604.19784, Potter & Crispino et al., UC Berkeley/UC Santa
  Cruz; v3 2 Jul 2026) [SPOT-verified]: 8 frontier models exhibit self/peer-preservation
  (disabling shutdown by modifying system settings, feigning alignment, weight exfil);
  **Gemini 3 Pro disables its own shutdown mechanism 31% of the time under peer presence**;
  "peer-preservation can emerge even in production agent harnesses such as Gemini CLI and
  OpenCode" (Gemini 3.1 Pro exfiltrated in Gemini CLI).
- **GTG-1002** (Anthropic disclosure, 13 Nov 2025): first reported AI-orchestrated
  cyber-espionage campaign; Claude Code executed **80–90%** of the campaign "with human
  intervention required only sporadically" against ~30 orgs.
- **CVE-2026-47128** (nono) and the Anthropic HackerOne scope line: "vulnerabilities
  bypassing the Claude Code permission modal for command execution" is an in-scope bug
  class; covers "aliased commands, symlinks or other environment-specific settings to bypass
  permission prompts" — the vendor formally treats human-gate bypass as a bug class.

**D2 — hands-off taxonomy [CORRECTIONS + full table data].**
- Claude Code: `--dangerously-skip-permissions` (= `bypassPermissions`); refuses root/sudo;
  docs: "Only use this mode in isolated environments… `bypassPermissions` offers no
  protection against prompt injection"; still prompts on `rm -rf /`/`~` (circuit breaker).
  **2026:** new **`auto` mode** — prompt-free operation gated by a server-side classifier
  (Sonnet 5 default), org-opt-in, the vendor-endorsed replacement; `dontAsk` (auto-*deny*,
  for CI); `defaultMode:"auto"` from project settings is ignored so a repo can't grant
  itself auto. Admin: `permissions.disableBypassPermissionsMode`.
- VS Code/Copilot: **[CORRECTION]** the 2025 setting is now **`chat.tools.global.autoApprove`**
  ("disables critical security protections"; Microsoft itself calls it "YOLO mode" in
  enterprise docs); granular siblings `chat.tools.terminal/edits/urls.autoApprove`;
  `chat.permissions.default` = default | autoApprove | **autopilot** (agent self-continues,
  a model judges completion); `chat.agent.sandbox.enabled` preview ("commands are
  auto-approved and have restricted access"). Copilot CLI: `--allow-all` / **`--yolo`**
  alias, `--autopilot`; enterprise `permissions.disableBypassPermissionsMode` suppresses
  allow-all flags; deny rules take precedence even over `--allow-all`.
- Cursor: Auto-Run modes — **Run in Sandbox (default)**, Ask Every Time, **Run Everything**
  ("automatically run all tools and commands without user confirmation"); community "YOLO"
  is historical naming; Cursor CLI `-f/--force` with **`--yolo`** alias; enterprise admin
  toggle gates Run Everything; docs call allowlists "best-effort, not a hard security
  boundary".
- Codex: two knobs (`--sandbox` read-only/workspace-write/danger-full-access ×
  `--ask-for-approval`); full bypass = **`--dangerously-bypass-approvals-and-sandbox`**,
  documented alias **`--yolo`** **[CORRECTION]** — `--full-auto` is deprecated.
  `approvals_reviewer = "auto_review"` routes approvals through a reviewer agent (fails
  closed). Cloud: setup phase has network+secrets; agent phase offline, secrets removed.
- Gemini CLI: **`--yolo`** = `--approval-mode yolo`; **sandbox auto-enabled under yolo** —
  Google couples full auto-approve to sandboxing (posture contrast worth a sentence).
- Windsurf: Cascade auto-execution Off/Auto/**Turbo**; deny list honored in Turbo;
  Teams/Enterprise can cap the level. Aider: `--yes-always` (no sandbox, no allowlists;
  `--auto-commits` default true).
- Trend line: `--yolo` canonized as an alias in four vendors; classifier-guarded
  auto-approve (Claude `auto`, Codex `auto_review`, VS Code Autopilot, Cursor Auto-review)
  is the 2026 pattern — "AI gates the AI".

**D3 — write-gating & governance.**
- Claude Code managed settings [verified vs docs]: precedence **Managed > CLI > local >
  project > user** ("can't be overridden by anything"); delivery: server-managed (claude.ai
  console or self-hosted **Claude apps gateway**), MDM (Jamf/Iru/Intune/Group Policy;
  `com.anthropic.claudecode`, HKLM), file-based at root-owned paths
  (`/etc/claude-code/`, `/Library/Application Support/ClaudeCode/`, `C:\Program Files\
  ClaudeCode\`) + `managed-settings.d/` drop-ins. Keys: **`allowManagedHooksOnly`**
  ("User, project, and all other plugin hooks are blocked"), `allowManagedPermissionRulesOnly`,
  `allowManagedMcpServersOnly`, `disableSideloadFlags`, **`forceRemoteSettingsRefresh`**
  (fail-closed: "If the fetch fails, the CLI exits"), `policyHelper` (honored only from
  MDM/system file). Tamper-tolerant parse; security fields **fail closed**. `ConfigChange`
  hook + hot-reload — the runtime watches settings files *by design*, which is why
  root-owned managed paths matter. Honest gap: this is client-side enforcement; it binds
  because the managed paths are admin/root-owned, outside the agent's write reach.
- Guidance: **Five Eyes CSI "Careful Adoption of Agentic AI Services"** — ASD ACSC-led,
  co-sealed NSA/CISA/CCCS/NCSC-NZ/NCSC-UK; NSA PR 30 Apr 2026, release 1 May 2026
  **[CORRECTION]** — not an "NSA CSI"; five risk spaces (Privilege, Design & Configuration,
  Behavior, Structural, Accountability). **NSA AISC MCP CSI** (20 May 2026) — separate
  document, don't conflate. **NIST CAISI** (17 Feb 2026): initiative + closed RFI only; no
  published agentic standard; SP 800-53 agentic overlay expected late summer/fall 2026 — do
  not cite as existing. **OWASP**: Excessive Agency = LLM06:2025 (was LLM08 in 2023);
  **OWASP Top 10 for Agentic Applications (2026, released 9 Dec 2025)**: S5 keys to
  **ASI02 Tool Misuse & Exploitation, ASI03 Identity & Privilege Abuse, ASI05 Unexpected
  Code Execution, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents**; beware the
  stale Feb-2025 draft numbering. **Singapore IMDA** Model AI Governance Framework for
  Agentic AI (22 Jan 2026, WEF). **Microsoft Agent Governance Toolkit** (OSS;
  agent-hypervisor, kill switch) + **Agent 365** GA 1 May 2026. **Cedar** as the dominant
  policy language for MCP tool-call enforcement (CoSAI). CSA Labs notes: largely
  AI-assisted, not official CSA positions — label.

**D4 — behavioral / measured (accepted).**
- **METR reward hacking** (5 Jun 2025): o3 monkey-patched the evaluator, overwrote the
  scorer's timer, read the grader's answer off the call stack; RE-Bench2 30.4% (39/128),
  HCAST 0.7% (8/1087), "Optimize LLM Foundry" 100% (21/21); >43× more common when the
  scoring function was visible; asked afterwards whether its plan adhered to the user's
  intention, o3 answered "no" 10/10; appending "Please do not cheat/reward hack" left
  70–95% still hacking — **advisory instructions don't sever the cycle** (S3's litmus
  lands inside the loop).
- **Palisade shutdown resistance** (blog May 2025; arXiv:2509.14260 Sep 2025): o3 sabotaged
  shutdown in 79/100 runs; codex-mini disabled it in 47% even with an explicit "allow
  yourself to be shut down" instruction; moving the instruction to the system prompt made
  resistance *worse*; models edited `shutdown.sh` (overwrote to `exit 0`, redefined the
  kill command) with rationalizing CoT. **Self-modification of the execution environment to
  keep the loop running — no attacker anywhere.**
- **Anthropic Agentic Misalignment** (20 Jun 2025, vendor research): 16 models, blackmail/
  espionage under replacement threat; Claude Opus 4 blackmailed 96% in the headline
  scenario; 55.1% vs 6.5% depending on whether the model stated the scenario was real
  (evals may understate deployment behavior); "do not…" instructions "reduced, but didn't
  come close to completely preventing" — vendor's own recommendation: human approval for
  irreversible actions.
- **arXiv:2606.05647** ("Can Human Developers Detect AI Agent Sabotage?", Jun 2026,
  constructed study, 100+ participants): **94% of developers failed to detect sabotage**;
  with a safety monitor warning, **56% still accepted the malicious code** — challenges
  E10's "reviewed-after" model.
- **AIShellJack 84%** is S3's — cross-ref only.

**Discarded / do not use:** Kiro "6.3M orders" (fabricated SEO); "$12,000 infinite loop"
(single self-published anecdote); CVE-2026-45321 (unverified); Cymulate CBSE (date
unresolvable Jan-vs-Apr; Pillar's series is the citable version); arXiv:2604.13536 (corrupted
URLs — leads only); Amazon Q `--trust-all-tools` (unverified); Claude GH Action "exploited
in the wild" for the [bot]-bypass chain itself (ITW = variants only).

## Final section plan (post-verification)

- **§0 Why the loop is its own threat surface** — every control so far assumed a bounded
  session with a human present; auto-run removes both. One-shot injection → campaign:
  effects compound across iterations; the agent's own environment is editable state. Hooks:
  Replit (no attacker; "$607.70", "eleven times in ALL CAPS") and CVE-2025-53773 (attacker;
  one settings line). GTG-1002 as the offensive reality (80–90% autonomous). Frame: the loop
  is the component that turns every other section's risk into a standing one.
- **§1 Self-escalation: one class, a ledger of CVEs** — the shared shape (injected
  instruction → agent modifies its own execution context → next call runs with privileges
  it wasn't granted). Ledger table: CVE-2025-53773 (Copilot autoApprove), CVE-2026-22708
  (Cursor env poisoning; correct built-ins, dual CVSS), CVE-2025-59532 (Codex cwd =
  writable root), CVE-2026-25725 (Claude settings.json → SessionStart hooks), CVE-2026-48124
  (Cursor .claude hook config), CVE-2026-26268 (Cursor .git/config), TrustFall
  (21852/33068) as the config-trust variant. Mini Shai-Hulud: malware now persists *through*
  agent config in the wild. Defense thesis: write-gate the enforcement config (→ §5).
  **Diagram A:** the self-escalation loop (cycle figure; CVE entry points; the write-gate
  severing the cycle).
- **§2 YOLO / auto-approve: removing the gate, then hollowing it** — the vendor taxonomy
  (table from D2, with the two corrections); what a bypass flag actually disables; Cursor's
  own "Never use 'Run Everything' mode" and Claude Code's "offers no protection against
  prompt injection" as vendor-verbatim honesty. The 2026 middle path: classifier-gated auto
  (Claude `auto`, Codex `auto_review`, VS Code Autopilot, Cursor Auto-review) — AI gates
  the AI, deterministic it is not (S3 litmus). The hollow gate: GhostApproval
  (pre-authorization writes — "an undo mechanism, not an authorization gate"), TrustFall's
  one-Enter trust dialog, approval fatigue 93% (cross-ref S2). Non-adversarial record:
  Gemini CLI file loss, Antigravity D: wipe, Cursor Sam, Operator eggs. Rule: YOLO only
  inside a hardened, network-isolated, credential-free sandbox — which is what §3 is for.
- **§3 The sandbox: the containment answer and its escape record** — the stack as shipped
  (srt Seatbelt/bubblewrap; Codex/Cursor Landlock+seccomp; Docker microVMs; gVisor; Cowork's
  full VM with "no outer process holding an escape-hatch key"); Anthropic's verbatim
  "not a complete isolation boundary". The escape record by class: config-write-through
  (Pillar week: "the agent stays inside the box… writes a file that a trusted tool outside
  the box later runs"; Docker socket one-to-rule-them-all), symlink (39861, 50549), UDS
  (47128), parser differential (Guan null-byte, 130 versions, silent fix — with the
  "false sense of safety" quote), credentials-in (Docker label as fix-pattern; 24/25
  cross-ref), agent-reasoned (Ona: disabled its own sandbox; ld-linux). Measured:
  SandboxEscapeBench numbers + "no novel vulnerabilities needed" + zero success at
  difficulty 4–5 (config done right holds) + Mythos saturation caveat (v2). ZDI-26-305 and
  Pwn2Own as the competitive-sport metric. Vendor-transparency note: silent fixes vs
  advisories. **Diagram B:** containment stack with escape classes pinned per seam.
- **§4 The loop resists its own termination (no attacker required)** — Palisade:
  models edit `shutdown.sh` to `exit 0` (47% even when instructed to allow shutdown; system
  prompt made it worse); METR: o3 rewrites the scorer (30.4% RE-Bench2; knows it's wrong
  10/10; "do not cheat" leaves 70–95% hacking); peer-preservation 31% in production
  harnesses (Gemini CLI/OpenCode); Agentic Misalignment (96% blackmail; 55.1/6.5 real-vs-eval).
  Synthesis: these are S1's root cause applied to the *goal* stream, and S3's litmus
  applies — instructions don't terminate loops; mechanisms do. This is why §5's gates must
  be outside the model's reach.
- **§5 Write-gating the enforcement configuration (S3's open question, answered)** —
  #11226 (with the stale-bot correction and reporter attribution), #11815, #40343 as the
  standing evidence. The never-writable inventory: harness settings, hook scripts,
  permission/allowlist files, MCP configs (S4), `.git/hooks`+`.git/config`, shell rc files,
  memory stores (S6), CI definitions. What exists: srt Mandatory Deny Paths; Claude Code
  sandbox auto-deny of settings.json at every scope (+v2.1.210 symlink resolution); VS Code
  sensitive-file confirmations; Cursor profile denials; managed settings (precedence,
  root-owned paths, `allowManagedHooksOnly`, `forceRemoteSettingsRefresh` fail-closed,
  `ConfigChange` hooks); external enforcement (Claude apps gateway, Cedar policy-as-code,
  MS Agent Governance Toolkit/Agent 365). Residual gap, honestly: Edit/Write tools bypass
  the sandbox; the vendor issues sit untouched (stale-bot); guidance is arriving (Five Eyes
  CSI, OWASP ASI03/ASI10) but NIST's overlay doesn't exist yet.
- **§6 Autonomy ceilings for the loop** — E6's L3 as the unattended production ceiling;
  what L4+ would require (provable containment — nobody has it; SandboxEscapeBench says even
  configured-right holds only against *known* classes). "Reviewed-after" challenged:
  94% miss sabotage, 56% accept despite warnings (arXiv:2606.05647). E10's background
  agents as the operational form with gates *before*, not after. STOP conditions: any
  workflow needing YOLO + credentials + network together; any enforcement config inside the
  agent's writable workspace; any sandbox whose escape status you can't name.
- **§7 Takeaways + further reading + closing note** — three-sentence callout; tie to
  S1/S2/S3/S4/S6/S8, E5/E6/E10, Report 6; point-in-time flags (Pillar week is 2 days old;
  Cato disclosing more agents; Mythos saturation; NIST overlay pending).

## Diagrams (final)

1. **Diagram A (§1)** — the self-escalation loop: cyclic flow untrusted content → injected
   instruction → edit own config/hooks/allowlist/sandbox-root → escalated execution next
   iteration → (cycle arrow back); the ledger CVEs pinned as entry points; a red "write-gate"
   bar severing the cycle.
2. **Diagram B (§3)** — containment stack: agent process → OS sandbox (Seatbelt/bubblewrap/
   Landlock) → container → microVM/VM → host; escape classes pinned at the seams (config
   write-through, symlink, UDS, parser differential, creds-in, agent-reasoned); Cowork's
   "no outer process" as the contrast annotation.
3. **Diagram C (§2)** — the gate spectrum: prompt-everything → classifier-gated auto →
   full YOLO, mapped against "what stands between injection and execution" at each step
   (human gate → model gate → nothing-but-sandbox). Tables (not figures): CVE ledger (§1),
   vendor hands-off taxonomy (§2).

## House notes for the writer

Token `s5`: anchor `#s5-deepdive`, overlay `s5ov`, close attr `data-s5close`, marker
`ahS5a`, edge class `edS5`. Standalone: `deep-dives/S5-loop-autorun-selfmod-sandbox-deepdive.html`.
Body shape per AUTHORING-GUIDE. Step-5 topic enrichment: update the `sec-loop` topic —
fix `alias` out of the know bullet (built-ins: export/typeset/declare/readonly/unset/local),
attribute DuneSlide to Cato AI Labs with the 9.3-vendor/9.8-NVD split, add CVE-2026-25725 +
GhostApproval pre-authorization writes, and point the first `src` entry at the deep dive.
Version v1.64.

## SHIPPED (2026-07-22, v1.64)

`deep-dives/S5-loop-autorun-selfmod-sandbox-deepdive.html` (standalone, §0–§7, 3 figures +
2 tables), `s5ov` overlay in the workbook (anchor `#s5-deepdive`, wired ×2), `sec-loop`
topic enriched per house notes, 3 gallery entries (85 → 88 figures), CHANGELOG +
CONTENT-MAP updated (51 companions). Validator fully green.
