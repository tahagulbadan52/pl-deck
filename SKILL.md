---
name: pl-deck
description: "Platinumlist presentation builder. Generates branded HTML slide decks (16:9) from raw content, findings, or topics. Uses Platinumlist design system with MD Nichrome + Inter fonts, purple/cyan and dark/green themes, card-based layouts, and Chart.js data visualization. Outputs a self-contained HTML file on the first pass — PDF export is deferred until the user explicitly asks for it after reviewing and finalizing edits. Triggers on: presentation, deck, slides, make a deck, build presentation, pitch deck, campaign report deck, create slides."
argument-hint: "[topic or content description]"
---

# Platinumlist Presentation Builder

Generates self-contained branded HTML presentations from raw content, findings,
or topic descriptions. Follows the Platinumlist design system with two visual
themes, card-based layouts, and Chart.js data visualization.

## Quick Reference

| Command | What it does |
|---------|-------------|
| `/pl-deck` | Interactive intake → asks questions → generates deck |
| `/pl-deck campaign report for [event]` | Generates a campaign report deck |
| `/pl-deck marketing pitch` | Generates a marketing services pitch deck |

---

## Phase 1: Intake & Clarification

When invoked, ALWAYS go through this intake process. Never generate a deck without
understanding the full context. Ask questions until everything is crystal clear.

### Step 1: Understand the Request

Read what the user has provided. They may give you:
- **Raw data** (campaign metrics, analytics exports, CSV data)
- **Topics/bullet points** (a list of things to cover)
- **A full brief** (detailed content for each slide)
- **A vague request** ("make a deck about our marketing services")

### Step 2: Ask Clarifying Questions

Combine ALL questions into ONE message. Never drip-feed questions one at a time.
Only ask what you genuinely don't know — skip questions the user already answered.

**Always determine:**
1. **Deck type** — Which best describes this?
   - Campaign Report (post-campaign results for a client)
   - Marketing Pitch (selling Platinumlist marketing services)
   - Platform Overview (showcasing Platinumlist as a platform)
   - Custom (describe the purpose)

2. **Audience** — Who will see this? (event organizer, sponsor, internal team, partner)

3. **Key message** — What's the ONE thing the audience should remember after seeing this deck?

4. **Data availability** — Do you have specific numbers/metrics to include, or should I use placeholders?

5. **Slide count preference** — Quick & punchy (5-8 slides) or detailed walkthrough (12-20 slides)?

6. **Specific content** — Any must-include slides, stats, or talking points?

7. **CTA** — What should the audience do after seeing this? (book a call, sign a contract, approve budget, etc.)

### Step 3: Research & Enrich (if needed)

Before generating, consider whether the content would benefit from:
- **Web research** — Look up current market stats, industry benchmarks, competitor data if the user's content references claims that need backing
- **Platform data** — If Adspirer/Windsor connections are available, pull live campaign data
- **Brand context** — Load Platinumlist brand voice skills for tone alignment

Use the WebSearch tool or Adspirer MCP tools when the user provides raw data that
needs context (e.g., "our ROAS was 22x" → research industry average to show how
impressive that is).

### Step 4: Content Architecture

Before writing any HTML, plan the deck structure. Present it to the user for approval:

```
Proposed Deck Structure:
========================
Slide 1: [Cover] — Title + subtitle
Slide 2: [Stats] — Platform overview numbers
Slide 3: [Audience] — Target audience profile with charts
...
Slide N: [CTA] — Next steps + contact
```

**Content restructuring rules (apply automatically):**
- If the user gives content in a suboptimal order, REARRANGE it for narrative flow
- Group related content — don't scatter similar topics across distant slides
- Lead with the hook/problem, build the case, close with proof + CTA
- If a slide has too much content, SPLIT it into multiple slides
- If a slide has too little, MERGE it with an adjacent slide
- Every data point should serve the narrative — cut vanity metrics that don't support the key message

**Narrative arc templates:**

**Campaign Report arc:**
Cover → Executive Summary (1 slide, 3 hero stats) → Audience Profile → Channel Performance (1 per channel) → Key Insights & Learnings → Recommendations → CTA

**Marketing Pitch arc:**
Cover → The Opportunity (problem/market) → Platform Stats (credibility) → Services Overview → Audience Data → Case Study / Proof → Packages / Pricing → CTA

**Platform Overview arc:**
Cover → Market Position → Key Stats → Products & Features → Audience Profile → Success Stories → CTA

Wait for user approval of the structure before generating.

---

## Phase 2: HTML Generation

### Design System

**Format:** 16:9 (1920 x 1080px), self-contained HTML file

**Fonts:**
- **MD Nichrome Bold** — Headlines ONLY. Always `text-transform: uppercase`, `letter-spacing: -0.02em`. Load from base64 embedded @font-face. The font file is at: `~/.claude/skills/pl-deck/assets/MDNichrome-Bold (3).otf` — convert to base64 and embed.
- **Inter** — Everything else (body, labels, descriptions, card text). Load from Google Fonts CDN: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`

**Type scale (enforce strictly):**

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Slide headline | MD Nichrome | 48-64px | 700 |
| Card title | MD Nichrome | 24-32px | 700 |
| Hero stat number | Inter | 48-80px | 700 |
| Body text | Inter | 18-22px | 400-500 |
| Card description | Inter | 16-18px | 400 |
| Labels/captions | Inter | 14-16px | 400 |

**Minimum font size: 14px anywhere on the slide. Body text minimum: 18px.**

**Color Themes:**

Two themes, applied via CSS class on each slide container:

| Token | Purple/Cyan `.theme-purple` | Dark/Green `.theme-dark` |
|-------|---------------------------|------------------------|
| `--bg` | `#1a0533` | `#1a1a2e` |
| `--accent-primary` | `#79E2FF` (cyan) | `#B8FF00` (lime) |
| `--accent-secondary` | `#7B2FF2` (purple) | `#79E2FF` (cyan) |
| `--card-bg` | `#79E2FF` | `#B8FF00` |
| `--card-text` | `#1a0533` | `#1a1a2e` |
| `--text` | `#ffffff` | `#ffffff` |

**Theme auto-selection:**
- **Purple/Cyan** — Cover slides, services/features, platform overview, CTA, any "selling" slide
- **Dark/Green** — Data slides, campaign performance, metrics, charts, any "proving" slide

**CSS Custom Properties:**
```css
:root {
  --bg-purple: #1a0533;
  --cyan: #79E2FF;
  --purple: #7B2FF2;
  --bg-dark: #1a1a2e;
  --lime: #B8FF00;
  --text-white: #ffffff;
  --card-radius: 16px;
  --slide-padding: 60px;
}
```

### Layout Components

**Every slide** uses `display: flex; flex-direction: column; justify-content: center; gap: 40px;` with `padding: var(--slide-padding)`. Slides are 1920×1080 — content MUST fill the canvas vertically. Never leave the bottom 30%+ empty.

**Card density rules (critical — violating these makes decks feel broken):**
When a grid stretches cards to fill vertical space, each card MUST have enough content to justify its footprint. An 8-card 4×2 grid on a 1920×1080 slide gives each card ~400px of height — a 22px title + 16px subtitle occupies 50px and leaves the other 350px empty. That reads as broken, not minimal.

Minimum content per stretched card (≥300px tall) — **ALL FIVE required, not four**:
1. **Icon (phosphor, 48–72px)** — sits in the header row alongside a faint number (01, 02…) — icon is mandatory, the number alone does NOT satisfy this
2. **Title** — MD Nichrome, 26–32px
3. **Body copy** — 2–3 lines of real description at 15–18px (not a single 8-word fragment)
4. **Mid-card content block** — a deliverables list (3 checkmark items), mini-stat row (3 numbers + labels), or feature chips. This is what fills the dead middle. **Never leave a gap between body copy and the bottom tag.**
5. **Proof tag / metric / timing badge** — pinned to the bottom, visually distinct (contrasting pill, border-top divider, or inverted background chip). Not just a low-opacity label.

Use `display: flex; flex-direction: column;` with `margin-top: auto` on the mid-card block's parent so it pushes the bottom tag down and expands to fill. Do NOT use `justify-content: space-between` alone — it creates a vacuum in the middle when there's nothing to push apart.

**The empty-middle test:** Squint at the card. If the vertical center is blank (no text, no divider, no icon), the card fails. Add a deliverables list, a stat row, or shrink the grid (e.g. go from 5 columns to 4, or from 2 rows to 1) so the cards don't stretch that tall in the first place.

**When in doubt — shrink the card, don't inflate the content.** A 5-across grid of timeline steps looks better at 720px height than 900px with padding. Options to shrink:
- Reduce the grid's `.fill` height by giving the header more space (e.g. `flex: 0 0 280px` header, `flex: 0 0 auto` grid, footer)
- Cap the grid with `max-height` and let slide padding absorb the excess
- Drop to fewer, wider cards (3 big cards beats 5 thin empty ones)

Also add a supporting sub-headline/description next to the main headline (right-aligned, 40% width, 20–22px) — a lone H1 at the top of a grid slide looks unfinished.

**Vertical fill rules:**
- Base slide CSS includes `justify-content: center` so content is vertically centered by default
- For header + body layouts, wrap the body in a `.fill` container (`flex: 1 1 auto; min-height: 0`) so grids/charts expand to consume available space
- Card grids inside `.fill` should use `height: 100%` so cards stretch
- If content looks sparse at 1920×1080, SCALE UP font sizes (use the upper end of each range) rather than leaving whitespace
- Base body font-size on `.slide` is `22px`; headlines default to `64px`; subheadlines `28px` — do NOT go below these unless the slide is genuinely information-dense

**Icon convention (MANDATORY — do not use emojis):**

All icons come from the user's `assets/` folder. Never use emoji characters, never use Unicode symbols, never invent SVGs. Before generating a deck, **always list the assets folder** to see what's available:

```bash
ls ~/.claude/skills/pl-deck/assets/
ls ~/.claude/skills/pl-deck/assets/phosphor-icons/SVGs/bold/
```

The user keeps adding new assets over time. Re-list the folder every run — don't rely on memory.

**Current assets (as of last check):**
- `assets/phosphor-icons/SVGs/bold/` — 1,512 Phosphor bold icons (also available: `light`, `regular`, `fill`, `thin`, `duotone`). **Default to `bold` for pitch decks.**

**How to use icons:**

Include this CSS helper once in the deck `<style>` block:

```css
.icon {
  display: inline-block;
  width: 48px; height: 48px;
  -webkit-mask: var(--icon) center / contain no-repeat;
  mask: var(--icon) center / contain no-repeat;
  background-color: currentColor;
  flex-shrink: 0;
}
.icon-sm { width: 28px; height: 28px; }
.icon-lg { width: 72px; height: 72px; }
```

Then drop icons in like this (color is controlled by the parent `color:` or direct `color:`):

```html
<span class="icon icon-lg" style="--icon:url('data:image/svg+xml;base64,PHN2Zy...');color:var(--cyan);"></span>
```

**HARD RULE — icons must be base64 data URIs, not file paths.** While authoring, you may write the HTML with `url('assets/...svg')` placeholders for readability, but **before writing the final file to disk, run the icon-inlining step** so every `url('assets/phosphor-icons/...')` becomes `url('data:image/svg+xml;base64,...')`. This:

1. Makes the HTML fully portable (works from any CWD, not just next to the assets folder)
2. Makes the HTML self-contained (can be emailed, shared, uploaded without a folder)
3. Makes PDF export reliable (headless Chrome doesn't block on file:// mask resources)

Inlining script (run every time the deck is regenerated):

```python
import re, base64, pathlib, os
skill_dir = pathlib.Path(os.path.expanduser("~/.claude/skills/pl-deck"))
html_path = pathlib.Path("[deck-name]-deck.html")
html = html_path.read_text()
pattern = re.compile(r"url\('(assets/phosphor-icons/SVGs/bold/[^']+\.svg)'\)")
for ref in set(pattern.findall(html)):
    icon_path = skill_dir / ref
    if icon_path.exists():
        b64 = base64.b64encode(icon_path.read_bytes()).decode('ascii')
        html = html.replace(f"url('{ref}')", f"url('data:image/svg+xml;base64,{b64}')")
html_path.write_text(html)
```

**Icon pairing cheatsheet (use these mappings, or grep the folder for alternatives):**
- Visibility → `eye-bold.svg`
- Targeting / Audience → `target-bold.svg`, `users-three-bold.svg`, `users-bold.svg`
- Consistency / Loops → `arrows-clockwise-bold.svg`
- Broadcast / Awareness → `broadcast-bold.svg`, `megaphone-bold.svg`
- Conversions / Growth → `trend-up-bold.svg`, `chart-line-bold.svg`
- Strategy → `compass-bold.svg`, `strategy-bold.svg`
- Content / Video → `film-slate-bold.svg`, `video-camera-bold.svg`, `camera-bold.svg`
- Editing / Post-prod → `scissors-bold.svg`, `palette-bold.svg`, `paint-brush-bold.svg`
- Email → `envelope-bold.svg`, `envelope-open-bold.svg`, `paper-plane-bold.svg`
- Push / Mobile → `bell-bold.svg`, `device-mobile-bold.svg`
- Reporting → `trend-up-bold.svg`, `chart-line-bold.svg`, `presentation-bold.svg`
- Link / Connection → `link-bold.svg`, `handshake-bold.svg`
- Speed / Urgency → `lightning-bold.svg`, `rocket-bold.svg`, `fire-bold.svg`
- Platform logos → `meta-logo-bold.svg`, `google-logo-bold.svg`, `tiktok-logo-bold.svg`, `apple-logo-bold.svg`, `instagram-logo-bold.svg`, `youtube-logo-bold.svg`, `linkedin-logo-bold.svg`, `amazon-logo-bold.svg`

**Enforcement:**
1. Before finalising a deck, `grep` for emojis (`&#x1F`, `&#x2`, 🎯 📣 🚀 etc.) — if any appear, replace them with phosphor icons.
2. Before finalising, verify every `url('assets/...')` actually exists on disk. A 404'd icon breaks the layout.
3. If no icon fits the concept, search the folder: `ls assets/phosphor-icons/SVGs/bold/ | grep -i <keyword>`.

**Future assets:**
The `assets/` folder will grow. Re-list it at the start of every run. If a future folder exists (e.g., `assets/brand-photos/`, `assets/illustrations/`, `assets/textures/`), prefer those over the `img-placeholder` pattern.

**Image placeholder convention:**
When a slide needs a visual (photo, illustration, mockup) that Claude can't generate, insert an `.img-placeholder` div instead of skipping it. The placeholder reserves the correct footprint and tells the user exactly what image is needed.

```html
<div class="img-placeholder" style="height: 400px;">
  <div>
    <div class="label">IMAGE NEEDED</div>
    <div class="prompt">Hero shot of a packed concert crowd at night, stage lights visible, shot from behind audience toward stage. Energetic, premium feel.</div>
    <div class="size">1200 × 800px • JPG or PNG</div>
  </div>
</div>
```

Required placeholder CSS (include in every deck):
```css
.img-placeholder {
  display: flex; align-items: center; justify-content: center;
  text-align: center; border: 3px dashed rgba(121, 226, 255, 0.6);
  background: rgba(121, 226, 255, 0.05); border-radius: var(--card-radius);
  padding: 32px; color: rgba(255,255,255,0.7);
}
.img-placeholder .label { font-size: 14px; font-weight: 700; color: var(--cyan); letter-spacing: 0.1em; margin-bottom: 12px; }
.img-placeholder .prompt { font-size: 20px; line-height: 1.4; margin-bottom: 12px; max-width: 80%; }
.img-placeholder .size { font-size: 14px; color: rgba(255,255,255,0.5); font-family: monospace; }
```

Placeholder prompts must be specific: subject, mood, composition, and exact pixel dimensions. Never write "photo here" — always write a directable brief.

**Viewport scaling (required JS):**
Every deck must scale the 1920×1080 container to fit the browser window. Include:
```javascript
function scaleSlides() {
  const c = document.getElementById('slideContainer');
  const s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
  c.style.transform = 'scale(' + s + ')';
  const w = document.querySelector('.slide-wrapper');
  w.style.justifyContent = 'center';
  w.style.alignItems = 'center';
}
window.addEventListener('resize', scaleSlides);
scaleSlides();
```
Wrapper should always center the scaled container so small viewports don't feel "zoomed out in the corner."

**Card Grid (most common layout):**
```css
.grid-2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.grid-3x2 { display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 16px; }
.grid-2x4 { display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: repeat(4, 1fr); gap: 16px; }
```

**Card types:**
- `.card-cyan` — Background `#79E2FF`, text `#1a0533`, border-radius 16px, padding 24px
- `.card-purple` — Background `#7B2FF2`, text white, border-radius 16px, padding 24px
- `.card-lime` — Background `#B8FF00`, text `#1a1a2e`, border-radius 16px, padding 24px
- `.card-bordered-lime` — Border 2px solid `#B8FF00`, transparent bg, white text, border-radius 16px
- `.card-bordered-cyan` — Border 2px solid `#79E2FF`, transparent bg, white text, border-radius 16px

**Split layout:**
Left side (60%) = headline + description. Right side (40%) = stacked stat cards.

**Hero stat pattern:**
Number at 48-80px (Inter 700), label beneath at 18px, inside accent-color card.

**Checklist (not bullets):**
```css
.checklist li::before { content: '✓ '; color: inherit; font-weight: 700; }
```
Max 4-6 items. Never use plain bullet points.

### Logos

**Platinumlist icon (cyan)** — embed as inline SVG on cover slides, centered above title:
```
~/.claude/skills/pl-deck/assets/Pl Logos/icon/blue/icon_blue.svg
```

**Platinumlist wordmark (white)** — embed on CTA/closing slide:
```
~/.claude/skills/pl-deck/assets/Pl Logos/latin/horizontal/svg/vertical_white.svg
```

Other logo variants available under `~/.claude/skills/pl-deck/assets/Pl Logos/`:
- `icon/{blue,purple,white,black}/icon_{color}.svg` — just the icon mark
- `latin/horizontal/svg/horizontal_{black,blue,purple,white}.svg` — horizontal wordmark
- `latin/vertical/svg/vertical_{black,blue,purple,white}.svg` — stacked wordmark
- `arabic/horizontal/` and `arabic/vertical/` — Arabic variants for RTL decks

Read these SVG files and inline them directly in the HTML.

### Charts (Chart.js)

Load from CDN: `https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js`

**Chart color palette:**
- Purple theme charts: `#79E2FF`, `#B8FF00`, `#7B2FF2`, `#FF6B6B`, `#FFB347`
- Dark theme charts: `#B8FF00`, `#79E2FF`, `#7B2FF2`, `#FF6B6B`, `#FFB347`

**Chart rules:**
- One chart per slide maximum
- Chart title = the insight, not the metric name
- Always annotate the key data point
- Doughnut charts for proportions (max 5 segments), bar charts for comparisons, horizontal bar for rankings
- No 3D effects, no unnecessary gridlines
- Font family: Inter
- Background transparent, no chart border

**Chart.js configuration defaults:**
```javascript
Chart.defaults.font.family = 'Inter';
Chart.defaults.color = '#ffffff';
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.padding = 20;
```

### Slide Types Reference

Use these patterns when building slides. Mix and match based on content:

| Slide Type | When to Use | Layout |
|-----------|-------------|--------|
| **Cover** | First slide always | Icon top-center, big headline, subtitle, platform row |
| **Stats Grid** | Showcasing numbers | 2x2 or 3x2 grid of accent-color cards with hero stats |
| **Audience Profile** | Demographics data | Pie chart + bar chart + stacked stat cards |
| **Services Grid** | Features/offerings | 2x4 or 2x3 grid of purple cards with title + desc |
| **Digital Ads** | Ad performance | KPI cards + platform breakdown cards + phone mockups |
| **Purchase Behavior** | Buying patterns | Legend + stacked bar chart + value cards |
| **Live Events** | Event showcases | Two large cards with event visual + checklist |
| **Campaign Results** | Performance proof | Bar chart + hero stat cards |
| **Numbers Row** | Impact stats | 4-6 hero stats in horizontal row, full-width |
| **Data Visualization** | Complex data | Full-width chart, minimal decoration |
| **Comparison** | Before/after, A vs B | Two columns with contrasting data |
| **Quote/Testimonial** | Social proof | Large quote text, attribution, optional photo |
| **CTA** | Always last slide | Wordmark logo, headline, CTA button, contact info |

### Navigation & Interactivity

```javascript
// Arrow key navigation (Left/Right, PageUp/PageDown)
// Slide counter in bottom-right: "3 / 12"
// URL hash tracking: #slide-1, #slide-2, etc.
// Smooth opacity fade transitions (300ms)
```

### Print/PDF Support

```css
@media print {
  .slide { page-break-after: always; break-after: page; }
  .slide-counter { display: none; }
  /* Show all slides stacked, no transforms */
}
```

---

## Phase 3: Output & Review

### File Output

Write the HTML file to the current working directory:
- Filename: `[deck-name]-deck.html` (kebab-case, e.g., `marketing-pitch-deck.html`)
- The file must be **completely self-contained** — embedded font, inline SVGs, CDN scripts only

### Post-Generation

After writing the file, present:
```
✓ [filename].html generated ([N] slides)

Deck structure:
  1. [Slide title] — [theme]
  2. [Slide title] — [theme]
  ...

To view: Open the HTML file in any browser

Want me to adjust any slides, add/remove content, or change the narrative flow?

When you're happy with the final version, ask me to export to PDF and I'll generate it then.
```

---

## PDF Export (Phase 4 — On Request Only)

**HARD RULE: Never generate a PDF on the first deck build. Never generate a PDF as part of the same turn that produced the HTML. Never proactively suggest "I'll also export the PDF now."**

The PDF is produced ONLY after the user has reviewed the HTML and explicitly asks for the export (e.g., "export to PDF", "now make the PDF", "finalize as PDF", "I'm happy, generate the PDF").

### Why deferred

1. Decks always need 2–5 rounds of content/layout edits after the first pass
2. Re-exporting the PDF after every edit wastes ~30 seconds per round and clutters the folder
3. The PDF is a **sign-off artifact**, not a working draft — it should reflect the final approved deck
4. Users iterate faster when they only have to open the HTML in a browser (live reload on refresh) vs. re-opening a new PDF each time

### Trigger phrases that justify running the export

- "export to PDF" / "make the PDF" / "now PDF it" / "finalize as PDF"
- "I'm happy with it, generate the PDF"
- "ship it" / "it's done, PDF please"
- Any explicit mention of "PDF" AFTER the initial HTML has been reviewed

### Triggers that do NOT justify auto-exporting

- Initial `/pl-deck` invocation — HTML only
- "generate the deck" / "build the deck" / "make the presentation" — HTML only
- User approving the proposed structure — HTML only
- User saying "looks good" or "nice" without mentioning PDF — HTML only (ask if they want the PDF now)

### Pre-export checklist (run silently before invoking Puppeteer)

1. Inline all Phosphor SVG icons as base64 data URIs (Chrome headless fails to load file:// mask resources during print — icons render as solid blocks otherwise). Script:
   ```python
   import re, base64, pathlib
   html_path = pathlib.Path("[deck-name]-deck.html")
   html = html_path.read_text()
   pattern = re.compile(r"url\('(assets/phosphor-icons/SVGs/bold/[^']+\.svg)'\)")
   for ref in set(pattern.findall(html)):
       p = pathlib.Path(ref)
       if p.exists():
           b64 = base64.b64encode(p.read_bytes()).decode('ascii')
           html = html.replace(f"url('{ref}')", f"url('data:image/svg+xml;base64,{b64}')")
   html_path.write_text(html)
   ```
2. Verify the `@media print` block has all `!important` overrides for `.slide` positioning (the deck uses `position: absolute` + `opacity: 0` for inactive slides; print CSS must un-stack them).
3. Verify MD Nichrome is base64-embedded in the `@font-face` rule, not linked externally.

### Export command (Puppeteer, not Chrome CLI)

**HARD RULE: Use Puppeteer, never `chrome --print-to-pdf`.** Chrome's CLI does not honor `@page` sizes in pixels and frequently defaults to 1440×810 regardless of overrides. Puppeteer's `page.pdf({ width, height })` is the only reliable path to true 1920×1080.

Script (`/tmp/render-pdf.js`):
```javascript
const puppeteer = require('/tmp/node_modules/puppeteer');
(async () => {
  const htmlPath = '[absolute path to deck].html';
  const pdfPath  = '[absolute path to deck].pdf';
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0', timeout: 60000 });
  await new Promise(r => setTimeout(r, 2000));  // font + Chart.js settle
  await page.emulateMediaType('print');
  await page.pdf({
    path: pdfPath,
    width: '1920px', height: '1080px',
    printBackground: true, preferCSSPageSize: false,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });
  await browser.close();
})();
```

Install puppeteer to `/tmp/node_modules` if not already present: `cd /tmp && npm install puppeteer --silent`

### Post-Export

After writing the PDF, present:
```
✓ [filename].pdf generated (N pages, ~X MB, true 1920×1080)

Location: [absolute path]

Want me to adjust any slides? The HTML is still editable — just tell me what to change and I'll regenerate both.
```

---

## Quality Gates (Hard Rules — Never Violate)

### Content Rules
1. **One message per slide** — if a slide makes two points, split it
2. **Max 75 words per slide** (excluding chart labels and footnotes)
3. **Headlines are assertions, not topics** — "20M+ Users Trust Platinumlist" not "User Statistics"
4. **Max 6 checklist items per slide** — prefer icon+text cards over long lists
5. **No bullet-point walls** — if you have >4 text items, use a card grid instead
6. **Every deck ends with a CTA slide** — never "Thank you" or "Questions?"

### Visual Rules
7. **Card-based layouts by default** — rounded corners (16px), accent-color backgrounds, grid alignment
8. **MD Nichrome for headlines only, Inter for everything else** — no exceptions
9. **Three type sizes max per slide** — Heading, Subheading, Body
10. **20%+ whitespace** — generous padding, never crowd the slide
11. **One chart per slide maximum** — pair with stat callouts, not another chart
12. **No messy tables** — use card grids to display tabular data visually
13. **No generic stock imagery** — use CSS shapes, icons, or phone mockups instead
14. **Consistent color coding** — if "Meta" is cyan on slide 3, it stays cyan everywhere

### Structural Rules
15. **First slide is always a cover** — PL icon, bold headline, subtitle
16. **Last slide is always a CTA** — PL wordmark, action-oriented headline, contact info
17. **Theme consistency** — don't alternate themes randomly; group purple slides and dark slides
18. **Narrative flow** — hook → build → prove → close. Never start with data.
19. **Confidentiality footer** on data-sensitive slides: "This presentation contains proprietary information of Platinumlist."

### Anti-Patterns (Banned)
20. No text-heavy slides on services/pitch content
21. No slides without a clear purpose in the narrative arc
22. No orphan stats without context (always provide comparison or benchmark)
23. No Comic Sans, Papyrus, or any font other than MD Nichrome + Inter
24. No centered paragraph text — left-align body text, center only headlines and hero stats

### Pricing Card Rules (MANDATORY for any slide with packages/tiers)

- **Price is the hero, not a button.** Display the price as a large Inter 700 number (48–64px) in the accent color. Never wrap it in a pill/button shape — that makes viewers think it's clickable. CTA buttons belong on the final CTA slide only, and even there sparingly.
- **Every tier card must include:** icon + tier label (TIER 01) + name + duration/scope + **hero price** + "WHAT'S INCLUDED" deliverables list + "BEST FOR" bottom tag. Never six rows of floating text.
- **Mark one tier as MOST POPULAR** with a contrasting border + floating pill label — gives the viewer a recommended default and breaks visual monotony across a 4-across grid.
- **Group dense price lists into categories.** If you have 8 price points for the same thing (e.g. 6s/15s/30s/60s videos), collapse them into one card with a mini inner-grid of price tiles — not 8 separate cards.
- **Minimum body text on price slides: 15px.** Never go to 14px or below to cram in rows.

### CTA / Final Slide Rules

- **Final slide hierarchy:** eyebrow label → big headline → supporting paragraph → impact-stat row → contact section (GET IN TOUCH + email) → **wordmark logo at the bottom** → cities line → confidentiality note.
- **Logo goes at the BOTTOM on the CTA slide, not the top.** Think of it as a signature, not a letterhead. Leave visual breathing room above it.
- **Do NOT use `.cta-btn` styling on the final slide.** Buttons in a printed/presented deck are misleading — they imply interactivity that doesn't exist. Instead use MD Nichrome type + an arrow icon + contact line below it.
- **Cities line is the second-to-last element**, before confidentiality. Format: `platinumlist.net · Dubai · Abu Dhabi · Riyadh · Cairo` at 16px, low opacity.

### Card Density Gate (MANDATORY pre-flight check before delivering any deck)

Before declaring a deck done, walk through every card grid and apply the **empty-middle test**:

25. **No empty middles.** Every stretched card (≥300px tall) must have content occupying its vertical center — not just top (icon/title) and bottom (tag). Dead middle = card fails. Fix options: add a deliverables checklist, add a 3-stat mini-row, add feature chips, OR shrink the card.
26. **No `justify-content: space-between` without middle content.** That pattern creates vacuum when only two children exist. Either add a third child (deliverables/stats/chips) or use `margin-top:auto` on the bottom tag with real content above it.
27. **5-component card minimum on grids that stretch cards tall:** icon + title + body + middle-block + bottom-tag. If you can't fill all five, the grid has too many columns/rows — reduce it (5→4→3 columns, or 2→1 row).
28. **Bottom tag must be visually distinct** — contrasting pill, inverted background chip, or separated by a divider. An opacity-dimmed label floating alone at the bottom reads as forgotten, not designed.
29. **Height audit before sign-off:** for each grid slide, estimate card height = `(1080 − header − footer − gaps) / rows`. If cards are >350px and only have <4 content elements, the slide fails. Either add content or collapse the grid.
30. **If a screenshot shows empty bottom halves on cards, do NOT ship it.** Fix before declaring done — this is a terminal defect, not polish.
31. **Tiny-row pricing grids are banned.** An 8-cell grid of 18px title + 16px price on a full slide is visual noise. Rework into themed category cards with mini-grids inside, or a single-table layout with 32px+ rows. If a single row of data occupies <60px height on a 1080-tall slide, it's too small.
32. **No floating header-only slides.** If the page header takes 120px and the grid takes 300px, you have 660px of dead vertical canvas. Either expand the grid, add a supporting visual panel (chart/image placeholder/callout), or reduce slide padding. Never ship a slide where the bottom third is empty background.
33. **Image placeholders count as content.** If you can't fill a slot, drop in a `.img-placeholder` with a specific prompt and dimensions — the user provides images later. A placeholder with a real prompt is dramatically better than dead space.

### Chart & Data-Slide Rules

34. **Charts must have readable tick labels (13px+).** Chart.js defaults to ~11px ticks which are unreadable at presentation scale. Always set `ticks.font.size: 13–15px` and `weight: 600` for axis labels.
35. **Annotate bar values directly** on the bar (custom `afterDatasetsDraw` plugin) instead of forcing the viewer to read off the axis. Hide tooltips (`tooltip.enabled: false`) since decks are static.
36. **Donut/pie charts need a center label.** Put the dominant value (e.g. "61.6% MALE SKEW") absolute-positioned inside the donut hole — the chart without it is meaningless at a glance.
37. **Bar thickness 20–28px** for horizontal bars in presentation decks. Thin default bars disappear from the back of a room.
38. **Highlight the hero bar** with full accent color and dim the others (`rgba(…, 0.35)`) — gives the chart a point of view, not just data.
39. **Stats grids beat stat rows.** If you have 4+ data points, render them as a 2×2 or 3×2 card grid with icon + hero number + label + context line. A single-column list of thin 60px rows reads as a spreadsheet, not a pitch slide.
40. **Every stat needs a context line** (12–14px, low opacity) explaining why it matters — "Push-reachable in a single click" beats a bare "3M+ App Downloads".

---

## Content Improvement Rules

When the user provides raw content, ALWAYS apply these improvements:

### Data Presentation
- Round numbers for impact: "19,847,233" → "20M+" on the slide (exact number in speaker notes)
- Add context to every stat: "+26% YoY" or "3x industry average"
- Use the hero stat pattern for impressive numbers — big number, small label
- If showing money, always specify currency (AED, USD)

### Narrative Flow
- Open with the problem or opportunity, not with "About Us"
- Place the most impressive stat within the first 3 slides
- Build credibility before making the ask
- If the audience is skeptical, lead with proof; if curious, lead with vision
- End every section with a bridge to the next (implicit or explicit)

### Language
- Use active voice: "We drove 22x ROAS" not "22x ROAS was achieved"
- Headlines should provoke: "Your Audience Is Already Here" not "Audience Overview"
- Remove filler words: "very", "really", "basically", "actually"
- Match the Platinumlist B2B voice: confident, data-backed, direct but not aggressive

### When to Research
- If the user mentions a metric without context → research the industry benchmark
- If the user references a competitor → look up their public ad presence
- If the user makes a market claim → verify with a quick web search
- If data seems outdated → flag it and suggest refreshing
