# Highlight-notes on Deep Dives — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let a reader select text inside a workbook deep-dive overlay, save it as a note (with an optional personal thought added later), see all such notes in one modal on the main page, and click any note to jump back to its exact — still-highlighted — passage.

**Architecture:** All changes live in the single file `workbook/agentic-development-study.html`. Highlights are stored as a new `state.highlights` array persisted through the existing `store` backend (`agentic-study-v1`). Passages are re-located by **text-quote anchoring** (quote + short prefix/suffix + occurrence index) and wrapped in runtime-only `<mark>` elements on overlay open, hooked into the existing per-overlay `MutationObserver` inside `initDeepDiveNav()`.

**Tech Stack:** Hand-authored zero-build single-file HTML + vanilla ES (no framework, no bundler, no test runner). Deterministic gate: `python3 scripts/validate.py`. Behavioural gate: load the file in a browser.

## Global Constraints

- **Only edit `workbook/agentic-development-study.html`** for the feature itself (plus `docs/CHANGELOG.md` and `docs/ARCHITECTURE.md` in the housekeeping task). Do **not** touch `deep-dives/*.html`.
- **Stable topic IDs** — never rename any topic `id`.
- **All persistence goes through the single `store` backend** under key `agentic-study-v1`; reuse `state`, `scheduleSave()`, `saveNow()`. Never call `localStorage`/`window.storage` directly.
- **No external links or assets** — everything inline; no new CDN/font/image dependencies.
- **`<mark>` highlights are runtime-only** — never written into the static file (so `validate.py` is unaffected by them).
- **Topic count must stay 52.**
- After every task that edits the file, `python3 scripts/validate.py` must exit 0 (green).
- **Build gotcha:** apostrophes inside Python heredocs break tooling; there is no Python string-building here, but when using `Edit`, match whitespace exactly. Bash brace-expansion may be unavailable — list paths explicitly.
- Existing helpers available in the trailing `<script>`: `$(sel,root)`, `$$(sel,root)`, `esc(s)`, `state`, `scheduleSave()`, `store`, `storeOK`. Use them.

---

## File Structure

Single file, five logical regions touched (all in `workbook/agentic-development-study.html`):

| Region | Location (current line) | Task |
|---|---|---|
| `state` object + `loadState`/`exportData`/`importData` | 4761, 4786, 4811, 4820 | Task 1 |
| CSS (after version-modal rules) | ~305 | Task 2 |
| Sidebar "Data" button group | 414–417 | Task 3 |
| Notes modal HTML (before `<footer>`) | before 3659 | Task 3 |
| Trailing `<script>` — new highlight helpers + capture + apply + notes modal JS | append before final init IIFE (~5369) | Tasks 3,4,5 |
| `initDeepDiveNav()` skip-list + MutationObserver hook | 5271, 5358 | Task 5 |
| init IIFE calls | ~5377 | Tasks 3,4,5 |
| Version bump (`#verov` vitem 2043, footer 3660, CHANGELOG) + ARCHITECTURE note | — | Task 6 |

---

## Task 1: Data layer — `state.highlights`, load, export, import merge

**Files:**
- Modify: `workbook/agentic-development-study.html:4761` (state), `:4786` (loadState), `:4811` (exportData), `:4820` (importData)

**Interfaces:**
- Produces: `state.highlights` — `Array<{id:string, ov:string, title:string, quote:string, prefix:string, suffix:string, occ:number, thought:string, created:string}>`. Later tasks push to it, read/filter it, and mutate `thought`.

- [ ] **Step 1: Add the field to the `state` initializer**

At line 4761, change:
```js
let state={progress:{},notes:{},seen:{},updatedAt:null};
```
to:
```js
let state={progress:{},notes:{},seen:{},highlights:[],updatedAt:null};
```

- [ ] **Step 2: Load highlights in `loadState`**

In `loadState` (line ~4791), change:
```js
    if(r&&r.value){const p=JSON.parse(r.value);state.progress=p.progress||{};state.notes=p.notes||{};state.seen=p.seen||{};}
```
to:
```js
    if(r&&r.value){const p=JSON.parse(r.value);state.progress=p.progress||{};state.notes=p.notes||{};state.seen=p.seen||{};state.highlights=Array.isArray(p.highlights)?p.highlights:[];}
```

- [ ] **Step 3: Include highlights in the export payload**

In `exportData` (line ~4812), change:
```js
  const payload={key:KEY,exportedAt:new Date().toISOString(),progress:state.progress,notes:state.notes,seen:state.seen};
```
to:
```js
  const payload={key:KEY,exportedAt:new Date().toISOString(),progress:state.progress,notes:state.notes,seen:state.seen,highlights:state.highlights};
```

- [ ] **Step 4: Merge highlights on import (dedupe by id) + loosen guard**

In `importData` (lines ~4825–4828), change:
```js
      if(!p||typeof p!=='object'||(!p.progress&&!p.notes))throw new Error('not an export file');
      Object.assign(state.progress,p.progress||{});
      Object.assign(state.notes,p.notes||{});
      if(p.seen)Object.assign(state.seen,p.seen);
```
to:
```js
      if(!p||typeof p!=='object'||(!p.progress&&!p.notes&&!p.highlights))throw new Error('not an export file');
      Object.assign(state.progress,p.progress||{});
      Object.assign(state.notes,p.notes||{});
      if(p.seen)Object.assign(state.seen,p.seen);
      if(Array.isArray(p.highlights)){var have={};state.highlights.forEach(function(h){have[h.id]=1;});p.highlights.forEach(function(h){if(h&&h.id&&!have[h.id])state.highlights.push(h);});}
```

- [ ] **Step 5: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0; output ends with a topic count of **52** and no error lines. (The trailing `<script>` must still parse under `node --check`.)

- [ ] **Step 6: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(highlights): add state.highlights with load/export/import"
```

---

## Task 2: CSS — mark, flash, floating save button, notes-modal cards

**Files:**
- Modify: `workbook/agentic-development-study.html` — insert a CSS block immediately **after** line 305 (`.e1ov .vitem p{...}`) and before the `@media (max-width:760px)` rule at 306. (Placing it right after the version-modal rules keeps related overlay CSS together.)

**Interfaces:**
- Produces CSS classes used by later tasks: `mark.hl-note`, `mark.hl-note.flash`, `#hlSave`, `#hlToast`, `#notesBody`, `.hlcard`, `.hlcard blockquote`, `.hlcard .hlmeta`, `.hlcard textarea`, `.hlcard .hlact`, `.hlgroup`, `.hlempty`.

- [ ] **Step 1: Insert the CSS block**

After line 305, insert:
```css
/* ------- highlight-notes ------- */
mark.hl-note{background:linear-gradient(transparent 55%, #FCE8C0 55%);color:inherit;border-radius:2px;padding:0 .5px;cursor:default}
mark.hl-note.flash{animation:hlflash 1.3s ease-out}
@keyframes hlflash{0%{background:#F6C858}35%{background:#F6C858}100%{background:linear-gradient(transparent 55%, #FCE8C0 55%)}}
#hlSave{position:fixed;z-index:70;display:none;font-family:var(--mono);font-size:11px;font-weight:600;color:#fff;background:var(--cobalt-deep);border:0;border-radius:999px;padding:6px 12px;cursor:pointer;box-shadow:0 4px 14px rgba(20,40,90,.28)}
#hlSave:hover{background:var(--cobalt)}
#hlToast{position:fixed;z-index:71;left:50%;bottom:26px;transform:translateX(-50%);display:none;font-family:var(--mono);font-size:11px;color:#fff;background:#20303f;border-radius:8px;padding:8px 14px;box-shadow:0 6px 20px rgba(0,0,0,.25)}
#hlToast.show{display:block;animation:hltoast 2.2s ease forwards}
@keyframes hltoast{0%{opacity:0;transform:translate(-50%,8px)}12%{opacity:1;transform:translate(-50%,0)}80%{opacity:1}100%{opacity:0}}
#notesBody{padding:4px 0 8px}
.hlgroup{margin:0 0 22px}
.hlgroup>h4{font-family:var(--disp);font-size:14px;margin:0 0 10px;color:var(--ink);border-bottom:1px solid var(--line);padding-bottom:6px}
.hlcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:0 0 10px}
.hlcard blockquote{margin:0 0 8px;padding:6px 0 6px 12px;border-left:3px solid var(--amber);font-family:var(--serif,inherit);font-size:14px;line-height:1.5;color:var(--ink);white-space:normal;overflow-wrap:anywhere}
.hlcard .hlmeta{font-family:var(--mono);font-size:10px;color:var(--soft);margin:0 0 8px}
.hlcard textarea{width:100%;min-height:52px;resize:vertical;font-family:var(--mono);font-size:12px;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:8px;padding:8px}
.hlcard textarea::placeholder{color:var(--idle)}
.hlcard textarea:focus{border-color:var(--cobalt);outline:none}
.hlcard .hlact{display:flex;gap:10px;align-items:center;margin-top:8px}
.hlcard .hlopen{font-family:var(--mono);font-size:11px;font-weight:600;color:var(--cobalt-deep);background:#EBEFFA;border:1px solid #D6DDF3;border-radius:999px;padding:4px 11px;cursor:pointer}
.hlcard .hlopen:hover{background:#DFE6F8}
.hlcard .hldel{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--soft);background:none;border:0;cursor:pointer}
.hlcard .hldel:hover{color:#b3402e}
.hlempty{font-size:14px;color:var(--soft);padding:14px 0}
```

> Note: `var(--serif)`/`var(--amber)`/`var(--card)`/`var(--line)`/`var(--soft)`/`var(--idle)`/`var(--ink)`/`var(--cobalt)`/`var(--cobalt-deep)` are existing tokens in `:root`. If `--serif` is not defined, the `inherit` fallback applies; the others are all used elsewhere in the file (confirmed by the `.note`/`.vitem` rules).

- [ ] **Step 2: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0, no errors. (CSS lives inside the single `<style>`; tag balance and topic count unchanged.)

- [ ] **Step 3: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(highlights): add CSS for marks, save button, toast, notes cards"
```

---

## Task 3: Notes modal — button, shell, render, open/close wiring

**Files:**
- Modify: `workbook/agentic-development-study.html` — sidebar Data group (414–417), new modal HTML before `<footer>` (line 3659), new JS appended before the init IIFE (~5369), init IIFE (~5377), and `initDeepDiveNav()` skip-list (5271).

**Interfaces:**
- Consumes: `state.highlights` (Task 1); `esc()`, `$`, `$$`, `scheduleSave()`.
- Produces:
  - `renderNotes()` — rebuilds `#notesBody` from `state.highlights`, grouped by `title`.
  - `updateNotesCount()` — sets `#notesN` text to `(N)`.
  - `openNotes()` / `closeNotes()` — show/hide `#notesov`.
  - `hlOpenNote(h)` — **stub in this task** (real body in Task 5): `closeNotes()` then opens `#<h.ov>ov`. Task 5 extends it with scroll+flash.
  - DOM ids: `#notesbtn`, `#notesN`, `#notesov`, `#notesBody`; attributes `data-notesopen`, `data-notesclose`.

- [ ] **Step 1: Add the sidebar button**

In the Data group (line ~416), change:
```html
      <button id="impData" title="Merge a previously exported JSON back in">import data</button>
```
to:
```html
      <button id="impData" title="Merge a previously exported JSON back in">import data</button>
      <button id="notesbtn" type="button" data-notesopen title="Your saved highlight-notes from the deep dives">my notes <span id="notesN">(0)</span></button>
```

- [ ] **Step 2: Add the modal shell before `<footer>`**

Immediately before line 3659 (`<footer>`), insert:
```html
<div class="e1ov" id="notesov" role="dialog" aria-modal="true" aria-label="My highlight-notes">
  <div class="panel">
    <div class="bar"><span class="tag">MY NOTES</span><h3>Highlight-notes</h3>
      <button class="x" type="button" data-notesclose>✕ close</button></div>
    <div class="body"><div id="notesBody"></div></div>
  </div>
</div>
```

- [ ] **Step 3: Exclude `#notesov` from deep-dive nav**

At line 5271, change:
```js
    if(ov.id==='verov')return;
```
to:
```js
    if(ov.id==='verov'||ov.id==='notesov')return;
```

- [ ] **Step 4: Append the notes-modal JS**

Immediately before the `/* ---------- init ---------- */` comment (line ~5369), insert:
```js
/* ===== highlight-notes: central modal ===== */
function updateNotesCount(){var n=$('#notesN');if(n)n.textContent='('+state.highlights.length+')';}
function hlToast(msg){var t=$('#hlToast');if(!t){t=document.createElement('div');t.id='hlToast';document.body.appendChild(t);}t.textContent=msg;t.classList.remove('show');void t.offsetWidth;t.classList.add('show');}
function renderNotes(){
  var body=$('#notesBody');if(!body)return;
  if(!state.highlights.length){body.innerHTML='<div class="hlempty">No highlight-notes yet. Open a deep dive, select any passage, and choose “+ save as note”. Your saved passages collect here.</div>';return;}
  var groups={},order=[];
  state.highlights.forEach(function(h){if(!groups[h.ov]){groups[h.ov]={title:h.title||h.ov,items:[]};order.push(h.ov);}groups[h.ov].items.push(h);});
  body.innerHTML=order.map(function(ov){
    var g=groups[ov];
    var cards=g.items.slice().sort(function(a,b){return (b.created||'').localeCompare(a.created||'');}).map(function(h){
      var when=(h.created||'').slice(0,10);
      return '<div class="hlcard" data-hid="'+esc(h.id)+'">'+
        '<blockquote>'+esc(h.quote||'')+'</blockquote>'+
        '<div class="hlmeta">saved '+esc(when)+'</div>'+
        '<textarea data-hthought="'+esc(h.id)+'" placeholder="your thought on this… (saved automatically)">'+esc(h.thought||'')+'</textarea>'+
        '<div class="hlact"><button type="button" class="hlopen" data-hopen="'+esc(h.id)+'">open in deep dive →</button>'+
        '<button type="button" class="hldel" data-hdel="'+esc(h.id)+'">delete</button></div>'+
        '</div>';
    }).join('');
    return '<div class="hlgroup"><h4>'+esc(g.title)+'</h4>'+cards+'</div>';
  }).join('');
}
function openNotes(){var ov=$('#notesov');if(!ov)return;renderNotes();ov.classList.add('show');document.body.style.overflow='hidden';var p=ov.querySelector('.panel');if(p)p.scrollTop=0;}
function closeNotes(){var ov=$('#notesov');if(!ov)return;ov.classList.remove('show');document.body.style.overflow='';}
function hlOpenNote(h){closeNotes();var ov=document.getElementById(h.ov+'ov');if(!ov)return;ov.classList.add('show');document.body.style.overflow='hidden';var p=ov.querySelector('.panel');if(p)p.scrollTop=0;}
function initNotes(){
  var openers=$('#notesbtn');
  document.addEventListener('click',function(e){
    if(e.target.closest('[data-notesopen]')){openNotes();return;}
    if(e.target.closest('[data-notesclose]')||e.target===$('#notesov')){closeNotes();return;}
    var op=e.target.closest('[data-hopen]');
    if(op){var h=state.highlights.filter(function(x){return x.id===op.getAttribute('data-hopen');})[0];if(h)hlOpenNote(h);return;}
    var del=e.target.closest('[data-hdel]');
    if(del){var id=del.getAttribute('data-hdel');state.highlights=state.highlights.filter(function(x){return x.id!==id;});scheduleSave();updateNotesCount();renderNotes();var ovEl=del.closest('.hlcard');return;}
  });
  var nb=$('#notesBody');
  if(nb)nb.addEventListener('input',function(e){var ta=e.target.closest('textarea[data-hthought]');if(!ta)return;var id=ta.getAttribute('data-hthought');var h=state.highlights.filter(function(x){return x.id===id;})[0];if(h){h.thought=ta.value;scheduleSave();}});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&$('#notesov')&&$('#notesov').classList.contains('show'))closeNotes();});
  updateNotesCount();
}
```

- [ ] **Step 5: Call `initNotes()` from the init IIFE**

In the init IIFE (after `initDeepDiveNav();`, line ~5378), add on the next line:
```js
  initNotes();
```

- [ ] **Step 6: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0; topic count 52; every `#*-deepdive` anchor still appears exactly twice; JS parses.

- [ ] **Step 7: Browser check**

Open `workbook/agentic-development-study.html` in a browser (or use the `run` skill). Confirm: a **"my notes (0)"** button appears in the sidebar Data group; clicking it opens a modal with the empty-state message; the ✕ button, backdrop click, and Escape all close it. No console errors.

- [ ] **Step 8: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(highlights): notes modal, sidebar button, render + open/close"
```

---

## Task 4: Capture — selection detection, floating button, text-anchor, save

**Files:**
- Modify: `workbook/agentic-development-study.html` — append JS before the init IIFE (~5369); add one call in the init IIFE.

**Interfaces:**
- Consumes: `state.highlights` (Task 1); `updateNotesCount()`, `hlToast()` (Task 3); `scheduleSave()`.
- Produces (shared with Task 5):
  - `hlTextMap(root)` → `{text:string, nodes:Array<{node:Text,start:number,end:number}>}` — visible text of `root`, skipping `<svg>/<script>/<style>`.
  - `hlOccurrence(text, quote, at)` → `number` — index of the occurrence starting at char `at`.
  - `hlOverlayToken(ov)` → `string` (`"i4ov"`→`"i4"`); `hlOverlayTitle(ov)` → `string` (`"I4 · Memory Systems for Agents"`).
  - `hlId()` → unique string id.
  - `applyHighlights(ov)` — **defined in Task 5**; called here after a save. In this task, guard the call: `if(typeof applyHighlights==='function')applyHighlights(ov);`

- [ ] **Step 1: Append the capture JS**

Immediately before the `/* ---------- init ---------- */` comment, insert:
```js
/* ===== highlight-notes: shared anchoring helpers ===== */
var HL_CTX=32;
function hlOverlayToken(ov){return ov.id.replace(/ov$/,'');}
function hlOverlayTitle(ov){
  var tag=ov.querySelector('.bar .tag'),h3=ov.querySelector('.bar h3');
  var code=tag?tag.textContent.split('·')[0].replace(/[▾▾\s]+$/,'').trim():hlOverlayToken(ov).toUpperCase();
  var name=h3?h3.textContent.trim():'';
  return code+(name?' · '+name:'');
}
function hlTextMap(root){
  var nodes=[],parts=[],total=0;
  var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
    if(!n.nodeValue)return NodeFilter.FILTER_REJECT;
    var p=n.parentNode;
    while(p&&p!==root){var t=p.nodeName.toLowerCase();if(t==='svg'||t==='script'||t==='style')return NodeFilter.FILTER_REJECT;p=p.parentNode;}
    return NodeFilter.FILTER_ACCEPT;
  }});
  var n;while((n=w.nextNode())){var len=n.nodeValue.length;nodes.push({node:n,start:total,end:total+len});parts.push(n.nodeValue);total+=len;}
  return {text:parts.join(''),nodes:nodes};
}
function hlOffsetOf(map,container,offset){
  if(container.nodeType===3){for(var i=0;i<map.nodes.length;i++){if(map.nodes[i].node===container)return map.nodes[i].start+offset;}return -1;}
  var child=container.childNodes[offset];
  if(child){for(var j=0;j<map.nodes.length;j++){if(child===map.nodes[j].node||(child.contains&&child.contains(map.nodes[j].node)))return map.nodes[j].start;}}
  for(var k=0;k<map.nodes.length;k++){if(container.contains&&container.contains(map.nodes[k].node))return map.nodes[k].start;}
  return -1;
}
function hlOccurrence(text,quote,at){var i=-1,c=0;while((i=text.indexOf(quote,i+1))!==-1){if(i===at)return c;c++;}return 0;}
function hlId(){return 'h_'+Date.now().toString(36)+'_'+Math.random().toString(36).slice(2,7);}

/* ===== highlight-notes: capture ===== */
function hlCaptureSelection(){
  var sel=window.getSelection();
  if(!sel||sel.rangeCount===0||sel.isCollapsed)return null;
  var range=sel.getRangeAt(0);
  var node=range.commonAncestorContainer;
  var host=(node.nodeType===3?node.parentNode:node);
  var ov=host&&host.closest?host.closest('.e1ov[role="dialog"]'):null;
  if(!ov||ov.id==='verov'||ov.id==='notesov')return null;
  var panel=ov.querySelector('.panel');if(!panel)return null;
  var map=hlTextMap(panel);
  var gS=hlOffsetOf(map,range.startContainer,range.startOffset);
  var gE=hlOffsetOf(map,range.endContainer,range.endOffset);
  if(gS<0||gE<0||gE<=gS)return null;
  var quote=map.text.slice(gS,gE);
  if(quote.replace(/\s+/g,'').length<3)return null;
  return {ov:hlOverlayToken(ov),title:hlOverlayTitle(ov),quote:quote,
    prefix:map.text.slice(Math.max(0,gS-HL_CTX),gS),suffix:map.text.slice(gE,gE+HL_CTX),
    occ:hlOccurrence(map.text,quote,gS)};
}
function initCapture(){
  var btn=document.createElement('button');btn.id='hlSave';btn.type='button';btn.textContent='+ save as note';
  document.body.appendChild(btn);
  var pending=null;
  function hide(){btn.style.display='none';pending=null;}
  function evaluate(){
    var cap=hlCaptureSelection();
    if(!cap){hide();return;}
    var sel=window.getSelection(),rect=sel.getRangeAt(0).getBoundingClientRect();
    if(!rect||(!rect.width&&!rect.height)){hide();return;}
    pending=cap;btn.style.display='block';
    var top=rect.bottom+6,left=rect.left;
    top=Math.min(top,window.innerHeight-38);left=Math.min(left,window.innerWidth-140);
    btn.style.top=top+'px';btn.style.left=Math.max(6,left)+'px';
  }
  document.addEventListener('mouseup',function(){setTimeout(evaluate,10);});
  document.addEventListener('keyup',function(e){if(e.key==='Shift'||e.shiftKey)setTimeout(evaluate,10);});
  document.addEventListener('scroll',function(){if(btn.style.display==='block')hide();},true);
  btn.addEventListener('mousedown',function(e){e.preventDefault();});
  btn.addEventListener('click',function(){
    if(!pending)return;
    var h={id:hlId(),ov:pending.ov,title:pending.title,quote:pending.quote,prefix:pending.prefix,suffix:pending.suffix,occ:pending.occ,thought:'',created:new Date().toISOString()};
    state.highlights.push(h);scheduleSave();updateNotesCount();
    var ov=document.getElementById(h.ov+'ov');if(ov&&typeof applyHighlights==='function')applyHighlights(ov);
    var s=window.getSelection();if(s)s.removeAllRanges();
    hide();hlToast('saved — add your thought in “my notes”');
  });
}
```

- [ ] **Step 2: Call `initCapture()` from the init IIFE**

After the `initNotes();` line added in Task 3, add:
```js
  initCapture();
```

- [ ] **Step 3: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0; JS parses; topic count 52.

- [ ] **Step 4: Browser check**

Open the file. Open any deep dive (e.g. click a "Go deeper" deep-dive link, or the E4 link). Select a sentence of prose. Confirm: the **"+ save as note"** button appears just below the selection; clicking it shows the toast, clears the selection, and increments the sidebar **"my notes (N)"** count. Open the notes modal — the new note shows its quoted passage under the correct deep-dive group. Type a thought into the card's textarea, close and reopen the modal — the thought persists. Confirm no button appears when selecting text on the **main page** (outside overlays) or inside the version-history modal. No console errors.

- [ ] **Step 5: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(highlights): selection capture, floating save button, text anchoring"
```

---

## Task 5: Re-highlight — locate, cross-node wrap, MutationObserver hook, scroll+flash

**Files:**
- Modify: `workbook/agentic-development-study.html` — append JS before the init IIFE (~5369); extend the MutationObserver in `initDeepDiveNav()` (5358); extend `hlOpenNote()` (from Task 3).

**Interfaces:**
- Consumes: `hlTextMap()`, `hlOverlayToken()` (Task 4); `state.highlights` (Task 1); `hlToast()` (Task 3).
- Produces: `applyHighlights(ov)` — unwraps stale `mark.hl-note` in `ov` and re-wraps every matching highlight; `hlLocate(text,note)` → `{start,end}|null`; `hlWrap(root,gStart,gEnd,id)`.

- [ ] **Step 1: Append the apply/locate/wrap JS**

Immediately before the `/* ---------- init ---------- */` comment, insert:
```js
/* ===== highlight-notes: locate + wrap + apply ===== */
function hlLocate(text,note){
  var q=note.quote;if(!q)return null;
  var idxs=[],i=-1;while((i=text.indexOf(q,i+1))!==-1)idxs.push(i);
  if(!idxs.length)return null;
  if(idxs.length===1)return {start:idxs[0],end:idxs[0]+q.length};
  var best=idxs[0],bestScore=-1;
  idxs.forEach(function(pos){
    var pre=text.slice(Math.max(0,pos-(note.prefix||'').length),pos);
    var suf=text.slice(pos+q.length,pos+q.length+(note.suffix||'').length);
    var s=(note.prefix&&pre===note.prefix?2:0)+(note.suffix&&suf===note.suffix?2:0);
    if(s>bestScore){bestScore=s;best=pos;}
  });
  if(bestScore<=0&&typeof note.occ==='number'&&note.occ<idxs.length)best=idxs[note.occ];
  return {start:best,end:best+q.length};
}
function hlWrap(root,gStart,gEnd,id){
  var map=hlTextMap(root),targets=[];
  map.nodes.forEach(function(rec){var s=Math.max(gStart,rec.start),e=Math.min(gEnd,rec.end);if(e>s)targets.push({node:rec.node,from:s-rec.start,to:e-rec.start});});
  for(var k=targets.length-1;k>=0;k--){
    var t=targets[k],r=document.createRange();
    try{r.setStart(t.node,t.from);r.setEnd(t.node,t.to);var m=document.createElement('mark');m.className='hl-note';m.setAttribute('data-note-id',id);r.surroundContents(m);}catch(err){}
  }
}
function applyHighlights(ov){
  var panel=ov.querySelector('.panel');if(!panel)return;
  $$('mark.hl-note',panel).forEach(function(m){var p=m.parentNode;while(m.firstChild)p.insertBefore(m.firstChild,m);p.removeChild(m);p.normalize();});
  var token=hlOverlayToken(ov);
  var mine=state.highlights.filter(function(h){return h.ov===token;});
  if(!mine.length)return;
  var text=hlTextMap(panel).text,ranges=[];
  mine.forEach(function(h){var loc=hlLocate(text,h);if(loc)ranges.push({start:loc.start,end:loc.end,id:h.id});});
  ranges.sort(function(a,b){return b.start-a.start;});
  ranges.forEach(function(rg){hlWrap(panel,rg.start,rg.end,rg.id);});
}
```

- [ ] **Step 2: Hook `applyHighlights` into the existing MutationObserver**

In `initDeepDiveNav()` at line ~5358, change:
```js
    var mo=new MutationObserver(function(){
      if(ov.classList.contains('show')){
        if(state.seen[ov.id])seen=new Set(state.seen[ov.id]);
        requestAnimationFrame(measure);
      }else{closePop();}
    });
```
to:
```js
    var mo=new MutationObserver(function(){
      if(ov.classList.contains('show')){
        if(state.seen[ov.id])seen=new Set(state.seen[ov.id]);
        requestAnimationFrame(measure);
        applyHighlights(ov);
      }else{closePop();}
    });
```

- [ ] **Step 3: Extend `hlOpenNote()` to scroll + flash**

Replace the Task-3 `hlOpenNote` body with:
```js
function hlOpenNote(h){
  closeNotes();
  var ov=document.getElementById(h.ov+'ov');if(!ov)return;
  ov.classList.add('show');document.body.style.overflow='hidden';
  var panel=ov.querySelector('.panel');if(panel)panel.scrollTop=0;
  requestAnimationFrame(function(){requestAnimationFrame(function(){
    applyHighlights(ov);
    var mark=panel?panel.querySelector('mark.hl-note[data-note-id="'+(window.CSS&&CSS.escape?CSS.escape(h.id):h.id)+'"]'):null;
    if(mark){
      var bar=ov.querySelector('.bar'),barH=bar?bar.offsetHeight:0;
      var delta=mark.getBoundingClientRect().top-panel.getBoundingClientRect().top-barH-16;
      panel.scrollBy({top:delta,behavior:'auto'});
      mark.classList.add('flash');setTimeout(function(){mark.classList.remove('flash');},1400);
    }else{hlToast('couldn’t locate the exact passage — it may have changed');}
  });});
}
```

- [ ] **Step 4: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0; JS parses; topic count 52; deep-dive anchors still exactly twice.

- [ ] **Step 5: Browser check (the full loop)**

Open the file. Open a deep dive, select a passage, save it. Close the overlay. Confirm: reopening that deep dive shows the passage **persistently tinted**. Open **my notes**, click **"open in deep dive →"** on that note: the modal closes, the correct deep dive opens, scrolls to the passage, and the passage **flashes** then stays tinted. Save a **second** highlight in a different deep dive and confirm it only tints its own deep dive. Delete a note from the modal and confirm it disappears from the list, the count drops, and (on reopening that deep dive) its tint is gone. Confirm export includes the highlights (open the exported JSON and check the `highlights` array), and importing it into a fresh profile restores them. No console errors.

- [ ] **Step 6: Commit**

```bash
git add workbook/agentic-development-study.html
git commit -m "feat(highlights): persistent re-highlight on open + scroll/flash from notes"
```

---

## Task 6: Housekeeping — version bump v1.29, CHANGELOG, ARCHITECTURE note

**Files:**
- Modify: `workbook/agentic-development-study.html` (`#verov` vitem ~2043, footer ~3660), `docs/CHANGELOG.md`, `docs/ARCHITECTURE.md`.

**Interfaces:** none (docs + version metadata only).

- [ ] **Step 1: Prepend the new version item in `#verov`**

Immediately before line 2043 (`<div class="vitem"><span class="vv">v1.28</span>...`), insert (match the existing indentation of the surrounding `.vitem` lines):
```html
      <div class="vitem"><span class="vv">v1.29</span><span class="vd">2026-07-16</span><p><strong>Highlight-notes.</strong> Select any passage inside a deep-dive overlay and save it as a note via the floating “+ save as note” button; add your own thought later. A new <strong>my notes</strong> button (sidebar Data group) opens a modal listing every saved passage grouped by deep dive, each with an editable thought and an “open in deep dive →” jump that scrolls to and flashes the passage. Saved passages stay tinted in the deep dive on every open. Stored in the same per-origin profile; included in export/import.</p></div>
```

- [ ] **Step 2: Update the footer current-version line**

At line 3660, change:
```html
  <b>v1.28</b> · 2026-07-16 · <button class="verlink" type="button" data-veropen>full version history &amp; changelog</button><br>
```
to:
```html
  <b>v1.29</b> · 2026-07-16 · <button class="verlink" type="button" data-veropen>full version history &amp; changelog</button><br>
```

- [ ] **Step 3: Mirror the entry to `docs/CHANGELOG.md`**

Insert immediately after the `Dates are when the work was done in-session.` intro line and before `## v1.28` (so v1.29 is first):
```markdown
## v1.29 · 2026-07-16

Added **highlight-notes**. In any in-page deep-dive overlay, selecting a passage
shows a floating **“+ save as note”** button that stores the passage (text-quote
anchored) in the profile. A new **my notes** button in the sidebar Data group
opens a modal listing every saved passage grouped by deep dive, each with an
editable personal thought, a delete control, and an **“open in deep dive →”**
jump that scrolls to and flashes the source passage. Saved passages are
re-highlighted (persistent tint) every time the deep dive is opened, via the
existing per-overlay `MutationObserver` in `initDeepDiveNav()`. Highlights persist
through the single `store` backend (`agentic-study-v1`) and travel with
export/import. Runtime-only `<mark>` wrapping — the static file (and
`scripts/validate.py`) is unaffected. Workbook-only; standalone deep-dive files
unchanged (they have no storage backend). Known limitation: overlapping
highlights may nest (slightly darker tint).

```

- [ ] **Step 4: Add `state.highlights` to `docs/ARCHITECTURE.md`**

In the "Storage" section, after the line describing the persisted keys (the `Progress + notes persist under key ...` paragraph / the states line), add a bullet:
```markdown
- **Highlights** (deep-dive annotations) persist in the same `state` under
  `agentic-study-v1` as `state.highlights` — an array of
  `{id, ov, title, quote, prefix, suffix, occ, thought, created}`. Passages are
  re-located by text-quote anchoring and wrapped in runtime-only `<mark>`
  elements on overlay open; nothing is written back to the file.
```

- [ ] **Step 5: Run the deterministic gate**

Run: `python3 scripts/validate.py`
Expected: exit 0; topic count 52.

- [ ] **Step 6: Confirm the version label updated in-app**

Browser check: the top-bar version button label and the version-history modal both show **v1.29** at the top (the label is read from the first `.vitem .vv` at load).

- [ ] **Step 7: Commit**

```bash
git add workbook/agentic-development-study.html docs/CHANGELOG.md docs/ARCHITECTURE.md
git commit -m "docs(highlights): bump to v1.29, changelog + architecture notes"
```

---

## Task 7: End-to-end verification pass

**Files:** none (verification only).

- [ ] **Step 1: Deterministic gate, clean run**

Run: `python3 scripts/validate.py`
Expected: exit 0; no errors; topic count **52**; every `#*-deepdive` anchor exactly twice.

- [ ] **Step 2: Cross-deep-dive regression**

Browser: confirm the existing deep-dive section-nav ("jump to section" popover, the "N/M read" chip, scroll progress bar) still works in a deep dive that has highlights — i.e. the `applyHighlights` addition to the shared `MutationObserver` did not break `measure()`/`paint()`.

- [ ] **Step 3: Anchoring robustness**

Browser: save a highlight over a phrase that occurs more than once in a deep dive (if available), plus one that spans **inline markup** (e.g. a phrase containing a `<strong>` or `<a>`). Confirm the correct occurrence is tinted and the inline markup is not broken. Save a highlight adjacent to an SVG figure and confirm the figure still renders.

- [ ] **Step 4: Persistence round-trip**

Browser: add 2–3 highlights with thoughts, reload the page, confirm all reappear (count, quotes, thoughts, tints). Export, clear site data (or use a fresh browser profile), import the JSON, confirm highlights restore.

- [ ] **Step 5: Final commit (if any verification fix was needed)**

```bash
git add -A
git commit -m "fix(highlights): verification-pass adjustments"
```
(Skip if Steps 1–4 passed with no changes.)

---

## Self-Review (completed by plan author)

**Spec coverage:**
- Scope (workbook overlays only) → Global Constraints + Task 1–5 (no `deep-dives/*` edits). ✅
- Capture: floating button, save-immediately, empty thought, <3-char / SVG exclusion → Task 4. ✅
- Central modal from a top-of-page control, grouped, editable thought, open→, delete, empty state, live count → Task 3. ✅
- Return trip: open + scroll + flash + persistent tint → Task 5. ✅
- Data model (`state.highlights` fields) + load/export/import merge dedupe → Task 1. ✅
- Anchoring (quote+prefix+suffix+occ), MutationObserver hook, cross-node wrap, runtime-only marks → Tasks 4–5. ✅
- Edge cases: not-found toast (Task 5 Step 3), overlapping nesting tolerated (documented), no-store behaviour (existing warnbar). ✅
- Housekeeping: v1.29 vitem + footer + CHANGELOG + ARCHITECTURE → Task 6. ✅

**Placeholder scan:** No TBD/TODO; every code step shows complete code; every command has expected output. ✅

**Type consistency:** `applyHighlights` (defined Task 5, forward-guarded in Task 4); `hlTextMap` return shape `{text,nodes}` used identically in Tasks 4 & 5; `hlOverlayToken`/`hlOverlayTitle`/`hlOccurrence`/`hlId` defined once (Task 4) and reused; `renderNotes`/`updateNotesCount`/`openNotes`/`closeNotes`/`hlOpenNote`/`hlToast` names consistent across Tasks 3 & 5; note object field names (`id/ov/title/quote/prefix/suffix/occ/thought/created`) identical in data layer, capture, render, locate. ✅

**Deviation from spec noted for reviewer:** the spec said "top-bar button"; the plan places the button in the sidebar **Data** group instead (next to export/import) so it stays visible on ≤900px screens where `.verbtn` is hidden — this matches the approved mock's grouping of notes with export/import and avoids a mobile dead-end.
