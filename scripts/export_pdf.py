#!/usr/bin/env python3
"""Robust PDF export for pl-deck decks — SCREENSHOT-BASED, not Chrome print-to-PDF.

WHY THIS EXISTS
---------------
Deck icons are CSS masks (`-webkit-mask` + `background-color: currentColor`).
Chrome's print-to-PDF engine (`page.pdf()` / `--print-to-pdf`) rasterizes masks
unreliably: when the mask drops out, the element fills as a solid CURRENTCOLOR
BOX; when it partially applies, the icon is CLIPPED. This is specific to the
print path — on-screen rendering (and screenshots) are always correct.

So instead of printing, we screenshot each slide exactly as the browser draws it
(high-res), then stitch the PNGs into a true 1920x1080 PDF. The PDF becomes
pixel-identical to the browser. Trade-off: pages are images, not selectable text
— fine for a pitch deck, and the only reliable path for mask-icon decks.

USAGE
-----
    python3 export_pdf.py /abs/path/to/deck.html [/abs/path/out.pdf]

Requires: puppeteer at /tmp/node_modules (the skill installs it there), and
Pillow (`pip install Pillow`).
"""
import sys, os, subprocess, tempfile, glob, pathlib

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: export_pdf.py <deck.html> [out.pdf]")
    html = pathlib.Path(sys.argv[1]).resolve()
    out  = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else html.with_suffix(".pdf")
    shots = pathlib.Path(tempfile.mkdtemp(prefix="pldeck_shots_"))
    SCALE = 2  # 3840x2160 capture → crisp text

    node_script = shots / "_shoot.js"
    node_script.write_text(f"""
const puppeteer = require('/tmp/node_modules/puppeteer');
(async () => {{
  const browser = await puppeteer.launch({{ headless: true, args: ['--no-sandbox'] }});
  const page = await browser.newPage();
  await page.setViewport({{ width: 1920, height: 1080, deviceScaleFactor: {SCALE} }});
  await page.goto('file://{html}', {{ waitUntil: 'networkidle0', timeout: 60000 }});
  await page.evaluateHandle('document.fonts.ready');
  const n = await page.evaluate(() => document.querySelectorAll('.slide-holder').length);
  for (let i = 0; i < n; i++) {{
    await page.evaluate((idx) => {{
      document.querySelectorAll('.slide-holder').forEach((h, k) => {{
        h.classList.toggle('active', k === idx);
        h.style.opacity = (k === idx) ? '1' : '0';
      }});
    }}, i);
    await new Promise(r => setTimeout(r, 350));
    await page.screenshot({{ path: '{shots}/slide_' + String(i+1).padStart(2,'0') + '.png',
      clip: {{ x: 0, y: 0, width: 1920, height: 1080 }} }});
  }}
  await browser.close();
  console.log('shots:' + n);
}})();
""")
    subprocess.run(["node", str(node_script)], check=True)

    from PIL import Image
    files = sorted(glob.glob(str(shots / "slide_*.png")))
    if not files:
        sys.exit("no screenshots captured")
    imgs = [Image.open(f).convert("RGB") for f in files]
    # resolution=72*SCALE → 3840px/192*72 = 1440pt = 1920px @96dpi (true 16:9 1080p)
    imgs[0].save(str(out), save_all=True, append_images=imgs[1:], resolution=72.0 * SCALE)
    print(f"wrote {out} ({len(files)} pages, {out.stat().st_size//1048576} MB, true 1920x1080)")

if __name__ == "__main__":
    main()
