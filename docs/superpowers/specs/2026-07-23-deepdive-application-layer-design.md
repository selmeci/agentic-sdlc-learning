# Deep-Dive Application Layer — Design

Date: 2026-07-23
Status: approved in brainstorming; awaiting written-spec review

## Problem

Deep dives (e.g. B3 Mutation Testing) read as excellent evidence briefs but weak learning
instruments. Application material exists ("Designing the gate", "Takeaways for our
engagement") but it arrives after ~5,000 words of citations, presents conclusions rather
than the reasoning that reaches them, never branches on the client actually in front of
the reader (brownfield unhappy paths), offers no rehearsal, and almost never links into
the PB runbooks (~5 `#pbN-deepdive` links across the whole corpus).

Diagnosis (from three independent perspective reviews — instructional design,
field practitioner, refactor feasibility): **the deep dives fail on placement,
branching, and rehearsal — not on content.**

## Goals (success criteria, ranked)

After reading a deep dive, the reader can:
1. **Act at a client engagement** — decide what to assess, propose, build first, and
   measure, plugged into PB1–PB5 phases. (Primary.)
2. **Apply in their own daily work** — concrete harness/workflow changes to adopt.
3. **Teach/convince others** — arguments, numbers, and demos for a skeptical CTO.

## Non-goals / invariants

- No rewrite of the evidence spine. Evidence rigor, the strong-evidence /
  vendor-claim / synthesis separation, and honesty flags are the material's moat and
  stay intact.
- No new `<h2>` sections, no changes to frozen section `id`s, no TOC anchor churn.
- No real-client (Prosight) internals anywhere — the repo is public. All worked-example
  material is strictly fictional teaching content.
- Golden rules in CLAUDE.md continue to hold (two copies in sync, overlay links only,
  single `store` backend, English only, validate after every edit).
- **No version bump during this work.** The version-history entry, footer version, and
  CHANGELOG mirror are bumped only when the user explicitly says so.

## Design

### 1. New deep-dive shape (all 48 study deep dives; PB runbooks exempt)

Three additions per deep dive, in both copies (standalone + workbook overlay):

1. **"The call you're making" box** — end of §0. A `.callframe` callout carrying
   `data-app-frame`: one sentence naming the decision this deep dive equips, plus a
   compact if/then table (3–5 rows: client signal → your move).
   This is the advance organizer; downstream evidence lands in the slots it opens.
2. **"So you…" hooks** — a one-line applied consequence appended to each evidence
   section (class `.soyou`). Added during enrichment, not the skeleton pass.
3. **"Application" section** — the existing "Takeaways for our engagement" `<h2>` is
   **absorbed in place** (same `id`, same TOC anchor; display text renamed to
   "Applying it — decision guide"). Body becomes fixed blocks inside one `data-app`
   container:
   - **Decision guide** (`.decis`) — the §0 frame expanded, branch-aware, unhappy
     paths included (e.g. "memory already exists in two tools"). The existing
     "three sentences to remember X by" closes this block.
   - **Worked example** — ~400 words on the recurring fictional client (see §2),
     the decision walked end-to-end with concrete numbers and one visible judgment
     call under ambiguity.
   - **First actions** — short sequenced week-one list.
   - **Self-test** — 3–4 scenario questions at apply/evaluate level, model answers
     behind `<details>` (no JS; works in both copies).
   - **PB bridge** — closing callout linking to the specific runbook step
     (`href="#pb[1-5]-deepdive"`), step named in text ("PB3, step 4").

### 2. Recurring worked-example client — "Meridian"

One stable fictional client reused across all worked examples so familiarity compounds.
Profile: mid-size insurer; ~25 repos / ~5 systems; mixed stack (legacy Java monolith,
two .NET services, React front end, Python data service); recurring pilot target
"PolicyCore" (policy administration) plus a CRM; developers already use AI assistants
ad hoc (unguided) so brownfield unhappy paths are the default scenario; stable cast of
2–3 named people (skeptical CTO, pragmatic lead engineer, PM).

Canon lives in **`docs/WORKED-EXAMPLE-CLIENT.md`** — single source for profile, cast,
and standing numbers. Deep dives may add topic-local numbers but must not contradict
canon. Hard rule: Meridian is a generic teaching device; no real-client internals are
ever transplanted into it.

### 3. Division of labor and two-way linking with PB runbooks

- **Deep dive owns:** why / when / how-much-to-trust — decision frame, worked
  reasoning, self-tests.
- **Runbook owns:** how — CTO talk tracks, artifact templates (ADR-for-the-bar, demo
  script, one-page findings), operational detail (CI access, operator, first-run
  duration), procedural branch tables. Assessment probes → PB1; build/gate steps →
  PB3; measurement/exit criteria → PB5 (whichever step the topic feeds).
- **Linking:** deep dive → runbook via the PB bridge (existing cross-reference
  convention; step named in text). Runbook step → deep dive via a one-line
  "Why: see B3 §8" back-link (runbooks are single-copy, so cheap).
- **Sync discipline:** when a deep dive is enriched, its procedural payload lands in
  the matching runbook step in the same commit, links wired both ways.

### 4. Deterministic enforcement — `check_application_section` in scripts/validate.py

Same shape as `check_diagram_lightbox` (~30 lines). For every study deep dive, in both
copies, require:
1. exactly one `data-app-frame` element containing at least one table/list row;
2. exactly one `data-app` container holding: a `.decis` block, at least one
   `<details>` self-test, and at least one `href="#pb[1-5]-deepdive"` link;
3. two-copy parity: marker counts in `deep-dives/` equal marker counts in workbook
   overlays.

Bookkeeping, explicit and total:
- `APP_EXEMPT` — PB1–PB5 (they are the application layer) and, if judged orientation
  rather than decision material, `SDLC-foundations`.
- `APP_PENDING` — shrinking allowlist of not-yet-enriched files so the check is green
  from day one. New deep dives are never added to it. Empty list → delete it; check
  becomes unconditional.

Boundary: the validator enforces structure (markers, blocks, links, parity). Content
quality is advisory (see §5) — the same advisory-vs-deterministic split the material
teaches (E5).

### 5. Advisory layer — where the guidance lives

- **`AGENTS.md`** (extend; create if missing): a concise "how deep dives teach"
  contract binding any authoring agent — decision frame before evidence, Meridian
  worked example, first actions, self-tests, PB bridge; evidence rigor and honesty
  flags preserved.
- **`docs/AUTHORING-GUIDE.md`**: full recipe update — section-by-section template with
  required markers, skeleton HTML/CSS, and the advisory quality checklist (Meridian
  canon consistency, "So you…" hooks, unhappy-path branch coverage).
- **`CLAUDE.md`**: one short house-style addition pointing at both.

Each rule stated once, in its right register: structure → validator; quality/intent →
AGENTS.md + AUTHORING-GUIDE.

### 6. Rollout

- **Step 1 — Foundations (one session):** WORKED-EXAMPLE-CLIENT.md; AUTHORING-GUIDE,
  AGENTS.md, CLAUDE.md updates; validator check + `APP_PENDING` (all 48 files);
  skeleton template (`.callframe`/`data-app-frame`, `data-app` blocks, `.decis`,
  `<details>` self-test, PB bridge callout) + scoped CSS.
- **Step 2 — Skeleton pass (scripted, one commit):** Python pass over the 41 files
  with the clean "Takeaways for our engagement" heading: rename display text, wrap the
  existing body in `data-app`, inject empty-but-valid block skeletons + placeholder PB
  link, insert the §0 `data-app-frame` stub, mirror into the workbook overlay
  (byte-exact wrapper swap per the known gotcha), validate after every file. Skeletons
  carry a visible "decision guide being enriched" note so a stub is never mistaken for
  finished guidance. The 7 variant-heading files are done by hand in Step 3.
- **Step 3 — Enrichment (incremental, prioritized):** per topic: real decision frame +
  decision guide, Meridian worked example, first actions, self-tests, "So you…" hooks;
  procedural payload moved into the matching PB runbook step with two-way links; one
  commit per topic; `APP_PENDING` shrinks by one. Priority: topics feeding the live
  engagement first (B-series, I4, E4, …); long tail touch-as-you-edit. Each enrichment
  is a well-scoped, parallelizable agent task.

**Definition of done:** `APP_PENDING` empty and deleted; every study deep dive reads
decision-first, rehearses on Meridian, and lands in a runbook step. Version bump only
on the user's explicit go.

## Risks & mitigations

- **Overlay byte-match fragility** during the skeleton pass → script validates after
  every file; one commit, reviewable as structure-only diff.
- **Stub mistaken for content** → visible "being enriched" note in every skeleton.
- **Canon drift in worked examples** → single canon file; advisory checklist item;
  numbers cross-checked at enrichment time.
- **Runbook bloat** → runbooks gain step-shaped material only; judgment-shaped
  material stays in deep dives.
