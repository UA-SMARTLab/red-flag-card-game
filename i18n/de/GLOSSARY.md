# Red Flag: German terminology (Glossar)

Why the German card text uses the terms it does. Written for a native methodologist who wants to check or overrule a
choice. Translated 31 October 2026 from the English source in `i18n/en/`, then checked by an independent reviewer pass
(see "Review" below); Methodical's
`i18n/de/GLOSSARY.md` is the kit's terminology source, and every term the two games share is spelled the same way.

**Rule used (as in Methodical).** Where German-speaking researchers really use the English term (in IQWiG, DNEbM or
Cochrane texts, or in the German Wikipedia article for the concept), the English term stays, spelled the German way:
nouns capitalised and multi-word compounds hyphenated (Duden rule for English loan compounds), e.g.
*Immortal-Time-Bias*, *Survivorship-Bias*. Where an established German term exists, it is used. Players are addressed
with *du*, as in Methodical.

**Numbers.** German conventions, as in Methodical: decimal comma (*r = 0,96*, *p = 0,01*), thousands point
(*50.000*), a space before the per-cent sign (*30 %*), *95-%-KI* for a 95% confidence interval. Only the format
changed; no number did. Numbers drawn by the code inside claim charts (bar values such as *7.4*) come from
`data/claims.json` and keep the decimal point; they are not translatable strings.

**Card types.** *Behauptung* (claim), *Flag* (kept: it is the game's own mechanic and its name, *Red Flag*; German
says *Warnsignal* in running text, used once in C36), *Check* (kept: Duden lists *Check*, short and familiar from
*Faktencheck*), *Stichhaltig* (the Sound card; *stichhaltig* is the standard German word for a sound argument). Verb
for playing a flag: *flaggen* (Duden: *flaggen*, to mark). The four families: *Ursache*, *Stichprobe*, *Zahlen*,
*Vorgehen*.

## Sources (codes used in the tables)

| Code | Source |
|---|---|
| DNEbM | Deutsches Netzwerk Evidenzbasierte Medizin, *Glossar zur Evidenzbasierten Medizin*, Stand Oktober 2018. https://www.ebm-netzwerk.de/de/medien/pdf/ebm-glossar.pdf/@@download |
| IQWiG | IQWiG, *Allgemeine Methoden*, Version 8.0 (19.12.2025), as cited in Methodical's glossary; for surrogate endpoints, IQWiG Rapid Report A10-05, *Aussagekraft von Surrogatendpunkten in der Onkologie* (2011). https://www.iqwig.de/download/a10-05_rapid_report_surrogatendpunkte_in_der_onkologie.pdf |
| WP | German Wikipedia article of that title (https://de.wikipedia.org/wiki/…), checked 31.10.2026 where marked ✓ |
| DC | DocCheck Flexikon (German medical encyclopaedia), checked 31.10.2026: *Prosecutor's Fallacy* (https://flexikon.doccheck.com/de/Prosecutor%E2%80%99s_Fallacy), *Lead-Time-Bias* (https://flexikon.doccheck.com/de/Lead-Time-Bias) |
| MTH | Methodical's German glossary and card text (`methodical-card-game/i18n/de/`) |
| — | No authoritative German source found; choice by usage judgement. Flagged for a native reviewer. |

## Game structure

| English | German | Evidence | Note |
|---|---|---|---|
| Claim | Behauptung | — | Reviewer agreed. *Aussage* is softer; a claim in this game is asserted and may be false, which *Behauptung* carries. |
| Flag / to flag | Flag / flaggen | game title | See card types above. |
| Check | Check | Duden | *Prüfung* also means an exam; *Gegenprobe* was considered. Reviewer agreed. |
| Sound (verdict) | stichhaltig | standard German | Card name *Stichhaltig*; deck tab *Stichhaltig-Karte*. |
| Flawed | fehlerhaft | | Card back: *FEHLERHAFT ODER STICHHALTIG?* |
| reasoning error | Denkfehler | | Plain word; *Fehlschluss* kept for named fallacies (*ökologischer Fehlschluss*). |
| false alarm | Fehlalarm | | |
| best / defensible / trap / unlisted | beste / vertretbar / Falle / nicht gelistet | MTH | Same as Methodical. |
| appeal | Einspruch | MTH | |
| answer key | Lösungsschlüssel, Lösungsheft | MTH | |
| key reference | Schlüsselreferenz | MTH | |
| move (what a Check is) | Schritt | — | |
| Cause / Sample / Numbers / Practice | Ursache / Stichprobe / Zahlen / Vorgehen | — | Draft had *Praxis*; the reviewer noted that medical readers take *Praxis* as clinical practice or a doctor's surgery. |
| calibrated | kalibriert | | |
| evidence | Evidenz | DNEbM | |
| outcome | Outcome (das) | MTH, DNEbM | |
| exposure | Exposition | MTH, DNEbM | |
| confounder | Confounder | MTH, DNEbM | |
| confidence interval | Konfidenzintervall, 95-%-KI | MTH, DNEbM | |
| effect size | Effektstärke | MTH, DNEbM | |
| subgroup | Subgruppe | MTH, IQWiG | |
| preregistration | Präregistrierung | MTH | |
| replication | Replikation | MTH | |
| follow-up | Nachbeobachtung | MTH | |
| adjust for | adjustieren für | MTH (*Adjustierung für*) | |
| randomised | randomisiert | MTH, DNEbM | |
| allocation | Zuteilung | MTH, DNEbM | |
| usual care | Regelversorgung | standard German health-services term | |
| mortality | Mortalität / Sterblichkeit | DNEbM | *Mortalität* where the technical measure is meant (C42, lead-time flag). |
| pooled | gepoolt | MTH (*poolen*) | |
| probability (vs odds) | Wahrscheinlichkeit; *1 von n* | DNEbM (*Chance* = odds) | *Chance* and *1 zu n* read as odds in German statistics, so probabilities say *Wahrscheinlichkeit* and *1 von n* (C24, C26, C49, transposed-conditional flag). C49 matters most: odds of 1:6 would be 14%, the card's answer is 16%. C25's headline *Ein Prozent Chance* stays as colloquial voice; C26's fallacious claim keeps *1 zu einer Million* (its own voice). |
| intensive care (C05) | Intensivstation | | Draft *Intensivpflege* means (often long-term) intensive nursing care. |
| drive (a cause drives both) | beeinflussen | | Draft *treiben* was a calque. |
| case mix | Patientenstruktur | German health-services usage — | |
| abortion | Schwangerschaftsabbruch | neutral medical term | |
| lead time | Vorlaufzeit; *Lead-Time-Bias* | DC ✓ | *Vorlaufzeit* for the time itself, *Lead-Time-Bias* for the bias (C48). |
| natural frequencies | natürliche Häufigkeiten | Gigerenzer's German usage — | |
| 2×2 table | Vierfeldertafel | standard German statistics | |
| number needed to treat | Number Needed to Treat | DNEbM | |
| true / false positives | richtig / falsch Positive | DNEbM | |
| null result | Nullbefund | MTH | |
| back-test | Backtest | finance usage | |
| C-statistic | C-Statistik | | |

## Flags

| English | German | Evidence | Note |
|---|---|---|---|
| Correlation as causation | Korrelation als Kausalität | — | Literal and transparent. |
| Hidden third factor | Verborgene Drittvariable | German textbooks: *Drittvariable*, *Drittvariablenproblem* — | Card text uses *Confounder* (MTH). |
| Reverse causation | Umgekehrte Kausalität | MTH | |
| Two trends, one clock | Gemeinsamer Zeittrend | — | Draft *Zwei Trends, eine Uhr*; the clock image doesn't carry in German (review). The textbook phrase *Scheinkorrelation durch Zeittrend* is too long for the name bar. |
| Collider bias | Collider-Bias | MTH | |
| Immortal time | Immortal-Time-Bias | MTH | Methodical's card name; the English card here drops "bias". |
| Beyond the data | Jenseits der Daten | — | *Extrapolation* is in the short text by meaning. |
| Mice to people | Von der Maus zum Menschen | — | |
| Ecological fallacy | Ökologischer Fehlschluss | MTH, WP | |
| Survivorship bias | Survivorship-Bias | MTH, WP | |
| Unrepresentative sample | Nicht repräsentative Stichprobe | — | |
| Narrow sample, universal claim | Enge Stichprobe, Aussage über alle | — | The concept is the WEIRD-sample problem (Henrich et al. 2010); Methodical mentions *WEIRD-Stichproben*. |
| Simpson's paradox | Simpson-Paradoxon | WP ✓ (article title) | |
| Regression to the mean | Regression zur Mitte | MTH, WP | |
| Small numbers, wild swings | Kleine Zahlen, große Schwankungen | — | |
| Base-rate neglect | Basisratenfehler | WP ✓ *Prävalenzfehler* (synonyms *Basisratenfehler*, *Basisratenmissachtung*) | *Basisratenfehler* chosen because the card text says *Basisrate*; *Prävalenzfehler* is the WP title. |
| Transposed conditional | Vertauschte Bedingung | DC ✓ lists *Fehlschluss des Anklägers* and *Transpositionsfehler der Konditionalen* | The card covers more than the courtroom case (p-values too), so the courtroom name was not used; reviewer agreed. |
| No significance, no effect | Nicht signifikant, kein Effekt | — | |
| Significant but trivial | Signifikant, aber belanglos | — | |
| Relative risk alone | Nur relatives Risiko | DNEbM (*relatives Risiko*) | |
| Distorted chart | Verzerrte Grafik | — | |
| Overfitting | Overfitting | MTH, WP *Überanpassung (englisch overfitting)* | |
| Forking paths | Forking Paths | MTH (*Forking Paths & p-Hacking*) | Card text adds *(p-Hacking)*, as the flag's id and Methodical's card pair the two. |
| Many tests, one hit | Viele Tests, ein Treffer | — | Text: *Korrektur*, *Nullhypothesen*. |
| Subgroup surprise | Überraschende Subgruppe | — | |
| File drawer | Schubladenproblem | WP ✓ *Publikationsbias* ("auch als Schubladenproblem … bekannt") | Text adds *(Publikationsbias)*, MTH's term. |
| One study, settled | Eine Studie, Fall erledigt | — | Draft *schon bewiesen*: a study is not "proved" (review). |
| Surrogate endpoint | Surrogatendpunkt | IQWiG A10-05 ✓ | WP's title is *Surrogatmarker* (syn. *Surrogat-Parameter*); Methodical uses *Surrogatparameter* in running text. *Surrogatendpunkt* matches the English card name and IQWiG usage. |
| Survival-time illusion | Überlebenszeit-Illusion | — | The concept is lead-time bias plus overdiagnosis (DC ✓ *Lead-Time-Bias*, *Überdiagnose-Bias*); traps use *Vorlaufzeit* (lead time) and *Überdiagnose*. |
| Changed yardstick | Geänderter Maßstab | — | |

## Checks

| English | German | Note |
|---|---|---|
| Ask for the denominator | Nach dem Nenner fragen | Picture label OUT OF ? → NENNER? (the literal *VON WIE VIELEN?* ran out of the picture). |
| Compared with what? | Verglichen womit? | |
| Draw the causal diagram | Kausaldiagramm zeichnen | MTH *Kausaldiagramm (DAG)*. *Hintertürpfade* for back-door paths; *selektieren* on a collider, as MTH (*Selektion nach*). |
| Check the timeline | Zeitablauf prüfen | *Zeitachse* avoided so it doesn't echo *Zwei Trends, eine Uhr*. |
| Plot it over time | Zeitverlauf darstellen | |
| Split by subgroup | Nach Subgruppen aufteilen | |
| Ask for individual data | Individualdaten verlangen | *Individualdaten* as in *individuelle Patientendaten* (MTH). |
| Find who's missing | Herausfinden, wer fehlt | |
| Check who and what was studied | Wer und was wurde untersucht? | A question, like *Verglichen womit?*, to fit the name bar. |
| Find the preregistration | Präregistrierung suchen | |
| Look for the other studies | Andere Studien suchen | |
| Read the confidence interval | Konfidenzintervall lesen | |
| Ask how big | Fragen, wie groß | *Effektstärke* reads as a standardised effect (Cohen's d), the opposite of this card's point: absolute differences, NNT, real units (review). |
| Ask what was measured | Fragen, was gemessen wurde | |
| Test it on new data | An neuen Daten testen | |
| Read the axes | Achsen lesen | |

## Real cases on Flag cards

Names, numbers, years and sources are unchanged. Paper titles are not translated. Small wording choices:
*WHI-Studie*, *Hormonersatztherapie* (HRT); *Trauungen der Church of England*; *US-Countys*; *Zweiter Weltkrieg*;
ISIS-2 star signs as *Zwillinge oder Waage*; the 1995 pill scare as *Thromboserisiko* (the English says "clot
risk"); the 2015 House chart as *Krebsvorsorgen* (cancer screenings). "1 in 73 million" is *1 zu 73 Millionen*.

## Picture labels (`ui.json` → `art`, and claim `labels`)

Labels were shortened where the German ran into a neighbouring label or out of the picture (checked by measuring
every SVG text box in headless Chrome, German against English): C08 USERS / NON-USERS → STATIN / KEIN STATIN;
C17 % SURVIVE → % LEBEND; C53 MEAN SCORE → Ø PUNKTE; C59 SD GAIN → SD-GEWINN; K01 OUT OF ? → NENNER?.
After review: FAKE LINK → SCHEINKORRELATION (fits), FITS NOISE → LERNT RAUSCHEN, UNSEEN → UNBEKANNT, C26 → 1 VON
1.000.000.
C05 % NEEDING ICU → % AUF INTENSIV (clinical shorthand for *auf der Intensivstation*). GOT IT / DIDN'T on the
comparison check → MIT / OHNE.

## Review (31 October 2026)

An independent reviewer pass, acting as a German-speaking methodologist, read the English source, this translation
and Methodical's glossary, without the translator's notes. All 13 must-fix points and most style points were taken:

- **Meaning and facts:** C56 read as deaths rising (*60 … statt 45*), now *von 60 auf 45*; the survivorship example
  had lost "on survivors" (*an Rückkehrern*); C57's sentence misparsed dose and timing; *Chance* / *1 zu n* used for
  probabilities (see the table); *Intensivpflege* (C05); C24's *zu etwa 95 %* was ambiguous.
- **Sally Clark example:** the English "accidental" had become *natürlich*; it now follows the source:
  *Unglücksfälle*.
- **Grammar:** C23 case agreement, C10 number agreement, *allem, was*, an incomplete clause in the forking-paths
  text, *Sichereres Radfahren* (C56 title), *30 in 2008–12* (anglicism).
- **Terminology:** *Selektion nach* (collider, as MTH), *Hintertürpfade*, *verzerrte Stichprobe*, *relatives Risiko*
  (was *Risk Ratio*), *Nullbefund*, *Dosis-Wirkungs-Beziehung*, *Lead-Time-Bias*, *A-priori-Plausibilität*,
  *Datenfischen* (was *Fischzug*), *Bundesstaaten*, *Sensibilisierung* (not *Aufmerksamkeit* on an ADHS card).
- **Names:** *Vorgehen*, *Gemeinsamer Zeittrend*, *Eine Studie, Fall erledigt*, *Fragen, wie groß*,
  *Zeitverlauf darstellen*.
- **Interface:** *Echter Fall: {flag}* and *Welcher Check deckt „{flag}“ auf?*, because flag names are phrases;
  *oder nenne die Behauptung stichhaltig* (the pronoun could point at the Flag).
- **Register:** C31's advert used *Sie*; now *du*, like every other card.
- About 25 smaller wording points (C08, C09, C11, C15, C28, C30, C32, C36, C37, C40, C42, C46, C47, C52, C53, checks).

**Not taken, with reasons:**
- *home.quick* stays *Schnelle Behauptung* and the footer keeps *Streite mit ihm*, to match Methodical's
  *Schnelle Frage* and footer word for word, so the kit reads alike. The reviewer proposed *Schnellrunde* and
  *Widersprich ihm ruhig*.
- *Surrogatendpunkt*, *Flag*, *Check*, *Behauptung* and *Vertauschte Bedingung* stay (reviewer agreed).

## Open questions for a native methodologist

1. *Vertauschte Bedingung* for the transposed conditional: translator and reviewer both keep it, but a statistician
   may prefer an established name. *Fehlschluss des Anklägers* fits only the courtroom half of the card.
2. *Gemeinsamer Zeittrend* (card name) vs the English image "two trends, one clock": is anything lost?
3. Kit-wide: *Surrogatendpunkt* (here, IQWiG) vs *Surrogatparameter* (Methodical's running text). The reviewer
   recommends unifying the kit on *Surrogatendpunkt* in Methodical's next pass.
4. Kit-wide: *Schnelle Behauptung* / *Streite mit ihm* (kept for parallel wording with Methodical) vs the reviewer's
   *Schnellrunde* / *Widersprich ihm ruhig*; if changed, change both games.
5. *Settled 2026-10-31.* Sally Clark: the RSS (2002) letter, read that day, says "Some press reports at the time
   stated that this was the chance that the deaths of Sally Clark's two children were accidental." The English and
   *Unglücksfälle* match the source; keep them.
6. Family "Practice": *Vorgehen*, or *Forschungspraxis* if it fits?
