#!/usr/bin/env python3
"""
Deterministic validator for the agentic-development study workbook + deep dives.

Run from the repo root:  python3 scripts/validate.py
Exit code 0 = all good; non-zero = something to fix. This is the gate CLAUDE.md refers to.

Checks:
  workbook/agentic-development-study.html
    - the trailing <script> parses under `node --check` (if node is available)
    - HTML start/end tags balance (ignoring void + SVG elements)
    - every <svg> is well-formed XML
    - every #<token>-deepdive anchor appears exactly twice (Go-deeper link + JS handler)
    - the topic count is reported (expected 52 unless topics were intentionally added)
    - playbook checklist step ids (data-step) are unique (frozen progress keys)
  deep-dives/*.html
    - HTML balances, every <svg> well-formed, TOC #sN anchors all resolve to an id
    - SVG ids are unique within and across deep dives
  gallery
    - gallery-registry.json schema, coverage, duplicate keys, orphaned entries
    - sectionAnchor values exist as ids in the corresponding deep-dive file
    - gallery.html is up-to-date with scripts/generate-gallery.py
  all files
    - CSS class coverage: every class used in markup is either styled by a CSS
      selector in <style> or referenced as a JS selector (querySelector/closest/
      matches) — catches drift like `.rt` markup vs `.ti` stylesheet
"""
import json
import os, re, sys, subprocess, shutil, tempfile
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKBOOK = os.path.join(ROOT, "workbook", "agentic-development-study.html")
DEEPDIR = os.path.join(ROOT, "deep-dives")

VOID = {"meta","link","input","br","img","path","circle","line","rect",
        "polygon","marker","text","g","defs","hr","source","use","stop","ellipse","polyline"}

problems = []

GALLERY_REGISTRY = os.path.join(ROOT, "gallery-registry.json")

def load_registry():
    if not os.path.exists(GALLERY_REGISTRY):
        return None
    try:
        with open(GALLERY_REGISTRY, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        note(False, f"gallery-registry.json is not valid JSON: {e}")
        return None

def note(ok, msg):
    print(("  ok  " if ok else " FAIL ") + msg)
    if not ok:
        problems.append(msg)

class Balancer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.bad = None
    def handle_starttag(self, t, a):
        if t not in VOID:
            self.stack.append(t)
    def handle_endtag(self, t):
        if self.stack and self.stack[-1] == t:
            self.stack.pop()
        elif t in self.stack:
            self.bad = t

def check_html_balance(s, label):
    p = Balancer(); p.feed(s)
    note(not p.stack and p.bad is None,
         f"{label}: HTML tags balanced" if (not p.stack and not p.bad)
         else f"{label}: HTML imbalance (leftover={p.stack[-3:]}, mismatch={p.bad})")

def check_svgs(s, label):
    svgs = re.findall(r"<svg\b.*?</svg>", s, flags=re.S)
    bad = 0
    for v in svgs:
        try:
            ET.fromstring(v.replace("&amp;", "&#38;").replace("&nbsp;", "&#160;"))
        except Exception as e:
            bad += 1
            print(f"       SVG error in {label}: {e}")
    note(bad == 0, f"{label}: {len(svgs)} SVG(s) well-formed" if bad == 0
         else f"{label}: {bad} malformed SVG(s)")

def check_css_class_coverage(s, label):
    css = "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, flags=re.S))
    covered = set(re.findall(r"\.([A-Za-z_][\w-]*)", css))
    js = "".join(re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", s, flags=re.S))
    for sel in re.findall(
            r"""(?:querySelector(?:All)?|closest|matches)\(\s*['"]([^'"]+)['"]""", js):
        covered |= set(re.findall(r"\.([A-Za-z_][\w-]*)", sel))
    used = set()
    for attr in re.findall(r'<[a-zA-Z][^>]*?\bclass="([^"]+)"', s):
        used |= {t for t in attr.split() if re.fullmatch(r"[A-Za-z_][\w-]*", t)}
    missing = sorted(used - covered)
    note(not missing, f"{label}: all {len(used)} markup classes covered by CSS/JS"
         if not missing else f"{label}: classes used but never styled/referenced: {missing}")

def check_gallery_registry():
    print("gallery registry")
    before = len(problems)
    registry = load_registry()
    if registry is None:
        return

    entries = registry.get("entries", [])
    if not isinstance(entries, list):
        note(False, "gallery-registry.json: 'entries' must be a list")
        return

    # Schema check
    keys = set()
    dup_keys = set()
    required = {"deepDive", "figureIndex", "why"}
    for i, e in enumerate(entries):
        missing = required - set(e.keys())
        if missing:
            note(False, f"gallery-registry.json entry {i} missing fields: {sorted(missing)}")
        if not isinstance(e.get("deepDive"), str):
            note(False, f"gallery-registry.json entry {i}: deepDive must be a string")
        if not isinstance(e.get("figureIndex"), int):
            note(False, f"gallery-registry.json entry {i}: figureIndex must be an int")
        if not isinstance(e.get("why"), str):
            note(False, f"gallery-registry.json entry {i}: why must be a string")
        if isinstance(e.get("why"), str) and not e.get("why").strip():
            note(False, f"gallery-registry.json entry {i}: why is empty")
        key = (e.get("deepDive"), e.get("figureIndex"))
        if key in keys:
            dup_keys.add(key)
        keys.add(key)
    if dup_keys:
        note(False, f"gallery-registry.json duplicate keys: {sorted(dup_keys)}")

    # Coverage check: every figure in deep-dives has a registry entry.
    deep_figures = {}
    for fn in sorted(os.listdir(DEEPDIR)):
        if not fn.endswith(".html"):
            continue
        stem = fn[:-5]
        s = open(os.path.join(DEEPDIR, fn), encoding="utf-8").read()
        count = len(re.findall(r"<figure\b", s))
        deep_figures[stem] = count

    # Only structurally valid entries participate in coverage/orphan/anchor
    # checks; malformed ones were already noted above and must not crash the
    # run with a KeyError before the remaining checks execute.
    valid_entries = [
        e for e in entries
        if isinstance(e.get("deepDive"), str) and isinstance(e.get("figureIndex"), int)
    ]

    registry_figures = {}
    for e in valid_entries:
        registry_figures.setdefault(e["deepDive"], set()).add(e["figureIndex"])

    for stem, count in sorted(deep_figures.items()):
        expected = set(range(count))
        actual = registry_figures.get(stem, set())
        missing = expected - actual
        if missing:
            note(False, f"{stem}.html missing gallery-registry entries for figureIndex: {sorted(missing)}")
        extra = actual - expected
        if extra:
            note(False, f"gallery-registry.json has orphaned figureIndex for {stem}.html: {sorted(extra)}")

    # Orphaned deepDive values pointing to non-existent files.
    for stem in sorted(registry_figures.keys() - deep_figures.keys()):
        note(False, f"gallery-registry.json references missing deep-dive file: {stem}.html")

    # sectionAnchor values must exist as ids in the corresponding deep-dive file.
    for i, e in enumerate(valid_entries):
        anchor = e.get("sectionAnchor", "")
        if not anchor:
            continue
        stem = e.get("deepDive")
        html_path = os.path.join(DEEPDIR, f"{stem}.html")
        if not os.path.exists(html_path):
            continue
        s = open(html_path, encoding="utf-8").read()
        if f'id="{anchor}"' not in s:
            note(False, f"gallery-registry.json entry {i}: sectionAnchor '#{anchor}' not found in {stem}.html")

    note(len(problems) == before,
         f"gallery-registry.json covers all {sum(deep_figures.values())} figures"
         if len(problems) == before
         else "gallery-registry.json has problems (see above)")


def h2_anchors(s, label):
    """Return (list of h2 info, missing_ids, duplicate_ids)."""
    h2s = []
    for m in re.finditer(r'(<h2\b[^>]*>)(.*?)</h2>', s, flags=re.S):
        attr = m.group(1)
        content = m.group(2)
        idm = re.search(r'id="([^"]+)"', attr)
        h2s.append({
            'id': idm.group(1) if idm else None,
            'text': re.sub(r'<[^>]+>', '', content).strip()[:60]
        })
    ids = [h['id'] for h in h2s if h['id']]
    missing = [h for h in h2s if not h['id']]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    return h2s, missing, dup_ids


def check_h2_anchors(s, label, scope='all'):
    """Check h2 anchors. scope='all' for standalone, 'overlays' for workbook overlays."""
    before = len(problems)
    if scope == 'overlays':
        # Find each overlay body and check h2s within it.
        starts = [(m.start(), m.group(1)) for m in re.finditer(r'<div class="e1ov" id="([a-z0-9]+ov)" role="dialog"[^>]*>', s)]
        starts.append((len(s), None))
        all_missing = []
        all_dups = []
        for i, (start, ov_id) in enumerate(starts[:-1]):
            end = starts[i+1][0]
            block = s[start:end]
            # extract body content
            body_open = re.search(r'<div class="body">', block)
            if not body_open:
                continue
            depth = 1
            body_end = None
            for m in re.finditer(r'<(/?)div\b[^>]*>', block[body_open.end():]):
                if m.group(1) == '':
                    depth += 1
                else:
                    depth -= 1
                    if depth == 0:
                        body_end = body_open.end() + m.start()
                        break
            if body_end is None:
                continue
            body = block[body_open.end():body_end]
            h2s, missing, dup_ids = h2_anchors(body, label)
            all_missing.extend([(ov_id, h) for h in missing])
            all_dups.extend([(ov_id, d) for d in dup_ids])
        if all_missing:
            note(False, f"{label}: overlay h2 missing id: " +
                 ", ".join(f"{ov}: {h['text'][:40]}" for ov, h in all_missing[:5]))
        if all_dups:
            note(False, f"{label}: duplicate overlay h2 ids: {all_dups[:10]}")
    else:
        h2s, missing, dup_ids = h2_anchors(s, label)
        if missing:
            note(False, f"{label}: h2 missing id: " +
                 ", ".join(h['text'][:40] for h in missing[:5]))
        if dup_ids:
            note(False, f"{label}: duplicate h2 ids: {dup_ids[:10]}")
    note(len(problems) == before,
         f"{label}: all h2 anchors stable and unique")


def check_svg_id_uniqueness():
    print("svg id uniqueness")
    ids_by_file = {}
    cross_file_dupes = {}
    within_file_dupes = {}
    for fn in sorted(os.listdir(DEEPDIR)):
        if not fn.endswith(".html"):
            continue
        s = open(os.path.join(DEEPDIR, fn), encoding="utf-8").read()
        seen_in_file = set()
        for svg in re.findall(r"<svg\b.*?</svg>", s, flags=re.S):
            for i in re.findall(r'<[^>]+\bid="([^"]+)"', svg):
                if i in seen_in_file:
                    within_file_dupes.setdefault(fn, set()).add(i)
                seen_in_file.add(i)
                if i in ids_by_file and ids_by_file[i] != fn:
                    cross_file_dupes.setdefault(i, set()).update([ids_by_file[i], fn])
                ids_by_file[i] = fn
    messages = []
    if cross_file_dupes:
        messages.append(f"SVG ids reused across deep dives (would collide in gallery.html): {sorted(cross_file_dupes)}")
    if within_file_dupes:
        messages.append(f"SVG ids duplicated within a deep dive: {within_file_dupes}")
    if messages:
        note(False, "; ".join(messages))
    else:
        note(True, "all SVG ids are unique within and across deep-dives")


def check_workbook():
    print("workbook/agentic-development-study.html")
    if not os.path.exists(WORKBOOK):
        note(False, "workbook file missing"); return
    s = open(WORKBOOK, encoding="utf-8").read()

    # trailing <script> parses
    blocks = re.findall(r"<script>\n(.*?)\n</script>", s, flags=re.S)
    if blocks and shutil.which("node"):
        tmp = "/tmp/_wb_app.js"; open(tmp, "w").write(blocks[-1])
        r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
        note(r.returncode == 0, "app <script> parses (node --check)"
             if r.returncode == 0 else f"app <script> JS error: {r.stderr.strip()[:200]}")
    elif blocks:
        note(True, "app <script> found (node not available — skipped parse)")
    else:
        note(False, "no trailing <script> block found")

    check_html_balance(s, "workbook")
    check_svgs(s, "workbook")
    check_css_class_coverage(s, "workbook")
    check_h2_anchors(s, "workbook", scope='overlays')

    # deep-dive anchors wired: link(s) + exactly one JS handler.
    # sdlc has two entry links (intro + section) + 1 handler = 3; others have 1 link + 1 handler = 2.
    tokens = sorted(set(re.findall(r"#([a-z0-9]+)-deepdive", s)))
    for tok in tokens:
        c = s.count(f"#{tok}-deepdive")
        handlers = s.count(f'a[href="#{tok}-deepdive"]')
        exp = 3 if tok == "sdlc" else 2
        ok = (c == exp and handlers == 1)
        note(ok, f"#{tok}-deepdive wired x{c} (+1 handler)" if ok
             else f"#{tok}-deepdive wired x{c}, handlers={handlers} (expected {exp} total, 1 handler)")

    # topic count
    ids = re.findall(r'id:"((?:eng|prod|hand|ia|brown|traj|des|sec|pb)-[a-z0-9-]*)"', s)
    dups = {i for i in ids if ids.count(i) > 1}
    note(len(set(ids)) == len(ids), f"topic ids unique ({len(ids)} topics)"
         if not dups else f"DUPLICATE topic ids: {dups}")
    print(f"  ->  topic count = {len(ids)} (expected 60 unless intentionally changed)")

    # CONTENT-MAP.md must list exactly the workbook's topic ids (ids are frozen
    # progress keys — a wrong id in the docs invites a progress-wiping "fix")
    cmap = os.path.join(ROOT, "docs", "CONTENT-MAP.md")
    if os.path.exists(cmap):
        doc = open(cmap, encoding="utf-8").read()
        doc_ids = set(re.findall(r"`((?:eng|prod|hand|ia|brown|traj|des|sec|pb)-[a-z0-9-]+)`", doc))
        wb_ids = set(ids)
        extra, missing = sorted(doc_ids - wb_ids), sorted(wb_ids - doc_ids)
        note(not extra and not missing, "CONTENT-MAP.md topic ids match the workbook"
             if not extra and not missing
             else f"CONTENT-MAP.md id drift: not-in-workbook={extra}, undocumented={missing}")

    # playbook checklist step ids are frozen progress keys - duplicates would
    # silently merge two steps' saved state
    steps = re.findall(r'data-step="([\w-]+)"', s)
    dup_steps = sorted({x for x in steps if steps.count(x) > 1})
    note(not dup_steps, f"playbook step ids unique ({len(steps)} step(s))"
         if not dup_steps else f"DUPLICATE playbook step ids: {dup_steps}")

def check_gallery_freshness():
    print("gallery freshness")
    gallery_path = os.path.join(ROOT, "gallery.html")
    if not os.path.exists(gallery_path):
        note(False, "gallery.html missing")
        return
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp_path = tmp.name
    try:
        r = subprocess.run(
            [sys.executable, os.path.join(ROOT, "scripts", "generate-gallery.py"), "--output", tmp_path],
            capture_output=True, text=True
        )
        if r.returncode != 0:
            note(False, f"generate-gallery.py failed: {r.stderr.strip()[:200]}")
            return
        generated = open(tmp_path, encoding="utf-8").read()
        committed = open(gallery_path, encoding="utf-8").read()
        note(generated == committed,
             "gallery.html is up-to-date" if generated == committed
             else "gallery.html is stale; run `python3 scripts/generate-gallery.py`")
    finally:
        os.unlink(tmp_path)


def check_deepdives():
    print("deep-dives/")
    if not os.path.isdir(DEEPDIR):
        note(False, "deep-dives/ missing"); return
    for fn in sorted(os.listdir(DEEPDIR)):
        if not fn.endswith(".html"):
            continue
        s = open(os.path.join(DEEPDIR, fn), encoding="utf-8").read()
        check_html_balance(s, fn)
        check_svgs(s, fn)
        check_css_class_coverage(s, fn)
        check_h2_anchors(s, fn, scope='all')
        anc = set(re.findall(r'href="#([\w-]+)"', s))
        ids = set(re.findall(r'id="([\w-]+)"', s))
        missing = {a for a in anc if a.startswith("s") and a[1:].isdigit()} - ids
        note(not missing, f"{fn}: TOC anchors resolve"
             if not missing else f"{fn}: unresolved TOC anchors {missing}")

if __name__ == "__main__":
    check_workbook()
    print()
    check_deepdives()
    print()
    check_gallery_registry()
    print()
    check_svg_id_uniqueness()
    print()
    check_gallery_freshness()
    print()
    if problems:
        print(f"RESULT: {len(problems)} problem(s) — fix before committing.")
        sys.exit(1)
    print("RESULT: all checks passed.")
