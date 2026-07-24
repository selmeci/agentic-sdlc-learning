# REFACTOR mechanics — restructuring an existing deep dive without changing its facts

Every rule here was learned on the 2026-07 B3 pilot (application layer + Step 1c prose
surgery, commits `8afdcf8…ef42f9c` on the application-layer branch) — including the
mistakes. The facts are the product; the refactor only changes their load order and
packaging. A refactor that loses or re-scopes a single number has failed, no matter how
much better it reads.

Work in four phases. Do not start R3 before R2's inventories exist.

## R1 — Diagnose (read-only)

1. **Structural conformance.** Does the file carry the application layer — exactly one
   `data-app-frame` box at the end of §0, one `<div data-app>` with `.decis`, worked
   example, ONE `<details class="apptest">`, `.pbbridge`? How many `data-app-stub`
   markers remain (`python3 scripts/validate.py` prints them)? Is the PB bridge still
   the generic `#pb1-deepdive` placeholder, and if so, which runbook step is the real
   landing zone (grep the PB runbooks' `.pbstep`/`.pbtpl` blocks for topic-relevant
   rows — I4's landing zone turned out to be a pre-existing `[agent memory]` matrix row
   in PB3 step C1 that nobody had wired)? When several runbooks cite the topic, pick the
   step where the reader actually *executes* the topic's procedure as the bridge target
   and mention the other links in passing — one landing zone, not a link farm.
   Also count the `.soyou` hooks: Step 1b requires one applied-consequence line per
   evidence section (B3 has 7); a file with zero has an enrichment gap the validator
   does not see — the E7 eval showed this is the easiest gap to overlook.
2. **Prose diagnosis against Step 1c.** Per evidence section, count studies cited and
   numbers per paragraph. Flag every paragraph that stacks 3+ citations or ~8+ numbers
   before interpretation, and every occurrence of the tic
   `Name (authors; venue; arXiv:ID) measured: "quote"` used as a paragraph opener.
   Check each section opener: does the first sentence state the claim in plain language?
   (B3's diagnosis found ~25 studies across §1–§7, the tic firing ~10 times, and one
   paragraph carrying 12 unanchored numbers — that is the shape you are looking for.)
3. **Respect the exempt zones.** Callouts, `.io`/`.comp` card *structure*, §0 leads,
   figures, takeaways/Applying-it, and `soyou` hooks already read as argument — leave
   them alone unless a specific finding says otherwise. The disease lives in the
   evidence-body paragraphs.
4. **Rank targets** high / medium / leave-alone, with line numbers, and estimate the
   cost honestly: good prose runs +15–20% longer on touched paragraphs. Targeted
   surgery on the worst ~30%, never a whole-file rewrite — a bulk rewrite is
   unreviewable and multiplies fact-loss risk.

## R2 — Plan the surgery (inventories before prose)

1. **Fact-survival inventory, per target paragraph, written into the plan:** every
   arXiv ID, author name, venue, year, verbatim-quoted string, and numeric literal in
   the old text. This list is the contract the rewrite must satisfy. (The B3 fix wave
   shipped a paragraph that silently dropped a paper title — caught only because a
   reviewer diffed the inventory.)
2. **Anchor design with population discipline.** Every number gets a comparison,
   ratio, or consequence *that describes what the number actually measures* — check
   the denominator before writing the anchor. A mutation score is a whole-corpus rate;
   anchoring it as "faults caught in the covered third" is a factual error dressed as
   clarity, and it is exactly the mistake a fluent rewrite makes. When two numbers
   come from different measurement scopes (single subject vs corpus average), never
   compute a single delta across them.
3. **Apparatus demotion with a landing check.** Citation parentheticals move AFTER the
   point lands; full paper titles move to Further reading — but VERIFY the Further
   reading entry actually carries the title before deleting it from the paragraph
   (B3's did not; the "it lives in Further reading" premise was false for that paper).
   Keep publication-status qualifiers ("accepted at", "preprint") — they are evidence-
   class information, not filler.
4. **Structure invariants.** No new `<h2>` (absorb in place — new sections mean id and
   TOC bookkeeping across both copies); ids are frozen, display text only; exactly one
   `<details>` per data-app container and no nested `<div>` inside the frame box (the
   validator's region logic depends on both); new CSS classes need a per-file CSS
   block (`check_css_class_coverage` fails otherwise).
5. **TOC label trap.** If a heading's display text changes, the standalone TOC label
   changes too — but TOC labels are abbreviated (`<b>N</b> · Label`), the separator is
   a RAW `·` (U+00B7) in most files and the `&middot;` entity in a few, so never match
   by full heading text: locate the TOC anchor by section id and rewrite only its
   trailing label. Assert exactly one replacement happened — a silent `.replace()`
   no-op once shipped 41 files with renamed headings and untouched TOCs while its
   report claimed success.

## R3 — Execute

- Both copies get the identical edit: standalone file and the `<tok>ov` workbook
  overlay (prefixed ids; no TOC, no CSS there). After editing, compare the touched
  sections programmatically (normalize the id prefix, whitespace-fold, diff) — do not
  eyeball parity.
- The apostrophe trap: never build edits via bash-heredoc Python; use the file-editing
  tools.
- `python3 scripts/validate.py` after every file. Green before moving on.

## R4 — Review loop (fresh eyes, evidence over reports)

1. **Fact-survival audit by a fresh reviewer** working from the diff: for each changed
   line pair, extract every identifier/quote/number from the OLD line and verify it in
   the NEW line (or verify the claimed relocation actually exists in the file). Quotes
   must remain verbatim inside quotation marks. Tag-sequence diff old vs new — no
   markup added or removed unless the plan said so.
2. **Anchor-correctness check** as its own pass: does each new anchor describe the
   number's real population/denominator/condition?
3. **Review by execution.** When any claim is "the script/tool now does X", the
   reviewer RUNS it against real inputs instead of reading it — this caught a
   generator whose committed regex crashed on 37 of 41 real files while the shipped
   content looked perfect (it had been produced by a different, uncommitted one-off).
   Reports are unverified claims; reviewers grep, count, execute.
4. **Fix → re-review with the same reviewer** until both verdicts are clean. Then a
   visual check: headless-chrome screenshots of the changed sections (fragment
   scrolling is unreliable headless — extract the section into a scratch page reusing
   the file's own `<head>` for a targeted shot).
5. **No version bump** and no CHANGELOG entry unless the user explicitly ordered it in
   this conversation.

## Exemplars

- Target shape: `deep-dives/B3-mutation-testing-gate-deepdive.html` end to end.
- Before/after of the two canonical surgeries (§2 back-to-back abstracts, §6 the
  12-number paragraph): git history of that file, commits `61ec638` and `ef42f9c`.
- The playbook's corrections & do-not-cite register applies to every fact you touch —
  a refactor is the moment mis-citations get caught or cemented.
