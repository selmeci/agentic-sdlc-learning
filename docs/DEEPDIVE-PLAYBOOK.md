# Deep-dive playbook — how a deep dive is researched, written, built, and reviewed

This is the tool-agnostic process guide for authoring deep-dive companions in this repo.
It applies to every agent and every tool (Claude Code teammates, Kimi swarm, or a human).
The Claude Code skill `.claude/skills/deepdive/` is a thin orchestrator over this file.
Mechanical file recipes live in `docs/AUTHORING-GUIDE.md` (Steps 1–7, 1b, 1c); this
playbook covers the *process* — what happens in which order, and why.

Two modes share the same rules:
- **NEW** — author a deep dive from scratch (all four phases).
- **ENRICH** — replace an existing skeleton's stubs with real content (Phases 2–4; Phase 1
  runs in reduced form: verify only the facts you add, plus the prose-surgery diagnosis).

---

## Phase 1 — Research (outline first, verify adversarially, then write nothing yet)

The deep dives' credibility rests on evidence discipline. Every failure we have had came
from trusting a secondhand number. The order below exists to catch those before prose
locks them in.

1. **Outline before facts.** Draft the section skeleton (§0 why → evidence sections →
   Applying it → further reading) with one-line claims per section. A claim you cannot
   state in one plain-language sentence is not ready to be researched.
2. **Pin candidate facts.** For each claim, list the facts you *believe* support it —
   with the identifier you'd cite (arXiv ID, DOI, vendor report name + year, CVE).
   No identifier = not a fact yet, just a lead.
3. **Adversarial verification fan-out.** Spawn one verifier per claim cluster with the
   explicit instruction to **refute**, not confirm: find the primary source, check the
   number against it verbatim, check the population/denominator the number describes,
   check the date and whether it was superseded. A verifier that only echoes the claim
   back has failed its job. (In Claude Code: teammates; in Kimi: swarm — same brief.)
4. **One divergent scout.** One agent searches for what the outline forgot — adjacent
   evidence, counter-evidence, and practitioner reports the outline's framing would
   never look for. Its findings are candidates, held to the same verification bar.
5. **Check the corrections register** (below) before citing anything that appears in it.
6. **Classify every surviving fact** into exactly one of:
   - **strong independent evidence** (peer-reviewed, replicated, or industry-scale data),
   - **vendor claim** (self-reported by the party that benefits — cite it labeled as such),
   - **practitioner synthesis** (experience reports, our own D1–D5-style constructions —
     always flagged as synthesis, never as an industry standard).
7. **Fast-moving tool facts** (versions, GA dates, pricing) are marked point-in-time in
   the text and expected to rot; phrase them so re-verification is easy.

Exit gate for Phase 1: a fact table (claim → source ID → verbatim number → class →
verifier verdict). Facts without a verdict do not enter Phase 2.

## Phase 2 — Writing

Follow the shape and the prose rules exactly; they are the product of measured reader
feedback, not taste:

- **Shape** (AUTHORING-GUIDE Step 1): `§0 why it matters` → evidence sections with
  `.io`/`.comp`/`.callout`/figures → `Applying it — decision guide` → further reading →
  `.closingnote`. Every topic ties back to the framework (name the E-/P-/D- topics).
- **Application layer** (Step 1b): the §0 `data-app-frame` decision box (if/then rows of
  observable client signals), and the `data-app` section — branch-aware decision guide
  (unhappy paths first), Meridian worked example (canon:
  `docs/WORKED-EXAMPLE-CLIENT.md`; fictional only, never real-client data), ONE
  `<details>` self-test with reasoned answers, PB-runbook bridge. Write the decision
  frame FIRST — it is the advance organizer the evidence sections fill.
- **Prose architecture** (Step 1c, the anti-abstract rules): assertion first — the
  paragraph opens with the claim in plain language, the citation follows as support;
  one claim per paragraph with a closing consequence; every number anchored in its
  sentence (comparison, ratio, or consequence); citation apparatus demoted to a
  parenthetical after the point lands; findings explicitly connected; written for
  experts (no re-explaining basics, no seductive-detail trivia inline).
- **Diagrams** where they carry structure words cannot: inline SVG only, wrapped in
  `<figure>` with `role="img"` + descriptive `aria-label`, unique marker id + edge class
  per SVG (`ahXNa`/`edXN`), registered in the gallery. A diagram that merely decorates
  a list is not worth its maintenance cost.
- **English only.** Every label, heading, mnemonic. `WHAT`/`WHY`, never `ČO`/`PREČO`.

## Phase 3 — Build

Mechanics per AUTHORING-GUIDE Steps 2–7. The non-negotiables:

- **Two copies stay in sync**: standalone file + workbook overlay, identical body modulo
  the `<tok>ov-` id prefix. Build both from one shared body; after any later edit,
  re-verify parity programmatically (normalize prefixes, compare).
- **Never rename an existing id** (section ids, overlay ids, topic ids, `data-step`).
- **`python3 scripts/validate.py` after every file edit.** Red = stop and fix.
- Gallery registration for every new figure; regenerate `gallery.html`.
- **Version bump only when the maintainer explicitly says so** — never as a side effect.

## Phase 4 — Review gates (in this order)

1. **Fact-survival audit** — mandatory for ANY prose edit to existing evidence text:
   extract every arXiv ID, author, venue, quote, and numeric literal from the old text
   and verify each survives (or moved to Further reading, actually present there).
   A reviewer once caught a "fixed" paragraph that silently dropped a paper title and
   misread a whole-population metric as a subset rate — this gate exists because
   plausible prose hides factual damage.
2. **Anchor-correctness check** — every number's anchor must describe what the number
   actually measures (population, denominator, condition). "18.8% mutation score" is a
   whole-corpus rate, not "faults caught in the covered third".
3. **Adversarial content review** — a fresh reviewer, instructed to refute: spec shape,
   Step 1b/1c compliance, evidence-class labels, Meridian canon consistency.
4. **Deterministic gate** — validator green, both copies, stub count as expected.
5. **Visual check** — headless-chrome screenshots of new/changed rendered sections and
   every new SVG (clipping has been caught three times this way). Fragment scrolling in
   headless Chrome is unreliable; extract the section into a scratch page with the
   file's own `<head>` when you need a targeted shot.

---

## Corrections & do-not-cite register (point-in-time: July 2026)

Hard-won corrections from past verification passes. Check before citing; when a
verifier re-confirms or overturns an entry, update it here.

**Never cite (folklore / unpinnable / third-hand):**
- DORA "2.4×" AI-productivity multiplier — folklore, never appears in a DORA report.
- Atlassian "67%", Primer "71→96", Spotify rebrand story — conference folklore.
- TestGen-LLM "1:4 / 1:20" ratios — unpinnable to the paper.
- JFreeChart cost figure — third-hand, excluded.
- Pseudo-tested code percentage as a universal number — unpinnable; report per-study.
- "2–3+ MCP servers reduce accuracy" — unpinnable; use MCP-Universe distractor data.
- GitLost "VP of Sales" anecdote and "Jira has its own version of reality" quote.

**Cite only with the correction applied:**
- CTXBENCH (not "AGENTbench") for context benchmarks.
- METR: Opus 4.6 horizon = 11.98h (not 14.5h); METR 2026 = contamination cautionary
  tale only, never a clean reversal.
- MIT NANDA: verbatim is "zero *measurable* return"; methodology is 300+/52/153
  (the 150/350 framing is a misquote).
- SpecBench: the "therefore" sentence is verbatim; the 28pp headline sits over an
  R²=0.21 fit — cite with that caveat.
- MUTGEN 53% plateau = a single blocked subject, not a corpus average.
- TCE 7.4%/5.7%/21%/5.4% = C vs Java splits — keep the language pairing.
- Tan 28.9%/4.7yr → arXiv:2212.01479 (attribution).
- arXiv:2606.24429 = multi-method census, NOT "AIDev"; AIDev = arXiv:2602.09185.
- DORA 2024 mechanism = batch-size/testing wording; throughput sign flipped in 2025.
- Swarmia has no "demotion" concept — that is Digital Apprentice (arXiv:2606.04321).
- Böckeler (not Fowler) for the pairing-with-agents material; gplint is 2024 not 2026.
- Hooks do NOT override deny rules (E5 erratum).
- GitGuardian 3.2% vs 1.5% secrets rate = vendor telemetry, label as vendor claim.
- DTCG: theming/Resolver Module NOT in stable 2025.10 — do not implement/cite as GA.
- zeroheight 56→84: 2025 report, n=294 (86% figure is 2026, n=147, only 40% have pipelines).
- Figma Variables API = Enterprise-only; native DTCG export ~Nov 2026, not GA.

---

## Roles and fan-out shape (when orchestrating agents)

- Verifiers: one per claim cluster, refute-mode, primary sources only, verdict per fact.
- Divergent scout: one, explicitly briefed to look OUTSIDE the outline.
- Writer: one (voice consistency matters); consumes the fact table, never invents facts.
- Reviewers: fact-survival auditor + adversarial content reviewer, fresh context each.
- Always give every agent the exact working directory (worktree path, not the main
  checkout) — including read-only ones: an agent anchored to the wrong checkout once
  committed there.
