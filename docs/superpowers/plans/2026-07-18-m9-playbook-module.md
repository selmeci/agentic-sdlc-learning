# M9 Playbook Module Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add module M9 "Playbook" to the workbook — five `pb-` topics organised by the engagement journey, with the full PB1 Assess runbook (standalone + overlay), store-backed interactive checklists, copy-paste templates, and a validator extension — released as v1.48.

**Architecture:** Everything lives in the existing single-file workbook (`workbook/agentic-development-study.html`) plus one new standalone deep-dive file. The M9 module is a new entry in the `MODULES` data array (rendering is fully generic). Checklist state persists through the existing `store` backend as a new `pb` field inside the `agentic-study-v1` JSON state. The PB1 runbook follows the two-copies rule: one shared body → standalone file + in-page overlay.

**Tech Stack:** Hand-authored HTML/CSS/vanilla JS (no build), Python validator (`scripts/validate.py`), git.

## Global Constraints (from the spec — read the spec first: `docs/superpowers/specs/2026-07-18-playbook-module-design.md`, rev. 2)

- **Content language is English** (the conversation with the user was Slovak; the artifact content is English, per CLAUDE.md).
- Topic IDs (`pb-assess`, `pb-bootstrap`, `pb-harness`, `pb-handoff`, `pb-pilot`) and checklist step IDs (`pb1-s1` … `pb1-s9`) are **frozen forever** once released — progress is keyed on them.
- All persistence goes through the single `store` backend (key `agentic-study-v1`). **No raw `localStorage`/`window.storage` calls anywhere.** The standalone file deliberately does NOT persist.
- No team-level/shared progress tracking in this increment — per-browser `store` only (spec Out of scope; aggregation across a team is a ROADMAP backlog note, not a feature).
- Cross-references open in-page overlays (`#e4-deepdive` …), never relative file links.
- Template rule (spec rev. 2): where the underlying theory is deterministic, the template is the **real runnable artifact** (hook script, permission baseline, CI config), not prose about it — the E5 litmus. PB1's templates are documents (questionnaire, report), so the rule binds from PB3 Harness onward; the PB3 stub and the AUTHORING-GUIDE note must say so.
- Baseline rule (spec rev. 2): the delivery baseline is captured at **assess time** (PB1), never deferred to PB5 — a pilot without a baseline can be neither proven nor disproven (METR perception gap).
- `python3 scripts/validate.py` must pass after **every** task. Baseline before Task 1: all checks pass, 55 topics.
- Version bump is **v1.48**, date **2026-07-18** (v1.47 = D2 deep dive, already shipped).
- Known traps (CLAUDE.md): no apostrophes inside Python-generated strings when scripting file edits — use the Edit tool; no bash brace expansion; unique SVG marker id (`ahPB1a`) + edge class (`edPB1`).
- Line numbers below were verified at plan time but WILL shift as tasks land — always locate anchors by the quoted `old_string`, not by line number.

---

### Task 1: Validator — recognise the `pb-` prefix and check step-ID uniqueness

**Files:**
- Modify: `scripts/validate.py`

**Interfaces:**
- Produces: validator that (a) counts `pb-*` topic ids, (b) cross-checks them against CONTENT-MAP.md, (c) fails on duplicate `data-step` ids in the workbook. Later tasks rely on all three.

- [ ] **Step 1: Extend the two topic-id regexes with the `pb` prefix**

In `scripts/validate.py`, edit the workbook topic-id regex:

```python
    ids = re.findall(r'id:"((?:eng|prod|hand|ia|brown|traj|des|sec|pb)-[a-z0-9-]*)"', s)
```

(old string is identical minus `|pb`). Then the CONTENT-MAP regex:

```python
        doc_ids = set(re.findall(r"`((?:eng|prod|hand|ia|brown|traj|des|sec|pb)-[a-z0-9-]+)`", doc))
```

- [ ] **Step 2: Add the step-ID uniqueness check**

In `check_workbook()`, immediately after the CONTENT-MAP block (the `if os.path.exists(cmap):` block), add:

```python
    # playbook checklist step ids are frozen progress keys - duplicates would
    # silently merge two steps' saved state
    steps = re.findall(r'data-step="([\w-]+)"', s)
    dup_steps = sorted({x for x in steps if steps.count(x) > 1})
    note(not dup_steps, f"playbook step ids unique ({len(steps)} step(s))"
         if not dup_steps else f"DUPLICATE playbook step ids: {dup_steps}")
```

- [ ] **Step 3: Update the module docstring**

In the docstring at the top, after the line about topic count, add:

```
    - playbook checklist step ids (data-step) are unique (frozen progress keys)
```

- [ ] **Step 4: Run the validator**

Run: `python3 scripts/validate.py`
Expected: all checks pass; new line `ok  playbook step ids unique (0 step(s))`; topic count still 55.

- [ ] **Step 5: Commit**

```bash
git add scripts/validate.py
git commit -m "validate: recognise pb- topic prefix, check playbook step-id uniqueness"
```

---

### Task 2: M9 module skeleton — five `pb-` topics in the workbook data + CONTENT-MAP

**Files:**
- Modify: `workbook/agentic-development-study.html` (MODULES array, ends near line 6958)
- Modify: `docs/CONTENT-MAP.md`
- Modify: `scripts/validate.py` (expected-count message only)

**Interfaces:**
- Produces: topic ids `pb-assess`, `pb-bootstrap`, `pb-harness`, `pb-handoff`, `pb-pilot`; module DOM id `m9pb`. Task 6 will prepend the overlay link to `pb-assess`'s `src` array — in this task its `src` contains only plain entries.

- [ ] **Step 1: Append the M9 module to the MODULES array**

Locate the end of the MODULES array — the unique sequence (last topic of module `m6`/M8, then array close):

```
src:[{t:"OWASP agentic top 10; published incident postmortems; large-company governance patterns"}]}
]}
];
```

Replace the trailing `]}\n];` so the M9 module is inserted after module `m6`:

```js
]},
{id:"m9pb",code:"M9",name:"Playbook — from theory to practice",base:"runbook layer distilled from M1–M7 (no new research)",
desc:"The practice layer: five runbooks ordered by the engagement journey at a brownfield client — assess, bootstrap the verification base, stand up the harness, run the handoff, measure the pilot. Each runbook is a checklist with templates whose every step links back to the theory topic that justifies it. Built for the internal team; progress is saved in this workbook.",
topics:[
{id:"pb-assess",code:"PB1",title:"Assess: client maturity & the F0 entry gate",
know:[`The runbook: baseline the verification loop (test suite, CI signal) and capture the delivery baseline up front (DORA keys + cost per merged PR — a pilot without a baseline can be neither proven nor disproven), inventory source-of-truth artifacts, check the governance minimum (env separation, secrets, write permissions), name the review owner — then score it into an L1–L5 recommendation and a go/no-go at the F0 gate.`,
`Why assess before build: DORA 2024 associates +25% AI adoption with −7.2% delivery stability — AI amplifies the surrounding system, so the surrounding system is measured first (E7, B1).`,
`The scoring model and the non-compensable gate criteria are our synthesis (Report 4 + E6/B6 material), not an industry standard.`,
`Output artifacts: a filled questionnaire, a delivery-baseline snapshot, an assessment report from the template, and a recorded F0 go/no-go decision with STOP criteria attached.`],
concepts:["maturity assessment","delivery baseline","entry gate","non-compensable criteria","autonomy recommendation","assessment report"],
open:[`Which client signals that the questionnaire cannot capture (politics, incentive structure) should still veto a go decision?`],
src:[{t:"E6 autonomy levels, B1 safe ordering, B6 gates & STOP criteria, E7 metrics — the theory this runbook distils (open those topics' deep dives)"}],
checks:[{q:`Why are the four gate criteria non-compensable rather than averaged into the score?`,a:`Because each one guards a failure mode that no amount of strength elsewhere offsets: an untrusted test suite means no external truth for the loop (E4); unreadable CI signal means the agent cannot self-correct; missing dev/prod separation makes the blast radius unbounded (the Replit incident); secrets in the repo leak through every agent context. A high average with one of these missing is exactly the false-confidence case the assessment exists to catch.`}]},

{id:"pb-bootstrap",code:"PB2",title:"Bootstrap: build the verification base (runbook in preparation)",
know:[`Will cover, in order: characterization tests on the first module (B2), a minimal CI loop the agent can read, the mutation-score baseline and the ~70% working heuristic (B3), and read-only comprehension before any writes (B1, B4).`,
`The safe ordering exists because of the bootstrap paradox: the agent needs a verification loop that legacy code does not have, and the agent is also the cheapest tool to build it — unanchored, this closes into the bug-as-spec loop (B1).`],
concepts:["characterization tests","mutation baseline","safe ordering"],
open:[`Which module of the client codebase is the first characterization target — and does the heatmap (B5) pick it, or does risk?`],
src:[{t:"Runbook companion in preparation — will open here as an overlay in a future version"},{t:"Theory: B1 bootstrap paradox, B2 characterization, B3 mutation gate (open those deep dives)"}]},

{id:"pb-harness",code:"PB3",title:"Harness: stand up the engineering harness (runbook in preparation)",
know:[`Will cover: the CLAUDE.md/AGENTS.md skeleton extracted-not-decreed (B1, E9), hooks and permissions with the advisory-vs-deterministic split (E5), the verification gate in CI (E4), and information architecture for the agent (I1–I5).`,
`Its templates are the harness starter kit: where the theory is deterministic, the copy-paste block IS the runnable artifact — hook scripts, permission baselines, CI gate configs (the E5 litmus: what must never happen ships as enforcement, not advice).`,
`Ordering constraint: the harness is built on top of the PB2 verification base — write autonomy without external truth is the anti-pattern the whole framework exists to prevent.`],
concepts:["CLAUDE.md skeleton","advisory vs deterministic","hooks","write permissions"],
open:[`Which harness rules graduate from prose to enforced hooks in week one at a typical client?`],
src:[{t:"Runbook companion in preparation — will open here as an overlay in a future version"},{t:"Theory: E1–E5, E9 harness tuning, I2 write permissions (open those deep dives)"}]},

{id:"pb-handoff",code:"PB4",title:"Handoff: run the contract end-to-end (runbook in preparation)",
know:[`Will cover: writing the first handoff contract (H1 anatomy, T0–T2 sizing), EARS/Gherkin acceptance criteria as the agent's reward signal (H2), traceability IDs (H3), and the return channel with its anti-patterns (H4).`,
`The exit test: one real feature delivered by an agent against the contract, with the review running against passing acceptance tests.`],
concepts:["handoff contract","EARS/Gherkin","return channel"],
open:[`What is the smallest real client feature suitable for the first contract-driven delivery?`],
src:[{t:"Runbook companion in preparation — will open here as an overlay in a future version"},{t:"Theory: H1–H4 (open those deep dives)"}]},

{id:"pb-pilot",code:"PB5",title:"Pilot: measure, gate, decide (runbook in preparation)",
know:[`Will cover: the DORA baseline + METR-style pilot design from E7 (objective time, pre-registered success, perception-gap capture), the F0–F3 gate table with back-triggers, and STOP criteria (B6). The baseline itself is captured earlier, in PB1 — PB5 compares against it.`,
`Self-reported speed is disqualified as evidence by design: METR measured devs 19% slower while believing they were ~20% faster.`],
concepts:["DORA baseline","pre-registered success","STOP criteria","F0–F3 gates"],
open:[`Which DORA keys can this client actually compute from day 0, and what replaces the ones they cannot?`],
src:[{t:"Runbook companion in preparation — will open here as an overlay in a future version"},{t:"Theory: E7 metrics & anti-patterns, B6 roadmap F0–F3 (open those deep dives)"}]}
]}
];
```

- [ ] **Step 2: Update the validator's informational count message**

In `scripts/validate.py` change `(expected 52 unless intentionally changed)` to `(expected 60 unless intentionally changed)`.

- [ ] **Step 3: Add M9 to `docs/CONTENT-MAP.md`**

Append after the M8 module section, matching the existing table style:

```markdown
### M9 · Playbook — from theory to practice (id `m9pb`) — runbook layer, no research notes
| Topic | id | Deep dive |
|---|---|---|
| PB1 Assess: client maturity & the F0 entry gate | `pb-assess` | PB1-assess-runbook.html + overlay |
| PB2 Bootstrap: build the verification base | `pb-bootstrap` | in preparation |
| PB3 Harness: stand up the engineering harness | `pb-harness` | in preparation |
| PB4 Handoff: run the contract end-to-end | `pb-handoff` | in preparation |
| PB5 Pilot: measure, gate, decide | `pb-pilot` | in preparation |
```

Also update the header line counts: `8 modules, 55 topics` → `9 modules, 60 topics` (leave the companion count until Task 7).

- [ ] **Step 4: Run the validator**

Run: `python3 scripts/validate.py`
Expected: all pass; `topic ids unique (60 topics)`; CONTENT-MAP check green.

- [ ] **Step 5: Commit**

```bash
git add workbook/agentic-development-study.html docs/CONTENT-MAP.md scripts/validate.py
git commit -m "feat: M9 Playbook module skeleton - five pb- topics (PB1 full topic, PB2-PB5 in preparation)"
```

---

### Task 3: Store schema `state.pb` + checklist/copy JS + CSS in the workbook

**Files:**
- Modify: `workbook/agentic-development-study.html` (app `<script>` near lines 6968–8135; main `<style>`)

**Interfaces:**
- Consumes: nothing from earlier tasks (markup arrives in Task 6; all selectors match nothing until then, which is safe).
- Produces: `state.pb` (object: runbook topic id → array of checked step-id strings), `syncPb()` (sets checkbox state + progress chips from `state.pb`), delegated `change` handler on `.pbck` (checkboxes carry `data-pb` = runbook topic id and `data-step` = step id), delegated `click` handler on `.pbcopy` (button carries `data-copy` = id of the `<pre>` to copy), CSS classes `.pbstep .pbck .pbtxt .pbwhat .pbwhy .pbdone .pbtpl .pbcopy .pbprog .pbnote`. Tasks 4–6 write markup against exactly these names.

- [ ] **Step 1: Extend the state object and its (de)serialization**

Four edits in the app script:

1. `let state={progress:{},notes:{},seen:{},highlights:[],updatedAt:null};`
   → `let state={progress:{},notes:{},seen:{},highlights:[],pb:{},updatedAt:null};`

2. In `stateBlob()`: `{progress:state.progress,notes:state.notes,seen:state.seen,highlights:state.highlights,updatedAt:state.updatedAt}`
   → add `pb:state.pb,` before `updatedAt`.

3. In `loadState()`, the line assigning parsed fields (`state.progress=p.progress||{};…`): append `state.pb=(p.pb&&typeof p.pb==='object')?p.pb:{};` before the closing brace of that `if`.

4. In the import-merge function (locate `if(p.seen)Object.assign(state.seen,p.seen);`), add after that line:

```js
      if(p.pb)Object.keys(p.pb).forEach(function(rb){var cur=state.pb[rb]||(state.pb[rb]=[]);(p.pb[rb]||[]).forEach(function(sid){if(cur.indexOf(sid)===-1)cur.push(sid);});});
```

- [ ] **Step 2: Mirror `pb` into the Yjs sync doc (follow the highlights pattern)**

In `mirrorToDoc()`, extend the map declarations line to add `B=ydoc.getMap('pb')`, and inside the `ydoc.transact` callback add:

```js
    var pbHave={};
    Object.keys(state.pb||{}).forEach(function(rb){(state.pb[rb]||[]).forEach(function(sid){var k=rb+':'+sid;pbHave[k]=1;if(B.get(k)!==true)B.set(k,true);});});
    Array.from(B.keys()).forEach(function(k){if(!pbHave[k])B.delete(k);});
```

In `materializeFromDoc()`, add before the closing brace:

```js
  var B=ydoc.getMap('pb'),pbm={};
  Array.from(B.keys()).forEach(function(k){var i=k.indexOf(':'),rb=k.slice(0,i),sid=k.slice(i+1);if(!pbm[rb])pbm[rb]=[];pbm[rb].push(sid);});
  state.pb=pbm;
```

- [ ] **Step 3: Add `syncPb()` and the delegated handlers**

Insert after the `refreshAll` function definition:

```js
function syncPb(){
  $$('.pbck').forEach(function(cb){cb.checked=(state.pb[cb.dataset.pb]||[]).indexOf(cb.dataset.step)!==-1;});
  $$('[data-pbprog]').forEach(function(el){
    var rb=el.dataset.pbprog,total=$$('.pbck[data-pb="'+rb+'"]').length,done=(state.pb[rb]||[]).length;
    el.textContent=done+' / '+total+' steps done';
  });
}
document.addEventListener('change',function(e){
  var cb=e.target.closest('.pbck');if(!cb)return;
  var arr=state.pb[cb.dataset.pb]||(state.pb[cb.dataset.pb]=[]);
  var i=arr.indexOf(cb.dataset.step);
  if(cb.checked&&i===-1)arr.push(cb.dataset.step);
  if(!cb.checked&&i!==-1)arr.splice(i,1);
  syncPb();scheduleSave();
});
document.addEventListener('click',function(e){
  var b=e.target.closest('.pbcopy');if(!b)return;
  var pre=document.getElementById(b.dataset.copy);if(!pre)return;
  var txt=pre.textContent;
  function ok(){b.textContent='copied ✓';setTimeout(function(){b.textContent='copy';},1400);}
  function fb(){var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();try{document.execCommand('copy');ok();}catch(err){}document.body.removeChild(ta);}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(ok,fb);}else{fb();}
});
```

Then wire it into the two refresh points:
- `function refreshAll(){syncFromState();updateCounts();updateNotesCount();renderTopicHls();applyFilter();}` → add `syncPb();` before `applyFilter();`.
- In the init IIFE (locate `await loadState();` then `syncFromState();`), add `syncPb();` on the next line after `syncFromState();`.

- [ ] **Step 4: Add the runbook CSS**

In the main `<style>` block, insert after the last `.e1ov svg .ed*` rule (currently the D2 rule, near line 341):

```css
/* ===== M9 playbook runbooks (v1.48) ===== */
.pbstep{display:flex;gap:11px;align-items:flex-start;padding:11px 13px;border:1px solid var(--line);border-radius:10px;background:var(--card);margin:9px 0}
.pbstep input.pbck{margin-top:4px;width:16px;height:16px;accent-color:var(--cobalt);flex:none;cursor:pointer}
.pbtxt{flex:1;min-width:0}
.pbwhat{font-family:var(--disp);font-weight:600;font-size:14.5px;cursor:pointer}
.pbwhy{font-size:13.5px;color:var(--soft);margin:3px 0 0}
.pbdone{font-family:var(--mono);font-size:11px;color:var(--pine);margin-top:5px}
.pbtpl{position:relative;margin:12px 0}
.pbtpl pre{font-family:var(--mono);font-size:12px;line-height:1.5;background:var(--idle-bg);border:1px solid var(--line);border-radius:10px;padding:13px 15px;overflow-x:auto;white-space:pre-wrap}
.pbcopy{position:absolute;top:8px;right:8px;font-family:var(--mono);font-size:10.5px;padding:3px 10px;border:1px solid var(--line);border-radius:6px;background:var(--card);cursor:pointer;color:var(--soft)}
.pbcopy:hover{border-color:var(--cobalt);color:var(--cobalt-deep)}
.pbprog{font-family:var(--mono);font-size:11px;color:var(--soft);border:1px solid var(--line);border-radius:999px;padding:3px 10px}
.pbnote{font-family:var(--mono);font-size:11.5px;color:var(--soft)}
```

- [ ] **Step 5: Run the validator**

Run: `python3 scripts/validate.py`
Expected: all pass — in particular `app <script> parses (node --check)`.

- [ ] **Step 6: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat: pb checklist state in store + copy/checkbox handlers + runbook CSS"
```

---

### Task 4: Author the PB1 Assess shared body

**Files:**
- Create: `/tmp/claude-1000/-home-roan-WebstormProjects-agentic-sdlc-learning/65e0df03-9153-47e6-b224-70b53af01fae/scratchpad/pb1body.html` (section content only, no `<html>/<head>`)

**Interfaces:**
- Produces: the shared body consumed verbatim by Task 5 (standalone) and Task 6 (overlay). Section `<h2>` elements carry **no** `id` attributes (Task 5 adds `id="sN"`; the overlay copy stays id-less — this matches how existing overlays avoid duplicate `s1` ids in the workbook). All checkboxes use the Task-3 contract: `class="pbck" data-pb="pb-assess" data-step="pb1-sN"`. If the scratchpad file is lost between sessions, regenerate the body by stripping the head/TOC/footer from the Task-5 standalone file.
- Step IDs (frozen): `pb1-s1`…`pb1-s9`. Template pre IDs: `pb1-tpl-quest`, `pb1-tpl-report`.

- [ ] **Step 1: Write the body skeleton with all fixed markup**

The body has sections §0–§7, numbered `<h2><span class="n">N</span>Title</h2>`. Structure and required content:

**§0 Why this runbook exists** — `.lead` paragraph: PB1 is the entry point of every engagement; you assess the surrounding system before building anything on it, because AI amplifies that system (DORA 2024: +25% AI adoption associated with −7.2% delivery stability; METR RCT: experienced devs 19% slower while believing ~20% faster). One `.callout amber` "What this is not": not an audit for the client's benefit alone — the output decides *our* entry decision at the F0 gate. Cross-link topics E7, B1 by overlay links.

**§1 How to run it** — prose: one person, 2–4 focused days, read access to repo + CI + one team interview; every step below has WHAT (the action), WHY (the theory link), and DONE (the exit criterion); check steps off as you go. Include the progress chip + note:

```html
<p><span class="pbprog" data-pbprog="pb-assess"></span></p>
<p class="pbnote">Progress is saved locally in this workbook (same store as topic progress). The standalone copy of this runbook does not persist checkbox state.</p>
```

Then the journey SVG figure (complete, use as-is):

```html
<figure>
<svg viewBox="0 0 900 150" role="img" aria-label="The five-runbook engagement journey, PB1 highlighted">
  <defs><marker id="ahPB1a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#57656F"/></marker></defs>
  <text x="30" y="30" class="tg">THE ENGAGEMENT JOURNEY</text>
  <rect x="24" y="48" width="150" height="52" rx="10" class="bxC"/><text x="40" y="70" class="tt">PB1 Assess</text><text x="40" y="88" class="ts">you are here</text>
  <rect x="200" y="48" width="150" height="52" rx="10" class="bxG"/><text x="216" y="70" class="ti">PB2 Bootstrap</text><text x="216" y="88" class="ts">verification base</text>
  <rect x="376" y="48" width="150" height="52" rx="10" class="bxG"/><text x="392" y="70" class="ti">PB3 Harness</text><text x="392" y="88" class="ts">CLAUDE.md · hooks · CI</text>
  <rect x="552" y="48" width="150" height="52" rx="10" class="bxG"/><text x="568" y="70" class="ti">PB4 Handoff</text><text x="568" y="88" class="ts">contract · EARS</text>
  <rect x="728" y="48" width="150" height="52" rx="10" class="bxG"/><text x="744" y="70" class="ti">PB5 Pilot</text><text x="744" y="88" class="ts">metrics · gates</text>
  <line x1="174" y1="74" x2="200" y2="74" class="edPB1"/>
  <line x1="350" y1="74" x2="376" y2="74" class="edPB1"/>
  <line x1="526" y1="74" x2="552" y2="74" class="edPB1"/>
  <line x1="702" y1="74" x2="728" y2="74" class="edPB1"/>
  <text x="30" y="132" class="ts">Each runbook ends in an exit gate; PB1 ends in the F0 go/no-go (B6).</text>
</svg>
<figcaption>The journey the M9 module walks. PB1 produces the assessment report, the delivery baseline, and the F0 entry decision; PB2–PB5 build on its findings in order.</figcaption>
</figure>
```

**§2 Phase A — Verification base & delivery baseline** (steps A1, A2, A3)
**§3 Phase B — Information architecture** (step B1)
**§4 Phase C — Governance minimum** (steps C1, C2)
**§5 Phase D — Team readiness** (step D1)
**§6 Phase E — Evaluation & the F0 gate** (steps E1, E2 + both templates + the recommendation table)
**§7 Exit gate & takeaways** (`.callout pine` exit criteria, three-sentence `.callout`, closing `.closingnote`)

Each step uses exactly this markup pattern (shown filled for A1; repeat for all nine with the content in Step 2):

```html
<div class="pbstep">
  <input type="checkbox" class="pbck" id="pb1-s1" data-pb="pb-assess" data-step="pb1-s1">
  <div class="pbtxt">
    <label class="pbwhat" for="pb1-s1">A1 · Baseline the test suite</label>
    <p class="pbwhy">Run the full suite three times from a clean checkout. Record: one-command invocation, wall-clock runtime, pass rate, and the list of flaky tests. Why: the suite is the external truth the whole loop stands on — without a trusted, fast signal there is nothing for an agent to converge on (<a href="#e4-deepdive">E4 Verification-first</a>, <a href="#b1-deepdive">B1 Safe ordering</a>).</p>
    <div class="pbdone">DONE = runtime, pass rate and flaky list recorded in report §2; the suite runs headless with a single documented command.</div>
  </div>
</div>
```

- [ ] **Step 2: Fill the nine steps with this content**

| Step | Label + action | WHY links | DONE criterion |
|---|---|---|---|
| `pb1-s1` | A1 · Baseline the test suite (runtime, pass rate, flaky list; 3 clean runs) | `#e4-deepdive`, `#b1-deepdive` | numbers in report §2; one-command headless run documented |
| `pb1-s2` | A2 · Verify CI emits agent-readable signal (a deliberately broken test produces a machine-readable failure: exit code + parseable log/status) | `#e4-deepdive`, `#e7-deepdive` | broken-test experiment run; failure artifact linked in report §2 |
| `pb1-s3` | A3 · Capture the delivery baseline (DORA four keys retroactively from git/CI history + cost per merged PR; agree the before/after window and confirm access to git history, deploy logs, and the incident system) | `#e7-deepdive` (the day-0 DORA checklist); note in the prose: the baseline is captured now, at assess time — a pilot without it can be neither proven nor disproven (METR perception gap), so it cannot wait for PB5 | baseline numbers recorded in report §3; window + data access confirmed in writing |
| `pb1-s4` | B1 · Inventory source-of-truth artifacts (architecture docs, ADRs, specs, READMEs — owner + last-touched date + retrievability) | `#i1-deepdive`, `#i3-deepdive` | artifact table in report §4 with gaps explicitly listed |
| `pb1-s5` | C1 · Verify dev/prod separation and run a secrets scan on the repo history | `#e5-deepdive` + M7 (cite the Replit production-DB incident and GitGuardian 2026: AI-assisted commits leak secrets at 3.2% vs 1.5% baseline) | scan report attached; prod credentials proven unreachable from the dev environment |
| `pb1-s6` | C2 · Map write permissions (branch protection, CODEOWNERS, who/what can merge; where would an agent's write access stop today) | `#i2-deepdive`, `#e5-deepdive` | draft write-permission matrix in report §5 |
| `pb1-s7` | D1 · Name the editor/curator and measure review capacity (who reviews agent PRs, hours/week; cite E7's review bottleneck: +98% PRs, +91% review time) | `#p4-deepdive`, `#h4-deepdive`, `#e7-deepdive` | named owner(s) + weekly review budget recorded in report §6 |
| `pb1-s8` | E1 · Score the questionnaire and derive the L1–L5 recommendation | `#e6-deepdive` | filled questionnaire archived with the engagement notes; recommended level written into report §7 |
| `pb1-s9` | E2 · Deliver the report and run the F0 go/no-go with STOP criteria | `#b6-deepdive` | decision (go / no-go / go-with-preconditions) recorded with date, criteria and signatories |

- [ ] **Step 3: Add the two templates in §6**

Template 1 — questionnaire (`.pbtpl` block; the copy button precedes the pre). Unchanged at 24 points: the delivery baseline is measurement data captured by step A3, not a scored maturity dimension — scoring it would double-count evidence the gates already cover and would break the calibrated thresholds in the recommendation table.

```html
<div class="pbtpl"><button class="pbcopy" type="button" data-copy="pb1-tpl-quest">copy</button><pre id="pb1-tpl-quest">
# Agentic-readiness assessment — questionnaire (v1)
Client: ____________   Assessor: ____________   Date: ____________
Score each 0 (absent) / 1 (partial) / 2 (solid). Gate criteria marked [GATE] are
non-compensable: any [GATE] at 0 caps the recommendation at L1 regardless of total.

## A — Verification base
A1 [GATE] Trusted automated test suite exists and passes ........... 0 1 2
A2 [GATE] Full suite runs headless in under ~15 min ................ 0 1 2
A3 CI runs on every PR and blocks merge on red ..................... 0 1 2
A4 [GATE] CI failure output is machine-readable (agent-consumable) . 0 1 2

## B — Information architecture
B1 Architecture/decision docs exist and are findable from the repo . 0 1 2
B2 Docs freshness: last-touched within ~6 months for core docs ..... 0 1 2
B3 A newcomer can locate the source of truth for a feature ......... 0 1 2

## C — Governance minimum
C1 [GATE] Dev/prod separated; prod creds unreachable from dev ...... 0 1 2
C2 Secrets scan clean (or remediation plan agreed) ................. 0 1 2
C3 Branch protection + review requirement on the default branch .... 0 1 2

## D — Team readiness
D1 A named owner will curate agent config & review agent PRs ....... 0 1 2
D2 Review capacity exists (agent PRs will not queue for days) ...... 0 1 2

TOTAL ____ / 24        GATES PASSED ____ / 4
</pre></div>
```

Template 2 — report skeleton (`pb1-tpl-report`, same wrapper pattern) — includes the delivery-baseline section filled by step A3:

```html
<div class="pbtpl"><button class="pbcopy" type="button" data-copy="pb1-tpl-report">copy</button><pre id="pb1-tpl-report">
# Agentic-readiness assessment — report
Client / system: ____________     Date: ____________     Assessor: ____________

## 1 Executive summary
Recommendation: L__ entry, F0 scope: ____________. Go / No-go / Go with preconditions.

## 2 Verification base (steps A1–A2)
Suite runtime: ____  Pass rate: ____  Flaky tests: ____
CI signal experiment result: ____________

## 3 Delivery baseline (step A3)
Deploy frequency: ____  Lead time: ____  Change-fail rate: ____  Recovery time: ____
Cost per merged PR (tokens/seats): ____
Before/after window agreed: ____________  Data access confirmed (git / CI / incidents): ____

## 4 Information architecture (step B1)
| Artifact | Owner | Last touched | Retrievable from repo? |
|---|---|---|---|

## 5 Governance minimum (steps C1–C2)
Dev/prod separation: ____________   Secrets scan: ____________
Write-permission matrix (draft): ____________

## 6 Team readiness (step D1)
Editor/curator: ____________   Review budget: ____ h/week

## 7 Score & recommendation (steps E1–E2)
Total ____ / 24 · Gates ____ / 4 → recommended level L__ (rationale: ...)
Preconditions before F1: ____________

## 8 STOP criteria agreed for F0
(from B6: e.g. stability drop beyond agreed threshold, secrets leak,
unreviewed-merge incident — list the concrete triggers + who pulls the cord)
</pre></div>
```

- [ ] **Step 4: Add the recommendation table + STOP criteria in §6, exit gate in §7**

Recommendation table (`table.map` inside `<div class="figscroll">`), flagged as our synthesis in the surrounding prose:

| Score | Gates | Recommendation |
|---|---|---|
| < 10 | any | L1 only; engagement starts by fixing the base (PB2 becomes the deliverable, not a prerequisite) |
| 10–16 | 4/4 | L2 entry; F0 read-only archaeology can start (B4) |
| ≥ 17 | 4/4 | L3 pilot candidate; proceed to PB2 with the F0→F1 exit criteria from B6 |
| any | < 4/4 | no L2+ autonomy until the failed gate is fixed — non-compensable |

§7 `.callout pine` exit criteria: report delivered; delivery baseline recorded (report §3 is the pilot's "before" snapshot — PB5 compares against it); go/no-go recorded; if GO → PB2 with the report's §2 numbers as the bootstrap baseline. Three-sentence takeaway `.callout`. Closing note (`.closingnote`): standalone availability (PB1-assess-runbook.html), neighbours (E6, E7, B1, B6), the scoring model + gate criteria flagged as this workbook's synthesis, point-in-time facts marked for re-verification.

House style: dense English prose; every claim that has a number keeps the number; separate strong evidence (DORA, METR — independent) from vendor claims (GitGuardian — vendor telemetry, flag it) from our synthesis (the scoring model, the gate list).

- [ ] **Step 5: Sanity-check the body fragment**

Run: `python3 -c "import re;s=open('/tmp/claude-1000/-home-roan-WebstormProjects-agentic-sdlc-learning/65e0df03-9153-47e6-b224-70b53af01fae/scratchpad/pb1body.html').read();steps=re.findall(r'data-step=\"([\w-]+)\"',s);print(len(steps),sorted(steps))"`
Expected: `9` steps, `pb1-s1`…`pb1-s9`, no duplicates. (No commit — scratchpad file.)

---

### Task 5: Generate the standalone file `deep-dives/PB1-assess-runbook.html`

**Files:**
- Create: `deep-dives/PB1-assess-runbook.html`
- Consumes: the Task-4 body; the `<head>` of `deep-dives/E1-agent-model-harness-deepdive.html` (lines 1–133).

- [ ] **Step 1: Assemble the file**

Per the AUTHORING-GUIDE step-2 recipe:
1. Copy E1's full `<head>` (doctype through `</head>`); set `<title>PB1 Runbook — Assess: Client Maturity &amp; the F0 Entry Gate</title>`.
2. Append to the copied `<style>`, before `</style>`: the entire Task-4 `.pb*` CSS block, plus `.closingnote{font-family:var(--mono);font-size:11.5px;color:var(--soft);border-top:1px solid var(--line);padding-top:14px;margin-top:26px;line-height:1.7}` (copy the exact `.closingnote` rule from any existing deep-dive file instead if it differs), plus `svg .edPB1{stroke:#57656F;stroke-width:1.3;fill:none;marker-end:url(#ahPB1a)}`.
3. Header block: copy E1's `<header class="hdr">` with tag `PB1 · RUNBOOK`, h1 `Assess: Client Maturity &amp; the F0 Entry Gate`, breadcrumb `companion to module M9 · Playbook`.
4. `<nav class="toc">` listing `#s0`…`#s7` with the section titles from Task 4.
5. `<main>` (do not forget the wrapper — the H2–H4 missing-`<main>` layout bug is documented in v1.24) containing the body, with `id="sN"` added to each `<h2>` — loop N from 7 down to 0 so `s1` does not match inside `s10`-style ids.
6. In the runbook the overlay theory links (`#e4-deepdive` etc.) do not resolve in the standalone document — that is the repo-wide convention for standalone copies (they reference workbook overlays); leave them as-is, matching existing deep dives.
7. After §1's `.pbnote`, this file keeps the same sentence — the standalone copy does not persist.
8. Close with E1-style `<footer>` and this script (replaces E1's backtop-only script; keep the backtop part, add the runbook part):

```html
<script>
(function(){
  document.querySelectorAll("figure>svg").forEach(function(svg){
    if(svg.parentNode&&svg.parentNode.classList.contains("figscroll"))return;
    var sc=document.createElement("div");sc.className="figscroll";
    var wr=document.createElement("div");wr.className="figwrap";
    svg.parentNode.insertBefore(wr,svg);wr.appendChild(sc);sc.appendChild(svg);
  });
  var b=document.createElement("button");b.className="backtop";b.type="button";
  b.setAttribute("aria-label","Back to top");
  b.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>';
  document.body.appendChild(b);
  b.addEventListener("click",function(){
    var rm=window.matchMedia&&window.matchMedia("(prefers-reduced-motion:reduce)").matches;
    window.scrollTo({top:0,behavior:rm?"auto":"smooth"});
  });
  var tick=false;
  function upd(){var d=document.documentElement,t=window.pageYOffset||d.scrollTop;b.classList.toggle("show",t>640);tick=false;}
  window.addEventListener("scroll",function(){if(!tick){tick=true;requestAnimationFrame(upd);}},{passive:true});
  /* runbook: live progress count (non-persistent) + copy buttons */
  function upd2(){var t=document.querySelectorAll(".pbck").length,d=document.querySelectorAll(".pbck:checked").length;
    document.querySelectorAll("[data-pbprog]").forEach(function(el){el.textContent=d+" / "+t+" steps done";});}
  document.addEventListener("change",function(e){if(e.target.closest(".pbck"))upd2();});
  upd2();
  document.addEventListener("click",function(e){
    var b2=e.target.closest(".pbcopy");if(!b2)return;
    var pre=document.getElementById(b2.dataset.copy);if(!pre)return;
    var txt=pre.textContent;
    function ok(){b2.textContent="copied ✓";setTimeout(function(){b2.textContent="copy";},1400);}
    function fb(){var ta=document.createElement("textarea");ta.value=txt;document.body.appendChild(ta);ta.select();try{document.execCommand("copy");ok();}catch(err){}document.body.removeChild(ta);}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(ok,fb);}else{fb();}
  });
})();
</script>
```

- [ ] **Step 2: Run the validator**

Run: `python3 scripts/validate.py`
Expected: `PB1-assess-runbook.html: HTML tags balanced`, `1 SVG(s) well-formed`, `all N markup classes covered by CSS/JS`, `TOC anchors resolve`.

- [ ] **Step 3: Commit**

```bash
git add deep-dives/PB1-assess-runbook.html
git commit -m "feat: PB1 Assess runbook - standalone companion"
```

---

### Task 6: Overlay — insert, wire, and link PB1 in the workbook

**Files:**
- Modify: `workbook/agentic-development-study.html`
- Consumes: the Task-4 body verbatim (NOT the standalone file's body — no `id="sN"` attributes in the overlay copy); the token contract: anchor `#pb1-deepdive`, overlay id `pb1ov`, close attr `data-pb1close`.

- [ ] **Step 1: Build and insert the overlay**

Wrap the body:

```html
<div class="e1ov" id="pb1ov" role="dialog" aria-modal="true" aria-label="PB1 runbook">
  <div class="panel">
    <div class="bar"><span class="tag">PB1 · RUNBOOK</span><h3>Assess: Client Maturity &amp; the F0 Entry Gate</h3>
      <button class="x" type="button" data-pb1close>✕ close</button></div>
    <div class="body">
… Task-4 body …
    </div>
  </div>
</div>
```

Insert immediately before `<footer>` (after the last existing overlay).

- [ ] **Step 2: Add the scoped marker CSS**

After the last `.e1ov svg .ed*` rule (D2's), add:

```css
.e1ov svg .edPB1{stroke:#57656F;stroke-width:1.3;fill:none;marker-end:url(#ahPB1a)}
```

(The `.pb*` component CSS from Task 3 is global, so it styles the overlay copy already.)

- [ ] **Step 3: Prepend the JS handler**

Immediately before `var d2ov=document.getElementById('d2ov');` insert:

```js
var pb1ov=document.getElementById('pb1ov');
if(pb1ov){
  document.addEventListener('click',function(e){
    var open=e.target.closest('a[href="#pb1-deepdive"]');
    if(open){e.preventDefault();pb1ov.classList.add('show');document.body.style.overflow='hidden';pb1ov.querySelector('.panel').scrollTop=0;return;}
    if(e.target.closest('[data-pb1close]')||e.target===pb1ov){pb1ov.classList.remove('show');document.body.style.overflow='';}
  },true);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&pb1ov.classList.contains('show')){pb1ov.classList.remove('show');document.body.style.overflow='';}});
}
```

- [ ] **Step 4: Link the topic**

In the `pb-assess` topic's `src` array, prepend before the existing theory entry:

```js
{t:"↳ PB1 Runbook — open here (assessment checklist, delivery-baseline capture, questionnaire & report templates, the F0 go/no-go)",u:"#pb1-deepdive"},
```

- [ ] **Step 5: Run the validator**

Run: `python3 scripts/validate.py`
Expected: all pass; `#pb1-deepdive wired x2 (+1 handler)`; `playbook step ids unique (9 step(s))`; topic count 60.

- [ ] **Step 6: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat: PB1 Assess runbook - workbook overlay, handler, topic link"
```

---

### Task 7: Version v1.48, docs, and the browser smoke test

**Files:**
- Modify: `workbook/agentic-development-study.html` (version modal + footer)
- Modify: `docs/CHANGELOG.md`, `docs/ROADMAP.md`, `docs/AUTHORING-GUIDE.md`, `docs/CONTENT-MAP.md`

- [ ] **Step 1: Version-history entry**

In the workbook, after `<p class="kicker">Every released version of this workbook</p>` and before the v1.47 `.vitem`, insert:

```html
      <div class="vitem"><span class="vv">v1.48</span><span class="vd">2026-07-18</span><p><strong>NEW MODULE M9 — Playbook: from theory to practice. First runbook PB1 Assess.</strong> The practice layer lands inside the workbook: five <span class="mono">pb-</span> topics ordered by the engagement journey (Assess → Bootstrap → Harness → Handoff → Pilot), built for the internal team to carry the methodology to a brownfield client. PB1 ships complete — a runbook companion in both copies (PB1-assess-runbook.html + overlay) with nine checklist steps across five phases (verification base &amp; delivery baseline, information architecture, governance minimum, team readiness, evaluation), each step carrying the action, the theory link that justifies it, and a DONE criterion; plus two copy-paste templates (readiness questionnaire with four non-compensable [GATE] criteria, assessment-report skeleton with a delivery-baseline section), the score→L1–L5 recommendation table and the F0 go/no-go with STOP criteria (the scoring model is our synthesis, flagged). The delivery baseline (DORA keys + cost per merged PR) is captured at assess time — a pilot without it can be neither proven nor disproven. NEW interaction layer: runbook checkboxes persist through the existing store (<span class="mono">agentic-study-v1</span>, new <span class="mono">pb</span> field, mirrored into cross-device sync), with a per-runbook progress chip and copy buttons; the standalone copy is deliberately non-persistent. PB2–PB5 are visible as in-preparation topics (one runbook per future version; PB3's templates will be the harness starter kit — runnable hook/permission/CI configs, not prose). Validator extended: <span class="mono">pb-</span> prefix recognised, checklist step ids checked for uniqueness (they are frozen progress keys, like topic ids).</p></div>
```

- [ ] **Step 2: Footer + docs mirrors**

1. Footer: `<b>v1.47</b> · 2026-07-18 ·` → `<b>v1.48</b> · 2026-07-18 ·`.
2. `docs/CHANGELOG.md`: prepend a `## v1.48 — 2026-07-18` entry mirroring the vitem text (plain markdown, match the file's existing entry style).
3. `docs/CONTENT-MAP.md`: header line — update the companion count (35 → 37: D2 shipped in v1.47 was never counted, PB1 adds one; verify by `ls deep-dives/*.html | wc -l`) and the version reference to v1.48; in the M9 table PB1's deep-dive cell already says `PB1-assess-runbook.html + overlay`.
4. `docs/ROADMAP.md`: mark the M9 step done and plan the rest — add under "Next":

```markdown
### M9 — Playbook module (the practice layer)
Decided 2026-07-18 (spec: docs/superpowers/specs/2026-07-18-playbook-module-design.md):
the theory→practice layer lives inside the workbook as runbooks ordered by the
engagement journey; the harness starter-kit templates and hands-on labs derive from
these runbooks later — no separate repo.
- ~~Module skeleton (pb- topics, store-backed checklists) + **PB1 Assess** runbook~~ — **done (v1.48)**.
- Next, one per version: **PB2 Bootstrap** (B1–B3 distilled) → **PB3 Harness** (E1–E5, I2 —
  templates ship as runnable configs: hook scripts, permission baselines, CI gates, per the
  E5 litmus) → **PB4 Handoff** (H1–H4) → **PB5 Pilot** (E7, B6 — converges with T2's pilot
  playbook; compares against the delivery baseline captured in PB1).
- Backlog (deliberately deferred):
  - **Field-report loop** — a completed client runbook feeds an anonymized results entry
    back into the relevant deep dive; the corpus is currently 100% externally cited, and
    pilot outcomes are the first first-party evidence. The persisted checklist data in
    `store` is the hook for it.
  - **Team-level tracking** — `store` is per-browser/per-device; aggregating progress
    across a Sudo team at a client would need shared state. Deferred: adding it would
    reopen the rejected "engagement mode" app-creep.
```

5. `docs/AUTHORING-GUIDE.md`: append a section:

```markdown
## Runbook companions (M9 playbook topics)

Runbooks are deep dives with a fixed practice shape — same two-copies recipe as above
(token `pb1` → `#pb1-deepdive`, `pb1ov`, `data-pb1close`, marker `ahPB1a`, edge `edPB1`),
plus:
- Shape: `§0 why → §1 how to run it (progress chip + persistence note) → phase sections
  with steps → evaluation §  with templates → exit gate & takeaways`.
- Each step: `.pbstep` block with `input.pbck` carrying `data-pb="<topic id>"` and a
  **frozen** `data-step="pbN-sM"` id (progress keys — same never-rename rule as topic ids;
  the validator enforces uniqueness), a `.pbwhat` label, `.pbwhy` with overlay links to the
  theory, and a `.pbdone` criterion.
- Templates: `.pbtpl` wrapper + `.pbcopy` button with `data-copy` pointing at the `<pre>` id.
  Where the underlying theory is deterministic, the template is the **real runnable
  artifact** — hook scripts, permission baselines, CI gate configs (the E5 litmus: what
  must never happen ships as enforcement, not advice). This applies above all to PB3
  Harness, whose templates are the client-facing starter kit.
- Persistence: workbook only — `state.pb` via the single store; the standalone copy ships
  the non-persistent script (live count + copy) and the `.pbnote` disclaimer.
- The `.pb*` CSS block lives in the workbook `<style>` and is copied into each standalone
  runbook head.
```

- [ ] **Step 3: Run the validator**

Run: `python3 scripts/validate.py`
Expected: all pass.

- [ ] **Step 4: Browser smoke test (manual, required by the spec)**

Open `workbook/agentic-development-study.html` in a browser (or drive it with the chrome-devtools/playwright MCP tools):
1. M9 appears in the sidebar nav and renders 5 topics; PB1 shows the "Open panel" runbook card.
2. Open the PB1 overlay → check two steps → close → reload the page → reopen: both stay checked and the chip reads `2 / 9 steps done`; the save indicator flashed `saving… → saved`.
3. Click a `copy` button → button flips to `copied ✓` and the clipboard holds the template.
4. Uncheck a step → reload → it stays unchecked (removal persists).
5. Export data (sidebar Data → export) → the JSON contains `"pb":{"pb-assess":[…]}`.
6. Open `deep-dives/PB1-assess-runbook.html` directly: checkboxes toggle and the count updates, but reload resets them; the `.pbnote` disclaimer is visible; copy buttons work.
7. A theory link inside the overlay (e.g. E4) opens the E4 overlay on top / in place.

Record the results; any failure is a stop-and-fix before the final commit.

- [ ] **Step 5: Final commit**

```bash
git add workbook/agentic-development-study.html docs/CHANGELOG.md docs/ROADMAP.md docs/AUTHORING-GUIDE.md docs/CONTENT-MAP.md
git commit -m "release v1.48: M9 Playbook module + PB1 Assess runbook"
```
