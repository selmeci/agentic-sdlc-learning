#!/usr/bin/env python3
"""Verify the gallery modal scales the SVG to fill the viewport.

This is a structural guard, not a pixel-perfect visual test. It checks that
gallery.html styles the modal box with viewport units and the modal SVG with
width/height scaling so the enlarged diagram fills the screen rather than
rendering at the thumbnail's capped size.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GALLERY = os.path.join(ROOT, "gallery.html")


def extract_css_blocks(s):
    return "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, flags=re.S))


def rule_for(css, selector):
    """Return the declaration block for the first matching selector."""
    pattern = re.escape(selector) + r"\s*\{([^}]*)\}"
    m = re.search(pattern, css)
    return m.group(1).strip() if m else ""


def main():
    if not os.path.exists(GALLERY):
        print("FAIL gallery.html missing")
        return 1

    s = open(GALLERY, encoding="utf-8").read()
    css = extract_css_blocks(s)

    box = rule_for(css, ".gallery-modal-box")
    body = rule_for(css, ".gallery-modal-body")
    svg = rule_for(css, ".gallery-modal-body svg")

    problems = []

    # The modal must be sized in viewport units so it grows with the screen.
    if not re.search(r"\bwidth\s*:\s*[^;]*vw", box):
        problems.append(".gallery-modal-box does not use vw for width")
    if not re.search(r"\bheight\s*:\s*[^;]*vh", box):
        problems.append(".gallery-modal-box does not use vh for height")

    # It must not be capped at the old 1100px thumbnail-like width.
    if "1100px" in box:
        problems.append(".gallery-modal-box still caps width at 1100px")

    # The modal body should center the SVG and fill the box.
    if "display:flex" not in body:
        problems.append(".gallery-modal-body is not a flex container")
    if "align-items:center" not in body or "justify-content:center" not in body:
        problems.append(".gallery-modal-body does not center the SVG")

    # The SVG must scale to fill the available space, not keep thumbnail sizing.
    if "width:100%" not in svg or "height:100%" not in svg:
        problems.append(".gallery-modal-body svg does not fill the modal body")

    if problems:
        print("FAIL gallery modal is not viewport-scaled:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("PASS gallery modal scales to fill the viewport")
    return 0


if __name__ == "__main__":
    sys.exit(main())
