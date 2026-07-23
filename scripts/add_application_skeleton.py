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
    # 2. section body ends at the next <h2>, or (S1-S3 shape) at an un-numbered
    # <h3>Further reading heading — whichever comes first; anything else raises.
    end_h2 = s.find("<h2", m.end())
    fr = re.search(r"<h3\b[^>]*>\s*Further reading", s[m.end():])
    end_h3 = m.end() + fr.start() if fr else -1
    candidates = [e for e in (end_h2, end_h3) if e >= 0]
    if not candidates:
        raise SystemExit(f"{fn}: no <h2> or <h3>Further reading after takeaways")
    end = min(candidates)
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
    # 4. TOC label (standalone only). TOC labels are abbreviated (e.g.
    # '<a href="#s10"><b>10</b> &middot; Takeaways</a>') so they never contain HEAD
    # verbatim — locate the anchor by the section's own id instead, and assert the
    # replacement actually happened exactly once (a silent no-op here is the bug
    # this replaced).
    if is_standalone:
        sec_id = h2_id_prefix + m.group(1)  # e.g. "s10"
        toc_a_re = re.compile(
            r'(<a href="#' + re.escape(sec_id) + r'">.*?)</a>'
        )
        toc_matches = toc_a_re.findall(new)
        if len(toc_matches) != 1:
            raise SystemExit(
                f"{fn}: expected exactly one TOC anchor for #{sec_id}, found {len(toc_matches)}"
            )
        before = new
        new = toc_a_re.sub(
            lambda mm: re.sub(r'(<b>\d+</b>)(?:\s*&middot;\s*\S.*)?$',
                               r'\1 &middot; Applying it', mm.group(1)) + "</a>",
            new, count=1,
        )
        if new == before:
            raise SystemExit(f"{fn}: TOC label replace was a no-op for #{sec_id}")
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
