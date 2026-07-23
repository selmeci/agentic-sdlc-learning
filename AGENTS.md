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

## Everything else

For content shape, house style, the golden rules (stable topic ids, two-copies-in-sync, in-page
overlays, inline SVG, single `store` backend, validate-after-every-edit), and the authoring
recipe, follow `CLAUDE.md` and `docs/AUTHORING-GUIDE.md`. They apply to all agents.
