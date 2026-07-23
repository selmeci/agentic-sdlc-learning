## Residual Review Findings

Source: `ce-code-review` run `20260723-095012-b1011c3e` on branch `feat/section-deep-link-anchors`.
These findings were not applied as code changes. They are recorded here as durable context for the PR.

### Accepted design decisions

- **P1 — `scripts/validate.py:216` — Validator does not enforce overlay/standalone ID parity**
  The workbook keeps DOM IDs unique by prefixing overlay section IDs with the overlay token (`e2ov-s3`). A literal parity check against standalone IDs would fail because the same standalone section number (`s3`) appears in many overlays. The convention is now documented in `docs/AUTHORING-GUIDE.md` Step 3, and `validate.py` enforces global uniqueness and no collisions between overlay, module, and topic IDs.

- **P2 — `workbook/agentic-development-study.html:1046` — Overlay section IDs do not match standalone IDs / Overlay h2 IDs override standalone IDs**
  Same as above: the prefixed-id convention is intentional and documented. Standalone files remain reachable via `#s3`; the workbook uses `#<ov.id>-s3`.

- **P2 — `deep-dives/B1-bootstrap-paradox-deepdive.html:333` — Anchor-link script and CSS duplicated in every standalone deep-dive**
  Intentional under the zero-build, hand-authored HTML architecture. Each standalone file is self-contained and has no external script dependency. `validate.py` now verifies that the anchor-link affordance is present in every deep-dive file.

### Deferred to future work

- **P2 — `scripts/validate.py:216` — Validator omits generated positional ID check**
  The runtime fallback (`ov.id+'-s'+i`) produces the same string shape as the documented prefixed convention, so a dedicated rejection regex cannot distinguish the two. The validator already fails on any overlay `h2` missing an explicit `id`, which prevents reliance on the fallback generator in practice.

- **P2 — `scripts/validate.py:231` / `scripts/validate.py:226` — Validator extracts overlay bodies with regex / brittle regex parsing**
  The current regex extraction passes the full validator suite on the existing workbook. Refactoring it to use `html.parser.HTMLParser` is a worthwhile follow-up but does not change observable behavior.

- **P2 — `deep-dives/B1-bootstrap-paradox-deepdive.html:337` / `workbook/agentic-development-study.html:11965` / `workbook/agentic-development-study.html:12257` — No automated behavioral tests for anchor links / fragment routing**
  The project has no jsdom/playwright/test harness and preserves a zero-build static site. Manual browser verification was performed; adding automated browser tests would require a new testing toolchain decision.
