# M9 Playbook module — design spec

**Date:** 2026-07-18
**Status:** approved design, pre-implementation (rev. 2: ideation-review amendments —
executable templates, assess-time baseline, feedback-loop + team-tracking backlog)
**Owner:** Roman (Sudolabs)

## Purpose

Turn the workbook's theoretical material into a practice layer the internal Sudo team can
execute at a client engagement. The layer lives **inside the existing workbook** (no new
repository, no disconnected artifacts): a new module **M9 Playbook** organised by the
engagement journey, where each topic is an interactive **runbook** that distils the existing
deep dives into concrete steps — what to do, why (linked to the theory), with copy-paste
templates and persistent checklists. Over time the templates in these runbooks become the
"harness starter kit" and the runbooks are exercised in hands-on labs — but both grow out of
the workbook, keeping every practice step traceable to the knowledge base and replicable.

**Primary audience:** the internal Sudo team learning to carry the methodology into practice
at a brownfield client.

## Decisions taken (with the user)

1. **Structure:** new module organised by the rollout journey (not per-deep-dive practice
   sections, not a separate repo). Practice follows the engagement sequence.
2. **Interactivity:** interactive checklists with progress persisted through the existing
   `store` backend, plus copy-paste template blocks with a Copy button. No free-form input
   fields, no generated reports ("engagement mode" explicitly rejected as app-creep).
3. **First increment:** module skeleton with all five topics visible, but only **PB1 Assess**
   gets the full runbook + overlay. PB2–PB5 ship as visible topics marked "in preparation"
   and follow one-per-version, the repo's established rhythm.

## Module structure and IDs

New topic ID prefix **`pb-`** — stable forever, same golden rule as all other prefixes
(add, never renumber; user progress is keyed on them).

| ID | Topic | First release (v1.47) |
|---|---|---|
| `pb-assess` | PB1 Assess — client maturity, entry gate to F0 | **full runbook + overlay** |

*(Release number note: written as v1.47 below at spec time; the parallel session shipped
D2 as v1.47 the same day, so this increment releases as **v1.48**.)*
| `pb-bootstrap` | PB2 Bootstrap — verification base (B1–B3) | visible, "in preparation" |
| `pb-harness` | PB3 Harness — CLAUDE.md, hooks, CI (E1–E5) | visible, "in preparation" |
| `pb-handoff` | PB4 Handoff — contract, EARS/Gherkin (H1–H4) | visible, "in preparation" |
| `pb-pilot` | PB5 Pilot — metrics, STOP criteria (E7, B6) | visible, "in preparation" |

PB1 exists in two copies per golden rule 2: `deep-dives/PB1-assess-runbook.html`
(standalone) + workbook overlay `#pb1-deepdive`, both generated from one shared body file
(AUTHORING-GUIDE recipe). All cross-references to theory open **in-page overlays**
(`#e6-deepdive` etc.), never relative file links (golden rule 3).

## Runbook format (new house style)

Fixed shape, parallel to the deep-dive shape, to be documented in `docs/AUTHORING-GUIDE.md`:

```
§0 when & why this step → phases with numbered steps → exit gate → next step on the journey
```

Each numbered step has four parts:

- **ČO / What** — a concrete action, imperative, executable in a day or two.
- **PREČO / Why** — 2–3 sentences plus an overlay link to the theory topic holding the
  reasoning and evidence. The runbook never restates theory; it links it.
- **ŠABLÓNA / Template** — a copy-paste block with a Copy button (questionnaire, report
  skeleton, config snippet). Where the underlying theory is deterministic, the template is
  the **real runnable artifact, not prose about it** (E5 litmus: "what must never happen" is
  deterministic — hook/permission, not advice): hook scripts, permission baselines, CI gate
  configs, lint rules. This applies above all to **PB3 Harness, whose templates ARE the
  harness starter kit installed at the client** — copy-paste is the delivery mechanism, but
  the pasted content must be an enforceable config an agent cannot talk its way around.
- **DONE** — a completion criterion, machine-verifiable where possible (E4 spirit).

Steps carry stable IDs (`pb1-s1`, `pb1-s2`, …) because checklist progress is keyed on them —
same stability rule as topic IDs.

## Interactivity & persistence

- Checkbox per step; state persists **exclusively through the single `store` backend**
  under the existing `agentic-study-v1` key (golden rule 5). Proposed shape:
  `pb: { "pb-assess": ["pb1-s1", ...] }` (array of checked step IDs per runbook).
  No raw `localStorage` / `window.storage` calls anywhere else.
- Per-runbook progress indicator (e.g. `3/8`).
- Copy buttons: one small JS helper using the Clipboard API with a
  select-and-`execCommand` fallback.
- **Deliberate limitation:** persistence lives only in the workbook overlay. The standalone
  PB1 file has visually functional checkboxes but does **not** persist, with a short note
  ("progress is saved in the workbook version"). Duplicating the store backend into
  standalone files would violate golden rule 5.

## PB1 Assess — content outline

A distillation, not new theory; every step links its source topic:

1. **Verification base** — test-suite speed/trustworthiness, CI signal an agent can read
   (E4, B1).
2. **Baseline capture** — git history, CI/CD deploy logs, incident data, cost-per-merged-PR
   (E7 day-0 DORA checklist). Collected at assess time, before anything changes: a pilot
   without a baseline can be neither proven nor disproven (METR perception gap), so it
   cannot wait for PB5.
3. **Information architecture** — are source-of-truth artifacts retrievable? (I1, I3).
4. **Governance minimum** — dev/prod separation, secrets hygiene, RBAC (E5, M7).
5. **Team readiness** — who acts as editor/curator, review capacity (P4, H4).
6. **Evaluation** — score → recommended autonomy level L1–L5 (E6) + entry gate to F0 with
   STOP criteria (B6).
7. **Assessment report template** for the client (copy block).

## Validation, versioning, documentation

- `scripts/validate.py` must pass after every edit. The existing checks cover
  `#pb1-deepdive` wiring (link + JS handler) and topic count (count updated for +5 topics).
  **New check:** uniqueness of checklist step IDs across the document.
- Version **v1.47**: prepend `.vitem` to `#verov`, update the footer current-version line,
  mirror to `docs/CHANGELOG.md`.
- `docs/ROADMAP.md`: add an M9 section with the PB2–PB5 plan (one runbook per version);
  note that the starter-kit templates and hands-on labs derive from these runbooks. Include
  two backlog notes: (1) a **field-report loop** — a completed client runbook feeds an
  anonymized results entry back into the relevant deep dive (the corpus is currently 100%
  externally cited; pilot outcomes are the first first-party evidence, and the persisted
  checklist data in `store` is the hook for it); (2) **team-level tracking** — the `store`
  backend is per-browser/per-device, so aggregating progress across a Sudo team at a client
  would need shared state; deferred deliberately (see Out of scope).
- `docs/AUTHORING-GUIDE.md`: add the runbook house style and the checklist/store recipe.

## Testing

- `scripts/validate.py` green (deterministic gate).
- Manual browser smoke test: checklist persistence (localStorage and the `window.storage`
  fallback), copy buttons, overlay navigation from PB1 to theory topics and back.

## Out of scope (explicitly)

- No new repository or build pipeline; single-file, zero-build stays.
- No input fields, client-name capture, or generated status reports (rejected option 3).
- No team-level/shared progress tracking across people (per-browser `store` stays the only
  backend in this increment; aggregation is a roadmap backlog note, not a feature — adding
  it would reopen the rejected "engagement mode" app-creep).
- No practice sections inside the 35 existing deep dives (rejected option 2); theory files
  stay untouched in this increment. Backlinks from theory to practice ("in practice → PB_n",
  the hybrid option) are deferred and may be added later per-runbook if wanted.
- PB2–PB5 runbook content (each is its own future version).
