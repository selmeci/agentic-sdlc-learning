# Deep-Dive Application Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every study deep dive an application scaffold — a §0 decision frame, an absorbed "Applying it" section (decision guide, Meridian worked example, first actions, self-tests, PB bridge) — deterministically enforced by validate.py, with B3 fully enriched as the exemplar.

**Architecture:** Absorb-in-place: the existing "Takeaways for our engagement" `<h2>` keeps its frozen `id` and TOC anchor; its body is wrapped in a `data-app` container and extended with stub blocks. A scripted pass handles the 41 standard files (both copies); 7 variant files are hand-converted; B3 is enriched end-to-end as the pilot. Spec: `docs/superpowers/specs/2026-07-23-deepdive-application-layer-design.md`.

**Tech Stack:** Hand-authored single-file HTML (no build), Python 3 (`scripts/validate.py`, new `scripts/add_application_skeleton.py`), git.

## Global Constraints

- **English only** in all authored text (enforced by `check_language_english`).
- **NO version bump** anywhere in this plan: do not touch the `#verov` version modal, the footer version line, or `docs/CHANGELOG.md`. The user bumps explicitly later.
- **Two copies stay in sync:** every deep-dive edit lands in `deep-dives/<file>.html` AND its overlay in `workbook/agentic-development-study.html`.
- **Never rename an existing `id`** (section ids `sN`, overlay ids `<tok>ov-sN`, topic ids, `data-step` ids). Display text may change; ids may not.
- **No new `<h2>` sections** in retrofitted files — absorb into the existing takeaways section.
- **Run `python3 scripts/validate.py` after every file edit.** Red = stop and fix before continuing.
- **CSS class coverage:** any new class used in a file must be styled in that same file's `<style>` (`check_css_class_coverage` fails otherwise). The application CSS block (Task 2) is injected into every touched standalone and once into the workbook.
- **Apostrophe trap:** apostrophes in Python heredocs/inline strings break builds — write scripts to files with the Write tool, not bash heredocs.
- Work happens on branch `worktree-deepdive-application-layer`; commits are per-task; the PR is opened in Task 7.

## Shared vocabulary (used by every task)

**Markers (validator anchors, id-free so both copies stay textually identical):**
- `data-app-frame` — on the §0 "call you're making" callout. Exactly one per study deep dive per copy.
- `data-app` — on the container wrapping the Application-section body. Exactly one per study deep dive per copy.
- `data-app-stub` — on placeholder text inside skeleton blocks. Informational only; counted, never failed.

**New CSS classes:** `.callframe`, `.decis`, `.apptest`, `.pbbridge`, `.appstub`, `.soyou`.

**The application CSS block** (inject verbatim; uses existing house vars `--card`, `--line`):

```css
/* application layer */
.callframe{border-left-color:#B26A00}
.callframe ul{margin:8px 0 2px}
.decis{margin:12px 0}
.apptest{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:10px 0;max-width:74ch}
.apptest summary{cursor:pointer;font-weight:600}
.pbbridge{border-left-color:#2E7D5B}
.appstub{font-style:italic;opacity:.75}
.soyou{display:block;margin:10px 0 0;font-style:italic;opacity:.85;max-width:74ch}
```

**The §0 frame skeleton** (inserted immediately before `<h2 id="s1"` / `<h2 id="<tok>ov-s1"`):

```html
<div class="callout callframe" data-app-frame><b>The call you're making</b>
<ul><li class="appstub" data-app-stub>Decision frame being enriched — the if/then rows (client signal → your move) land here. Until then, see the Applying it section below.</li></ul>
</div>
```

**The Application skeleton** (wraps the existing takeaways body; `[EXISTING BODY]` = everything currently between the takeaways `<h2>` and the next `<h2>`):

```html
<div data-app>
<div class="decis">
[EXISTING BODY]
</div>
<div class="callout"><b>Worked example — Meridian.</b> <span class="appstub" data-app-stub>The end-to-end walkthrough on the recurring fictional client is added during enrichment (canon: docs/WORKED-EXAMPLE-CLIENT.md).</span></div>
<details class="apptest"><summary>Self-test — can you apply this?</summary><p class="appstub" data-app-stub>Scenario questions with model answers are added during enrichment.</p></details>
<div class="callout pbbridge"><b>Where this becomes procedure:</b> <a href="#pb1-deepdive">PB playbook</a> <span class="appstub" data-app-stub>— the exact runbook step is wired during enrichment.</span></div>
</div>
```

**Heading rename (display text only, ids untouched):** `Takeaways for our engagement` → `Applying it — decision guide` in the section `<h2>` and, in standalones, the matching TOC entry.

**Scope sets:**
- `APP_EXEMPT = {"PB1-…", "PB2-…", "PB3-…", "PB4-…", "PB5-…"}` (the five runbook files; they ARE the application layer).
- 41 scripted files: every non-PB deep dive whose takeaways `<h2>` text is exactly `Takeaways for our engagement` (includes SDLC-foundations).
- 7 hand files: `B1` (heading "Takeaways"), `B2` ("Takeaways", separate "toolbox and the exit criteria" section), `E1` (named ids — `id="takeaways"`, "Takeaways for introducing a harness"), `S4 S5 S6 S7` (fused "Takeaways &amp; further reading").

---

### Task 1: Meridian canon document

**Files:**
- Create: `docs/WORKED-EXAMPLE-CLIENT.md`

**Interfaces:**
- Produces: the canonical client profile every worked example must not contradict. Later tasks cite it as `docs/WORKED-EXAMPLE-CLIENT.md`.

- [ ] **Step 1: Write the canon file**

```markdown
# Meridian — the recurring worked-example client

Every deep-dive worked example runs on ONE stable fictional client so familiarity
compounds across the corpus. This file is the single source of truth. Deep dives may
add topic-local numbers but must never contradict what is written here. When a worked
example needs a new standing fact (a number reused by other topics), add it here first.

**Hard rule:** Meridian is a teaching device for a public repository. It is a *generic*
brownfield mid-size insurer. Never transplant real-client internals (names, repo lists,
headcounts, findings) into it.

## Profile

- **Meridian** — mid-size insurer, ~220 employees, ~40 engineers in 6 teams.
- Estate: **~25 repositories across ~5 systems**, grown over 12 years.
- Stack mix: **"PolicyCore"** policy-administration system (legacy Java 11 monolith,
  ~600k LOC), two .NET services (claims, documents), a React front end, one Python
  data/reporting service, a vendor CRM with in-house extensions.
- Delivery: trunk-ish git flow, Jenkins CI, quarterly-release habit on PolicyCore,
  weekly on the services.

## AI-tooling state (the brownfield default, not the exception)

- Developers already use **Cursor and Claude Code ad hoc, unguided** — no shared
  rules files, no memory discipline, no permission baseline. Assume artifacts
  (rules, memories, half-adopted configs) already exist and disagree.

## Verification state (standing numbers)

- PolicyCore billing module: **82% branch coverage**, no one has ever measured a
  mutation score anywhere.
- Test suite: ~14 min; **flake rate ~3%** (retry culture: "re-run until green").
- No characterization-test practice; golden files exist only in the reporting service.

## Cast

- **Dana Kovář — CTO.** Skeptical, numbers-driven; burned by a 2024 "AI pilot" that
  shipped demos and no process. Objects with metrics ("we already have 82% coverage").
- **Petr Lang — lead engineer, PolicyCore.** Pragmatic, protective of the monolith;
  adopts anything that demonstrably saves review time.
- **Mira Stone — PM, retail line.** Wants predictable delivery, asks what changes
  for requirements and acceptance.

## Usage rules

1. Worked examples name the module and the person they address (usually PolicyCore,
   Dana, or Petr) and walk ONE decision end to end with concrete numbers.
2. Show at least one judgment call under ambiguity (the reasoning, not just the verdict).
3. Numbers must be realistic and self-consistent with this file.
```

- [ ] **Step 2: Verify and commit**

Run: `python3 scripts/validate.py` — Expected: `RESULT: all checks passed.` (md files are not validated; this confirms nothing else broke.)

```bash
git add docs/WORKED-EXAMPLE-CLIENT.md
git commit -m "docs: add Meridian worked-example client canon"
```

---

### Task 2: Advisory guidance — AUTHORING-GUIDE, AGENTS.md, CLAUDE.md

**Files:**
- Modify: `docs/AUTHORING-GUIDE.md` (new section after Step 1, before Step 2)
- Modify: `AGENTS.md` (new section before "## Everything else")
- Modify: `CLAUDE.md` (one bullet in "House style for content")

**Interfaces:**
- Produces: the advisory contract (what the validator cannot check) that Tasks 4–6 and all future authoring follow.

- [ ] **Step 1: Add the application-layer recipe to AUTHORING-GUIDE.md**

Insert after the Step 1 section (after the "House rules" paragraph, before `## Step 2`):

```markdown
## Step 1b — the application layer (required in every study deep dive)

Every study deep dive teaches a *decision*, not just evidence. Two required parts,
both marked with data-attributes the validator checks (`check_application_section`):

1. **The call you're making** — a `.callout.callframe` box carrying `data-app-frame`,
   at the END of §0. One sentence naming the decision this deep dive equips, then an
   if/then list (3–5 `<li>`: client signal → your move). Write it first — it is the
   advance organizer every later section fills in.
2. **Applying it — decision guide** — the penultimate section (the old "Takeaways for
   our engagement" slot; keep its `id`). Body wrapped in ONE `<div data-app>` holding,
   in order:
   - `.decis` block — the frame expanded, branch-aware, unhappy paths included
     (brownfield realities first: what if the artifact/practice already exists,
     half-broken?). Close with the "three sentences to remember X by" callout.
   - **Worked example — Meridian** (`.callout`): ~400 words, one decision walked
     end to end on the canon client (`docs/WORKED-EXAMPLE-CLIENT.md`) with concrete
     numbers and one visible judgment call under ambiguity.
   - **Self-test** (`<details class="apptest">`): 3–4 scenario questions at
     apply/evaluate level ("client says/has X — what do you do/say?"), model answers
     inside the details body.
   - **PB bridge** (`.callout.pbbridge`): one line naming WHERE this becomes
     procedure, with an overlay link `href="#pb[1-5]-deepdive"` and the step named in
     text (e.g. "PB1 Assess — step 1.2"). In the standalone copy the link is inert
     (fragment only resolves in the workbook) — that is accepted; the named step keeps
     it usable. When you enrich a deep dive, land the procedural payload (talk tracks,
     templates, ops detail) in that runbook step in the SAME commit, with a one-line
     "Why: see <topic> §N" back-link.
3. **"So you…" hooks** — append a one-line applied consequence (`<span class="soyou">`)
   to each evidence section: the single sentence that re-aims the section at action.

Advisory quality checklist (validator cannot see these — you must):
- decision frame rows are *signals a consultant can actually observe*, not theory labels;
- worked example numbers are consistent with the Meridian canon file;
- unhappy paths covered (the client already has a broken version of the thing);
- self-test answers model reasoning, not just verdicts;
- evidence sections stay intact: rigor, strong-evidence vs vendor-claim vs synthesis
  labeling, honesty flags. The application layer ADDS; it never dilutes.

Skeleton stubs (from `scripts/add_application_skeleton.py`) carry `data-app-stub`
notes. Enrichment = replacing every stub in the file; the validator prints the
remaining stub count per file (informational).
```

- [ ] **Step 2: Add the authoring contract to AGENTS.md**

Insert before `## Everything else`:

```markdown
## How deep dives teach (binds every authoring agent)

Deep dives are decision-first learning material, not literature surveys. Every study
deep dive must carry: a "call you're making" decision frame at the end of §0
(`data-app-frame`), and an "Applying it — decision guide" section (`data-app`) holding
a branch-aware decision guide, a worked example on the Meridian canon client
(`docs/WORKED-EXAMPLE-CLIENT.md` — fictional, never real-client data), an
apply-level self-test, and a PB-runbook bridge link. Evidence sections keep their
rigor and honesty flags — the application layer adds, never dilutes. Structure is
enforced by `check_application_section` in `scripts/validate.py`; quality rules live
in `docs/AUTHORING-GUIDE.md` Step 1b. Follow both.
```

- [ ] **Step 3: Add the CLAUDE.md pointer**

In `CLAUDE.md`, "House style for content" list, append one bullet after the "Each deep dive follows a fixed shape" bullet:

```markdown
- **Every study deep dive carries the application layer** (v1.71 shape): the §0
  "call you're making" frame (`data-app-frame`) and the "Applying it — decision guide"
  section (`data-app`) with Meridian worked example, self-test, and PB-runbook bridge.
  Recipe: AUTHORING-GUIDE Step 1b; contract: AGENTS.md; enforced by
  `check_application_section`.
```

- [ ] **Step 4: Verify and commit**

Run: `python3 scripts/validate.py` — Expected: `RESULT: all checks passed.`

```bash
git add docs/AUTHORING-GUIDE.md AGENTS.md CLAUDE.md
git commit -m "docs: advisory contract for the deep-dive application layer"
```

---

### Task 3: Validator — `check_application_section`

**Files:**
- Modify: `scripts/validate.py` (new function after `check_diagram_lightbox` at line ~163; wire into `check_deepdives()` and `check_workbook()`)

**Interfaces:**
- Consumes: markers defined in Shared vocabulary.
- Produces: `APP_PENDING` (module-level set of filenames excluded from the check), `check_application_section(s, label)`, `app_stub_report()`. Tasks 4–6 shrink `APP_PENDING`.

- [ ] **Step 1: Add the check**

After the `check_diagram_lightbox` function add:

```python
# --- application layer (deep-dive application scaffold) ---------------------
# Study deep dives carry a decision frame + Applying-it section (AUTHORING-GUIDE
# Step 1b). PB runbooks ARE the application layer and are exempt. APP_PENDING lists
# files not yet converted; it only ever shrinks. New deep dives must comply
# immediately — never add to this set.
APP_EXEMPT_PREFIXES = ("PB1-", "PB2-", "PB3-", "PB4-", "PB5-")
APP_PENDING = {
    # all 48 study deep dives at introduction time; Tasks 4-5 empty this set
}
app_stubs = []  # (label, count) — informational

def check_application_section(s, label):
    fn = label.split(":")[0]
    if fn.startswith(APP_EXEMPT_PREFIXES):
        return
    if fn in APP_PENDING:
        return
    before = len(problems)
    frames = len(re.findall(r"data-app-frame\b", s))
    if frames != 1:
        note(False, f"{label}: expected exactly 1 data-app-frame, found {frames}")
    if not re.search(r"data-app-frame[^>]*>.*?<(li|tr)\b", s, flags=re.S):
        note(False, f"{label}: data-app-frame box has no <li>/<tr> row")
    apps = len(re.findall(r"<div data-app>", s))
    if apps != 1:
        note(False, f"{label}: expected exactly 1 <div data-app>, found {apps}")
    m = re.search(r"<div data-app>.*?</details>", s, flags=re.S)
    body = m.group(0) if m else ""
    if 'class="decis"' not in body:
        note(False, f"{label}: data-app container missing .decis block")
    if 'class="apptest"' not in body:
        note(False, f"{label}: data-app container missing .apptest self-test")
    if not re.search(r'href="#pb[1-5]-deepdive"', s):
        note(False, f"{label}: missing PB bridge link (#pb[1-5]-deepdive)")
    stubs = len(re.findall(r"data-app-stub\b", s))
    if stubs:
        app_stubs.append((label, stubs))
    note(len(problems) == before, f"{label}: application layer present")

def app_stub_report():
    if app_stubs:
        print(f"  info application-layer stubs awaiting enrichment in "
              f"{len(app_stubs)} copies: "
              + ", ".join(f"{l}({c})" for l, c in sorted(app_stubs)[:10])
              + (" …" if len(app_stubs) > 10 else ""))
```

- [ ] **Step 2: Wire into `check_deepdives()`**

In `check_deepdives()`, after the `check_standalone_anchor_affordance(s, fn)` line add:

```python
        check_application_section(s, fn)
```

- [ ] **Step 3: Wire into `check_workbook()` for overlays**

In `check_workbook()` (read the function first; it loads the workbook into a string), add a per-overlay loop after the existing overlay-related checks, extracting each overlay `<div class="e1ov" id="<tok>ov" …>…</div>` region and mapping tokens to standalone filenames. Overlay extraction that matches the existing file structure:

```python
    # application layer per overlay: map overlay token -> standalone filename
    dd_files = {f.split("-")[0].lower(): f for f in os.listdir(DEEPDIR)
                if f.endswith(".html")}
    for tok, fn in sorted(dd_files.items()):
        ovid = f'id="{tok}ov"'
        i = s.find(ovid)
        if i < 0:
            continue  # not embedded (should not happen; other checks catch it)
        j = s.find('<div class="e1ov"', i + 1)
        seg = s[i:j] if j > 0 else s[i:s.find("<footer")]
        check_application_section(seg, f"{fn}: overlay {tok}ov")
```

The label MUST start with the standalone filename followed by a colon — the guard in `check_application_section` keys on `label.split(":")[0]` to apply `APP_EXEMPT_PREFIXES` and `APP_PENDING` uniformly to both copies.

Note: `SDLC-foundations-deepdive.html` splits to token `sdlc`. Verify each token's overlay id actually exists (`grep -o 'id="[a-z0-9]*ov"' workbook/agentic-development-study.html | sort -u`) and adjust the mapping if any filename prefix ≠ overlay token; hardcode a small `TOKEN_FIXUPS = {}` dict if needed.

- [ ] **Step 4: Populate `APP_PENDING` with all 48 study files**

```bash
cd deep-dives && ls *.html | grep -v '^PB' 
```

Paste all 48 filenames into `APP_PENDING` as quoted strings.

- [ ] **Step 5: Call the stub report in `__main__`**

After `check_gallery_freshness()` in `__main__` add:

```python
    print()
    app_stub_report()
```

- [ ] **Step 6: Verify green, then verify the check actually bites**

Run: `python3 scripts/validate.py` — Expected: `RESULT: all checks passed.` (all 48 pending → check is dormant).

Temporarily remove `"B3-mutation-testing-gate-deepdive.html"` from `APP_PENDING`, rerun — Expected: FAIL with `B3-…: expected exactly 1 data-app-frame, found 0` (and the missing-container failures) for BOTH the standalone and the workbook overlay label. Restore the entry, rerun, green.

- [ ] **Step 7: Commit**

```bash
git add scripts/validate.py
git commit -m "feat(validate): check_application_section with APP_PENDING allowlist"
```

---

### Task 4: Skeleton script + scripted pass over the 41 standard files

**Files:**
- Create: `scripts/add_application_skeleton.py`
- Modify: `deep-dives/*.html` (41 files), `workbook/agentic-development-study.html`, `scripts/validate.py` (shrink `APP_PENDING`)

**Interfaces:**
- Consumes: markers + skeletons + CSS block from Shared vocabulary; `APP_PENDING` from Task 3.
- Produces: 41 files (×2 copies) carrying valid application-layer structure with `data-app-stub` placeholders; `APP_PENDING` reduced to the 7 hand files.

- [ ] **Step 1: Write the script**

`scripts/add_application_skeleton.py` — key requirements, implement exactly:

```python
#!/usr/bin/env python3
"""One-shot: inject the application-layer skeleton into every study deep dive whose
takeaways heading is exactly 'Takeaways for our engagement', in BOTH copies.
Idempotent: skips files already containing data-app. Run from repo root."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPDIR = os.path.join(ROOT, "deep-dives")
WORKBOOK = os.path.join(ROOT, "workbook", "agentic-development-study.html")
HEAD = "Takeaways for our engagement"
NEWHEAD = "Applying it — decision guide"

CSS = """/* application layer */
.callframe{border-left-color:#B26A00}
.callframe ul{margin:8px 0 2px}
.decis{margin:12px 0}
.apptest{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;margin:10px 0;max-width:74ch}
.apptest summary{cursor:pointer;font-weight:600}
.pbbridge{border-left-color:#2E7D5B}
.appstub{font-style:italic;opacity:.75}
.soyou{display:block;margin:10px 0 0;font-style:italic;opacity:.85;max-width:74ch}
"""

FRAME = ('<div class="callout callframe" data-app-frame><b>The call you'
         "’re making</b>\n<ul><li class=\"appstub\" data-app-stub>Decision "
         'frame being enriched — the if/then rows (client signal → your '
         'move) land here. Until then, see the Applying it section below.</li></ul>'
         "\n</div>\n")

def app_wrap(existing_body):
    return ('\n<div data-app>\n<div class="decis">\n' + existing_body
            + '\n</div>\n<div class="callout"><b>Worked example — Meridian.</b> '
              '<span class="appstub" data-app-stub>The end-to-end walkthrough on the '
              'recurring fictional client is added during enrichment (canon: '
              'docs/WORKED-EXAMPLE-CLIENT.md).</span></div>\n'
              '<details class="apptest"><summary>Self-test — can you apply '
              'this?</summary><p class="appstub" data-app-stub>Scenario questions '
              'with model answers are added during enrichment.</p></details>\n'
              '<div class="callout pbbridge"><b>Where this becomes procedure:</b> '
              '<a href="#pb1-deepdive">PB playbook</a> <span class="appstub" '
              'data-app-stub>— the exact runbook step is wired during '
              'enrichment.</span></div>\n</div>\n')

def transform(s, h2_id_prefix, is_standalone, fn):
    """h2_id_prefix: '' for standalone (ids sN), '<tok>ov-' for overlay.
    Idempotency lives in main() (skip when the standalone already has data-app) —
    do NOT check here: the workbook string accumulates data-app as overlays are
    transformed, so a whole-string check would skip every overlay after the first."""
    # 1. locate takeaways h2
    h2re = re.compile(r'<h2 id="' + re.escape(h2_id_prefix)
                      + r'(s\d+)"><span class="n">(\d+)</span>'
                      + re.escape(HEAD) + r"</h2>")
    m = h2re.search(s)
    if not m:
        raise SystemExit(f"{fn}: takeaways h2 not found (prefix={h2_id_prefix!r})")
    # 2. section body = up to next <h2
    end = s.find("<h2", m.end())
    if end < 0:
        raise SystemExit(f"{fn}: no following <h2> after takeaways")
    body = s[m.end():end]
    new = (s[:m.start()]
           + m.group(0).replace(HEAD, NEWHEAD)
           + app_wrap(body.strip("\n"))
           + s[end:])
    # 3. frame before <h2 id="<prefix>s1"
    s1 = new.find(f'<h2 id="{h2_id_prefix}s1"')
    if s1 < 0:
        raise SystemExit(f"{fn}: <h2 id={h2_id_prefix}s1> not found for frame insert")
    new = new[:s1] + FRAME + new[s1:]
    # 4. TOC label (standalone only)
    if is_standalone:
        new = new.replace(f'">{HEAD}</a>', f'">{NEWHEAD}</a>', 1)
        if HEAD in new:
            raise SystemExit(f"{fn}: leftover old heading text after TOC rename")
        # 5. CSS before the first closing </style>
        i = new.find("</style>")
        new = new[:i] + CSS + new[i:]
    return new

def main():
    dry = "--write" not in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    wb = open(WORKBOOK, encoding="utf-8").read()
    done = []
    for fn in sorted(os.listdir(DEEPDIR)):
        if not fn.endswith(".html") or fn.startswith("PB"):
            continue
        if only and fn not in only:
            continue
        s = open(os.path.join(DEEPDIR, fn), encoding="utf-8").read()
        tok = fn.split("-")[0].lower()
        if f"<h2 id=\"{tok}ov-" not in wb and f'id="{tok}ov"' not in wb:
            raise SystemExit(f"{fn}: overlay {tok}ov not found in workbook")
        h2 = re.search(r'<span class="n">\d+</span>' + re.escape(HEAD), s)
        if not h2:
            print(f"  skip {fn}: variant heading (hand task)")
            continue
        if "data-app" in s:
            print(f"  skip {fn}: already has data-app")
            continue
        new_s = transform(s, "", True, fn)
        new_wb = transform(wb, f"{tok}ov-", False, f"workbook:{fn}")
        if not dry:
            open(os.path.join(DEEPDIR, fn), "w", encoding="utf-8").write(new_s)
            wb = new_wb
        done.append(fn)
        print(f"  {'would write' if dry else 'wrote'} {fn} (+overlay)")
    if not dry:
        # one CSS block for the whole workbook (idempotent)
        if ".callframe{" not in wb:
            i = wb.find("</style>")
            wb = wb[:i] + CSS + wb[i:]
        open(WORKBOOK, "w", encoding="utf-8").write(wb)
    print(f"{len(done)} files {'planned' if dry else 'transformed'}")

if __name__ == "__main__":
    main()
```

Note the workbook-CSS subtlety: `transform()` must NOT inject CSS for overlays (`is_standalone=False`); the single workbook CSS injection happens once in `main()`.

- [ ] **Step 2: Dry-run on one file, then all**

Run: `python3 scripts/add_application_skeleton.py B3-mutation-testing-gate-deepdive.html`
Expected: `would write B3-… (+overlay)` and `1 files planned`, no errors.

Run: `python3 scripts/add_application_skeleton.py`
Expected: `41 files planned`, 7 `skip …: variant heading (hand task)` lines naming exactly B1, B2, E1, S4, S5, S6, S7.

- [ ] **Step 3: Write B3 only; validate; inspect**

Run: `python3 scripts/add_application_skeleton.py --write B3-mutation-testing-gate-deepdive.html`
Remove `"B3-mutation-testing-gate-deepdive.html"` from `APP_PENDING` in validate.py.
Run: `python3 scripts/validate.py` — Expected: green, and the stub-info line reports B3 twice (standalone + overlay).
Open `deep-dives/B3-…-deepdive.html` in a browser (or read the section) — frame box after §0, Applying-it section renders, `<details>` opens.

- [ ] **Step 4: Write the remaining 40; shrink APP_PENDING to the 7 hand files**

Run: `python3 scripts/add_application_skeleton.py --write`
Expected: 40 more `wrote` lines (B3 skipped as already done).
Edit `APP_PENDING` down to exactly:

```python
APP_PENDING = {
    "B1-bootstrap-paradox-deepdive.html",
    "B2-characterization-golden-master-deepdive.html",
    "E1-agent-model-harness-deepdive.html",
    "S4-mcp-tools-attack-surface-deepdive.html",
    "S5-loop-autorun-selfmod-sandbox-deepdive.html",
    "S6-memory-poisoning-multiagent-risk-deepdive.html",
    "S7-contract-brownfield-surfaces-secrets-deepdive.html",
}
```

Run: `python3 scripts/validate.py` — Expected: green; stub info reports 82 copies (41 × 2).

- [ ] **Step 5: Commit (structure-only pass, one commit)**

```bash
git add scripts/add_application_skeleton.py scripts/validate.py deep-dives workbook/agentic-development-study.html
git commit -m "feat(content): application-layer skeleton in 41 deep dives (both copies)"
```

---

### Task 5: Hand-convert the 7 variant files

**Files:**
- Modify: the 7 files listed in `APP_PENDING` + their workbook overlays + `scripts/validate.py` (empty `APP_PENDING`)

**Interfaces:**
- Consumes: skeletons/CSS from Shared vocabulary (same blocks, hand-placed).
- Produces: all 48 study deep dives structurally compliant; `APP_PENDING` empty.

Per file (do one file at a time; validate + spot-check after each; ids NEVER change):

- [ ] **Step 1: B1 and B2** — heading `Takeaways` (B1 `s7`, B2 `s7`; B2 also has `s6` "The toolbox and the exit criteria" which stays untouched). Rename display text `Takeaways` → `Applying it — decision guide` (h2 + standalone TOC), wrap body in the Application skeleton, insert the §0 frame before `<h2 id="s1"` / `<h2 id="<tok>ov-s1"`, inject CSS into the standalone `<style>`. Same edits in the `b1ov`/`b2ov` overlays (no TOC, no CSS there).
- [ ] **Step 2: E1** — named ids: takeaways is `<h2 id="takeaways">…Takeaways for introducing a harness</h2>`, §0 is `id="why"`, §1 is `id="eq"`. Keep ids `takeaways`/`why`/`eq`. Rename display text to `Applying it — introducing a harness`, wrap its body (up to `<h2 id="reading"`) in the skeleton, frame goes before `<h2 id="eq"`. Overlay ids are `e1ov-`-prefixed equivalents — verify with `grep -o 'id="e1ov-[a-z]*"' workbook/…` and mirror.
- [ ] **Step 3: S4–S7** — fused `Takeaways &amp; further reading` (S4/S5/S7 `s7`, S6 `s6`). Keep ONE section; rename display text to `Applying it &amp; further reading`. Wrap only the takeaways part (from after the `<h2>` to just before the further-reading block — locate the `.reading` list/nav start) in `<div data-app>`; the reading block stays inside the section but OUTSIDE the container. Frame before `…s1`. CSS into standalone `<style>`; mirror in overlays.
- [ ] **Step 4: Empty the allowlist**

Set `APP_PENDING = set()` in validate.py (keep the variable and its comment — future files must never be added, and the empty set documents that the rollout completed).

Run: `python3 scripts/validate.py` — Expected: green; stub info reports 96 copies (48 × 2).

- [ ] **Step 5: Commit**

```bash
git add deep-dives workbook/agentic-development-study.html scripts/validate.py
git commit -m "feat(content): application-layer skeleton in the 7 variant deep dives; APP_PENDING empty"
```

---

### Task 6: Pilot enrichment — B3 end to end

**Files:**
- Modify: `deep-dives/B3-mutation-testing-gate-deepdive.html` + `b3ov` overlay
- Modify: `deep-dives/PB1-assess-runbook.html` + `pb1ov` overlay (payload + back-link)

**Interfaces:**
- Consumes: Meridian canon (Task 1), skeleton structure (Task 4), AUTHORING-GUIDE Step 1b (Task 2).
- Produces: the exemplar every future enrichment imitates; zero `data-app-stub` in B3.

Content below is the approved draft — polish prose while writing, keep every fact. All edits go into BOTH copies.

- [ ] **Step 1: Replace the B3 frame stub with the real decision frame**

```html
<div class="callout callframe" data-app-frame><b>The call you’re making:</b> when a
client wants agent write-autonomy, what do you demand from their test suite — and in
what order?
<ul>
<li><b>Coverage-proud, no mutation number</b> → run extreme mutation (Descartes-style)
on the module they trust most; open with the pseudo-tested inventory, not a lecture.</li>
<li><b>Flaky suite (any “re-run until green” culture)</b> → quarantine first (B2);
a mutation score over a flaky suite is illegitimate — do not gate on it yet.</li>
<li><b>No test culture at all</b> → skip the score fight; start survivors-in-review
(Mode 1) on agent-touched diffs only.</li>
<li><b>Mixed stack</b> → pick the tool per pilot module: JVM → PIT, JS/TS → Stryker,
Python → mutmut / cosmic-ray, .NET → Stryker.NET.</li>
<li><b>Ready to gate</b> → module-level ~70% score at the F1→F2 boundary, fresh
mutants, ADR-recorded (Mode 2).</li>
</ul>
</div>
```

- [ ] **Step 2: Rebuild the Applying-it section body**

Order inside `<div data-app>`: `.decis` (existing takeaways content reorganized under the five frame branches, unhappy paths first; the existing "three sentences to remember B3 by" callout closes it) → worked example → self-test → PB bridge. Worked example (~400 words, expand from this skeleton, numbers per Meridian canon):

> **Worked example — Meridian.** PolicyCore billing: 82% branch coverage, 14-min suite, ~3% flake rate, no mutation score ever measured. Walk: (1) flake first — ten reruns show the 3% retry habit, so three known-flaky tests are quarantined before any measurement (gate legitimacy, §6); (2) extreme mutation over lunch — 23 of 210 methods pseudo-tested, including premium proration; (3) the demo to Dana Kovář is her own inventory, not a slide: a seeded proration fault the green suite misses; (4) diff-scoped mutation lands advisory in Jenkins (Mode 1); two weeks of survivors-fed-back tasks move the module 58% → 74%; (5) ADR-011 records the 70% module bar for the F1→F2 exit, graded on fresh mutants. **The judgment call:** the DTO mapper spews equivalent mutants; instead of chasing 80% there, generated code is excluded from mutation scope and the exclusion is written into ADR-011 — scope honesty beats score theater.

- [ ] **Step 3: Write the self-test (3 scenarios, answers in the details body)**

1. Dana says "we have 82% coverage, our tests are fine." Name the two checks you run before arguing, and the one sentence you say. *(Flake rate; extreme mutation on the most-trusted module. "Coverage proves the code ran; a mutation score proves the tests would notice it being wrong.")*
2. A legacy module scores 45% and the team wants agent write-autonomy this sprint. Gate now? *(No 70% gate yet — Mode 1 survivors-in-review + characterization tests (B2) first; the gate binds at the F1→F2 exit.)*
3. The team reports 71% — measured on the same mutants that drove their fix loop. Pass? *(No. The practice sheet is not the exam: regenerate held-out mutants for the gate run.)*

- [ ] **Step 4: PB bridge + PB1 payload (same commit)**

B3 bridge: `This becomes procedure in <a href="#pb1-deepdive">PB1 Assess</a> (coverage/flake reality + pseudo-tested demo) and gates in <a href="#pb3-deepdive">PB3 Harness</a> (CI wiring).`
In PB1 (both copies): find the assess-phase step covering test-suite reality (read PB1's `.pbstep` blocks; the step whose `.pbwhat` covers test/coverage assessment). Extend its `.pbwhy` with `Why: see <a href="#b3-deepdive">B3</a> — coverage vs mutation score.` and add a `.pbtpl` template block (with `.pbcopy` button, `data-copy` pointing at a new unique `<pre>` id) containing the CTO talk track:

```
Talk track — the coverage conversation (3 minutes)
1. "Coverage proves the code ran; a mutation score proves the tests would notice it
   being wrong."
2. Show THEIR pseudo-tested inventory (extreme mutation, ~1h run): "these N methods
   are executed by tests that fail to notice any behavior change."
3. Offer the no-KPI path: survivors-in-review on agent diffs only, advisory, two weeks.
   Decision we ask for today: pick the pilot module.
```

Do NOT add a new `.pbstep` (frozen `data-step` ids stay untouched); extend the existing step. Mirror in `pb1ov`. Add "So you…" hooks to B3 evidence sections §1–§7 (one `<span class="soyou">` line each).

- [ ] **Step 5: Validate, visual check, commit**

Run: `python3 scripts/validate.py` — Expected: green; stub info no longer lists B3 (94 copies remain).
Visual: open the workbook, open the B3 overlay, click the PB1 bridge link — the PB1 overlay opens on top. Known cosmetic caveat: closing the stacked overlay restores page scroll while B3 stays open — pre-existing behavior of all cross-overlay links, out of scope.

```bash
git add deep-dives/B3-mutation-testing-gate-deepdive.html deep-dives/PB1-assess-runbook.html workbook/agentic-development-study.html
git commit -m "feat(content): B3 enriched as application-layer exemplar; PB1 talk-track payload"
```

---

### Task 7: Final verification + PR

**Files:** none new.

- [ ] **Step 1: Full sweep**

```bash
python3 scripts/validate.py
git log --oneline origin/main..HEAD
git diff origin/main --stat | tail -5
```

Expected: all green; commits = spec + Tasks 1–6; diff touches only `deep-dives/`, `workbook/`, `scripts/`, `docs/`, `AGENTS.md`, `CLAUDE.md`. Confirm NO diff in `docs/CHANGELOG.md` and no `#verov` change (no version bump).

- [ ] **Step 2: Push and open the PR**

```bash
git push -u origin worktree-deepdive-application-layer
gh pr create --title "Deep-dive application layer: decision frames, Meridian worked examples, PB bridges" --body "$(cat <<'EOF'
## Summary
- Application scaffold in all 48 study deep dives (both copies): §0 decision frame, "Applying it — decision guide" section (decision guide / Meridian worked example / self-test / PB bridge), enforced by check_application_section
- Meridian worked-example client canon (docs/WORKED-EXAMPLE-CLIENT.md) + advisory contract (AUTHORING-GUIDE Step 1b, AGENTS.md, CLAUDE.md)
- B3 fully enriched as the exemplar incl. PB1 talk-track payload; remaining 47 carry validated skeletons with visible enrichment stubs
- No version bump (deferred on request)

Spec: docs/superpowers/specs/2026-07-23-deepdive-application-layer-design.md

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

Expected: PR URL printed. Report it to the user; version bump and enrichment of the remaining 47 happen in follow-up sessions on the user's schedule.
