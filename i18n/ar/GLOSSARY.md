# Arabic glossary for Red Flag (مسرد المصطلحات العربية)

This glossary explains the term choices in the Arabic edition of Red Flag (`i18n/ar/cards.json`, `i18n/ar/ui.json`)
so that a native-speaking methodologist can check or contest them. Red Flag is the second game of the SMART-Lab
Science Game Kit; its Arabic follows the decisions already made and reviewed for Methodical
(`methodical-card-game/i18n/ar/GLOSSARY.md`), so a concept has the same Arabic term in both games.

Principles (as in Methodical):

- **The term Arabic scientific writing actually uses**, with WHO EMRO usage (Unified Medical Dictionary, EMHJ)
  first for medicine and epidemiology, and Arabic textbooks and theses for statistics and social science.
- **The most widely understood form** where regions differ; alternatives are listed in the notes.
- **One concept, one term** across card names, card text, explanations, trap reasons, interface strings and the
  labels drawn in pictures.
- Modern Standard Arabic, Arabic punctuation (، ؛ ؟) and «guillemets», Western digits with a comma as thousands
  separator (1,000), as in Methodical. Author, study, journal and organisation names stay in Latin script
  (Matthews, WHI, Literary Digest, Harvard, Berkeley, FDA); place names are written in Arabic (أوهايو، الدنمارك، كوريا الجنوبية); Berkeley stays
  in Latin script because the case is about the university. Statistical symbols stay Latin (p، r، d، C، HR، N).
- Where Arabic-speaking researchers often keep the English term, the English is given once in parentheses, as in
  Methodical: (p-hacking)، (back-test)، (ADHD)، (NNT).

"Usage" in the source column marks a choice based on common usage in Arabic textbooks and articles for which no
authoritative online source was checked. "[M]" means the term is taken over unchanged from Methodical's reviewed
Arabic glossary. Numbers in brackets refer to the sources at the end.

## The game's own vocabulary

| English | Arabic used | Source | Note |
|---|---|---|---|
| Claim (card, deck) | **ادعاء / الادعاءات** | usage | The neutral word for an asserted conclusion. |
| Flag (card, deck); to flag | **راية / الرايات; ارفع راية** | usage | Keeps the game's metaphor (raising a flag). The game name *Red Flag* stays in Latin script, as *Methodical* does. |
| Check (card, deck) | **فحص / الفحوص** | [M] usage | Methodical: فحص الاتجاه المسبق. Because فحص is the card type, medical *screening* is never فحص (see below). |
| Sound (claim, card) | **سليم; ادعاء سليم; بطاقة «سليم»** | usage | "Call it sound" → احكم بأنه سليم / احكم بسلامته. |
| Flawed | **معيب** | usage | Card back: «معيب أم سليم؟». |
| Call (a decision at the table) | **حكم** | usage | "Best call" → أفضل حكم. |
| Reasoning error | **خطأ استدلالي** | usage | |
| False alarm | **إنذار كاذب** | usage | Same word family as الإيجابيات الكاذبة (false positives). |
| Calibrated (scepticism) | **متوازن; التشكك المتوازن** | usage | Metaphorical sense. Kept apart from المعايرة, which Methodical uses for the *statistical* calibration of prediction models. Card footer: «متوازن، لا مرتاب» (calibrated, not cynical). |
| Best / defensible / trap / unlisted; appeal | **الأفضل / يمكن الدفاع عنه / فخ / غير مدرج; اعتراض** | [M] | |
| Families: Cause / Sample / Numbers / Practice | **السببية / العينة / الأرقام / الممارسة** | [M] usage | السببية matches Methodical's CAUSE suit. |
| Move (what a Check is) | **خطوة** | usage | |
| Exposed by / exposes | **يكشفها / يكشف** | usage | |

## Cross-cutting decisions (shared with Methodical unless stated)

| English | Arabic used | Source | Note |
|---|---|---|---|
| exposure; outcome | **التعرض; الحصيلة (الحصائل)** | [M] | النتيجة is kept for *result, finding*, as in Methodical. |
| confounding; confounder | **الإرباك; العامل المُربِك** | [M] | Card name keeps the English metaphor: «عامل ثالث خفي». |
| bias | **التحيز** | [M] | |
| randomized; randomized trial | **بالتوزيع العشوائي; تجربة معشاة** | [M] | معشّاة only inside the fixed trial name, as in Methodical. |
| control group | **المجموعة الضابطة** | [M] | Bar label CONTROL → «الضابطة». |
| placebo | **دواء وهمي** | [M] | |
| preregistration; preregistered | **التسجيل المسبق; مسجَّل مسبقًا** | [M] | |
| statistically significant; not significant | **دالّ إحصائيًا; غير دالّ** | [M] | A significant result = «نتيجة دالّة»; a "hit" among many tests is also «نتيجة دالّة» (cards, art labels). |
| p-value | **قيمة p** | [M] | |
| effect size | **حجم الأثر** | [M] | |
| evidence | **البيّنات** | [M] | Also «دليل» where the sense is a single piece of evidence (DNA match, "absence of evidence"). |
| observational (studies) | **رصدية** | [M] | |
| population (who the claim is about) / (sampling frame) | **السكان / المجتمع الإحصائي** | [M] | |
| regression to the mean | **الانحدار نحو المتوسط** | [M] | |
| reverse causation | **السببية العكسية** | [M] | |
| collider; collider bias | **المُصادِم; تحيز المُصادِم** | [M] | Not found in an authoritative Arabic source (as noted in Methodical). |
| immortal time | **الزمن الخالد** | [M] | Card name drops تحيز, like the English. |
| ecological fallacy | **المغالطة الإيكولوجية** | [M] [4] | Arabic Wikipedia: مغالطة بيئية; بيئية is avoided because it also means "environmental". |
| survivorship bias | **تحيز النجاة** | [M] | |
| publication bias | **تحيز النشر** | [M] [4] | Card name «درج الملفات» (file drawer); the text names تحيز النشر. |
| forking paths; p-hacking | **المسارات المتشعبة; (p-hacking)** | [M] | |
| overfitting | **فرط الملاءمة** | [M] [4] | Fit / fitted → ملاءمة / مُلاءَمة على. |
| multiplicity correction | **تصحيح تعدد الاختبارات** | [M] | |
| replication | **التكرار; دراسة تكرار** | [M] | |
| external validation | **التحقق الخارجي** | [M] | |
| discrimination (of a model) | **القدرة التمييزية** | [M] | |
| causal diagram | **المخطط السببي** | [M] | Back door → الباب الخلفي. |
| adjust for | **التعديل لـ** | [M] | |
| covariates | **المتغيرات المصاحبة** | usage | |
| subgroup; interaction test | **مجموعة فرعية; اختبار التفاعل** | usage | |
| meta-analysis; systematic review | **تحليل تلوي; مراجعة منهجية** | [M] | |
| funnel plot | **مخطط القمع** | usage | No Arabic Wikipedia article found [4]. |

## New terms in Red Flag

| English | Arabic used | Source | Note |
|---|---|---|---|
| correlation as causation | **الارتباط بوصفه سببية** | [4] usage | Arabic Wikipedia's article is «الارتباط لا يقتضي السببية». |
| association | **ارتباط** | usage | |
| shared trend; spurious correlation of time series | **اتجاهان وساعة واحدة** (name); **الاتجاهات الزمنية** | [M] usage | Arabic Wikipedia for *spurious relationship*: علاقة زائفة [4]. |
| extrapolation | **ما وراء البيانات** (name) | [4] | The technical term is الاستكمال الخارجي [4]; the card keeps the English card's plain-words name. |
| model-to-human leap | **من الفئران إلى البشر** | usage | |
| unrepresentative sample; self-selected | **عينة غير ممثِّلة; مختارة ذاتيًا** | [M] usage | Methodical: معاينة ممثِّلة. |
| narrow sample, universal claim (WEIRD) | **عينة ضيقة، ادعاء كلّي** | [M] | Methodical: universal → كلّي. |
| Simpson's paradox | **مفارقة Simpson** | [4] | Name in Latin script per the kit rule; Arabic Wikipedia writes مفارقة سمبسون. |
| pooled (data) | **مدموجة / المدموج** | [M] | Methodical: pool → دمج. |
| small numbers, wild swings | **أعداد صغيرة، تقلبات كبيرة** | usage | |
| base rate; base-rate neglect | **المعدل الأساسي; إغفال المعدل الأساسي** | [4] usage | Arabic Wikipedia: «مغالطة معدل الأساس». المعدل الأساسي reads more naturally in running text. |
| natural frequencies | **التكرارات الطبيعية** | usage | |
| true / false positives | **إيجابية حقيقية / كاذبة** | usage | |
| transposed conditional | **قلب الاحتمال الشرطي** | usage | The English *P(D | H)* notation is kept in pictures; card text says it in words. |
| no significance, no effect | **غير دالّ، إذن لا أثر** | usage | "Absence of evidence…" → «غياب الدليل ليس دليلًا على الغياب». |
| significant but trivial | **دالّ لكنه تافه** | usage | |
| relative risk; absolute risk; risk ratio | **الخطر النسبي; الخطر المطلق; نسبة الخطر** | usage | UMD-style alternative: الاختطار النسبي. Methodical already uses خطر (عوامل الخطر). |
| percentage points | **نقاط مئوية** | usage | |
| confidence interval | **فترة الثقة** | [M] | Arabic Wikipedia: مجال ثقة [4]; also فاصل الثقة. Methodical's فترة is kept for the kit. |
| distorted chart; axis; scale | **رسم بياني مشوَّه; محور; مقياس** | usage | Cropped axis → محور مقتطع. |
| predictors | **المتنبئات** | usage | |
| many tests, one hit | **اختبارات كثيرة، نتيجة واحدة** | usage | |
| true null hypothesis | **فرضية صفرية صحيحة** | usage | |
| subgroup surprise | **مفاجأة المجموعة الفرعية** | usage | |
| one study, settled | **دراسة واحدة حسمت الأمر** | usage | |
| surrogate endpoint; marker | **نقطة نهاية بديلة; مؤشر** | [4] | Arabic Wikipedia: «نقطة النهاية البديلة». مؤشر for the measured marker (blood value, score); Methodical uses مؤشر بديل for a proxy. |
| screening; screened | **الكشف المبكر; خضعوا للكشف** | usage | فحص is taken by the Check cards, so screening is الكشف المبكر (common in Arab public-health campaigns). UMD-style alternative: التحرّي. Short chart labels: «مع الكشف / بلا كشف». |
| survival; five-year survival | **البقاء; البقاء لخمس سنوات** | usage | UMD-style alternative: البُقيا. |
| lead time; overdiagnosis | **زمن الاستباق; فرط التشخيص** | usage | The card name is «وهم مدة البقاء» (survival-time illusion), as in English. No authoritative Arabic form of *lead-time bias* was found. |
| mortality / deaths | **الوفيات** | usage | |
| changed yardstick | **تغيّر المعيار** | usage | |
| denominator | **المقام** | usage | |
| number needed to treat | **العدد اللازم علاجه (NNT)** | usage | |
| held-out data | **بيانات محجوبة** | usage | |
| back-test | **الاختبار الرجعي (back-test)** | usage | |
| C-statistic | **إحصائية C** | usage | |
| standard deviation | **انحراف معياري** | usage | |
| interaction | **تفاعل** | usage | |
| voxel | **فوكسل** | usage | |
| wellbeing | **الرفاه** | usage | |

## Units, numbers and right-to-left display

- Units in Arabic: ملغ، مم زئبق، ملغ/دسل، كم. Months: مايو، يونيو، يوليو، مارس (as Methodical's يونيو).
- Percentages are written in logical order ("90%"). Inside Arabic sentences the browser displays them in the
  established Arabic way, with the percent sign on the left of the digits (read after the number); this was
  measured in headless Chrome and is left as it is.
- **Signed numbers** (+3، −2، −0.2، +0.2) get an invisible left-to-right mark (U+200E, written `\u200e` in the
  JSON) before the sign. Without it, a sign after an Arabic word is displayed on the wrong side ("2−"); measured
  before and after in headless Chrome. The same mark ends the reference-card labels «الأفضل» «يمكن الدفاع عنه»
  «فخ», because the code prints the score (+3, −2) right after them.
- **Short formulas** (p = 0.01، r ≈ 0.62، C = 0.78، HR 1.29) use no-break spaces (`\u00a0`) so they are never split
  across lines; a split formula was found on two cards (C04, C38) and displayed out of order.
- **Picture labels.** Card pictures are drawn left to right (`direction: ltr` on the SVG, the fix Methodical made
  in commit 0001e1c so labels stay anchored in their frames). In a left-to-right drawing, a label that mixes Arabic
  with digits or Latin letters is displayed in the wrong order (for example "1 من 1,000,000" or "المستشفى B").
  Every such label is therefore wrapped in a right-to-left isolate (U+2067 … U+2069, `\u2067…\u2069`), which was
  checked character by character in headless Chrome. Pure-Arabic labels need no marks. Axis labels with a unit
  follow the kit's "Quantity (unit)" form: «الناجون (%)», «البطالة (%)».
- Year ranges keep the en dash ("2008–12"); inside Arabic text they read right to left.

## Per-card notes

- **C08** chart legend uses the singular «مستخدم / غير مستخدم» and the axis «أحياء (%)», so they do not collide.
- **C17** was rephrased («ينجو 90% … في المستشفى A، و85% في المستشفى B») so that no Latin letter is followed by a
  colon and a number, which displayed confusingly in Arabic.
- **C19** "coaching scheme" → «برنامج دعم» (school support); **C51** "coaching" → «برنامج توجيه صحي».
- **C37** migraine → «الصداع النصفي» (the common term; UMD: الشقيقة).
- **C43** ADHD → «اضطراب نقص الانتباه وفرط النشاط (ADHD)»; the title shortens it to «فرط النشاط».
- **C48** bowel cancer → «سرطان القولون والمستقيم».
- **Flag examples** keep every name, number and date of the English; names of people, studies and organisations stay
  in Latin script. Oscar winners → «الفائزون بجوائز الأوسكار»; the Beatles → «فرقة Beatles».

## Review

An independent reviewer pass (an Arabic-speaking methodologist role, given only the English source, the Arabic
draft and Methodical's glossary, 31 October 2026) checked every string. All numbers, names and dates in claims and
in the real cases on Flag cards matched the English. Changes made from the review:

- Meaning: C55 «المنطقتان» (dual) contradicted «مناطق» → «المنطقة ومناطق المقارنة»; C44 «تضاعفت أربع مرات» could
  read as ×16 → «إلى أربعة أمثالها»; C43 «ثابت» (flat) → «مطّرد» (steady) and «الحالة» → «الاضطراب»; 1995 pill
  scare «إجهاض» (also miscarriage) → «إجهاض مُتعمَّد»; C59 0.2 SD is "substantial", not «كبير» → «أثر ذو شأن»;
  C04 and the shared-trend flag «مهما كان ما يربطهما» presupposed a link → «سواء جمعتهما صلة أم لا».
- Hints and terms: C03 «مسح مستعرض» added a technical hint the English lacks → «مسح أُجري مرة واحدة»; «لجان
  الاستطلاع» (committees) → «المستجيبون عبر المنصات الإلكترونية»; C42 «معدل البقاء»; C39 «حاصل الذكاء (IQ)»;
  C15 «وسيلة إعلامية»; C30 «عنوان صحفي»; C46 «نقطة مئوية» and «إصابة»; C41 unit «ملغ/دل»; funnel-plot axis
  PRECISION → «دقة التقدير» (so «الدقة» stays for accuracy, C23); C21 «المعدل الوطني»; THEN → «لاحقًا».
- Grammar and style: C34 agreement «200 متغيرٍ مُلاءَمٍ لـ150 حالة»; «مُلاءَمة على» → «مُلاءَمة لـ» (C35);
  survivorship short «الحالات التي نجت»; Galton «الوالدين» (mid-parent, not fathers); small-sample flag text;
  C05, C01, C02, C18 phrasing; «تنجرفان» → «تتجهان»; «ليتنبؤوا»; «انقر لقلب البطاقة» («للقلب» read as "for the
  heart"); footer «مُعدّة» (not «مصنوعة», "fabricated") and «القرّاء المنصفين» ("reasonable readers").
- Consistency: a "hit" is «نتيجة دالّة» everywhere: art label «32 اختبارًا، نتيجة دالّة واحدة», flag name
  «اختبارات كثيرة، دالّة واحدة» (shortened so the name keeps a readable size). The lead-time flag now names
  «زمن الاستباق» and «فرط التشخيص» once, since traps use these terms.

Not taken over, with reasons:

- *Add LRM in «r ≈ −0.53»*: not needed; the Latin "r" before the number keeps the sign in place, measured in
  headless Chrome (no misplaced sign on any card).
- *«p < 0.001» renders mirrored*: measured, it does not; a Latin letter starts the expression, so the whole formula
  runs left to right. No-break spaces keep each formula on one line.
- *«ضبط» instead of «تعديل» for "adjust for"*: Methodical's card text uses «عدّل للعوامل المربكة», so the kit keeps
  تعديل; ضبط is listed as an open question.
- *«(التلاعب بقيمة p)» instead of «(p-hacking)»*: Methodical's forking-paths card itself ends with «(p-hacking)»;
  kept for kit consistency. «(تحيز النشر)» on the file-drawer card is kept as the matching gloss.
- *«المستخدمون / غير المستخدمين» on the C08 chart*: the plural legend ran into the axis label; the singular fits.
- *«ملم زئبقي»*: «مم» follows Methodical's unit abbreviation; kept as «مم زئبق».
- *C47 «يفتح الدرج»*: reverses the English image ("closes the file drawer") but says the same thing in Arabic:
  searching registries opens the drawer and brings the hidden results out. Kept.
- *Confidence interval*: the reviewer thought Methodical never names it; its cards use «فترات ثقة», so «فترة الثقة»
  is the kit's term (alternatives remain open below).

## Still open (for a native methodologist)

1. **Screening**: الكشف المبكر (chosen) or التحرّي (UMD-style)? فحص is excluded because it names the Check cards.
2. **Relative risk**: الخطر النسبي (chosen) or الاختطار النسبي (UMD-style)?
3. **Confidence interval**: فترة الثقة (kit choice, from Methodical) versus مجال الثقة (Arabic Wikipedia) or فاصل الثقة.
4. **Base-rate neglect**: إغفال المعدل الأساسي versus Arabic Wikipedia's مغالطة معدل الأساس.
5. **Lead time**: زمن الاستباق has no authoritative source; زمن التقدّم is also seen.
6. **Signed numbers**: this edition shows "−0.2" and "+3" with the sign on the left, as in mathematics with Western
   digits. Some Arabic typesetting puts the sign on the right; a native reader should confirm.
7. **Adjust for**: «التعديل لـ» (kit, from Methodical's cards) or «ضبط» (common in Arabic papers)?
8. **Wellbeing** (C29): «الرفاه» may read as economic welfare; «العافية» or «الرفاه النفسي» are alternatives.
9. **Common effect** (collider): «الأثر المشترك» shares أثر with "effect"; no better form was found.
10. **Marker**: «مؤشر» (chosen) versus UMD-style «واسم (حيوي)» for biomarkers.
11. **Survival vs survive**: البقاء for survival time and rates, النجاة/الناجون for surviving (C17, survivorship
    bias). Deliberate, but a reader should confirm it does not confuse.
12. **Card metaphors** (راية، «اتجاهان وساعة واحدة»، «درج الملفات»، «متوازن، لا مرتاب»): do they read naturally?

## Sources

1. Methodical's reviewed Arabic glossary, `methodical-card-game/i18n/ar/GLOSSARY.md` (its sources 1–9: WHO EMRO EMHJ,
   UMD, World Bank Arabic impact-evaluation slides, Arabic Wikipedia, WIPO, and others).
2. WHO EMRO, Unified Medical Dictionary (المعجم الطبي الموحد). https://umd.emro.who.int/WHODictionary/ (not
   re-queried for this edition).
3. Methodical commit 0001e1c, "Translations reviewed term by term; Arabic picture labels fixed" (SVG `direction: ltr`).
4. Arabic Wikipedia article titles, retrieved 31 October 2026 through the English Wikipedia API (langlinks):
   مفارقة سمبسون، مغالطة معدل الأساس، مجال ثقة، نقطة النهاية البديلة، استكمال خارجي، فرط الملاءمة، تحيز النشر،
   مغالطة بيئية، الارتباط لا يقتضي السببية، علاقة زائفة. No Arabic article was found for regression to the mean,
   survivorship bias, lead-time bias, overdiagnosis, funnel plot, number needed to treat, relative risk, collider
   bias or medical screening. Used as evidence of usage, not as an authority.
5. Unicode Bidirectional Algorithm (UAX #9) behaviour as measured in headless Chrome on the built pages,
   31 October 2026 (signs, percentages, isolates).
