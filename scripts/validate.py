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
  all files
    - CSS class coverage: every class used in markup is either styled by a CSS
      selector in <style> or referenced as a JS selector (querySelector/closest/
      matches) — catches drift like `.rt` markup vs `.ti` stylesheet
"""
import os, re, sys, subprocess, shutil
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKBOOK = os.path.join(ROOT, "workbook", "agentic-development-study.html")
DEEPDIR = os.path.join(ROOT, "deep-dives")

VOID = {"meta","link","input","br","img","path","circle","line","rect",
        "polygon","marker","text","g","defs","hr","source","use","stop","ellipse","polyline"}

problems = []

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
    print(f"  ->  topic count = {len(ids)} (expected 52 unless intentionally changed)")

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
    if problems:
        print(f"RESULT: {len(problems)} problem(s) — fix before committing.")
        sys.exit(1)
    print("RESULT: all checks passed.")
