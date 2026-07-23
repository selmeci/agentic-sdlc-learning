#!/usr/bin/env python3
"""Generate gallery.html from deep-dive figures and a curated registry."""
import html
import json
import os
import re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEEPDIR = os.path.join(ROOT, "deep-dives")
REGISTRY = os.path.join(ROOT, "gallery-registry.json")
OUT = os.path.join(ROOT, "gallery.html")


class FigureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.figures = []
        self._in_figure = False
        self._in_figcaption = False
        self._in_h2 = False
        self._current_h2_text = ""
        self._current_h2_anchor = None
        self._current_caption = ""
        self._current_section = ""
        self._current_section_anchor = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "figure":
            self._in_figure = True
            self._current_caption = ""
            self._current_section = self._current_h2_text
            self._current_section_anchor = self._current_h2_anchor
        elif tag == "figcaption" and self._in_figure:
            self._in_figcaption = True
        elif tag == "h2":
            self._in_h2 = True
            self._current_h2_text = ""
            self._current_h2_anchor = attrs.get("id")
        # Ignore any nested tags inside figcaption; we only collect text.

    def handle_endtag(self, tag):
        if tag == "figure" and self._in_figure:
            self.figures.append({
                "caption": self._current_caption.strip(),
                "section": self._current_section.strip(),
                "section_anchor": self._current_section_anchor,
            })
            self._in_figure = False
            self._in_figcaption = False
        elif tag == "figcaption":
            self._in_figcaption = False
        elif tag == "h2":
            self._in_h2 = False

    def handle_data(self, data):
        if self._in_h2:
            self._current_h2_text += data
        elif self._in_figcaption:
            self._current_caption += data


def extract_figures(html_path):
    parser = FigureParser()
    with open(html_path, encoding="utf-8") as f:
        parser.feed(f.read())
    return parser.figures


def deep_dive_stem(filename):
    """Return filename without .html extension."""
    return filename[:-5] if filename.endswith(".html") else filename


def draft_registry(deep_dir, out_path):
    entries = []
    for fn in sorted(os.listdir(deep_dir)):
        if not fn.endswith(".html"):
            continue
        stem = deep_dive_stem(fn)
        figures = extract_figures(os.path.join(deep_dir, fn))
        for idx, fig in enumerate(figures):
            entries.append({
                "deepDive": stem,
                "figureIndex": idx,
                "title": fig["caption"] or f"Diagram in {stem}",
                "section": fig["section"] or "",
                "sectionAnchor": fig["section_anchor"] or "",
                "why": "",
            })
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({"entries": entries}, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {len(entries)} draft entries to {out_path}")


SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S)
FIGURE_RE = re.compile(r"<figure\b.*?</figure>", re.S)


def extract_svgs(html_path):
    with open(html_path, encoding="utf-8") as f:
        s = f.read()
    return SVG_RE.findall(s)


def extract_figure_svgs(html_path):
    """Return one SVG per <figure>, in figure order.

    figureIndex enumerates <figure> elements (the registry was curated against
    FigureParser and validate.py's coverage check counts <figure> tags), so the
    generator must resolve the SVG *inside* the Nth figure — not the Nth <svg>
    in the file, which drifts when a file contains out-of-figure SVGs. A figure
    without an SVG yields None, making the entry unrenderable.
    """
    with open(html_path, encoding="utf-8") as f:
        s = f.read()
    svgs = []
    for block in FIGURE_RE.findall(s):
        m = SVG_RE.search(block)
        svgs.append(m.group(0) if m else None)
    return svgs


def collect_svg_styles(deep_dir):
    """Gather deep-dive SVG class CSS keyed by (file_stem, class_name).

    Deep-dive files style their figures with per-file class rules like:
      svg .bx { fill:#FBFCFD; stroke:#57656F; ... }
      svg .tt { font:600 13px var(--disp); fill:var(--ink) }
      svg .edE1 { stroke:#57656F; ...; marker-end:url(#ahE1a) }
    Because each gallery card prefixes SVG ids, this CSS must be scoped to the
    card that came from the same source file. Collapsing all files into a
    single class-keyed map would let one file's marker URL overwrite another's.
    """
    styles = {}
    for fn in sorted(os.listdir(deep_dir)):
        if not fn.endswith(".html"):
            continue
        stem = deep_dive_stem(fn)
        with open(os.path.join(deep_dir, fn), encoding="utf-8") as f:
            text = f.read()
        style_blocks = re.findall(r"<style[^>]*>(.*?)</style>", text, re.S)
        if not style_blocks:
            continue
        css = "".join(style_blocks)
        # Single-class and grouped selectors: svg .bx { ... }, svg .ed, svg .edD { ... }
        for rule in re.findall(r"svg\s+\.[\w-]+(?:\s*,\s*svg\s+\.[\w-]+)*\s*\{[^}]+\}", css):
            selectors_part, props = rule.split("{", 1)
            props = props.rstrip("}").strip()
            for sel in selectors_part.split(","):
                sel = sel.strip()
                m = re.search(r"\.([\w-]+)$", sel)
                if m:
                    cls = m.group(1)
                    styles[(stem, cls)] = props
    return styles


def collect_file_markers(deep_dir):
    """Map deep-dive file stem -> {marker_id: <marker> element string}.

    Some deep-dive files define a marker in one SVG and reference it from
    another SVG via url(#id). When only one SVG is inlined per gallery card,
    shared markers must be copied into the selected SVG before ids are prefixed.
    """
    file_markers = {}
    for fn in sorted(os.listdir(deep_dir)):
        if not fn.endswith(".html"):
            continue
        stem = deep_dive_stem(fn)
        markers = {}
        for svg in extract_svgs(os.path.join(deep_dir, fn)):
            for marker_html in re.findall(r'<marker\b[^>]*>.*?</marker>', svg, re.S):
                m = re.search(r'\bid="([^"]+)"', marker_html)
                if m:
                    markers[m.group(1)] = marker_html
        file_markers[stem] = markers
    return file_markers


def inject_missing_markers(svg, used_classes, file_edge_styles, file_markers):
    """Copy referenced markers from the source file into this SVG if absent."""
    referenced = set()
    for cls in used_classes:
        if cls in file_edge_styles:
            referenced.update(re.findall(r'url\(#([^)]+)\)', file_edge_styles[cls]))
    present = set(re.findall(r'\bid="([^"]+)"', svg))
    missing = sorted(referenced - present)
    if not missing:
        return svg
    to_inject = []
    for marker_id in missing:
        if marker_id in file_markers:
            to_inject.append(file_markers[marker_id])
    if not to_inject:
        return svg

    defs_match = re.search(r'<defs\b[^>]*>.*?</defs>', svg, re.S)
    if defs_match:
        defs = defs_match.group(0)
        new_defs = defs.replace('</defs>', ''.join(to_inject) + '</defs>')
        svg = svg[:defs_match.start()] + new_defs + svg[defs_match.end():]
    else:
        svg = re.sub(r'(<svg\b[^>]*>)', r'\1<defs>' + ''.join(to_inject) + '</defs>', svg, count=1)
    return svg


def prefix_svg_ids(svg, prefix):
    """Rewrite ids and internal id references inside an SVG string.

    Returns the rewritten SVG and the set of ids that were prefixed.
    """
    ids = set(re.findall(r'\bid="([^"]+)"', svg))
    svg = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{prefix}{m.group(1)}"', svg)

    # Rewrite internal references to the ids that exist in this SVG.
    for old_id in sorted(ids, key=len, reverse=True):
        new_id = prefix + old_id
        escaped = re.escape(old_id)
        svg = re.sub(rf'url\(\#{escaped}\)', f'url(#{new_id})', svg)
        svg = re.sub(rf'href="\#{escaped}"', f'href="#{new_id}"', svg)
        svg = re.sub(rf'xlink:href="\#{escaped}"', f'xlink:href="#{new_id}"', svg)
    return svg, ids


def scope_svg_css(card_class, id_prefix, used_classes, svg_ids, file_styles):
    """Generate scoped CSS rules for one card, rewriting marker url() refs."""
    rules = []
    for cls in sorted(used_classes):
        if cls not in file_styles:
            continue
        props = file_styles[cls]
        for old_id in sorted(svg_ids, key=len, reverse=True):
            new_id = f"{id_prefix}{old_id}"
            escaped = re.escape(old_id)
            props = re.sub(rf'url\(\#{escaped}\)', f'url(#{new_id})', props)
        rules.append(f'.{card_class} svg .{cls} {{ {props} }}')
    return "\n".join(rules)


GALLERY_CSS = """
.gallery-wrap{max-width:1200px;margin:0 auto;padding:30px 22px 90px}
.gallery-intro{max-width:74ch;margin:0 0 26px}
.gallery-filter{width:100%;max-width:420px;padding:10px 14px;border:1px solid var(--line);border-radius:10px;font-family:var(--body);font-size:15px;margin-bottom:24px;background:var(--card)}
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:22px}
.gallery-card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column}
.gallery-preview{padding:14px;border-bottom:1px solid var(--line);background:#fff;cursor:zoom-in}
.gallery-preview svg{width:100%;height:auto;max-height:180px;display:block}
.gallery-body{padding:16px 18px 18px;display:flex;flex-direction:column;gap:8px;flex:1}
.gallery-title{font-family:var(--disp);font-weight:700;font-size:16px;line-height:1.3}
.gallery-section{font-family:var(--mono);font-size:10.5px;color:var(--soft);text-transform:uppercase;letter-spacing:.06em}
.gallery-caption{font-family:var(--mono);font-size:10.5px;color:var(--soft);text-transform:uppercase;letter-spacing:.06em;padding:10px 14px 0;background:var(--card);border-bottom:1px solid var(--line-soft)}
.gallery-why{font-size:14px;color:var(--soft);line-height:1.5;flex:1}
.gallery-link{font-family:var(--mono);font-size:12px;color:var(--cobalt-deep);text-decoration:none;font-weight:600}
.gallery-link:hover{color:var(--cobalt)}
.gallery-empty{display:none;padding:30px 0;color:var(--soft)}
.gallery-empty.show{display:block}
@media (max-width:760px){.gallery-grid{grid-template-columns:1fr}}
.gallery-preview:focus-visible{outline:2px solid var(--cobalt);outline-offset:2px}
.gallery-modal{position:fixed;inset:0;z-index:60;display:flex;align-items:center;justify-content:center;padding:3vh 3vw;background:rgba(26,36,48,.72)}
.gallery-modal[hidden]{display:none}
.gallery-modal-box{position:relative;background:var(--card);border:1px solid var(--line);border-radius:14px;width:94vw;height:94vh;max-width:94vw;max-height:94vh;display:flex;flex-direction:column;overflow:hidden;padding:26px;box-shadow:0 18px 60px rgba(26,36,48,.35)}
.gallery-modal-body{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.gallery-modal-body svg{width:100%;height:100%;display:block}
.gallery-modal-close{position:absolute;top:10px;right:10px;z-index:1;width:34px;height:34px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink);font-family:var(--mono);font-size:16px;line-height:1;cursor:pointer}
.gallery-modal-close:hover{border-color:var(--cobalt);color:var(--cobalt)}
""".strip()


def escape_html(s):
    return html.escape(s, quote=True)


def render_card(entry, svg, file_stem, card_index, svg_styles, file_markers):
    title = entry.get("title") or "Diagram"
    section = entry.get("section") or ""
    why = entry.get("why") or ""
    anchor = entry.get("sectionAnchor") or ""
    href = f"deep-dives/{file_stem}.html"
    if anchor:
        href += f"#{anchor}"

    module = file_stem
    caption = f"{module} · {section}" if section else module

    used_classes = set()
    for class_attr in re.findall(r'class="([^"]+)"', svg):
        used_classes.update(class_attr.split())

    # Styles are keyed by (file_stem, class_name) so each card only sees
    # the CSS from the deep-dive file it was extracted from.
    file_styles = {
        cls: props for (stem, cls), props in svg_styles.items() if stem == file_stem
    }

    svg = inject_missing_markers(svg, used_classes, file_styles, file_markers.get(file_stem, {}))

    card_class = f"g-card-{card_index}"
    id_prefix = f"g-{card_index}-"
    svg, svg_ids = prefix_svg_ids(svg, id_prefix)

    scoped_css = scope_svg_css(card_class, id_prefix, used_classes, svg_ids, file_styles)

    return (
        f'<article class="gallery-card" data-title="{escape_html(title.lower())}" '
        f'data-section="{escape_html(section.lower())}" '
        f'data-module="{escape_html(module.lower())}" '
        f'data-why="{escape_html(why.lower())}">\n'
        f'  <div class="gallery-caption">{escape_html(caption)}</div>\n'
        f'  <div class="gallery-preview {card_class}" tabindex="0">{svg}</div>\n'
        f'  <div class="gallery-body">\n'
        f'    <div class="gallery-title">{escape_html(title)}</div>\n'
        f'    <div class="gallery-section">{escape_html(section)}</div>\n'
        f'    <p class="gallery-why">{escape_html(why)}</p>\n'
        f'    <a class="gallery-link" href="{escape_html(href)}">Open in deep dive →</a>\n'
        f'  </div>\n'
        f'</article>\n'
    ), scoped_css


def generate_gallery(deep_dir, registry_path, out_path):
    with open(registry_path, encoding="utf-8") as f:
        registry = json.load(f)
    entries = registry.get("entries", [])

    svg_styles = collect_svg_styles(deep_dir)
    file_markers = collect_file_markers(deep_dir)

    # figureIndex enumerates <figure> elements, so resolve the SVG inside the
    # Nth figure (not the Nth raw <svg> in the file).
    cards = []
    scoped_css_blocks = []
    skipped = []
    for card_index, entry in enumerate(entries):
        stem = entry["deepDive"]
        html_path = os.path.join(deep_dir, f"{stem}.html")
        if not os.path.exists(html_path):
            skipped.append(f"{stem}: deep-dive file missing")
            continue
        figure_svgs = extract_figure_svgs(html_path)
        idx = entry["figureIndex"]
        if idx < 0 or idx >= len(figure_svgs):
            skipped.append(f"{stem} figureIndex {idx} out of range ({len(figure_svgs)} figures)")
            continue
        svg = figure_svgs[idx]
        if svg is None:
            skipped.append(f"{stem} figureIndex {idx} has no SVG")
            continue
        card_html, card_css = render_card(entry, svg, stem, card_index, svg_styles, file_markers)
        cards.append(card_html)
        if card_css:
            scoped_css_blocks.append(card_css)

    if skipped:
        for msg in skipped:
            print(f"ERROR: registry entry not renderable: {msg}")
        raise SystemExit(1)

    svg_styles = "\n".join(scoped_css_blocks)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Diagram Gallery — Agentic Development Study</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400;1,8..60,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{{
  --paper:#EEF1F4; --card:#FBFCFD; --ink:#1A2430; --soft:#57656F;
  --line:#D6DDE4; --line-soft:#E4E9EE;
  --cobalt:#2A4AD0; --cobalt-deep:#20389E;
  --amber:#B26205; --amber-bg:#FBF1E1;
  --pine:#177245; --pine-bg:#E5F3EB;
  --idle:#9AA7B1; --idle-bg:#EDF1F4;
  --disp:'Bricolage Grotesque','Avenir Next',system-ui,sans-serif;
  --body:'Source Serif 4',Georgia,'Times New Roman',serif;
  --mono:'IBM Plex Mono',ui-monospace,'SF Mono',Menlo,Consolas,monospace;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.62}}
a{{color:var(--cobalt-deep)}} a:hover{{color:var(--cobalt)}}
.hdr{{position:sticky;top:0;z-index:40;background:rgba(238,241,244,.93);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}}
.hdr-in{{max-width:1200px;margin:0 auto;padding:11px 22px;display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}}
.hdr .tag{{font-family:var(--mono);font-size:10.5px;font-weight:600;color:#fff;background:var(--ink);border-radius:6px;padding:3px 8px;letter-spacing:.04em}}
.hdr h1{{font-family:var(--disp);font-weight:700;font-size:17px;letter-spacing:-.01em}}
.hdr .bc{{font-family:var(--mono);font-size:11px;color:var(--soft);margin-left:auto}}
{GALLERY_CSS}
{svg_styles}
footer{{max-width:1200px;margin:0 auto;padding:24px 22px 60px;border-top:1px solid var(--line);font-family:var(--mono);font-size:11px;color:var(--soft);line-height:1.75}}
@media (max-width:860px){{.hdr .bc{{display:none}}}}
</style>
</head>
<body>
<header class="hdr">
  <div class="hdr-in">
    <span class="tag">GALLERY</span>
    <h1>Diagram Gallery</h1>
    <span class="bc"><a href="workbook/agentic-development-study.html">Study workbook</a> · <a href="index.html">Home</a></span>
  </div>
</header>

<div class="gallery-wrap">
  <p class="gallery-intro">A browsable collection of every diagram across the deep-dive companions. Each card shows the diagram, the section it belongs to, and why it is there.</p>
  <input class="gallery-filter" type="search" placeholder="Filter by title, module, section, or reason…" aria-label="Filter diagrams by title, module, section, or reason">
  <div class="gallery-grid">
{''.join(cards)}
  </div>
  <p class="gallery-empty">No diagrams match your search.</p>
</div>

<footer>
  Part of the <a href="workbook/agentic-development-study.html">Agentic Development Study Programme</a>.
  Gallery is generated from <code>gallery-registry.json</code>; update the registry when adding diagrams.
</footer>

<div class="gallery-modal" role="dialog" aria-modal="true" aria-label="Enlarged diagram" hidden>
  <div class="gallery-modal-box">
    <button class="gallery-modal-close" type="button" aria-label="Close">&times;</button>
    <div class="gallery-modal-body"></div>
  </div>
</div>

<script>
(function(){{
  var input = document.querySelector('.gallery-filter');
  var grid = document.querySelector('.gallery-grid');
  var empty = document.querySelector('.gallery-empty');
  if (!input) return;
  input.addEventListener('input', function(){{
    var q = input.value.toLowerCase();
    var cards = grid.querySelectorAll('.gallery-card');
    var visible = 0;
    cards.forEach(function(card){{
      var match = (card.dataset.title + ' ' + card.dataset.module + ' ' + card.dataset.section + ' ' + card.dataset.why).indexOf(q) !== -1;
      card.style.display = match ? '' : 'none';
      if (match) visible++;
    }});
    empty.classList.toggle('show', visible === 0);
  }});
}})();

// Diagram lightbox: click (or Enter/Space on) a preview opens a modal with a
// full-size clone of that card's SVG. Cloned ids stay unique enough to render:
// every card's ids are prefixed (g-<n>-...) and the clone's defs are identical
// to the original's, so url(#...) resolution is correct either way.
(function(){{
  var modal = document.querySelector('.gallery-modal');
  var grid = document.querySelector('.gallery-grid');
  if (!modal || !grid) return;
  var body = modal.querySelector('.gallery-modal-body');
  var box = modal.querySelector('.gallery-modal-box');
  var closeBtn = modal.querySelector('.gallery-modal-close');
  var lastTrigger = null;

  function open(preview){{
    var svg = preview.querySelector('svg');
    if (!svg) return;
    // The card's SVG CSS is scoped to its g-card-N class; carry that class
    // onto the modal box so the clone renders with the original styling.
    var m = preview.className.match(/g-card-\\d+/);
    box.className = 'gallery-modal-box' + (m ? ' ' + m[0] : '');
    body.replaceChildren(svg.cloneNode(true));
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    lastTrigger = preview;
    closeBtn.focus();
  }}

  function close(){{
    if (modal.hidden) return;
    modal.hidden = true;
    body.replaceChildren();
    document.body.style.overflow = '';
    if (lastTrigger) {{
      lastTrigger.focus();
      lastTrigger = null;
    }}
  }}

  grid.addEventListener('click', function(e){{
    var preview = e.target.closest('.gallery-preview');
    if (preview) open(preview);
  }});
  grid.addEventListener('keydown', function(e){{
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var preview = e.target.closest('.gallery-preview');
    if (preview) {{
      e.preventDefault();
      open(preview);
    }}
  }});
  closeBtn.addEventListener('click', close);
  modal.addEventListener('click', function(e){{
    if (e.target === modal) close();
  }});
  document.addEventListener('keydown', function(e){{
    if (e.key === 'Escape') close();
  }});
}})();
</script>
</body>
</html>
'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {out_path} ({len(cards)} cards)")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--draft-registry":
        draft_registry(DEEPDIR, os.path.join(ROOT, "gallery-registry-draft.json"))
    elif len(sys.argv) > 2 and sys.argv[1] == "--output":
        generate_gallery(DEEPDIR, REGISTRY, sys.argv[2])
    else:
        generate_gallery(DEEPDIR, REGISTRY, OUT)
