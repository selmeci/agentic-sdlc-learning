---
name: deepdive
description: Author or enrich a deep-dive companion for the study workbook — the full research → write → build → review pipeline. Use this whenever the user asks to create a new deep dive, add a section/topic companion (e.g. "priprav S8", "add the next deep dive", "pokracujme v priprave studijnych materialov pre sekciu X"), enrich an existing deep dive's application-layer stubs, or do prose surgery on evidence sections. Also use it when the user asks to "verify facts via swarm/teammates" for study content — fact verification for this repo runs through this pipeline, not ad hoc.
---

# Deep-dive authoring pipeline

You are orchestrating the authoring of a deep-dive companion. The full process contract
is `docs/DEEPDIVE-PLAYBOOK.md` — **read it first, completely**. Mechanical file recipes
are `docs/AUTHORING-GUIDE.md` (Steps 1–7; 1b application layer; 1c prose rules). This
skill tells you how to run the pipeline as an orchestrator; the playbook tells you what
each phase demands.

## Mode selection

- **NEW** (a topic with no deep dive yet): all four playbook phases.
- **ENRICH** (an existing skeleton with `data-app-stub` markers, or prose surgery):
  Phase 1 in reduced form (verify only newly added facts; diagnose the prose against
  Step 1c), then Phases 2–4. Check the stub count first:
  `python3 scripts/validate.py` prints which files still carry stubs.

## Orchestration sequence

1. **Setup.** Confirm the working directory (if the session is in a worktree, every
   subagent gets the worktree path explicitly — even read-only ones). Read the
   playbook, AUTHORING-GUIDE, `docs/WORKED-EXAMPLE-CLIENT.md`, and for ENRICH the
   target file's current state. B3 (`deep-dives/B3-mutation-testing-gate-deepdive.html`)
   is the finished exemplar — read its Applying-it section before writing one.
2. **Phase 1 — research.** Draft the outline + candidate-fact table yourself, then fan
   out verification teammates per the playbook's roles (refute-mode verifiers per claim
   cluster + one divergent scout). Check every fact against the playbook's
   corrections & do-not-cite register. Do not start writing until the fact table has a
   verdict per fact.
3. **Phase 2 — writing.** One writer (you or a single subagent) produces the shared
   body from the fact table: shape per Step 1, application layer per Step 1b (decision
   frame first), prose per Step 1c. Meridian worked example must not contradict the
   canon file; extend the canon first if a new standing fact is needed.
4. **Phase 3 — build.** Steps 2–7 of the AUTHORING-GUIDE: standalone + workbook overlay
   from the same body, scoped CSS/marker ids, JS handler, gallery registration.
   `python3 scripts/validate.py` after every file edit. NO version bump unless the
   user explicitly ordered it in this conversation.
5. **Phase 4 — review gates, in order:** fact-survival audit (mandatory for any edit of
   existing evidence prose), anchor-correctness check, adversarial content review
   (fresh reviewer, refute-mode), validator green with expected stub count, and a
   headless-chrome visual check of changed sections and every new SVG.
6. **Report.** Summarize: fact-table verdicts, what shipped in both copies, review
   findings and their fixes, validator + visual results. Never claim a check you did
   not run.

## Hard rules (repeated because they bite)

- Two copies in sync; never rename an existing id; English only — all enforced by
  `scripts/validate.py`, which must be green before you call anything done.
- Real-client data never enters content — Meridian is the only client in examples.
- Facts: primary source + verbatim number + population/denominator, or it doesn't ship.
- Apostrophes in bash-heredoc Python break builds — use the file-writing tool.
- Version bump and `docs/CHANGELOG.md` only on the user's explicit instruction.
