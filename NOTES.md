# Working notes

Freeform scratchpad for the project. Not authoritative — the docs/ files are.
Use this for open questions, session hand-off notes, and things to check before a client meeting.

## Open questions
- (P5/E6) Exact wording of the P1–P5 rung definitions we want to commit to for the client deck.
- (T2) What DORA data can this specific client actually produce from day 0? (unknown until we see them)
- (D-scale) Keep re-confirming D1–D5 framing reads as clearly "original synthesis", not standard.

## Re-verify before any client meeting (point-in-time facts)
- Tool versions / status: verified 2026-07-15 against primary sources (Kiro GA Nov 2025,
  Spec Kit v0.11, Superpowers v5.x, BMAD v6.8, Claude Code 2026 surface) — re-verify if
  older than a month at meeting time.
- DORA: 2025 report incorporated (Rework Rate 5th metric, AI Capabilities Model); the 2026
  report is expected fall 2026 — check for it before any meeting after that.
- METR: Feb-2026 follow-up incorporated (self-flagged "very weak evidence"); watch for the
  redesigned experiment's results.
- CVEs and incident dates cited in E5/E7/E8 and M7 Security (all checked out on 2026-07-14).
- Still unverified: Superpowers "Anthropic marketplace, Jan 2026" claim (softened in E8);
  the Anthropic −17% comprehension RCT (no primary source located — softened in E7);
  Uber FlakyGuard exact numbers (attributed + re-verify flag in E6);
  Storybook MCP benchmark figures +12.8%/2.76×/−27% (no published source found 2026-07-15 —
  reframed as unquantified vendor claim in M6 notes, D3 topic and the D1 deep dive);
  Meta Astryx details (13k apps, component counts — vendor press coverage only, flagged in D1).
- Verified 2026-07-15 for I1 (primary sources): Ahrefs llms.txt study (137,210 domains, 97%
  zero traffic May 2026, 1.1% AI-retrieval fetches — point-in-time, re-verify), AGENTS.md
  stewardship (Agentic AI Foundation / Linux Foundation; "60k+ repos" self-reported,
  fast-moving), Anthropic memory tool GA (memory_20250818, six ops), Solmaz SimpleDoc
  (Dec 22 2025), Kiro .kiro/specs + Spec Kit .specify/memory/constitution.md layouts
  (fast-moving), Tan/Wagner/Treude 28.9%/4.7yr (top-1000 scope), Nygard ADR Nov 15 2011
  (four statuses incl. Deprecated), Cline Memory Bank six files (official docs).
- ~~I5 tension~~ RESOLVED in the I5 session (v1.30): official docs verbatim "Size: target
  under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."
  (code.claude.com/docs/en/memory) — workbook now says 200 and attributes "~300" to the
  practitioner range (HumanLayer: "&lt; 300 lines is best, and shorter is even better").
- Verified 2026-07-16 for I3 (primary sources; tool facts point-in-time): Treude & Baltes
  arXiv:2606.09090 (all numbers digit-checked), Tan arXiv:2212.01479 (28.9% = 265/918,
  4.7yr), DocPrism arXiv:2511.00215, Lulla arXiv:2601.20404 (~28.64%/~16.58%), Galster
  AIware '26 (arXiv:2602.14690, current title "Harness Engineering for Agentic AI Coding
  Tools"; the Zenodo DOI 10.5281/zenodo.19375880 we briefly noted is the COMPANION DATASET
  paper by Baltes et al. — corrected in the I5 session), DORA 2022 docs-quality lifts + DORA 2025
  "AI-accessible internal data" (official capability name), SWE-at-Google ch.10 quotes,
  Doc Detective v4.30.0 (active), Schemathesis/Specmatic (active), lychee (active),
  HCP Terraform Health Assessments. Graveyard status to re-verify before client meetings:
  Dredd archived, Optic archived 2026-01-12, driftctl maintenance since 2023-06,
  DeepDocs "deprecated", Swimm pivoted to agentic-modernization services. Fluri WCRE 2007
  97% figure: consistent across independent citations but primary PDF paywalled — not
  eyeballed. McMaster "Impressive, But Wrong": year not determinable from page.
- Verified 2026-07-15 for D1 (primary sources): Krebs slop audit numbers, NN/g State of UX 2026
  exact quote, Design2Code 49%/64% (GPT-4V-specific), DTCG 2025.10 status (CG deliverable, not
  W3C REC), CodeA11y CHI 2025, Code Connect frameworks, Frost quotes ("natural design system
  consumer" 2023; "machine-readable infrastructure" Dec 2025 — "AI is a new user" is NOT his).

- Verified 2026-07-16 for I5 (primary sources; tool facts point-in-time): Skills three levels +
  "~100 tokens per Skill" + "Under 5k tokens" + "body under 500 lines" (platform.claude.com
  docs), open standard Dec 18 2025 (agentskills.io, spec repo Apache-2.0), cross-vendor native
  SKILL.md — Codex, Copilot (changelog Dec 18 2025; paths from docs.github.com), Cursor 2.4,
  Gemini CLI, .agents/skills shared path (FAST-MOVING roster — re-verify before meetings);
  CLAUDE.md "target under 200 lines" + subdirectory on-demand + four-hop imports-load-at-launch
  + CLAUDE.local.md supported (code.claude.com/docs/en/memory); AGENTS.md nearest-file verbatim
  + AAIF stewardship + "60k+" self-reported; ETH arXiv:2602.11988 (−0.5%/−2% success,
  +20%/+23% cost — CTXBENCH-specific pair (v2 name; was misread as AGENTbench); +2.4% n.s. developer-written; 641 words/9.7 sections);
  McMillan arXiv:2605.10039 (1,650 sessions, BF10 0.05–0.10, ~5.6%/step OR 0.944);
  advanced-tool-use (Nov 24 2025: 58 tools/55K, 85% reduction, Opus 4 49%→74%, 4.5
  79.5%→88.1% — VENDOR) + code-exec-with-MCP (Nov 4 2025: 150k→2k "time and cost saving of
  98.7%" — VENDOR); HumanLayer guide (humanlayer.com, Nov 25 2025; cites arXiv:2507.11538 for
  ~150–200 instructions); matklad verbatim "2x…10x more time to figure out where"; aider
  --map-tokens 1k default ("personalized PageRank" = implementation, NOT in the 2023 post);
  Windsurf caps 6,000/12,000 chars (docs now served via docs.devin.ai post-Cognition —
  re-verify); Manus post July 18 2025; Nielsen Dec 3 2006 + Carroll & Carrithers CACM 1984;
  Ahrefs precise framing: 97% of valid llms.txt files got zero requests OF ANY KIND, AI-retrieval
  = 1.1% of the few fetches. NOT used: obra/superpowers star counts (unverifiable),
  aider 10x/10x/50x edge multipliers (secondary only).

- Verified 2026-07-16 for I7 (primary sources; tool facts point-in-time): Bird et al. ESEC/FSE
  2009 Table 1 read from the PDF (Eclipse 41.5%, Apache 49.6%, NetBeans 54.9%, OpenOffice 8.1%,
  GNOME 38.9%, AspectJ 30.6%; verbatim "In the apache project, 63% of the fixed minor bugs are
  linked, but only 15% of blocker bugs are linked"; severity trend = manually-verified projects
  only, NOT AspectJ/Eclipse_Z); Wang/Pradel/Liu arXiv:2503.15223 (ICSE 2026; 29.6% / 28.6%-of-77
  / 11.0% / 7.8% / 66.2%; inflation = 6.4 pts NOT 6.2; tool = PatchDiff); C4 "maps of your code…
  Google Maps" verbatim + L4 "very much an optional level of detail" + "most IDEs can generate
  this level of detail on demand" (c4model.com, CC BY 4.0; origin years NOT stated on-site);
  arc42 = CC BY-SA 4.0 (not CC BY), 12 sections; Structurizr mid-transition (cloud EOL →
  self-hosted open-core) — re-verify; Jira smart commits need key+command IN THE COMMIT MESSAGE
  (branch name alone does nothing) vs Linear branch-name autolink (magic words in PR title/desc,
  NOT comments); GitHub auto-close same-repo only + autolinks paid plans; GitLab push-rule regex
  Premium/Ultimate; GitHub ruleset metadata restrictions (describe as GA, no over-precise plan
  claims); matklad verbatim "the biggest difference between an occasional contributor and a core
  developer lies in the knowledge about the physical architecture of the project"; Willison
  trifecta verbatims (Jun 16 2025); Invariant Labs May 26 2025 "toxic agent flows"; General
  Analysis Supabase Jul 2025 (service_role/RLS mechanism; supabase.com/blog/defense-in-depth-mcp);
  Noma GitLost ~Jul 7 2026 ("additionally" bypass confirmed; "VP of Sales" + Agentic-Workflows
  preview date UNCORROBORATED — not used); MCP-Universe arXiv:2508.14704 §4.5 (7 servers/94
  tools: Claude-4.0-Sonnet Location Navigation 22.22%→11.11%, GPT-4.1 Browser Automation
  23.08%→15.38%) — replaces the UNPINNABLE "2–3+ MCP servers reduce accuracy" claim; Copilot↔Jira
  preview 2026-03-05 / GA 2026-06-25; Copilot commit→session-log Mar 20 2026 + session streaming
  to SIEM/Purview preview Jul 2 2026; Agent Trace = CURSOR-led v0.1.0 RFC Jan 2026 (partners Amp/
  Cognition/Cline/Cloudflare); Devin↔Linear playbook labels (docs.devin.ai); Linear changelog
  2025-08-21 (Cursor agents; "up to eight" = general Cursor capability); LinearB verbatim "In 75%
  of teams, 31% of branches are unlinked" (NOT a metric named "Branches Linked to Issues");
  Mueller "FWIW no AI system currently uses llms.txt" (Bluesky; the Illyes Search-Central-Live
  remark has NO primary transcript — report unquoted); Radar Lightweight ADRs verbatim "a record
  that remains in sync with the code itself" (Trial Nov 2016 → Adopt Nov 2017; NO "Architecture
  as code" entry found — don't assert one); census arXiv:2606.24429 = "Detecting AI Coding Agents
  in Open Source…" Khosravani & Mockus — NOT "AIDev" (AIDev = arXiv:2602.09185, the separate PR
  census compared against); 850,157 one-snapshot (3.3%/30× base) vs 886,122 cross-project total.
  NOT citeable: "~42% of GitHub issues correctly linked" (unpinnable); "Jira has its own version
  of reality" (not found); Conventional-Commits/interpret-trailers verbatims confirmed.
- New from the S3 session (2026-07-21): Mitiga Skillgate full report (in-the-wild
  instruction-file malware claim — only the teaser post existed as of 2026-07-21; confirm or
  soften before citing); sandbox.credentials (v2.1.187+) and mask mode (v2.1.199+) — fast-moving
  Claude Code surface, re-check the docs; Cursor's response to the Rules File Backdoor (only
  Pillar's side is documented — Cursor never published its own statement); the ATLAS site's
  AML.CS0041 study page 404s without JS (cite the mitre-atlas/atlas-data YAML instead);
  Snyk ToxicSkills figures (36.8% of 3,984 / 76 malicious — seen via the CSA relay only,
  not against Snyk's own report).

- New from the S4 session (2026-07-22): CVE-2026-33032 (MCPwn) patch status is contested —
  NVD lists ≤2.3.5 affected with "no publicly available patches" at publication, while
  Pluto/THN reported "fixed in 2.3.4" — re-check before citing; MCP registry GA status
  (preview since 8 Sep 2025, GA unannounced) — re-verify; Claude Code MCP allowlist bypass
  via CLI flags (issue #31508) and GitHub MCP `--read-only` ineffective under the `http`
  command (issue #2156, closed working-as-intended) — both point-in-time; "TrustFall"
  (alleged unpatched MCP flaw in Cursor CLI/Claude Code/Gemini CLI/Copilot CLI) seen only
  in vendor marketing, no primary research — do not cite without a primary source; Koi's
  "ClawHavoc" campaign (1,184 malicious agent skills) is skills-layer, not MCP — candidate
  for S3/S6 follow-up; Supabase's response post is dated 16 Sep 2025 (not July); mcp-scan
  is now Snyk Agent Scan (post-acquisition) and its CLI sends tool descriptions to Snyk's
  API — mention when recommending it.

## Next scoped initiative — DARK MODE (evaluated in v1.16, deliberately deferred)
Research backs dark mode as an **opt-in** (light stays default for a reading-heavy artifact;
NN/g + a 2025 tablet study find no fatigue win, and extended-reading legibility slightly favours
light). It was deferred in v1.16 because a *correct* build is a sizeable, higher-regression pass,
not because it lacks merit. When picking it up, do it token-first — do NOT `filter:invert()`:
1. **Tokenize the hardcoded colour.** ~34 unique hex (78 occurrences) live outside `:root` in the
   workbook `<style>` (e.g. `.gbar #DDE4EA`, `.seg #DCE3E9`, `.check #F7F9FB`, `.rc pre #10161C`,
   `.tid #EBEFFA/#D6DDF3`, the `.dmap`/`.e1ov` SVG fill classes `.fA/.fC/.fK/.fG/.fW`,
   `.bxC/.bxA/...`). Promote each to a semantic var on `:root` (`--surface`, `--surface-2`,
   `--code-bg`, `--diagram-*` …). Component CSS already mostly uses vars — this closes the gap.
2. **Add the dark block.** Redefine the token *values* under `@media (prefers-color-scheme:dark)`
   AND `:root[data-theme="dark"]` / `[data-theme="light"]` (toggle must beat the media query both
   ways). Non-pure-black surface (#121212–#1E1E1E, lighter with elevation); desaturate + lighten
   cobalt/amber/pine or they read neon. Verify body ≥4.5:1 (WCAG 2.2 AA), sanity-check with APCA
   (Lc 60–75), 3:1 for large text / UI / focus rings.
3. **Diagrams.** The 74 inline SVG `fill=/stroke=` in body markup are the ragged edge; the arrow
   `marker path` fills (#57656F) can be overridden in CSS (`svg marker path{fill:var(--…)}` beats
   the presentation attribute). The `.dmap`/`.e1ov` fill classes are already CSS — just add dark
   values. Budget for re-checking every diagram in dark.
4. **Toggle + persistence.** A header toggle (near the version button), persisted through the
   existing `store` backend (key `agentic-study-v1`, add a `theme` field) — never scatter raw
   localStorage. Set `data-theme` on `<html>` early (inline head script) to avoid a flash.
5. **×16 files.** Workbook + 15 standalones share the `<head>` tokens — script the token/dark-block
   insertion (mind the Python-apostrophe + brace-expansion build gotchas in CLAUDE.md) and re-run
   `scripts/validate.py`. Screenshot both themes at desktop + mobile before shipping.

## Session hand-off
- 2026-07-21 (S3 session): **S3 deep dive added (v1.62) — Advisory vs Deterministic Controls;
  the Rules File Backdoor.** Outline (docs/plans/2026-07-21-s3-deepdive-outline.md) → 6-agent
  swarm (4 fact clusters + 2 discovery) → 2-agent spot-verify round (catches: Anthropic's
  containment post is **25 May 2026**, not "Jun 2026" — retro-fixed in both S2 copies too;
  Check Point "Caught in the Hook" is **Feb 25** 2026; NVIDIA's AGENTS.md post is **Apr 2026**;
  GitHub issue #11226 was **closed not-planned**; arXiv:2602.11988 has **no venue**; CamoLeak
  has **no CVE** — CVE-2025-59145 in the press is the npm color-name takeover) → write →
  assemble per AUTHORING-GUIDE. Attribution fixes baked into the body: AML.CS0041 = case study
  (techniques AML.T0068/T0081/T0067); Tag-block range credited to the technique literature, not
  Pillar's prose; PoC = script injection, not exfil. Fact fix elsewhere: S8's "hooks override
  permission rules" rewritten — hooks can only tighten, never loosen (a blocking hook beats an
  allow rule; deny/ask are hook-proof), and Anthropic's own docs rank the permission system
  above hooks for a hard allow/deny. SVG lesson paid again: headless-chrome screenshots caught
  three clipped/overflowing labels across the three figures (two viewBox overflows, one
  box-border cross) — fixed identically in both copies, gallery regenerated. New re-verify
  items above (Mitiga Skillgate, sandbox.credentials, Cursor's side, ATLAS 404, Snyk via CSA).
  Validator green; nothing committed (per instruction).
- 2026-07-16 (I7 session): **I7 deep dive added (v1.38) — M4 COMPLETE (I1–I7).** Outline → 3
  teammates (i7jul16-facts-links / i7jul16-facts-mcp / i7jul16-scout) → i7jul16-spotverify on
  discovery finds (7th session in a row it paid: GitLost "VP of Sales" + preview-date dropped
  as uncorroborated; LinearB re-pinned to verbatim; Bird "every project" softened; "Jira has
  its own version of reality" NOT FOUND — excluded; Wang inflation 6.4 not 6.2). Fact fixes
  elsewhere: H3 "AIDev census" → "multi-method agent census" in both copies (AIDev
  arXiv:2602.09185 is the separate PR census that arXiv:2606.24429 compares against; verified
  the abstract myself), 30× base tightened to 850,157 one-snapshot; CONTENT-MAP companion
  count fixed 27→29 (I6 session had missed it). SVG lesson AGAIN: headless-chrome screenshot
  caught fig-1 label clipping (left edge + text under a box) — fixed in all three copies
  before commit. Full verified-facts list above. Next: M6 D2/D5, M5 B-topics, or T2.
- 2026-07-16 (I5 session): **I5 deep dive added (v1.30) — M4 at 5/7.** Outline → 3 teammates
  (2 fact-verify + 1 discovery, session-unique names) → spot-verify round on discovery finds
  (catches: matklad "bottleneck" line was a paraphrase — verbatim is "2x more time to write a
  patch… 10x more time to figure out where"; −2%/+23% is CTXBENCH-specific (v2 name), SWE-bench Lite
  is −0.5%/+20%; aider "personalized PageRank" not in the 2023 blog — attribute to the
  implementation; HumanLayer URL is humanlayer.com and its instruction-capacity source is
  arXiv:2507.11538). Seed corrections applied: L1 ~100 tokens (not ~80), body 500 lines (not
  "5k words"), 200-line official target (not ~300 — NOTES tension resolved), imports four hops
  (not five) and NOT lazy, CLAUDE.local.md not deprecated. The −2%/+23% figure finally PINNED:
  ETH Zurich arXiv:2602.11988. Fact fix elsewhere: I3 Galster reading item → arXiv:2602.14690
  + current title (Zenodo DOI was the dataset paper). Core/map/leaves framing flagged as our
  synthesis. Validator green.
- 2026-07-16 (I3 session): **I3 deep dive added (v1.26).** Outline → 3 teammates (2
  fact-verify + 1 discovery) → spot-verification on discovery sources — **4th catch**:
  scout's context-file population stats were materially wrong (real: Galster et al.
  AIware '26, 4,768 files across 2,586 of 2,853 repos, CLAUDE.md 34.4% > AGENTS.md 31.6%);
  also wolfejam post re-dated Jul **2026**, DocPrism 98%→14% is a *flag rate*, McMaster
  year undeterminable (left unstated). Fact fixes in the topic: Tan 28.9%/4.7yr pinned to
  **arXiv:2212.01479** (265/918; EMSE 2023 restates 28.9% only); DORA "2.4×" folklore
  UNPINNABLE → excluded (2022 amplification framing + published lifts used); Rios TD study
  = Rios/Mendonça-Neto/Spínola (not Seaman). Centerpiece source: Treude & Baltes
  arXiv:2606.09090 (DOCER on CLAUDE.md/AGENTS.md: stale refs in 23.0% of 356 repos;
  "without any visible error"; two-snapshot CI grep). Freshness policy flagged as
  Report-3 synthesis. **Teammate-name collision gotcha**: SendMessage to "spotverify"
  resumed the *I1-session* agent of the same name — use session-unique agent names.
  Validator green.
- 2026-07-15 (I1 session): **I1 deep dive added (v1.24) — M4 opened.** Outline → 3 teammates
  (2 fact-verify + 1 discovery) → spot-verification on discovery sources (caught a fabricated
  ".claudeignore"; two path/mechanism corrections). Load-bearing: the I1 src entry
  "Anthropic: memory typology (in-context/external/in-weights/cache)" **retired as
  unpinnable** (no primary source — third-party blogs only; replaced in src). Triad confirmed
  as Report-3 synthesis → flagged like D1–D5 (precedents: Majors durable/disposable code,
  records-management retention classes, never-hand-edit tooling conventions). I2 wording
  fixed: ADR statuses + Deprecated; feature_list.json → "JSON feature-list pattern".
  **Real bug fixed:** H2/H3/H4 *standalones* lacked `<main>` → desktop grid zigzagged content
  into the 210px TOC column (verified + fixed in-browser; overlays/mobile were fine, hence
  unnoticed). New re-verify items below. Validator green.
- 2026-07-15 (H4 session): **H4 deep dive added (v1.23) — M3 complete.** Outline → 3 teammates
  (2 fact-verify + 1 discovery) → spot-verification round on discovered sources (caught a
  misattributed ClarifyCodeBench figure — numbers kept out) → write → assemble per
  AUTHORING-GUIDE. Retired the unpinnable "30-min→3h" line in all copies; Kiro RA 60% figure
  relabelled as AWS-internal-via-The-New-Stack; reqproof quotes pinned to Bugaev May 2026.
  New re-verify items: HiL-Bench/Orchid/fix-PR/MSR-2026 arXiv preprints (point-in-time),
  Devin 2.1 confidence UX, Copilot/Codex plan-mode asking. CONTENT-MAP companion count fixed
  (15→19, had drifted since H1). Validator green.
- 2026-07-15 (design/responsive session): **v1.16 responsive & wayfinding pass.** Design skill +
  1 research teammate (2025–26 study-material/mobile/dark-mode best practice). Rendered the
  workbook at 390px → confirmed the dense SVG diagrams were squished to illegibility (the headline
  problem). Fix: JS wraps every diagram SVG in `.figwrap>.figscroll`; <760px they keep a legible
  min-width and scroll horizontally (fade + scrollbar cue), captions stay outside. Added scroll-spy
  nav highlight, top reading-progress line, back-to-top; bigger mobile tap targets; fluid `clamp()`
  headings. Mirrored diagram-fix + back-to-top into all 15 standalones. Validator green; desktop
  pixel-unchanged (min-width only engages on narrow screens). Dark mode evaluated & deferred (see
  the scoped initiative above).
- 2026-07-15 (later session): **D1 deep dive added (v1.15)** — outline → 3 research teammates
  (2 fact-verification, 1 discovery) → write → assemble per AUTHORING-GUIDE. Fact corrections
  applied workbook-wide (Storybook figures, Frost quote, CodeA11y). New sources adopted:
  Indeed/Wolosin, Meta Astryx, arXiv:2603.13036, shadcn-as-default. Validator green.
- 2026-07-15: quality-review session. 4 review agents ran (content ×2, workbook, fact-currency);
  user approved 4 improvement packages (A factual fixes, B 2026 currency, C content extensions,
  D workbook UX). Package A is ~half done (E2/E3 cross-refs, E1 Devin, E8 Böckeler, E6 Faros/
  FlakyGuard/provenance — all in both copies). Remaining: E7 −17% claim, P1 Torres numbers +
  P-scale flag, E4 ~70% flag, CONTENT-MAP id fixes; then packages B, C, D and version bump.
  **Full checkpoint with the complete remaining-work list: Claude memory file
  `improvement-rollout-checkpoint.md` (project memory dir).**
- Also done this session: `.rt`/`.chead` CSS drift fixed in all deep-dives; validate.py extended
  with a CSS-class-coverage check; dead `class="main"` removed from workbook.
- Previous: P2 deep dive added (workbook v1.10). Build recipe: docs/AUTHORING-GUIDE.md.
  Gate: `python3 scripts/validate.py` (green as of this hand-off).
