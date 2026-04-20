# pl-deck — Platinumlist Presentation Builder

A Claude Code skill that generates branded Platinumlist HTML presentations (16:9) from raw content, findings, or topic descriptions — then exports to true 1920×1080 PDF on request.

- **Two visual themes** (purple/cyan for selling, dark/green for proving with data)
- **Card-based layouts** — no bullet walls, no text-heavy slides
- **Phosphor icons** (~1,500 bold SVGs) with auto color recoloring
- **Chart.js** for data visualization with custom inline labels
- **MD Nichrome Bold + Inter** — brand typography enforced
- **40+ hard quality gates** — blocks empty-middle cards, button-styled CTAs, tiny text, and other deck failures
- **Two-phase workflow** — HTML first, PDF only when you're done editing

---

## Install

Clone into the standard Claude Code skills folder:

```bash
git clone https://github.com/YOUR-USERNAME/pl-deck.git ~/.claude/skills/pl-deck
```

That's it. Next time you open Claude Code, `/pl-deck` is available.

### Dependencies (only needed for PDF export)

- **Node.js 18+** (for Puppeteer)
- **Python 3** with `Pillow` and `PyMuPDF` (for preview rendering, optional)

Puppeteer auto-installs to `/tmp/node_modules` the first time you export a PDF.

---

## Usage

### Interactive intake

```
/pl-deck
```

Claude asks you clarifying questions in one batch (deck type, audience, key message, data, slide count, CTA), proposes a structure, waits for your approval, then builds the HTML.

### Direct invocation

```
/pl-deck campaign report for [event name]
/pl-deck marketing pitch for new clients
/pl-deck platform overview for sponsors
```

### Workflow

1. **Build HTML** — Claude generates `[deck-name]-deck.html` in your current working directory
2. **Review in browser** — open the HTML file, use arrow keys to navigate
3. **Iterate** — ask for edits ("swap slide 5 and 6", "tighten the copy on slide 10")
4. **Export PDF when done** — say "export to PDF" / "now make the PDF" / "finalize as PDF"

PDF export is **deliberately deferred** — it's a sign-off artifact, not a working draft. Don't expect a PDF on the first build.

---

## What's in this repo

```
pl-deck/
├── SKILL.md                    # 33 KB of rules + workflow (the brain)
├── README.md                   # this file
├── .gitignore
└── assets/
    ├── MDNichrome-Bold (3).otf          # headline font (base64-embedded at build time)
    ├── Pl Logos/                        # all Platinumlist logo variants (SVG/PNG/JPG)
    │   ├── icon/{blue,purple,white,black}/
    │   ├── latin/{horizontal,vertical}/{svg,png,jpg}/
    │   └── arabic/{horizontal,vertical}/{svg,png,jpg}/
    └── phosphor-icons/
        ├── LICENSE                      # Phosphor icons MIT license
        └── SVGs/bold/                   # 1,512 bold SVG icons
```

Total size: ~7 MB.

---

## Updating

```bash
cd ~/.claude/skills/pl-deck
git pull
```

Claude Code re-reads `SKILL.md` every time it's invoked — no restart needed.

---

## Design system quick reference

| Token | Purple/Cyan theme | Dark/Green theme |
|-------|-------------------|------------------|
| Background | `#1a0533` | `#1a1a2e` |
| Primary accent | `#79E2FF` (cyan) | `#B8FF00` (lime) |
| Secondary accent | `#7B2FF2` (purple) | `#79E2FF` (cyan) |
| Card background | `#79E2FF` | `#B8FF00` |

Fonts: **MD Nichrome Bold** (headlines) + **Inter** (everything else).
Minimum font size: 14px. Body minimum: 18px.

See `SKILL.md` for the full type scale, 40+ quality gates, and slide layout patterns.

---

## Credits

- **Phosphor Icons** — MIT-licensed icon set by Phosphor Bros
- **Inter** — SIL Open Font License, Rasmus Andersson
- **MD Nichrome** — Mass-Driver, used under Platinumlist license
- **Chart.js** — MIT
- Skill authored by the Platinumlist team
