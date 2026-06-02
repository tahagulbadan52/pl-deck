#!/usr/bin/env python3
"""Reusable deck assembler for pl-deck.

Turns a list of slide-HTML strings into ONE self-contained, navigable deck:
inlines MD Nichrome (base64), tokens.css + deck-base.css + deck-runtime.css,
base64-inlines every phosphor icon (incl. watermarks), and inlines logos.

Usage (a fresh composer is ~30 lines):
    from assemble_deck import *          # ic, stat, feat, pillar, tile, chk,
                                          # imgph, logo, build
    S = []
    S.append(f'''<section class="slide theme-sabbath"> … </section>''')
    S.append(feat('map-pin', 'MENA', 'UAE · KSA · …', 'Home base'))
    …
    build(S, "Geopolitical Risks 2026", "/path/out-deck.html")

Card helpers emit the standard filled patterns (icon-xl + content + tag +
watermark) so output obeys the font-floor and 55%-empty rules automatically.
"""
import base64, pathlib

SKILL = pathlib.Path(__file__).resolve().parent.parent
PHOS = SKILL / "assets/phosphor-icons/SVGs/bold"
_icache = {}

def _b64_icon(name):
    if name not in _icache:
        _icache[name] = base64.b64encode((PHOS / f"{name}-bold.svg").read_bytes()).decode()
    return _icache[name]

def ic(name, kind="lg"):
    """Inline phosphor icon (base64 data URI). kind: lg | xl | wm | sm."""
    cls = {"lg": "icon icon-lg", "xl": "icon icon-xl", "wm": "icon wm", "sm": "icon"}[kind]
    return f"<span class=\"{cls}\" style=\"--icon:url('data:image/svg+xml;base64,{_b64_icon(name)}')\"></span>"

def badge(name, sm=False):
    """Primary card icon in a SOLID accent badge — gives weight so icons never
    read thin/light. Use this for the main card icon (not watermarks)."""
    s = " sm" if sm else ""
    return (f"<span class=\"icon-badge{s}\"><span class=\"icon\" "
            f"style=\"--icon:url('data:image/svg+xml;base64,{_b64_icon(name)}')\"></span></span>")

def logo(name="icon_white"):
    """Inline a PL logo SVG. name e.g. icon_white / icon_blue. Wrap in .cover-logo."""
    folder = {"icon_white": "icon/white", "icon_blue": "icon/blue",
              "icon_purple": "icon/purple", "icon_black": "icon/black"}.get(name, "icon/white")
    return (SKILL / f"assets/Pl Logos/{folder}/{name}.svg").read_text()

def stat(icon, num, label, ctx="", cls="card-haze", numcls="num hero", extra="", center=False):
    c = f'<p class="ctx" style="margin:0;">{ctx}</p>' if ctx else ''
    ctr = " center" if center else ""
    return (f'<div class="card {cls} feature{ctr}" style="{extra}">{ic(icon,"wm")}'
            f'<div class="card-top">{badge(icon)}</div>'
            f'<div><div class="{numcls}">{num}</div><div class="label">{label}</div></div>{c}</div>')

def feat(icon, title, desc, tag="", cls="card-haze", idx=""):
    ix = f'<span class="idx">{idx}</span>' if idx else ''
    tg = f'<span class="tag">{tag}</span>' if tag else ''
    return (f'<div class="card {cls} feature center">{ic(icon,"wm")}'
            f'<div class="card-top">{badge(icon)}{ix}</div>'
            f'<div><div class="num" style="font-size:var(--fs-card-title);">{title}</div>'
            f'<p class="ctx" style="margin-top:14px;">{desc}</p></div>{tg}</div>')

def pillar(icon, idx, label, title, desc):
    return (f'<div class="card card-haze feature center">{ic(icon,"wm")}'
            f'<div class="card-top">{badge(icon)}<span class="idx">{idx}</span></div>'
            f'<div><div class="label" style="color:var(--accent);font-size:var(--fs-label);">{label}</div>'
            f'<div class="num" style="font-size:var(--fs-card-title);margin-top:6px;">{title}</div>'
            f'<p class="ctx" style="margin-top:14px;">{desc}</p></div></div>')

def tile(icon, label):
    return f'<div class="tile">{ic(icon,"sm")}<span>{label}</span></div>'

def chk(items):
    return "<ul class='checklist'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def imgph(prompt, dims):
    return (f'<div class="img-placeholder" style="flex:1 1 0;align-self:stretch;"><div>'
            f'<div class="label">Image needed</div><div class="prompt">{prompt}</div>'
            f'<div class="size">{dims}</div></div></div>')

def build(slides, title, out_path):
    font_b64 = base64.b64encode((SKILL / "assets/MDNichrome-Bold (3).otf").read_bytes()).decode()
    tokens  = (SKILL / "tokens.css").read_text()
    base    = (SKILL / "lib/deck-base.css").read_text()
    runtime = (SKILL / "lib/deck-runtime.css").read_text()
    rjs     = (SKILL / "lib/deck-runtime.js").read_text()
    holders = "\n".join(f'<div class="slide-holder" data-i="{i}">{s}</div>'
                        for i, s in enumerate(slides))
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Platinumlist</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@font-face {{ font-family:'MD Nichrome'; src:url(data:font/otf;base64,{font_b64}) format('opentype'); font-weight:700; }}
{tokens}
{base}
{runtime}
</style></head><body>
<div class="slide-wrapper"><div id="slideContainer">
{holders}
</div></div>
<div class="slide-counter" id="count"></div>
<script>{rjs}</script>
</body></html>"""
    p = pathlib.Path(out_path)
    p.write_text(html)
    print(f"wrote {p} ({len(slides)} slides, {p.stat().st_size//1024} KB)")
    return p
