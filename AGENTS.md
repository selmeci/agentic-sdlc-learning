# AGENTS.md — instructions for any AI agent working in this repo

This is the cross-tool steering file (Cursor, Copilot, Codex, Gemini, Claude Code, and any
other coding agent). Claude Code additionally reads `CLAUDE.md`; the two do not conflict —
`CLAUDE.md` holds the full working guide, this file states the rules that bind **every** agent.

## Hard rule: English only

**All authored text in this repository is strictly English.** This applies to every artifact
and every agent, without exception:

- Workbook, deep dives, runbooks (`workbook/`, `deep-dives/`), presentations (`presentations/`),
  documentation (`docs/`, `*.md`), code comments, and commit messages.
- Never write in the author's or client's native language (e.g. Slovak/Czech) — **not even a
  single label, heading, or mnemonic.** Use `WHAT` / `WHY` / `Template`, never `ČO` / `PREČO` /
  `ŠABLÓNA`.
- **Allowed:** established English technical terms, and cited proper names that carry diacritics
  (e.g. *Pavlič*, *Böckeler*, *Gáspár*) — these are names, not non-English prose.
- **Exempt:** the `archive/` folder preserves the legacy Slovak original by design. Do not
  translate it and do not edit it to satisfy this rule.

### This is enforced, not just requested

`scripts/validate.py` runs `check_language_english` over the workbook and every deep dive. It
flags non-English labels and any lowercase diacritic word that is not a whitelisted English
loanword, and **fails the build**. Run it after every change:

```bash
python3 scripts/validate.py
```

A red result means stop and fix. If you add a legitimate English loanword the check does not yet
know, add it to `LOANWORDS` in `scripts/validate.py` — do not work around the check by other means.

## How deep dives teach (binds every authoring agent)

Deep dives are decision-first learning material, not literature surveys. Every study
deep dive must carry: a "call you're making" decision frame at the end of §0
(`data-app-frame`), and an "Applying it — decision guide" section (`data-app`) holding
a branch-aware decision guide, a worked example on the Meridian canon client
(`docs/WORKED-EXAMPLE-CLIENT.md` — fictional, never real-client data), an
apply-level self-test, and a PB-runbook bridge link. Evidence sections keep their
rigor and honesty flags — the application layer adds, never dilutes. Evidence PROSE
follows the anti-abstract rules of `docs/AUTHORING-GUIDE.md` Step 1c: assertion
first, one claim per paragraph with a closing consequence, every number anchored in
its sentence, citation apparatus demoted to a parenthetical after the point lands.
Structure is enforced by `check_application_section` in `scripts/validate.py`;
quality rules live in `docs/AUTHORING-GUIDE.md` Steps 1b–1c. Follow all of them.

## Everything else

For content shape, house style, the golden rules (stable topic ids, two-copies-in-sync, in-page
overlays, inline SVG, single `store` backend, validate-after-every-edit), and the authoring
recipe, follow `CLAUDE.md` and `docs/AUTHORING-GUIDE.md`. When authoring or enriching a deep
dive, the end-to-end process (research → verify → write → build → review, including the
corrections & do-not-cite register) is `docs/DEEPDIVE-PLAYBOOK.md` — it binds every agent and
tool, not just Claude Code. They apply to all agents.
