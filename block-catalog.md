# Platinumlist Presentation Block Catalog

This is the **menu** the deck builder reads before composing. Building a deck =
choosing a sequence of these blocks and pouring content into their slots — NOT
drawing slides from scratch. Each block lives in `blocks/<id>/template.html`
with a header comment documenting its slots, compatible themes, and density.

All blocks consume `tokens.css` + `lib/deck-base.css`. To re-theme a block, set
the `.theme-*` class on its `.slide`. Kickers are optional everywhere — add
`no-kicker` to the `.slide` class to suppress them.

## How to read this table

- **Slots** = the content you fill in. Everything else is fixed layout.
- **Themes** = which background families the block is designed for.
- **Ref** = the slide(s) in the approved UAE Events deck this was extracted from.

| ID | Purpose | Slots | Themes | Ref |
|----|---------|-------|--------|-----|
| `cover-hero` | Opening slide | kicker-pills, headline, descender, subtitle, tag-pills, hero-graphic | haze, monday, sabbath | 1 |
| `section-divider` | Section break | section-title, one-line intro | deep/haze, sabbath | 19, 22 |
| `stat-grid` | Numbers showcase (3×2 / 2×2) | eyebrow, headline, sub-label, N×{label, num, delta, ctx} | monday, day | 2 |
| `segment-row` | 3–4 parallel segments | kicker, headline, lead, N×{title, desc} | monday, day | 3 |
| `hero-stat-row` | 1 dominant stat + supporting deltas | kicker, headline, lead, hero{label,num,ctx}, N×{label,num}, foot | day, monday | 4, 9 |
| `methodology-windows` | Define comparison windows | kicker, headline, lead, N×{name, dates, descriptor}, side-notes | sabbath, haze | 5 |
| `timeline-table` | Dated sequence of events | kicker, headline, lead, rows{date,event,impact}, hi-row, foot | sabbath, haze | 6 |
| `layer-columns` | 2–3 concepts side by side | kicker, headline, lead, N×{tag, title, body} | haze, sabbath | 7 |
| `data-table` | Comparison table, one row hero | kicker, headline, lead, header-cols, rows, hi-row+NEW tag, foot | haze, sabbath | 8 |
| `heatmap-matrix` | 2-axis colour-graded matrix (likelihood × impact, etc.) | kicker, headline, lead, col-heads, cells (hm-0..hm-4), legend | sabbath, haze | bespoke |
| `bar-compare` | 4-window bar chart | kicker, headline, lead, bars{label,value}, callouts | sabbath, haze | 10 |
| `quality-stats` | 3–4 stat cards w/ delta | kicker, headline, lead, N×{label,num,delta,ctx} | day, monday | 11, 16 |
| `funnel-table` | Metric × multi-column deltas | kicker, headline, lead, metrics rows, foot | haze, sabbath | 12, 17 |
| `split-audience` | Narrative + stacked stats | kicker, headline, lead, left-blocks, right{num,label,ctx}, foot | day, monday | 13 |
| `rank-list` | Two-column ranked deltas | kicker, headline, lead, colA-head, colB-head, rows | haze, sabbath | 14, 15 |
| `summary-numbered` | 4 numbered takeaways | kicker, headline, N×{no, title, body, tag} | monday, day | 18 |
| `case-study` | Proof w/ metrics + note | kicker, title, lead, N×{label,num,ctx}, foot | day, sabbath | 20 |
| `channels-table` | Channel performance grid | kicker, headline, lead, rows{channel,what,delta1,delta2,signal}, foot | sabbath, haze | 21 |
| `service-checklist` | How-it-works + side stats | kicker, title, lead, checklist[], M×{num,label,ctx} | day, monday | 24 |
| `service-pillars` | 4 numbered pillar cards | kicker, title, lead, 4×{no,title,desc}, foot | monday, day | 26 |
| `service-statpair` | 2 hero deltas + editorial list | kicker, title, lead, 2×{num,label,ctx}, list-title, list[] | day, monday | 27,28,29 |
| `process-steps` | How-it-works / steps-to-start (intro panel + numbered stepper) | kicker, headline+accentWord, lead, conf, 3–5×{num,title,desc}, cta | sabbath, haze | new |
| `cta-nextsteps` | Closing CTA | headline, lead, 4×{num,label}, contact, wordmark | haze, sabbath | 30 |
| `closing` | Thank-you | headline, optional wordmark | haze, sabbath | 31 |

## Batch 2 — added from the 2nd reference set

These were extracted from a second pack of approved Platinumlist slides. They cover
manifesto statements, milestones, charts, diagrams, photo segments, plan compares and
case stacks. Colours can change — every block re-themes from its `.theme-*` class.

| ID | Purpose | Slots | Themes | Ref |
|----|---------|-------|--------|-----|
| `statement-bold` | Giant manifesto line, bottom-left, optional inline icon glyphs | kicker, headline (+`.accent`, +`.glyph`) | haze, day, sabbath, monday | b2 |
| `milestone-stats` | Headline (accent phrase) + row of 3–4 big stat cards | kicker, headline, 3–4×{num, label, ctx} | haze, sabbath, monday | b2 |
| `bar-chart` | Tall categorical bar chart (pure CSS, many categories) | kicker, headline, 6–14×{label, value, heightPct, dim} | sabbath, haze | b2 |
| `bg-statement` | Full-bleed bg image + headline + 1–2 paragraphs | kicker, headline, 1–2 paras, image | haze, sabbath | b2 |
| `feature-cards` | Dominant headline + lead + 3–4 titled cards on the bottom edge | headline, lead, 3–4×{title, desc} | sabbath, haze | b2 |
| `segment-photos` | 3–4 photo segment cards w/ label + stat + desc overlaid | headline, 3–4×{image, title, num, desc} | sabbath, haze | b2 |
| `two-up-cards` | Two big statement cards (Brief/Objective, Problem/Solution) | 2×{title, desc} | sabbath, haze, monday | b2 |
| `numbered-cards` | 3–5 numbered principle/phase cards in a row | kicker, headline, lead, 3–5×{no, title?, desc} | sabbath, haze | b2 |
| `strategy-columns` | Funnel matrix — header pill · desc box · tactic chips · base bar | kicker, headline, 3–5×{head, desc, items[]}, bar | sabbath, haze | b2 |
| `converge-diagram` | Two source nodes → one dominant centre, dashed arrows in | headline, center, 2×{side} | sabbath, haze | b2 |
| `venn-diagram` | Two overlapping circles + filled lens + bracket captions | headline, left{title,desc}, right{title,desc}, center, top, bottom | sabbath, haze | b2 |
| `package-compare` | Two plans side by side (outline vs filled = recommended) | 2×{title, head, lines[], foot, recommended}, note | sabbath, haze | b2 |
| `case-stack` | Case study — left title + right stacked metric cards | kicker, title, note, 2×{icon, head, ctx} top, 2–4×{head, lines[]} | haze, sabbath | b2 |
| `closing-graphic` | Closing "let's talk" — headline left + graphic/icon right | headline, graphic, logo | haze, monday, sabbath | b2 |

## Theme rotation guidance

The reference deck groups themes rather than alternating randomly:
- **Cover / section dividers / CTA** → `theme-haze` (purple statement) or `theme-sabbath`.
- **Stat / segment / service-card slides** → `theme-monday` (cyan) or `theme-day` (lime), purple cards.
- **Data-heavy tables & charts** → `theme-sabbath` (near-black) or `theme-haze`.
- Use **one** `theme-day` accent moment sparingly (the punchline slide).

## Adding a new block (growth model)

1. Create `blocks/<new-id>/template.html` with the standard header comment.
2. Style it using existing classes in `lib/deck-base.css`. Only add new CSS to
   `deck-base.css` if no existing class fits — and make it token-based.
3. Add one row to the table above.
4. Render `scripts/build-gallery.sh` to eyeball it, then commit.

This keeps the library expanding deck-over-deck without rewriting the engine.
