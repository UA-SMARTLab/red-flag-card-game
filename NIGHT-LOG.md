# Night log: Red Flag, 2026-10-31

Built overnight by Claude (a sub-agent of the session that also had Major Revisions built in parallel), with the
user's go-ahead to proceed as fits. Repository kept local: no GitHub repo, no push, nothing public. Methodical's
files and the Major Revisions folder were not touched.

## Done
- **Scaffold** copied from Methodical and adapted: `tools/` (build, cards, art kit, i18n), `app/template.html`,
  launchers for Windows, Mac and Ubuntu, `.claude/launch.json` (127.0.0.1:8792), the i18n structure (English only).
  Same card frame, fonts, fit-to-box rule and app behaviour; Red Flag's own accent (#B42318), card colours and back
  with the kit mark "SMART-Lab Science Game Kit".
- **Cards** (`data/`): 60 Claims (15 sound), 30 Flags in four families, 16 Checks, the Sound card, 3 reference cards:
  115 printable cards. Claim pictures are drawn from each claim's numbers; Flag and Check pictures are our own
  diagrams.
- **App**: Home (fan of cards, live counts, a quick claim), Play (claim card, four whole cards with the Sound card
  always among them, tap-to-enlarge viewer with the green "Pick this card" button, the cards react, three-tier key,
  real case with source, key reference, bonus Check question), Browse the decks (with search and deck pop-ups).
- **Docs**: README, RULES (three table modes and solo), DESIGN (survey of 14 existing games with links, design
  choices, sources and verification, open questions), CLAUDE.md (game specifics, points to Methodical's kit rules),
  LICENSE.md (CC BY-NC-SA 4.0 content, PolyForm Noncommercial 1.0.0 code).
- **Tools added** beyond Methodical's: `check_refs.py` (Crossref), `check_cards.py` (overflow at print size, headless
  Chrome), `test_app.py` (plays every claim through the app; screenshots).

## Checked
- **References and examples**: all 30 key references resolve on Crossref with matching first author and year; all 30
  example links answer (`python tools/check_refs.py`: 0 problems in 60 links). Every real case was also checked
  against its source by a separate fact-check pass; 9 needed corrections, all applied (DESIGN.md §6).
- **Content review**: an independent methodologist pass read every claim, flag and check. About 25 fixes applied:
  arithmetic (C28, C08, C46, C50, C21, C59, C23), traps that were really defensible, missing defensible answers,
  explicit conclusions on flawed claims and justified ones on sound claims, tighter flag texts.
- **No card overflows**: `python tools/check_cards.py` gives 115 of 115 fitting at print size. The checker was tested
  on a copy with a deliberately over-long text and an over-long name; it caught both.
- **App**: `python tools/test_app.py` played all 60 claims through the real interface (tap, viewer, green button,
  bonus check): scoring matches the build's rule for every claim, the Sound card and the best answer are always among
  the four choices, no repeats, Escape closes the viewer, the decks show 60/30/16/1 cards, no card overflows in the
  app, no page errors. A deliberately broken scoring rule made the test fail, as it should.
- **Look**: screenshots in headless Chrome at 1280, 390 and 320 px wide, light and dark, for Home, the viewer, a
  result and the decks; print sheets checked page by page. Fixed on the way: pictures in a card that also sat in the
  hidden home fan lost their background (duplicate SVG ids), the error colour vanished on red Flag cards, bar labels
  dropped decimals, a headline overflowed.
- `app/` served on 127.0.0.1:8792 answered 200; the server was stopped afterwards. No other server was started.

## Open
1. **Play-test at a table** (Mode 1 pace, whether ★★★ claims need a reading pause). Not done: needs people.
2. **Translations** fr/nl/de/ar: not started. The English is complete and checked, but a translation with the
   kit's glossary and an independent review pass per language is a night of its own; better done next with care.
3. **Keyboard and screen reader** were checked only partly (Escape, native buttons, visible focus styles); a manual
   pass with a screen reader is still open.
4. **Publication**: no GitHub repo created, by agreement. When wanted: a private repo under UA-SMARTLab, then decide
   on Pages or a hosted artifact like Methodical's.
5. Barnett et al. (regression to the mean) is cited as 2004 (Crossref's issued date); the printed issue is 2005.
   Either is defensible; change both the card and `check_refs.py` expectations if the print year is preferred.
6. Checks have no key reference of their own (DESIGN.md §4.4); worth deciding whether the kit wants one.
