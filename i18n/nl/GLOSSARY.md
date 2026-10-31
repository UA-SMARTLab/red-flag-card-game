# Dutch glossary for Red Flag

Terms chosen for the Dutch translation (`cards.json`, `ui.json`), and the reasons for each choice. Written for a native methodologist reviewing or extending the translation. Red Flag is the second game of the SMART-Lab Science Game Kit; shared concepts use the terms of Methodical's Dutch glossary (`methodical-card-game/i18n/nl/GLOSSARY.md`, "Methodical-NL" below).

## Principles

- **Audience.** Researchers and students in Flanders and the Netherlands. Where the two differ, the translation uses the form understood in both, as Methodical-NL does. The review pass removed several Flemish-only uses (*besluiten* for "conclude", *opvolgen* for "follow up", *ophaling*, *tegen 2011*) and the Netherlands-leaning *wellicht*.
- **Keep the English term when Dutch researchers do.** Confounder, bias compounds (colliderbias, survivorship bias, publicatiebias), overfitting, forking paths, p-hacking, trial, follow-up, lead time, backtest, casemix, number needed to treat, backdoorpaden and immortal time stay in English, as in Methodical-NL. Everything else is in Dutch.
- **One concept, one term** across cards, interface, picture labels and Methodical. The table below lists the shared terms.
- **Numbers.** Dutch formatting as in Methodical-NL: decimal comma (r = 0,96; p = 0,01; HR 1,29), thousands with a period (5.000; 689.003), confidence interval written *95%-BI*. Only the formatting changed; every value, name and date on the Flag cards was compared with the English by the reviewer.
- **Real cases** (Flag `example`): names, numbers and facts kept exactly; nothing added. Study names (WHI, CAST, ISIS-2, TGN1412, Literary Digest, Church of England) stay in the original. Dutch abbreviations replace English ones only where they name the same thing (HRT → HST, hormoonsuppletietherapie; WWII → WOII; US → VS; UK → VK).
- **Evidence status.** "Verified" means the term was seen in the cited source while preparing this glossary. "Convention" means standard usage known to the translator or reviewer, not checked online. "Methodical-NL" means the term was taken over from the sister game, where its source is given.

## Main sources

| Short name | Source |
|---|---|
| Methodical-NL | Methodical's Dutch glossary, with its own sources (Cochrane Nederland checklists, Richtlijnendatabase, NTvG, CBS, Wikipedia-NL) |
| Wikipedia-NL | Dutch Wikipedia article titles, e.g. https://nl.wikipedia.org/wiki/Simpsons_paradox |
| Review | Independent review pass by a Dutch-speaking methodologist reviewer (2026-10-31), given only the English source, the Dutch files and Methodical-NL |

Online searches for Dutch sources on *basisfrequentie*, *surrogaateindpunt* and *lead time bias* returned no authoritative Dutch page (2026-10-31); these rows are marked "Convention" and are listed under open questions.

## Game vocabulary

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Claim (card type, deck) | Bewering, Beweringen | Convention | *Claim* is also Dutch, but *bewering* is plain and works in rules and app text. *Claim* is kept only in the fixed research phrase *causale claim*. |
| Flag (card type, deck); to flag | Vlag, Vlaggen; een vlag zetten op | Convention | The game title *Red Flag* stays English. *Rode vlag* is used figuratively in Dutch (C36 "de analysekeuzes zijn de rode vlag"). |
| Check (card type, deck) | Check, Checks | Convention; Methodical-NL uses *Pretrendcheck* | *Controle* clashes with *controlegroep* and *controles* (case–control) in Methodical-NL; *toets* clashes with the statistical test. The review agreed. |
| Sound; Sound card; Sound claim | steekhoudend; kaart Steekhoudend; Steekhoudende bewering | Convention | *Steekhoudend* ("holds water") is said of arguments and conclusions. *Deugdelijk* was the alternative. |
| Flawed | gebrekkig | Convention | "Flawed or sound?" (quick play title) is *Gebrekkig of steekhoudend?*. |
| FLAWED OR SOUND? (card back) | KLOPT HET OF NIET? | Length | *GEBREKKIG OF STEEKHOUDEND?* was clipped on the card back (checked on the rendered back, 2026-10-31). |
| Reasoning error | redeneerfout | Convention | |
| Move (Check type line) | zet | Convention | As in a game move. |
| Exposed by / Exposes | Blootgelegd door / Legt bloot | Convention | |
| Verdict / call | oordeel | Convention | |
| False alarm | vals alarm | Convention | Also in the base-rate picture label (1 ECHT · 5 VALS ALARM). |
| Calibrated, not cynical | Gekalibreerd, niet cynisch | Methodical-NL uses *kalibratie* | |
| Best / Defensible / Trap / Unlisted | Beste / Verdedigbaar / Valkuil / Niet vermeld | Methodical-NL | |
| appeal | beroep (in beroep gaan, beroep aanvaarden) | Methodical-NL (*card.appeal*) | Review suggested *honoreert*; kept *aanvaardt* to match Methodical. |
| key check | de check uit de sleutel | Review | *Sleutelcheck* read as a calque. |
| Key reference | Kernreferentie | Methodical-NL | |
| Families: Cause / Sample / Numbers / Practice | Oorzaak / Steekproef / Cijfers / Werkwijze | Oorzaak: Methodical-NL suit name. Others convention | *Praktijk* would suggest clinical practice; the family is about how research was analysed, measured and reported. |

## Core vocabulary in running text

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| confounder | confounder | Methodical-NL (verified: Cochrane-NL etiologie) | The Flag name is *Verborgen derde factor*, matching Methodical's short text for confounding. |
| exposure / outcome | blootstelling / uitkomst | Methodical-NL | |
| trial; randomised | trial; gerandomiseerd, door loting | Methodical-NL | Never *willekeurig* for randomisation. *Twee willekeurige stijgende reeksen* (C04) means "any two", not "random". |
| control group | controlegroep | Methodical-NL | Picture label CONTROLE. |
| usual care | gebruikelijke zorg | Convention | |
| loss to follow-up, drop out | uitval, uitvallen | Methodical-NL (verified: Cochrane-NL) | Review changed C19 *valt af* to *valt uit*. |
| relative risk | relatief risico | Methodical-NL (verified: Cochrane-NL etiologie) | Review changed *risicoratio* (Amrhein example) to *relatief risico*. |
| absolute risk / percentage point | absoluut risico / procentpunt | Convention | |
| confidence interval (CI) | betrouwbaarheidsinterval (95%-BI) | Convention (NTvG style) | |
| p-value; significant | p-waarde; significant | Convention | |
| hypothesis test (statistical) | toets, toetsen | Convention | Flag *Veel toetsen, één treffer*. |
| hit (significant result) | treffer | Methodical-NL (*Lage power* text: "een treffer") | |
| null result | nulresultaat | Methodical-NL (*Publicatiebias*: "De nulresultaten liggen nog in de la") | |
| effect size | effectgrootte | Convention | |
| smallest worthwhile benefit (C50) | kleinste klinisch relevante effect | Review, convention (MCID) | |
| prior probability | voorafkans | Review; Cochrane-NL diagnostiek usage | C25. |
| base rate | basisfrequentie | Convention | See open questions. |
| true / false positive | terecht-positief / fout-positief | Convention (Dutch diagnostic-test usage) | |
| natural frequencies | natuurlijke frequenties | Convention | |
| common cause / common effect | gemeenschappelijke oorzaak / gemeenschappelijk gevolg | Convention | Review unified *gedeeld gevolg* and *gedeelde uitkomst* to *gemeenschappelijk gevolg*. |
| backdoor paths | backdoorpaden | Review, convention (Pearl's term kept in Dutch epidemiology) | Draft had *achterdeurpaden*. |
| causal diagram | causaal diagram | Methodical-NL (*Causaal diagram (DAG)*) | |
| prediction model; discrimination | predictiemodel; discriminerend vermogen | Methodical-NL | Review replaced the verb *discrimineert* (C52), which reads as unfair treatment. |
| C-statistic | C-statistiek | Convention | |
| external validation | externe validatie | Methodical-NL | |
| preregistration; preregistered | preregistratie; gepreregistreerd | Methodical-NL | |
| replication | replicatie | Methodical-NL | |
| case mix | casemix | Review, convention (Dutch health-services research) | |
| survey (respondents) | enquête; respondenten | Methodical-NL (*enquête*); review (*respondenten*) | *Responders* means treatment responders in Dutch clinical usage. |
| mortality / deaths | sterfte / sterfgevallen | Convention | |
| heart attack | hartinfarct | Review, convention (NTvG) | Draft mixed *hartaanval* and *hartinfarct*. |
| screening; overdiagnosis; lead time | screening; overdiagnose; lead time | Convention | |
| surrogate endpoint; marker | surrogaateindpunt; marker | Convention; Methodical-NL (*marker*) | Dutch course material contrasts *surrogaateindpunten* with *harde eindpunten*; no NTvG page was found online. |
| department (Berkeley) | vakgroep | Review | A Dutch *faculteit* is a much larger unit and would change the level of the Simpson split. |
| hormone replacement therapy (HRT) | hormoonsuppletietherapie (HST) | Convention (Dutch medical abbreviation) | |

## Flag names

| English | Dutch | Source / evidence | Note |
|---|---|---|---|
| Correlation as causation | Correlatie als causaliteit | Methodical-NL uses *causaliteit* (*Omgekeerde causaliteit*) | |
| Hidden third factor | Verborgen derde factor | Methodical-NL (confounding short text) | |
| Reverse causation | Omgekeerde causaliteit | Methodical-NL | |
| Two trends, one clock | Twee trends, één klok | Convention | |
| Collider bias | Colliderbias | Methodical-NL | |
| Immortal time | Immortal time | Methodical-NL (*Immortal time bias*) | |
| Beyond the data | Buiten de data | Convention | |
| Mice to people | Van muis naar mens | Convention (Dutch set phrase) | |
| Ecological fallacy | Ecologische fout | Methodical-NL (verified: Wikipedia-NL) | |
| Survivorship bias | Survivorship bias | Methodical-NL | |
| Unrepresentative sample | Niet-representatieve steekproef | Methodical-NL (*Representatieve steekproef*) | |
| Narrow sample, universal claim | Smalle steekproef, algemene bewering | Review | Draft *brede bewering* weakened "universal". |
| Simpson's paradox | Simpsons paradox | Verified: Wikipedia-NL title "Simpsons paradox" | *Paradox van Simpson* is also heard. |
| Regression to the mean | Regressie naar het gemiddelde | Methodical-NL (verified: Wikipedia-NL) | |
| Small numbers, wild swings | Kleine aantallen, grote uitschieters | Convention | |
| Base-rate neglect | Basisfrequentie negeren | Convention | See open questions. |
| Transposed conditional | Verwisselde voorwaardelijke kans | Convention | *Verwisselde* avoids confusion with *Omgekeerde causaliteit*. The press error in the example is known as the *prosecutor's fallacy*; no Dutch page was found to confirm a Dutch name. |
| No significance, no effect | Niet significant, geen effect | Convention | |
| Significant but trivial | Significant maar triviaal | Convention | |
| Relative risk alone | Alleen relatief risico | Methodical-NL (*relatieve risico*) | |
| Distorted chart | Vertekende grafiek | Convention | *Vertekening* is the lay word for bias. |
| Overfitting | Overfitting | Methodical-NL | |
| Forking paths | Forking paths | Methodical-NL (*Forking paths & p-hacking*) | |
| Many tests, one hit | Veel toetsen, één treffer | Convention; Methodical-NL (*treffer*) | |
| Subgroup surprise | Verrassende subgroep | Convention | |
| File drawer | In de la | Review; Methodical-NL short text ("in de la") | Draft *Bureaula* was opaque as a name. The text names *publicatiebias* to link to Methodical. |
| One study, settled | Eén studie, uitgemaakte zaak | Convention | |
| Surrogate endpoint | Surrogaateindpunt | Convention | |
| Survival-time illusion | Schijnbare overlevingswinst | Convention | Avoids *overlevingsillusie*, which could be confused with survivorship bias. |
| Changed yardstick | Andere meetlat | Convention | |

## Check names

| English | Dutch | Note |
|---|---|---|
| Ask for the denominator | Vraag naar de noemer | |
| Compared with what? | Vergeleken met wat? | |
| Draw the causal diagram | Teken het causale diagram | |
| Check the timeline | Controleer de tijdlijn | The card type is *Check*; the verb is Dutch. |
| Plot it over time | Zet het uit in de tijd | Methodical-NL (*Zet de maat uit in de tijd*). |
| Split by subgroup | Splits per subgroep | |
| Ask for individual data | Vraag om individuele data | |
| Find who's missing | Zoek wie ontbreekt | |
| Check who and what was studied | Ga na wie en wat onderzocht is | |
| Find the preregistration | Zoek de preregistratie | |
| Look for the other studies | Zoek de andere studies | |
| Read the confidence interval | Lees het betrouwbaarheidsinterval | Wraps to two lines in the name bar; fits. |
| Ask how big | Vraag hoe groot | |
| Ask what was measured | Vraag wat er gemeten is | |
| Test it on new data | Test het op nieuwe data | |
| Read the axes | Lees de assen | |

## Picture labels

Labels are short and upper case, like the English, and were checked on the rendered print sheets (2026-10-31). Choices worth noting:

- THE DAILY CLAIM (newspaper masthead) → DE BEWERING, styled like a Dutch-language newspaper name.
- FAKE LINK → SCHIJNVERBAND; POOLED → GEPOOLD; UNSEEN → ONGEZIEN; GOT IT / DIDN'T → KREEG HET / NIET; SAME DEATH → ZELFDE STERFDAG; THEN → TOEN.
- Numbers in labels use Dutch formatting (1 OP 1.000.000; p < 0,05; C = 0,78; 1 → 2 OP 7.000).
- Shortened to fit: % ALIVE → % LEVEND; 5-YR SURVIVAL → 5-JR OVERLEVING; RATE PER 100,000 → PER 100.000.
- ONE HIT IN MANY TESTS → 1 TREFFER IN VEEL TOETSEN (upper case would lose the accents of *één*).
- % WHO FELL → % VIEL (review: *% GEVALLEN* reads as "% cases").

## Review

An independent reviewer pass checked every string against the English and Methodical-NL. It found no changed fact or number. Changes made from the review:

- Meaning: C50 title (*Precieze nulbevinding*, not "exactly zero"); Sally Clark example "accidental" restored as *een ongeluk* (the draft had *natuurlijk*); Wald example hedge *waarschijnlijk*; C52 *discriminerend vermogen*; C54 label; denominator Check text ("out of how many"); *respondenten*; Berkeley *vakgroep*; C21 village throughout and no added certainty; grammar in C02, C31 and the collider short text (*keert ... om*); tagline referent (*noem de bewering steekhoudend*).
- Terminology: *relatief risico*, *casemix*, *hartinfarct*, *gemeenschappelijk gevolg*, *uitval*, *concludeert*, *voorafkans*, *klinisch relevante effect*, *procentpunt*, *backdoorpaden*, *In de la*.
- Style: some twenty calques and awkward phrasings (listed in the review notes), and the card-back slogan, which was too long.

Not adopted, with reasons:

- *Waarom dit niet klopt* for "Why it fails", *honoreert* for "upholds" and *sla die over*: kept identical to Methodical's interface strings so the kit reads alike.
- *ging failliet* for "failed" (Find who's missing): too narrow, since the card also covers students and patients; *mislukte* used instead.
- Length warnings for NULRESULTATEN, GEDIAGNOSTICEERD %, SMARTPHONES and VERANDERING (PUNTEN): all fit on the rendered cards, so they were kept.

## Open questions for a native methodologist

1. **Basisfrequentie negeren.** Used in Dutch psychology teaching, but clinicians may think in terms of *voorafkans* or *prevalentie*. No authoritative Dutch source was found. An alternative is to keep the name and mention *voorafkans* in the text.
2. **Sally Clark example.** The English says the press reported "1 in 73 million" as the chance the deaths were "accidental"; the Dutch follows it (*een ongeluk*). *Settled 2026-10-31:* the RSS (2002) letter says "Some press reports at the time stated that this was the chance that the deaths of Sally Clark's two children were accidental", so the English and *een ongeluk* match the source.
3. **Bewering or claim** as the deck name. Researchers also say *claim*; *bewering* was chosen as plainer Dutch.
4. **Steekhoudend** for "Sound", and **KLOPT HET OF NIET?** on the card back. Alternatives: *deugdelijk*; *RAMMELT HET?*.
5. **Verwisselde voorwaardelijke kans.** Is there an established Dutch name for the transposed conditional (*drogreden van de aanklager* for the prosecutor's fallacy)?
6. **Hybrid or English names**: *Immortal time*, *Forking paths*, *Survivorship bias*, *Overfitting* follow Methodical; a reviewer may prefer Dutch for some of them in a game also used with students.
7. **Werkwijze** as the family name for "Practice" (analysis, measurement and reporting). *Onderzoekspraktijk* is more exact but longer.
8. **Context-dependent picture labels**: KREEG HET / NIET, TOEN and ZELFDE STERFDAG depend on the drawing; check them on printed cards.
