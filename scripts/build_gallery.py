#!/usr/bin/env python3
"""Assemble all block templates into one self-contained gallery.html for
visual QA. Embeds MD Nichrome (base64), inlines tokens.css + deck-base.css,
and stacks every block as a 1920x1080 slide. Run from the skill root."""
import base64, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORDER = [
    "cover-hero", "section-divider", "stat-grid", "segment-row", "hero-stat-row",
    "methodology-windows", "timeline-table", "layer-columns", "data-table",
    "bar-compare", "quality-stats", "funnel-table", "split-audience", "rank-list",
    "summary-numbered", "case-study", "channels-table", "service-checklist",
    "service-pillars", "service-statpair", "cta-nextsteps", "closing",
]

def read(p):
    return (ROOT / p).read_text() if (ROOT / p).exists() else ""

font_b64 = base64.b64encode((ROOT / "assets/MDNichrome-Bold (3).otf").read_bytes()).decode()
tokens = read("tokens.css")
base = read("lib/deck-base.css")

blocks = []
for bid in ORDER:
    tpl = ROOT / "blocks" / bid / "template.html"
    if tpl.exists():
        blocks.append(f"<!-- ===== {bid} ===== -->\n" + tpl.read_text())

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@font-face {{ font-family:'MD Nichrome'; src:url(data:font/otf;base64,{font_b64}) format('opentype'); font-weight:700; }}
{tokens}
{base}
body {{ background:#0a0a0a; }}
.slide {{ margin:0 auto 28px; box-shadow:0 0 0 1px rgba(255,255,255,.08); }}
</style></head><body>
{''.join(blocks)}
</body></html>"""

out = ROOT / "gallery.html"
out.write_text(html)
print(f"wrote {out} with {len(blocks)} blocks")
