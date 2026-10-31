# Red Flag

**Spot the reasoning error in a research claim, or call it sound.**

A card game for researchers, part of the **SMART-Lab Science Game Kit** (SMART-Lab, Universiteit Antwerpen). A Claim
card shows a headline, an abstract sentence or a small chart. Players play the Flag that names its reasoning error
(correlation as causation, Simpson's paradox, base-rate neglect, forking paths and 26 more) or the Sound card. About
one claim in four is sound, and a false alarm costs as much as a missed flaw: the game rewards calibrated scepticism,
not cynicism.

## What's in the box

| | |
|---|---|
| 60 Claim cards | constructed teaching examples, 15 of them sound, three difficulty levels |
| 30 Flag cards | reasoning errors in four families (Cause, Sample, Numbers, Practice), each with a real, sourced historical case and the paper that defines it |
| 16 Check cards | the move that exposes a flag: "Ask for the denominator", "Split by subgroup", "Find the preregistration"... |
| 6 Sound cards, 3 reference cards | one Sound card per player |
| Answer key | three tiers per claim (best, defensible, traps with reasons), in `print/answer-key.html` and `ANSWER_KEY.md` |
| Web app | Home, Play and Browse the decks, in `app/` |

## Start here

- **Play on screen:** double-click `play-windows.bat` (Windows), `play-mac.command` (Mac) or run `play-ubuntu.sh`
  (Ubuntu). Or open `app/index.html` in a browser. Everything works offline except the web fonts.
- **Print a deck:** open `print/cards.html` in Chrome and print at 100% on A4 with background graphics on; 115 cards in
  poker size, 9 per page. `print/backs.html` has the card back. Keep `print/answer-key.html` apart.
- **Rules:** [`RULES.md`](RULES.md): the Flag grid race, a calibrated class vote, a Check drill, and solo play.

## How it works in one paragraph

Flip a Claim. Read what the evidence shows, then what the claim says. If there is a gap, name it with a Flag; if
not, play Sound. Best +3, defensible +1, trap −2, unlisted 0 (appeal for +1); any flag on a sound claim and Sound on
a flawed claim are traps. Advanced players add the Check that would expose their flag for +1. The key explains each
call, and every Flag links to a real case and its source.

## Editing the cards

All card text lives in `data/` (`claims.json`, `flags.json`, `checks.json`, `meta.json`). After editing, run:

```
python tools/build.py          # validate, then regenerate app, print sheets and answer keys
python tools/check_cards.py    # no card overflows at print size (needs Chrome or Edge)
python tools/test_app.py       # play every claim through the app and check the scoring
python tools/check_refs.py     # every reference and example link against Crossref (online)
```

Generated files (`app/index.html`, `print/`, `ANSWER_KEY.md`, `i18n/en/cards.json`) are never edited by hand. Only
the Python standard library is needed. Design choices and sources are in [`DESIGN.md`](DESIGN.md).

## Languages

English is the source. The kit's translation system is in place (`i18n/`, as in Methodical): add a language to
`i18n/languages.json`, copy `i18n/en/ui.json` and `i18n/en/cards.json` to `i18n/<code>/`, translate the values and
rebuild. Anything missing falls back to English. French, Dutch, German and Arabic are planned.

## Status

Version 0.1, a checked English prototype (2026-10-31). Local repository only; not yet published. See
[`NIGHT-LOG.md`](NIGHT-LOG.md) for what was done and checked, and `DESIGN.md` §8 for next steps.

## Licence

Card content, art, rules and print sheets: CC BY-NC-SA 4.0. Software: PolyForm Noncommercial 1.0.0. Copyright ©
2026 Abdulhamid Baghdadi; developed at SMART-Lab, Universiteit Antwerpen. Commercial use only with written
permission. See [`LICENSE.md`](LICENSE.md).
