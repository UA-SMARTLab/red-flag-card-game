# Red Flag: working notes for Claude

Red Flag is the second game of the **SMART-Lab Science Game Kit**. The kit conventions (architecture, card look, app,
content rules, licence) are defined once, in Methodical's `CLAUDE.md`
(`C:\Users\A-Bag\Desktop\methodical-card-game\CLAUDE.md`, section "The kit: what every game shares"). Follow them;
this file adds only what is specific to Red Flag. General rules: `~/.claude/CLAUDE.md`.

## The game
- A Claim card (headline, abstract sentence or small chart) is flipped; players play the Flag that names its reasoning
  error, or the Sound card. About one claim in four is sound, and false alarms cost as much as missed flaws, so the
  game rewards calibrated scepticism. Advanced players add the Check card that would expose their Flag (+1).
- Decks (`data/`): `claims.json` (60, ids C01–C60; 15 sound), `flags.json` (30, four families: cause, sample,
  numbers, practice), `checks.json` (16), `meta.json` (families, scoring). The Sound card has the reserved answer id
  `sound`; Check → flags it exposes is derived from `flags[].checks` (single source).
- Scoring rule, in `tools/build.py` (`tier_of`) and mirrored in the app (`tierOf`): best +3, defensible +1, trap −2,
  unlisted 0. On a sound claim every flag is a trap; on a flawed claim, "sound" is a trap. `tools/test_app.py`
  checks the app against the build's rule for every claim.
- Claim pictures are drawn from numbers in each claim (`picture`: bars, line, scatter, headline, abstract, ci, grid,
  forest, funnel) by `tools/art_claims.py`; Flag and Check pictures are bespoke (`art_flags.py`, `art_checks.py`).
- Claim cards are constructed teaching examples. Real cases live only on Flag cards (`example` + `example_url`), each
  verified; never present an invented case as real.

## Colours
Claims #40402C (the kit's neutral prompt colour), Flags #B42318, Checks #0C4A6E, Sound #047857, back #0F172A with the
red flag and the kit mark. App accent #B42318 (dark theme #FF8A7A).

## Commands
- `python tools/build.py`: validate and generate everything (app, print sheets, answer keys).
- `python tools/check_cards.py`: no card overflows at print size (headless Chrome or Edge).
- `python tools/test_app.py [--shots <folder>]`: play every claim through the app; screenshots at 1280, 390 and 320 px,
  light and dark.
- `python tools/check_refs.py`: every Flag's reference and example link against Crossref (online).
- Local server: `.claude/launch.json` serves `app/` on 127.0.0.1:8792.

## Status
- English only so far; the i18n structure is in place (`i18n/`), add fr/nl/de/ar as in Methodical.
- Local repository only: no GitHub repo yet, nothing published. Open items: `NIGHT-LOG.md` and `DESIGN.md` §8.
