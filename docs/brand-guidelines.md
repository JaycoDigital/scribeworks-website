# Scribeworks Brand Guidelines — developer summary

Condensed from the Scribeworks Brand Guidelines v1.0 (Claude Design project,
"Scribeworks Brand Guidelines.dc.html"). Tokens live in `src/styles/global.css`.

## Colour

| Name        | Hex       | Role                                              |
|-------------|-----------|---------------------------------------------------|
| Graphite    | `#303030` | Ink / primary text / primary buttons              |
| Scribe Sand | `#C4B67D` | Accent — surfaces and highlights only, never text |
| Deep Sand   | `#8A7C43` | Accessible gold for text and links                |
| Site Slate  | `#42606E` | Support colour; only non-graphite that may carry white text |
| Chalk       | `#FAF9F6` | Page background                                   |
| Line        | `#E4E1D7` | Rules / borders                                   |
| Muted       | `#4A4A4A` | Secondary text                                    |

Balance: ~60% neutral, 20% graphite, 15% slate, 5% sand. Gold is a highlight, never a wash.

- Neutral steps: `#FAF9F6 · #EFEDE4 · #E4E1D7 · #9A9890 · #4A4A4A · #303030`
- Sand tints: `#F7F4E9 · #EDE7CF · #DCD1A6 · #C4B67D · #A99C63 · #8A7C43`
- Slate tints: `#EAF0F2 · #CBDBE1 · #8FAAB5 · #42606E · #35505C · #263C46`
- Functional: Success `#3F7D58`, Error `#B4463C`, Warning `#C08A2E`

Contrast: Sand on Chalk fails (1.9:1) — use Deep Sand for gold text.

## Typography

Logo is Glacial Indifference (never retype). Everywhere else: **Poppins** (display) and **Figtree** (text/UI). Google Fonts.

| Style | Font | Size / line | Tracking |
|-------|------|-------------|----------|
| H1 | Poppins 700 | 56/56 | -3% |
| H2 | Poppins 700 | 38/42 | -2.5% |
| H3 | Poppins 700 | 24/29 | -2% |
| Body | Figtree 400 | 17/29 | — |
| Small | Figtree 400 | 14/22 | — |
| Label / nav | Poppins 400 | 13px | +22%, uppercase |
| Button | Poppins 600 | 13px | +14%, uppercase |

Rules: never body copy in Poppins; uppercase only for labels/nav/buttons; one gold accent per block; left-align (centred paragraphs read as a flyer). Measures 45–70 characters.

## Logo

- Primary (dark) on white/light neutral; Reversed (light) on graphite, photography or dark ground. No mono variants.
- Clear space = cap-height of the "S" on all sides.
- Minimum 180px digital / 45mm print — below that, drop the strapline rather than shrink.
- Never stretch, rotate, recolour, or add effects.

## UI kit

- 8px spacing grid, square corners (`--radius: 0`), one shadow `0 2px 8px rgba(48,48,48,0.07)`, one transition `160ms ease-out`.
- Buttons: Primary = Graphite (one per screen), Accent = Sand, Support = Slate, Outline, Text link (always Deep Sand). Arrow only on quote/booking buttons; lifts up-right on hover.
- Text links: Deep Sand, hover → Graphite.
- Project cards: full-bleed photo with graphite scrim fading from the text edge.
- Icons: 1.5px stroke line icons on 48px grid, graphite (sand only as card hero). Lucide at 1.75px acceptable.
- Background grid (optional): 48px minor / 240px major lines in slate at low opacity, faded at edges.

## Voice

Straight-talking, craft-proud, unfussy, reassuring. Say the price, timescale and what's included. Short sentences, everyday words.
