# Glossaire français de Red Flag

Ce glossaire explique les choix de termes de la version française (`i18n/fr/cards.json`, `i18n/fr/ui.json`), pour qu'un relecteur méthodologiste puisse les vérifier ou les contester. Il prolonge celui de Methodical (`methodical-card-game/i18n/fr/GLOSSARY.md`) : un concept partagé par les deux jeux porte le même terme dans tout le SMART-Lab Science Game Kit.

Principes suivis :

- **Usage de France et de Belgique** d'abord ; on écarte les termes surtout québécois (« aînés », « devis », « données probantes »).
- **Le terme réellement employé par la discipline**, pas une traduction mot à mot. Quand les chercheurs francophones gardent l'anglais (*p-hacking*, *backtest*, *case-mix*), on le garde.
- **Un concept, un terme**, dans tous les champs : noms de cartes, textes courts, explications, pièges, interface, étiquettes des illustrations.
- **Même terme que Methodical** pour les concepts communs (tableau ci-dessous).
- **Cas réels** (champ `example` des cartes Drapeau) : noms, chiffres et années recopiés tels quels, sans fait ajouté ; titres d'articles laissés dans leur langue.
- **Typographie** : espace insécable (U+00A0) avant : ; ? ! % et à l'intérieur des « » ; virgule décimale (p = 0,01, r = 0,96) ; espace insécable comme séparateur des milliers (5 000) et autour du signe dans les formules courtes (p = 0,048), pour qu'elles ne soient pas coupées en fin de ligne.

Les numéros entre crochets renvoient aux sources en fin de document. « Usage courant » signale un choix fondé sur l'usage des manuels et articles francophones, sans source en ligne vérifiée lors de cette traduction.

## Types de cartes et vocabulaire du jeu

| Anglais | Français retenu | Note |
|---|---|---|
| Claim (card) | **Affirmation** ; paquet « Affirmations » | « Allégation » est le terme réglementaire (allégations de santé) et a une connotation commerciale ; « assertion » est plus logique que scientifique. |
| Flag (card) ; to flag | **Drapeau** ; **signaler** (une affirmation) | Garde l'image du jeu (*Red Flag*, drapeau rouge au dos des cartes). Le nom du jeu reste *Red Flag*. |
| Check (card) | **Vérification** ; paquet « Vérifications » | « Parade » est déjà pris par Methodical (*Safeguard*). |
| Move (sous-type de la carte Check) | **Geste** | Voir questions ouvertes (« coup »). |
| to expose (a flag) | **révéler** ; « Révélé par », « Révèle » | |
| Sound (claim) ; Sound card | **fondée** (« affirmation fondée ») ; **carte Fondée** | |
| Flawed (claim) | **bancale** ; *flaw* → **faille** | Registre familier choisi pour le jeu (« Bancale ou fondée ? »). |
| false alarm | **fausse alerte** | |
| calibrated (scepticism) | **calibré** (« Restez calibré », « Calibré, pas cynique ») | Terme de la recherche sur le jugement probabiliste ; voir questions ouvertes. |
| Best / Defensible / Trap / Unlisted | **Meilleur / Défendable / Piège / Non listé** | Identique à Methodical (le relecteur propose « hors corrigé » ; gardé pour l'unité du kit). |
| answer key | **corrigé** | Identique à Methodical. |
| family (Cause, Sample, Numbers, Practice) | **Cause, Échantillon, Chiffres, Pratique** | *NUMBERS* → CHIFFRES comme dans les illustrations de Methodical. |
| evidence | **preuves** | Identique à Methodical. |

## Termes partagés avec Methodical

| Anglais | Français retenu | Source | Note |
|---|---|---|---|
| outcome (mesuré, comparé) | **critère de jugement** | [1] | Methodical. *Real endpoint* → « critère final » (par opposition au marqueur). |
| outcome (qui survient) | **événement** | Methodical | « Prévenir l'événement », « l'exposition et l'événement ». |
| exposure | **exposition** | | |
| control group | **groupe témoin**, « TÉMOIN » | [1] | |
| randomised | **randomisé** ; « par tirage au sort » dans une phrase simple | [1] | |
| study design | **schéma d'étude** | Methodical | |
| confounder | **facteur de confusion** ; nom de carte « Tiers facteur caché » | [2] | Le nom anglais *Hidden third factor* est rendu par l'expression de la carte *Confounding* de Methodical (« Un tiers facteur caché… »). |
| reverse causation | **Causalité inverse** | Methodical | |
| collider bias ; collider | **Biais de collision** ; **collisionneur** | [3] | |
| immortal time | **Biais du temps immortel** | Methodical | Le nom anglais de Red Flag est plus court (*Immortal time*) ; on garde le nom de Methodical pour l'unité du kit (relecture). |
| ecological fallacy | **Erreur écologique** | Methodical | |
| survivorship bias | **Biais du survivant** | Methodical | |
| regression to the mean | **Régression vers la moyenne** | Methodical | Texte court repris mot pour mot de Methodical. |
| forking paths | **Chemins multiples** ; *p-hacking* gardé en anglais dans le texte | Methodical | Methodical : « Chemins multiples et p-hacking ». |
| overfitting | **Surapprentissage** | Methodical | « Surajustement » est l'usage québécois. |
| surrogate endpoint | **Critère de substitution** | [1] | |
| null results | **résultats négatifs**, « NÉGATIFS » | Methodical | |
| preregistration | **préenregistrement** | Methodical | |
| replication | **réplication** | Methodical | |
| users (of a drug) | **utilisateurs** / **non-utilisateurs** | Methodical | |
| new data | **données neuves** | Methodical (illustration NEW DATA) | |
| causal diagram | **diagramme causal** | Methodical, [3] | |

## Cartes Drapeau

| Anglais | Français | Source | Note |
|---|---|---|---|
| Correlation as causation | **Corrélation prise pour causalité** | usage courant | |
| Hidden third factor | **Tiers facteur caché** | voir ci-dessus | |
| Two trends, one clock | **Deux tendances, une horloge** | | Nom imagé, comme l'anglais ; le concept est la corrélation fallacieuse entre séries qui dérivent (Yule 1926). |
| Beyond the data | **Au-delà des données** | | Extrapolation. |
| Mice to people | **De la souris à l'humain** | | « L'humain » plutôt que « l'homme ». |
| Unrepresentative sample | **Échantillon non représentatif** | | |
| Narrow sample, universal claim | **Échantillon étroit, portée universelle** | | *WEIRD* non nommé, comme en anglais. |
| Simpson's paradox | **Paradoxe de Simpson** | usage courant | *pooled* → **agrégé** (données agrégées, taux agrégé). |
| Small numbers, wild swings | **Petits effectifs, grands écarts** | | « Effectif » = taille de groupe (illustration EFFECTIF →). |
| Base-rate neglect | **Négligence du taux de base** | [4] | Wikipédia en français titre « Oubli de la fréquence de base » [4] ; « négligence du taux de base » est la forme de la psychologie cognitive (proposée par le relecteur). Premier jet : « Oubli du taux de base ». |
| Transposed conditional | **Conditionnelle inversée** | [5] | Le cas juridique s'appelle « sophisme du procureur » [5], mais la carte couvre aussi la lecture de la valeur p. Voir questions ouvertes. |
| No significance, no effect | **Pas significatif, pas d'effet** | | |
| Significant but trivial | **Significatif mais négligeable** | | |
| Relative risk alone | **Risque relatif seul** | [1] | *risk ratio* (Amrhein) → « risque relatif ». |
| Distorted chart | **Graphique trompeur** | | |
| Many tests, one hit | **Tests multiples, un seul succès** | | *hit* → **succès** partout (illustrations 32 TESTS, 1 SUCCÈS ; 1 SUCCÈS SUR 480 TESTS). |
| Subgroup surprise | **Sous-groupe surprise** | [1] (*analyse en sous-groupes*) | |
| File drawer | **Effet tiroir** | [6] | Terme attesté pour *file drawer effect* [6] ; Methodical nomme la carte « Biais de publication » et dit « dans le tiroir ». Les noms anglais diffèrent aussi entre les deux jeux. |
| One study, settled | **Une étude, affaire classée** | | |
| Survival-time illusion | **Illusion de survie** | [7] | Les textes emploient le terme établi : « avance au diagnostic » (*lead time*) [7] et « surdiagnostic ». |
| Changed yardstick | **Changement d'étalon** | | Voir questions ouvertes. |

## Cartes Vérification

| Anglais | Français | Source | Note |
|---|---|---|---|
| Ask for the denominator | Demander le dénominateur | | *natural frequencies* → fréquences naturelles. |
| Compared with what? | Comparé à quoi ? | | |
| Draw the causal diagram | Dessiner le diagramme causal | [3] | *back doors* → **chemins détournés** (voir questions ouvertes). |
| Check the timeline | Vérifier la chronologie | | |
| Plot it over time | Tracer la série dans le temps | | |
| Split by subgroup | Ventiler par sous-groupe | usage courant (statistique publique) | |
| Ask for individual data | Demander les données individuelles | | |
| Find who's missing | Chercher qui manque | | |
| Check who and what was studied | Vérifier qui et quoi on a étudié | | Premier jet « Vérifier ce qui a été étudié » ; le relecteur a demandé de garder « qui ». |
| Find the preregistration | Trouver le préenregistrement | | |
| Look for the other studies | Chercher les autres études | | |
| Read the confidence interval | Lire l'intervalle de confiance | [1] | « IC à 95 % ». |
| Ask how big | Demander la taille de l'effet | [1] | Cochrane France : *effect size* = « taille de l'effet » ; *number needed to treat* = « nombre de sujets à traiter » ; *funnel plot* = « graphique en entonnoir ». |
| Ask what was measured | Demander ce qui a été mesuré | | |
| Test it on new data | Tester sur des données neuves | Methodical | |
| Read the axes | Lire les axes | | |

## Autres choix

| Anglais | Français | Note |
|---|---|---|
| precision / accurate (détecteur) | **performant**, **fiable** (« FIABLE À 99 % ») | « Précision » désigne en français la valeur prédictive positive : faux ami corrigé en relecture (C23, C34). |
| consistency (Bradford Hill) | **constance** | « Cohérence » est un autre critère de Hill (relecture, C57). |
| filled a prescription | **délivrance** (de statine) | Terme de la pharmaco-épidémiologie française (relecture, C08). |
| ICU | **réanimation**, « % EN RÉA » | Usage de France ; voir questions ouvertes (Belgique). |
| case mix | **patientèles différentes** | « Case-mix » est aussi courant à l'hôpital. |
| crime (comptage) | **infractions** ; « crimes de haine » gardé comme expression consacrée | En droit français, « crime » ne désigne que les infractions les plus graves (C44, C45). |
| victim surveys | **enquêtes de victimation** | Terme de la statistique publique française. |
| laptop | **ordinateur (portable)** | « Portable » seul désigne un téléphone en France (relecture, C12). |
| back-test | **backtest** | Usage de la finance. |
| billion km | **MD KM** (milliard) | Abréviation française « Md ». |
| SD | **ÉT** (écart-type) | |
| THE DAILY CLAIM (journal fictif) | **LA GAZETTE DU JOUR** | |

## Limites connues

- Les nombres dessinés à partir des données dans les graphiques des cartes Affirmation (valeurs des barres comme 7.4, 3.00) sont formatés par `tools/art_claims.py` avec un point décimal ; ils ne passent pas par la traduction. Les étiquettes traduites, elles, utilisent la virgule (p = 0,01).
- Dans l'application et l'impression, certaines ponctuations viennent du code commun (deux-points après un nom de carte dans le corrigé, « 1 pages ») et ne suivent pas la typographie française.

## Relecture indépendante

Un relecteur méthodologiste francophone indépendant (sous-agent sans accès au raisonnement du traducteur) a relu les fichiers anglais et français et le glossaire de Methodical. Il a vérifié mécaniquement l'encodage, les espaces insécables, les virgules décimales et les séparateurs de milliers, ainsi que, à la main, que tous les noms, nombres et années des affirmations et des cas réels correspondent à l'anglais. Aucun fait n'avait été modifié.

Corrections appliquées : « portable » → « ordinateur » (C12) ; faux ami « précision » (C23, C34) ; « cohérence » → « constance » (C57) ; tournures de C24, C37, C38, C25, C55 ; « ignorer » → « négliger » (taux de base, C23) ; « une conclusion causale / un effet causal » (C46, C11) ; accord « l'un » (tiers facteur caché) ; « critères » non limités au diagnostic (changement d'étalon) ; exemple du graphique trompeur raccourci ; « délivrance » (C08) ; « Seniors néerlandais » (C54) ; étiquettes raccourcies (GAIN (ÉT), 1 SUCCÈS SUR N TESTS, MD KM) ; « infractions » (C44, C45) ; « Vérifier qui et quoi on a étudié » ; « comptez les points », « Posez-en un », « un jeu du SMART-Lab » ; « pêche aux résultats », « sensibilisation », « Faire monter un marqueur », « presque certainement » ; « critère final » (substitution, Demander ce qui a été mesuré) ; noms « Négligence du taux de base » et « Biais du temps immortel ».

Désaccords :

- **« Non listé » → « hors corrigé »** : refusé pour garder le terme de Methodical dans tout le kit ; à trancher pour les deux jeux à la fois.
- **Critère de substitution** : le relecteur proposait « critère clinique » ; refusé parce que la carte couvre aussi des scores de tests et des clics. Retenu : « critère final ».
- **« Tiers facteur caché » → « Facteur tiers caché »** : refusé pour rester aligné sur le texte de Methodical ; laissé en question ouverte.
- **EFFECTIF →** : le relecteur demandait de vérifier ; l'illustration est celle de « Petits effectifs, grands écarts » (axe = taille du groupe), donc « effectif » est juste.

## Sources

1. Cochrane France, Lexique bilingue (*effect size* = taille de l'effet ; *number needed to treat* = nombre de sujets à traiter ; *funnel plot* = graphique en entonnoir ; *confidence interval* = intervalle de confiance ; *surrogate endpoint* = critère de substitution ; *subgroup analysis* = analyse en sous-groupes ; *relative risk* = risque relatif ; *outcome* = critère de jugement ; *control group* = groupe témoin). Consulté le 31 octobre 2026. https://france.cochrane.org/node/146
2. Université de Nantes, cours sur les biais (sélection, classement, confusion), source [19] du glossaire de Methodical. https://madoc.univ-nantes.fr/mod/resource/view.php?id=235890
3. Lanoy E., webinaire QuanTIM (SESSTIM / AP-HP), DAG et biais de collision, octobre 2024, source [23] du glossaire de Methodical. https://sesstim.univ-amu.fr/sites/default/files/2024-10/webinar-quantim-oct-24-lanoy.pdf
4. Wikipédia, « Oubli de la fréquence de base » (page consultée le 31 octobre 2026). https://fr.wikipedia.org/wiki/Oubli_de_la_fr%C3%A9quence_de_base
5. IREMI, Université de La Réunion, document de cours sur le sophisme du procureur et le théorème de Bayes. https://iremi.univ-reunion.fr/IMG/pdf/lucia1.pdf
6. *Médecine/Sciences* (2022), « un biais de publication, appelé également "effet tiroir" » (repéré par recherche ; texte intégral non accessible lors de la vérification). https://www.medecinesciences.org/en/articles/medsci/pdf/2022/04/msc200744.pdf ; *Bulletin des bibliothèques de France*, « file drawer effect ». https://bbf.enssib.fr/consulter/BBF-2020_contribution-062.pdf
7. « Biais d'avance au diagnostic » : Journées de statistique 2024 (SFdS) https://jds2024.sciencesconf.org/530813/document ; *La Revue du Praticien*, « Surdiagnostic des cancers : un risque réel souvent mal compris » https://www.larevuedupraticien.fr/article/surdiagnostic-des-cancers-un-risque-reel-souvent-mal-compris

## Questions ouvertes pour un relecteur natif

- **Négligence du taux de base** ou **Oubli de la fréquence de base** (Wikipédia) ?
- **Conditionnelle inversée** : nom non consacré. Alternatives : « Inversion des conditionnelles », « Sophisme du procureur » (connu mais plus étroit que le cas de la valeur p).
- **Changement d'étalon** : compréhensible mais peu idiomatique. Alternatives : « Changement de définition », « Changement de thermomètre ».
- **Effet tiroir** (Red Flag) et **Biais de publication** (Methodical) : le kit tolère-t-il deux noms quand les noms anglais diffèrent ?
- **Tiers facteur caché** ou **Facteur tiers caché** (plus courant) ? À changer dans les deux jeux à la fois.
- **Chemins détournés** pour *back-door paths*, ou « chemins de porte dérobée » / « chemins arrière » ?
- **Types de cartes** : Affirmation, Drapeau, Vérification ; « Geste » ou « Coup » pour *Move* ?
- **Bancale** (familier) ou « fragile » / « viciée » ? **Calibré, pas cynique** ou « Mesuré, pas cynique » ?
- **Non listé** ou **hors corrigé** (pour tout le kit) ?
- **Réanimation** (France) ou **soins intensifs** (Belgique) ?
- **Patientèles différentes** ou **case-mix** (C17) ?
- **IC à 95 % −0,2 à 3,2** ou la forme des revues françaises **IC 95 % [−0,2 ; 3,2]** : choix de style pour tout le kit.
