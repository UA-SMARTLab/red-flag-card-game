# Red Flag: design notes

## 1. Starting point

Researchers learn the classic reasoning errors (confounding, Simpson's paradox, regression to the mean, forking
paths) once, in a methods course, and then meet them for real in headlines, abstracts and slides, where they are
harder to spot. Red Flag trains the second skill: reading a short claim and naming what, if anything, is wrong with
it. It is the second game of the SMART-Lab Science Game Kit, after Methodical (which trains choosing a method), and
shares its card frame, app and conventions.

## 2. What a player should learn

1. To separate what a study **shows** from what a claim **says**: most flaws are a gap between evidence and conclusion.
2. To name the gap precisely, with the field's own term (one term per concept across cards, app and rules).
3. To know the move that would expose it (the Check), since naming a flaw is less useful than knowing how to test it.
4. To stay **calibrated**: sound research exists, and a reader who flags everything is as useless as one who flags
   nothing.

## 3. Existing games (surveyed 2026-10-31)

We looked for card games and online games that teach fallacies, critical thinking, statistical reasoning or
misinformation spotting, to avoid reinventing one and to avoid copying any. Descriptions are ours; nothing was copied.

| Game | Maker, year | Format | What it does | How Red Flag differs |
|---|---|---|---|---|
| [Cranky Uncle](https://crankyuncle.com/game/) ([paper](https://research.monash.edu/en/publications/the-cranky-uncle-gamecombining-humor-and-gamification-to-build-st/)) | John Cook, 2020 | App | A cartoon denier teaches about 14 denial techniques; players spot them in his arguments. | Denial rhetoric, not statistical flaws in research claims; solo |
| [Bad News](https://www.getbadnews.com/) ([lab page](https://www.sdmlab.psychol.cam.ac.uk/research/bad-news-game)) | Roozenbeek & van der Linden with DROG, 2018 | Browser | Players act as fake-news producers and learn manipulation tactics, which inoculates them. | Players create disinformation; social-media tactics, not study design |
| [Go Viral!](https://www.cam.ac.uk/stories/goviral) | Cambridge SDM Lab, DROG, UK Cabinet Office, 2020 | Browser | A short COVID-19 version of Bad News that prebunks pandemic conspiracy tactics. | Same producer-role inoculation |
| [Harmony Square](https://harmonysquare.game/) | Roozenbeek & van der Linden with DROG, 2020 | Browser | Players stir up political conflict in a fictional town to learn manipulation tactics. | Political disinformation; narrative |
| [Fallacymania](https://www.thegamecrafter.com/games/fallacymania-eng-) ([description](https://www.lesswrong.com/lw/nsa/fallacymania_party_game_where_you_notice)) | Moscow LessWrong community, about 2016 | Print-and-play | One side argues with fallacies from its cards; the other races to name them. | Everyday verbal fallacies; no sound arguments, no statistics |
| [Debunked](https://eu.nobleknight.com/P/2148026513/Debunked) | Stephen Woodford, 2020 | Card game | Fallacy and counter cards are played against argument cards, with blocking. | Argument fallacies with combat mechanics; no data or charts |
| [Critical Thinking Cards](https://yourlogicalfallacyis.com) ([biases](https://yourbias.is/)) | The School of Thought, 2010s | Reference deck | Fallacy and bias cards with a few suggested mini-games. | Reference cards, not a claim-judging game |
| [The Fallacy Detective](https://www.exodusbooks.com/fallacy-detective/bluedorn/27977/) | N. & H. Bluedorn, 2002 | Book with a game | Lessons on everyday fallacies; the appendix game has players invent examples. | Textbook on verbal argument |
| [Rationality Cardinality](https://www.greaterwrong.com/posts/Yydnu4irMXtYxJpP7/rationality-cardinality) | LessWrong community, 2015 | Party cards and web | A judge picks the funniest answer card; captions explain bias concepts. | Humour-judged, no right answers |
| [Homo Rationalis](https://www.lesswrong.com/posts/FxceJeR88j5NAn7Q3/i-made-a-card-game-to-reduce-cognitive-biases-and-logical) | Brad Dunn, 2025 | Card game | Players secretly act out biases in staged debates and score by spotting each other's. | Role-play of biases, not evaluating evidence |
| [Guess the Correlation](https://www.guessthecorrelation.com/) | Omar Wagih, 2016 | Browser | Estimate Pearson's r from scatter plots. | One statistical intuition; no reasoning errors |
| [Factitious](https://teachingcivics.org/lesson/factitious/) | American University Game Lab, 2017 | Browser | Swipe short articles as real or fake. | Binary real/fake; the error is never named |
| [Publish or Perish](https://www.the-scientist.com/publish-or-perish-the-board-game-of-academic-survival-73133) | Max Hui Bai, 2024 | Party cards | A satirical race to publish in which some cards let players p-hack or sabotage. | Questionable practices as mechanics, not things to detect |
| [p-hacking: the board game](https://srcole.github.io/2020/12/30/p-hacking-game) | Scott Cole, 2020 | Board game | Rivals process a shared dataset until their theory wins. | Satire of analysis flexibility |

**What is new in Red Flag.** (a) The material is research claims (headlines, abstract sentences, small charts), and
the errors are statistical and study-design errors rather than verbal fallacies. (b) A quarter of the claims are
sound and over-flagging costs points, so the game trains discrimination rather than blanket suspicion; the inoculation
literature raises the same concern about games that teach only scepticism. (c) Each Flag pairs with the Check that
exposes it, and each Flag carries a real, sourced case. We found no game that combines these.

## 4. Design choices

### 4.1 Calibration is the engine
- **Sound claims, one in four** (15 of 60). Fewer and players learn that "flag" is always right; many more and the
  game stops being about errors.
- **Symmetric penalty**: flagging a sound claim and calling a flawed one sound both score −2, the same as a listed
  trap. The expected score of "always flag" or "always sound" is negative.
- **The Sound card is always one of the four choices** in the app, so its presence never hints at the answer. On a
  sound claim the other three are the flags the key lists as tempting traps.
- **Sound claims are written like flawed ones**: they also end with a conclusion, modest and justified, so the form
  of the sentence doesn't give them away (a point raised in the independent review, §6).

### 4.2 Three-tier key, as in Methodical
Each claim lists the best flag, defensible flags (+1) and traps that look right but fail, each with a one-line reason.
Two claims have two equally good best answers (C17: Simpson's paradox or confounding by case mix; C33: a cropped chart
or a causal claim without comparison). Unlisted flags score 0 and can be appealed at the table.

### 4.3 Thirty Flags in four families
Cause (6), Sample (7), Numbers (9) and Practice (8). Families sort the deck for the table grid and help players
narrow down; all Flags share one red card colour so the family is a badge, not the whole card. The list covers the
errors named in the brief (correlation as causation, ecological fallacy, Simpson's paradox, regression to the mean,
survivorship bias, base-rate neglect, forking paths, "not significant" read as "no effect", relative risk without
absolute risk, extrapolation) plus confounding, reverse causation, shared trends, collider bias, immortal time,
model-to-human leaps, unrepresentative and narrow samples, small-number swings, transposed conditionals, trivial
effects, distorted charts, overfitting, multiple tests, subgroups, the file drawer, single studies, surrogate
endpoints, lead time and overdiagnosis, and changed definitions. A Texas-sharpshooter card was left out because it
overlaps "Many tests, one hit" and "Small numbers, wild swings".

### 4.4 Checks
Sixteen moves ("Ask for the denominator", "Split by subgroup", "Find the preregistration", "Plot it over time"...).
Each Flag lists the Checks that expose it; a Check's list of Flags is derived from that (one source of truth). Each
claim names its key check; in the app the bonus question accepts the key check or any check listed on the best flag.
Checks have no key reference of their own: they are moves, and the Flag they expose carries the reference.

### 4.5 Claims are constructed; cases are real
Claim cards are teaching examples written for the game, so that each isolates one error and none misrepresents a
real study. Some echo famous cases (chocolate and Nobel prizes, kidney stones, the HDL drug) without naming or
quoting them. Every **real** case is on a Flag card, with a source link, and was checked (§6). The footer of the app
says so.

### 4.6 Pictures
Claim pictures are drawn from the numbers in the claim (bar, line, scatter, interval, forest, funnel, headline and
abstract templates), so a new claim needs no new art and the picture always matches the text. A cut axis is drawn the
way it appears in the wild (C28, C32, C33) because the chart is part of the claim. Flag and Check pictures are
diagrams of the idea, drawn by us. On the red Flag cards the kit's rose "error" colour disappears, so it is pale pink.

### 4.7 Look and app
Same frame, fonts, sizes, fit-to-box rule and app behaviour as Methodical (see its CLAUDE.md). Red Flag's own:
accent #B42318, Flags #B42318, Checks #0C4A6E, Sound #047857, neutral Claims #40402C, card back with a red flag,
"FLAWED OR SOUND?" and the kit mark "SMART-Lab Science Game Kit". The app has Home, Play and Browse the decks.

## 5. Card data and tooling
- `data/*.json` holds every card; `tools/build.py` validates (unknown ids, overlapping tiers, a sound claim with
  defensible flags, missing https sources, flags never used as a best answer, the share of sound claims) and
  generates the app, the print sheets, the answer-key booklet and `ANSWER_KEY.md`.
- `tools/check_cards.py` renders the print sheets in headless Chrome at print size; `fitCards` marks any card whose
  text box still overflows after shrinking to 72%, or whose name doesn't fit its bar. The check was tested on a copy
  with a deliberately over-long text and name, and caught both.
- `tools/test_app.py` plays all 60 claims through the real interface (tap a card, green button, bonus check) and
  compares the app's scoring with the build's rule; a deliberately broken scoring rule made it fail.
- `tools/check_refs.py` checks every Flag reference and example link against Crossref.

## 6. Sources and verification
- **Key references**: one per Flag, the paper that defines or best explains the error (listed in `ANSWER_KEY.md` and
  on each card's "?"). All 30 DOIs resolve, and their first author and year match the citation (`check_refs.py`,
  2026-10-31). Barnett et al. on regression to the mean is cited as 2004, Crossref's issued date; its printed issue
  is IJE 34(1), 2005.
- **Real cases**: each checked against the primary paper or a reputable secondary source, with the link on the card.
  Corrections made during the check: Robinson (1950) reported illiteracy (−0.53 across states), so the example uses
  his framing; at Berkeley, department-level data showed little bias, not women admitted more often everywhere; the
  famous "armour where there are no holes" story about Wald is a simplification, so the card describes his method;
  CAST deaths are 63 vs 26 (all deaths); the 13,000 extra abortions after the 1995 pill scare come from Gigerenzer
  (2009), Bulletin of the WHO, not Furedi's abstract; the 2015 House chart's flaw was two unlabelled scales; the Sally
  Clark example follows the Royal Statistical Society's 2002 letter, which names the press reports as the
  Prosecutor's Fallacy; in Casscells et al. (1978) 95% was the commonest answer (27 of 60), not "most".
- **Independent review**: a separate reviewer pass read all claims, flags and checks as a methodologist would. It
  found arithmetic slips (C28 could not have been significant with 2 million users; C08's chart showed 52% not 30%;
  C46's interval was too narrow; C50's "too small to matter" lacked a stated threshold), traps that were really
  defensible, and missing defensible answers. All were fixed before the first release.

## 7. Balance
Every Flag is the best answer to at least one claim (17 are best twice, counting the two claims with two best
answers). Difficulty: ★ 14, ★★ 34, ★★★ 12; the sound claims spread ★ 2, ★★ 9, ★★★ 4 (see
`ANSWER_KEY.md`). Each claim's key check is listed on its best flag.

## 8. Open questions and next steps
1. **Play-test** at the table: is the race in Mode 1 too fast for ★★★ claims? A short reading pause may be needed.
2. **Translations** (fr, nl, de, ar) with the kit's glossary and review process; the i18n structure is ready, and
   claim picture labels are translatable per claim.
3. **More claims** for the Flags that are best only once, and claims from engineering and LCA (the lab's own field).
4. **Decide publication**: GitHub repo under UA-SMARTLab (private first), and a hosted copy like Methodical's.
5. Consider a key reference for each Check (for example the CONSORT or PRISMA item behind "Find the preregistration").
