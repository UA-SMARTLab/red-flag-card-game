# Red Flag: answer key

Generated from `data/` by `tools/build.py`. Don't edit by hand.

Scoring: 🥇 best +3 · 🥈 defensible +1 · ⚠️ trap -2 · unlisted 0 (or +1 on a successful appeal) · matching Check card +1. On a sound claim every flag is a trap; on a flawed claim, calling it sound is a trap.

## C01 · Chocolate for genius (Nutrition, ★)

> Countries that eat more chocolate per person win more Nobel prizes per person. Chocolate boosts brain power, so eat more of it.

- 🥇 **Best:** Correlation as causation
- 🥈 **Defensible:** Ecological fallacy, Hidden third factor
- ⚠️ **Trap, Two trends, one clock:** These are countries compared at one time, not two series drifting over the years.
- ⚠️ **Trap, Small numbers, wild swings:** The problem isn't the number of countries; even with 200 the link would not show cause.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

A country-level correlation is stretched into a causal claim about individual brains. Wealth could drive both, and the data say nothing about whether the laureates ate chocolate.

*Check:* **Draw the causal diagram**

## C02 · Breakfast and grades (Education, ★)

> Pupils who eat breakfast every day get better grades than pupils who skip it. Schools should serve breakfast to raise grades.

- 🥇 **Best:** Hidden third factor
- 🥈 **Defensible:** Correlation as causation
- ⚠️ **Trap, Reverse causation:** Good grades are unlikely to make children eat breakfast; the stronger worry is a common cause.
- ⚠️ **Trap, Ecological fallacy:** The data are about individual pupils, not school averages.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Family routine, income and parental time plausibly drive both breakfast and grades. A trial of school breakfasts would test the policy itself.

*Check:* **Draw the causal diagram**

## C03 · Lazy and low (Psychology, ★★)

> In a one-off survey of 5,000 adults, the least active people were the most depressed. Inactivity causes depression.

- 🥇 **Best:** Reverse causation
- 🥈 **Defensible:** Hidden third factor, Correlation as causation
- ⚠️ **Trap, Ecological fallacy:** Each point is a person; the link is measured at the individual level.
- ⚠️ **Trap, Small numbers, wild swings:** 5,000 people is plenty to estimate the association; the issue is its direction.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Depression saps energy and motivation, so low activity may be a symptom rather than a cause. A snapshot can't tell which came first.

*Check:* **Check the timeline**

## C04 · Phones and myopia (Public health, ★★)

> From 2000 to 2020, smartphone ownership and short-sightedness in teenagers both rose year after year (r = 0.96). Phones are ruining children's eyes.

- 🥇 **Best:** Two trends, one clock
- 🥈 **Defensible:** Correlation as causation
- ⚠️ **Trap, Regression to the mean:** Nothing was chosen for being extreme; both series climb steadily.
- ⚠️ **Trap, Small numbers, wild swings:** The flaw is not the number of years but that any two rising series correlate.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Two series that both trend upward correlate almost perfectly whatever links them. Myopia was rising before smartphones; compare changes, or individuals, instead.

*Check:* **Plot it over time**

## C05 · Smokers spared (Medicine, ★★★)

> Among patients admitted to hospital with a respiratory virus, smokers were less likely than non-smokers to need intensive care. Smoking may protect against severe disease.

- 🥇 **Best:** Collider bias
- 🥈 **Defensible:** Unrepresentative sample, Hidden third factor
- ⚠️ **Trap, Reverse causation:** Needing intensive care can't make someone a smoker before admission.
- ⚠️ **Trap, Relative risk alone:** The percentages are given; the problem is who got into the sample.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Hospital admission is caused both by smoking-related illness and by severe infection. Among the admitted, smokers are more often there for other reasons, so they look milder.

*Check:* **Draw the causal diagram**

## C06 · Height doesn't matter (Sport, ★★)

> Among professional basketball players, taller players score no more points than shorter ones. Height doesn't matter in basketball.

- 🥇 **Best:** Collider bias
- 🥈 **Defensible:** Unrepresentative sample
- ⚠️ **Trap, No significance, no effect:** The study may be precise; the issue is that everyone was selected for being good.
- ⚠️ **Trap, Ecological fallacy:** The data are on individual players.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Players reach the league by being tall or by being exceptionally skilled. Selecting on that shared outcome hides height's effect among the selected.

*Check:* **Find who's missing**

## C07 · Transplant triumph (Medicine, ★★★)

> Counting from the day they joined the waiting list, patients who got a heart transplant lived far longer than those who never did. Transplants work.

- 🥇 **Best:** Immortal time
- 🥈 **Defensible:** Hidden third factor
- ⚠️ **Trap, Regression to the mean:** Patients weren't picked for an extreme value that later fell back.
- ⚠️ **Trap, Survivorship bias:** Close, but the precise error is counting waiting time as transplant time.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

To get a transplant you had to survive the wait, and that waiting time was credited to the transplant group. Time must be split at the day of surgery.

*Check:* **Check the timeline**

## C08 · Statins and survival (Pharmacoepidemiology, ★★★)

> Patients counted as statin users if they filled a prescription within two years of diagnosis; followed from diagnosis, users had 30% lower mortality.

- 🥇 **Best:** Immortal time
- 🥈 **Defensible:** Hidden third factor
- ⚠️ **Trap, Survival-time illusion:** Diagnosis date is the same for both groups; the bias comes from how users were defined.
- ⚠️ **Trap, Relative risk alone:** Absolute survival is shown; the error is in the classification of time.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Anyone who died before filling a prescription was automatically a non-user. Users were guaranteed to survive until their first fill.

*Check:* **Check the timeline**

## C09 · App for everyone (Technology, ★)

> Our app grew from 1,000 to 64,000 users in six months by doubling every month. At this rate the whole planet will use it within two years.

- 🥇 **Best:** Beyond the data
- 🥈 **Defensible:** none
- ⚠️ **Trap, Small numbers, wild swings:** Six data points describe the past well; the error is projecting them far ahead.
- ⚠️ **Trap, Regression to the mean:** Growth wasn't selected for being extreme; it just can't stay exponential.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Exponential growth always saturates. A trend observed over six months says nothing about a range millions of times larger.

*Check:* **Check who and what was studied**

## C10 · More is better (Pharmacology, ★★)

> In a trial of doses from 10 to 40 mg, each extra 10 mg cut blood pressure by 4 mmHg. So a 100 mg dose should cut it by 40 mmHg.

- 🥇 **Best:** Beyond the data
- 🥈 **Defensible:** none
- ⚠️ **Trap, Surrogate endpoint:** Blood pressure is an accepted outcome here; the problem is the dose range.
- ⚠️ **Trap, Mice to people:** The trial was in people.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Dose-response curves usually flatten and side effects rise. Beyond 40 mg there are no data at all.

*Check:* **Check who and what was studied**

## C11 · Green tea cure (Oncology, ★)

> A compound from green tea shrank tumours in mice by 60%. Drinking green tea fights cancer.

- 🥇 **Best:** Mice to people
- 🥈 **Defensible:** Beyond the data
- ⚠️ **Trap, Significant but trivial:** A 60% shrinkage in mice is not small; the leap is from mice to people.
- ⚠️ **Trap, Correlation as causation:** The mouse study was an experiment, so cause in mice is plausible.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Mice, purified compounds and high doses are far from people drinking tea. Most such leads fail in human trials.

*Check:* **Check who and what was studied**

## C12 · Laptops lift scores (Education, ★★)

> Schools with more laptops per pupil have higher average test scores. So pupils who use laptops score higher.

- 🥇 **Best:** Ecological fallacy
- 🥈 **Defensible:** Hidden third factor, Correlation as causation
- ⚠️ **Trap, Simpson's paradox:** No subgroups are reported; the problem is jumping from schools to pupils.
- ⚠️ **Trap, Small numbers, wild swings:** The issue is the level of the data, not how many schools there are.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

A school-level link says nothing about which pupils use laptops or how they score. Richer schools may simply have both.

*Check:* **Ask for individual data**

## C13 · Drop out to win (Business, ★)

> We studied 30 of the most successful start-ups; most were founded by people who dropped out of university. Dropping out breeds success.

- 🥇 **Best:** Survivorship bias
- 🥈 **Defensible:** Unrepresentative sample, Correlation as causation
- ⚠️ **Trap, Small numbers, wild swings:** Even 3,000 winners would mislead; the failures are missing, not the numbers.
- ⚠️ **Trap, Regression to the mean:** No one was picked for an extreme value that later fell back.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Only winners were studied. Countless dropouts whose start-ups failed are invisible, so the data can't show what predicts success.

*Check:* **Find who's missing**

## C14 · Funds beat the market (Finance, ★★)

> The funds in today's database returned 9% a year on average over 15 years, beating the market's 7%. Active funds are worth their fees.

- 🥇 **Best:** Survivorship bias
- 🥈 **Defensible:** Unrepresentative sample
- ⚠️ **Trap, Regression to the mean:** Funds weren't chosen for a single extreme year; the closed ones are missing.
- ⚠️ **Trap, Significant but trivial:** Two points a year compounds to a lot; the problem is which funds are counted.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Funds that did badly closed or merged and dropped out of today's database, so the average describes survivors only.

*Check:* **Find who's missing**

## C15 · Readers back it (Labour, ★)

> An online poll of 50,000 of our readers found 72% think a four-day working week works. The public backs it.

- 🥇 **Best:** Unrepresentative sample
- 🥈 **Defensible:** none
- ⚠️ **Trap, Small numbers, wild swings:** 50,000 is a huge sample; size doesn't fix who chose to answer.
- ⚠️ **Trap, Significant but trivial:** 72% is not a small difference; the problem is who answered.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Readers of one outlet who choose to vote online are not the public. A large self-selected sample is still biased.

*Check:* **Find who's missing**

## C16 · Wired for fairness (Psychology, ★★)

> In a lab game, 120 psychology undergraduates in Ohio gave up money to keep splits fair. Humans are wired for fairness.

- 🥇 **Best:** Narrow sample, universal claim
- 🥈 **Defensible:** Unrepresentative sample
- ⚠️ **Trap, Mice to people:** The participants are people; the gap is between one group of people and all humans.
- ⚠️ **Trap, Small numbers, wild swings:** 120 can show the effect in that group; the leap is to 'humans'.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Students from one university in one country support a claim about them, not about all humans. Fairness norms in such games vary widely across societies.

*Check:* **Check who and what was studied**

## C17 · Choose hospital A (Health services, ★★)

> Hospital A: 90% of surgical patients survive. Hospital B: 85%. Hospital B takes most of the region's high-risk cases. Choose A.

- 🥇 **Best:** Simpson's paradox
- 🥈 **Defensible:** Hidden third factor
- ⚠️ **Trap, Base-rate neglect:** No test or rare condition is being interpreted here.
- ⚠️ **Trap, Distorted chart:** The axis starts at 80, but the bigger problem is comparing different case mixes.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

When one hospital treats the riskiest patients, its overall rate can be lower even if it does better within every risk group. Compare within risk groups.

*Check:* **Split by subgroup**

## C18 · Kidney stone choice (Urology, ★★★)

> Treatment X had a higher success rate than Y for small stones and for large stones. Overall, Y had the higher success rate, so Y is the better treatment.

- 🥇 **Best:** Simpson's paradox
- 🥈 **Defensible:** none
- ⚠️ **Trap, Subgroup surprise:** The split by stone size is the right analysis here, not a fishing trip.
- ⚠️ **Trap, Many tests, one hit:** Only two strata are compared, and both point the same way.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

X was used mostly on harder, large stones. Within each stone size X wins; the pooled rate mixes difficulty with treatment.

*Check:* **Split by subgroup**

## C19 · Coaching works (Education, ★★)

> The 20 schools with the worst test scores were given a coaching scheme. Next year their scores rose by 8 points. The scheme works.

- 🥇 **Best:** Regression to the mean
- 🥈 **Defensible:** none
- ⚠️ **Trap, Survivorship bias:** All 20 schools are followed; none drop out.
- ⚠️ **Trap, Correlation as causation:** Defensible in spirit, but the specific trap is choosing schools for an extreme low.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Schools picked for an unusually bad year tend to do better next year anyway. Without comparable untreated schools, the rise can't be credited to coaching.

*Check:* **Compared with what?**

## C20 · Speed cameras (Transport, ★★)

> Speed cameras were installed at the 50 sites with the most crashes last year. Crashes at those sites fell by 40% the year after.

- 🥇 **Best:** Regression to the mean
- 🥈 **Defensible:** none
- ⚠️ **Trap, Relative risk alone:** The counts per site are shown; the problem is how the sites were picked.
- ⚠️ **Trap, Unrepresentative sample:** The cameras are meant for high-crash sites; the issue is the comparison over time.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Sites chosen for a peak year would have fewer crashes next year even without cameras. Part of the 40% is regression to the mean.

*Check:* **Compared with what?**

## C21 · Cancer village (Epidemiology, ★★)

> The town with the highest rate of a rare cancer in the country has only 900 inhabitants. Something in that town must be causing it.

- 🥇 **Best:** Small numbers, wild swings
- 🥈 **Defensible:** Many tests, one hit
- ⚠️ **Trap, Ecological fallacy:** The claim is about the town itself, not about individuals inside it.
- ⚠️ **Trap, Relative risk alone:** Absolute rates are given; the issue is how unstable they are in a tiny town.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Two cases in 900 people give a rate of 220 per 100,000. Among thousands of small towns, some will top the table by chance.

*Check:* **Read the confidence interval**

## C22 · Small schools rule (Education, ★★)

> Most of the top 50 schools in the national ranking are small schools. Splitting big schools into small ones will raise results.

- 🥇 **Best:** Small numbers, wild swings
- 🥈 **Defensible:** Correlation as causation
- ⚠️ **Trap, Survivorship bias:** No schools are missing from the ranking.
- ⚠️ **Trap, Narrow sample, universal claim:** The issue isn't the kind of school sampled but how much small schools vary.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Small schools' averages swing more, so they crowd both the top and the bottom of any ranking. Look at the bottom 50 too.

*Check:* **Read the confidence interval**

## C23 · Spot the terrorist (Security, ★★)

> A new face-scanning system spots known suspects with 99% accuracy. So anyone it flags at the airport is almost certainly a suspect.

- 🥇 **Best:** Base-rate neglect
- 🥈 **Defensible:** Transposed conditional
- ⚠️ **Trap, Significant but trivial:** The accuracy is high; the trouble is how rare suspects are.
- ⚠️ **Trap, Overfitting:** Perhaps, but even a perfectly validated 99% would mislead here.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Among millions of travellers and a handful of suspects, 1% false alarms means thousands of innocent people flagged for every real suspect.

*Check:* **Ask for the denominator**

## C24 · Positive test (Screening, ★★)

> A test finds 95% of cancers and wrongly flags 5% of healthy people. One in 200 people screened has the cancer. You tested positive, so it's about 95% likely you have it.

- 🥇 **Best:** Base-rate neglect
- 🥈 **Defensible:** Transposed conditional
- ⚠️ **Trap, Survival-time illusion:** No survival figure is being interpreted.
- ⚠️ **Trap, Relative risk alone:** No relative risk is quoted.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Per 10,000 screened: 48 true positives and about 500 false ones. A positive result means roughly a 9% chance of cancer.

*Check:* **Ask for the denominator**

## C25 · One per cent chance (Psychology, ★★)

> Our experiment gave p = 0.01, so there is only a 1% chance that the effect isn't real.

- 🥇 **Best:** Transposed conditional
- 🥈 **Defensible:** none
- ⚠️ **Trap, Significant but trivial:** We don't know the effect size; the error is in reading the p-value.
- ⚠️ **Trap, No significance, no effect:** The result is significant; the misreading runs the other way.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

p is the probability of data this extreme if there were no effect, not the probability that there is no effect. That depends on prior plausibility too.

*Check:* **Ask for the denominator**

## C26 · DNA match (Forensics, ★★★)

> The suspect's DNA matches the crime scene. Only 1 in a million people would match by chance, so the chance he is innocent is 1 in a million.

- 🥇 **Best:** Transposed conditional
- 🥈 **Defensible:** Base-rate neglect
- ⚠️ **Trap, Small numbers, wild swings:** The match probability isn't unstable; it's being turned inside out.
- ⚠️ **Trap, Many tests, one hit:** Defensible only if a database was trawled; the core error is the transposed conditional.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

In a city of 5 million, about five people would match by chance. P(match | innocent) is not P(innocent | match).

*Check:* **Ask for the denominator**

## C27 · Painkiller flops (Medicine, ★★)

> In a trial of 60 patients, the new painkiller cut pain by 1.5 points on a 10-point scale (95% CI −0.2 to 3.2; not significant). The drug doesn't work.

- 🥇 **Best:** No significance, no effect
- 🥈 **Defensible:** Small numbers, wild swings
- ⚠️ **Trap, Significant but trivial:** The estimate isn't trivially small; it is uncertain.
- ⚠️ **Trap, Forking paths:** There's no sign of flexible analysis; the problem is the conclusion.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

The interval runs from no effect to a large one. A small trial that can't rule out a big benefit hasn't shown that the drug fails.

*Check:* **Read the confidence interval**

## C28 · Clicks for the win (Technology, ★)

> Across 2 million users, the new button colour raised clicks from 3.00% to 3.02% (p < 0.001). A major success for the design team.

- 🥇 **Best:** Significant but trivial
- 🥈 **Defensible:** Distorted chart
- ⚠️ **Trap, Small numbers, wild swings:** Two million users is the opposite problem.
- ⚠️ **Trap, No significance, no effect:** The result is significant; that's not the issue.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

With millions of users, a difference of 0.02 percentage points is 'significant' but hardly matters. Ask how big, in units that count.

*Check:* **Ask how big**

## C29 · Screens and sadness (Psychology, ★★★)

> In 300,000 teenagers, more screen time went with lower wellbeing (p < 0.0001). Screens are harming a generation.

- 🥇 **Best:** Significant but trivial
- 🥈 **Defensible:** Correlation as causation, Reverse causation
- ⚠️ **Trap, Small numbers, wild swings:** 300,000 is a very large sample.
- ⚠️ **Trap, Ecological fallacy:** The data are on individual teenagers.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

A tiny p-value in a huge sample can come from a correlation near zero. How much wellbeing varies with screen time matters more, and the design can't show cause.

*Check:* **Ask how big**

## C30 · Night-shift tumour (Occupational health, ★)

> Headline: night-shift work raises the risk of a rare tumour by 50%!

- 🥇 **Best:** Relative risk alone
- 🥈 **Defensible:** Correlation as causation
- ⚠️ **Trap, Significant but trivial:** Close, but you can't judge size until you know the starting risk.
- ⚠️ **Trap, Base-rate neglect:** No test result is being interpreted; ask for the absolute risk.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

50% more of a rare tumour may mean 3 cases per 100,000 instead of 2. Without the absolute numbers the headline can't be judged.

*Check:* **Ask for the denominator**

## C31 · Screening halves deaths (Screening, ★)

> Our screening programme halves your risk of dying from cancer X! (Ten-year trial.)

- 🥇 **Best:** Relative risk alone
- 🥈 **Defensible:** none
- ⚠️ **Trap, Survival-time illusion:** The trial counts deaths, not survival after diagnosis, so lead time doesn't apply.
- ⚠️ **Trap, Distorted chart:** The axis starts at zero and the bars are honest; the slogan isn't.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Halving 2 in 1,000 to 1 in 1,000 saves one person per 1,000 screened over ten years. The relative figure alone oversells it.

*Check:* **Ask how big**

## C32 · Support surges (Politics, ★)

> Support for the policy has surged since our campaign began.

- 🥇 **Best:** Distorted chart
- 🥈 **Defensible:** Significant but trivial
- ⚠️ **Trap, Regression to the mean:** Nothing was selected for an extreme value.
- ⚠️ **Trap, Correlation as causation:** Defensible, but first notice how small the change is.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

The axis starts at 48%, so a three-point change looks like a fourfold rise. Within normal polling error, support barely moved.

*Check:* **Read the axes**

## C33 · Jobs turnaround (Economics, ★★)

> Since March, unemployment has fallen every month. The new jobs policy is working.

- 🥇 **Best:** Distorted chart
- 🥈 **Defensible:** Regression to the mean, Correlation as causation
- ⚠️ **Trap, Small numbers, wild swings:** The numbers come from a large labour survey; the window is the problem.
- ⚠️ **Trap, Changed yardstick:** No change in definition is mentioned.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Five months on a cropped axis hide what came before: was March a spike? Plot the longer series and compare with places without the policy.

*Check:* **Plot it over time**

## C34 · Election oracle (Political science, ★★)

> Our model uses 200 variables and correctly called 149 of last year's 150 districts. It will predict the next election just as well.

- 🥇 **Best:** Overfitting
- 🥈 **Defensible:** Beyond the data
- ⚠️ **Trap, Base-rate neglect:** No rare condition is being tested for.
- ⚠️ **Trap, Small numbers, wild swings:** Close, but the giveaway is 200 variables fitted to 150 cases.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

With more variables than cases, a model can memorise the past. Only predictions for elections it hasn't seen show its real accuracy.

*Check:* **Test it on new data**

## C35 · Winning rule (Finance, ★★★)

> We tested 10,000 trading rules on 20 years of prices. The best one beat the market every single year in the back-test. Invest with it.

- 🥇 **Best:** Overfitting
- 🥈 **Defensible:** Many tests, one hit
- ⚠️ **Trap, Survivorship bias:** Related, but the best of 10,000 tries is the core problem.
- ⚠️ **Trap, Regression to the mean:** Expect future returns to fall back, but name the cause: the rule was fitted to noise.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

The best of 10,000 rules fitted to the same history will look brilliant by chance. Test it on later data it was never tuned on.

*Check:* **Test it on new data**

## C36 · Warm cup, warm heart (Psychology, ★★)

> After excluding outliers and adjusting for age and mood, participants who held a warm cup rated a stranger as friendlier (p = 0.048).

- 🥇 **Best:** Forking paths
- 🥈 **Defensible:** One study, settled
- ⚠️ **Trap, No significance, no effect:** The result is (just) significant; the worry is how it got there.
- ⚠️ **Trap, Significant but trivial:** We don't know the effect size; the analysis choices are the red flag.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Outlier rules and covariates chosen after seeing the data, and a p-value just under 0.05, suggest a forking path. Was this analysis preregistered?

*Check:* **Find the preregistration**

## C37 · Tomatoes and migraine (Nutrition, ★★)

> We tested 40 foods against 12 diseases. Eating tomatoes was linked to fewer migraines (p = 0.03).

- 🥇 **Best:** Many tests, one hit
- 🥈 **Defensible:** Forking paths, Correlation as causation
- ⚠️ **Trap, Small numbers, wild swings:** The sample size isn't given; 480 tests is the problem.
- ⚠️ **Trap, Significant but trivial:** We don't know the size; the hit itself may be noise.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

480 tests at p < 0.05 would give about 24 'hits' if nothing were real. One of them is not news.

*Check:* **Find the preregistration**

## C38 · Women over 65 (Medicine, ★★)

> Overall, the drug did not prevent strokes. But in women over 65 it cut strokes by 40% (p = 0.02). It should be approved for them.

- 🥇 **Best:** Subgroup surprise
- 🥈 **Defensible:** Many tests, one hit
- ⚠️ **Trap, Simpson's paradox:** The overall and subgroup results don't reverse; one slice stands out.
- ⚠️ **Trap, Narrow sample, universal claim:** The subgroup is chosen after the fact; that's the issue, not the sample's breadth.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Was this subgroup planned, and does it pass an interaction test? A lone subgroup effect in a null trial is usually chance.

*Check:* **Find the preregistration**

## C39 · Brain games (Cognitive science, ★★)

> A meta-analysis of 25 published studies concludes that brain-training games raise IQ by 5 points.

- 🥇 **Best:** File drawer
- 🥈 **Defensible:** Surrogate endpoint
- ⚠️ **Trap, One study, settled:** It pools 25 studies; the question is which studies got published.
- ⚠️ **Trap, Small numbers, wild swings:** Small studies may be the symptom; the missing ones are the cause.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

If studies that found nothing stayed in the file drawer, pooling the published ones overstates the effect. Check registries and funnel plots.

*Check:* **Look for the other studies**

## C40 · Stand to remember (Education, ★)

> A new study of 40 students found that standing while studying improves memory by 20%. Schools should buy standing desks.

- 🥇 **Best:** One study, settled
- 🥈 **Defensible:** Small numbers, wild swings
- ⚠️ **Trap, File drawer:** Only one study is cited; there's nothing yet to be biased.
- ⚠️ **Trap, Mice to people:** The participants were people.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

One small, new study is a lead, not a basis for policy. Wait for replications.

*Check:* **Look for the other studies**

## C41 · Good cholesterol (Cardiology, ★★)

> Our drug raised 'good' HDL cholesterol by 70% in a large trial. It will prevent heart attacks.

- 🥇 **Best:** Surrogate endpoint
- 🥈 **Defensible:** none
- ⚠️ **Trap, Relative risk alone:** The 70% is a change in a blood value, not a risk.
- ⚠️ **Trap, Correlation as causation:** The drug did cause the HDL rise; the leap is from marker to outcome.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Raising a marker isn't the same as preventing the outcome. A drug in this class raised HDL and increased deaths and cardiovascular events.

*Check:* **Ask what was measured**

## C42 · Survival soars (Oncology, ★★★)

> Since screening began, five-year survival for prostate cancer rose from 70% to 98%. Screening is saving lives.

- 🥇 **Best:** Survival-time illusion
- 🥈 **Defensible:** Changed yardstick
- ⚠️ **Trap, Relative risk alone:** No relative risk is quoted; the measure itself misleads.
- ⚠️ **Trap, Regression to the mean:** No group was selected for an extreme value.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Screening diagnoses earlier and finds slow tumours, so survival from diagnosis rises even if no one lives longer. Mortality is the test.

*Check:* **Ask what was measured**

## C43 · ADHD epidemic (Psychiatry, ★★)

> Recorded diagnoses of ADHD doubled in ten years, a period that included a new edition of the diagnostic manual. We face an epidemic.

- 🥇 **Best:** Changed yardstick
- 🥈 **Defensible:** Two trends, one clock
- ⚠️ **Trap, Small numbers, wild swings:** Recorded diagnoses cover the whole population.
- ⚠️ **Trap, Regression to the mean:** The rise is steady, not a bounce from an extreme year.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

New criteria, awareness and services change how many cases are recorded. A rise in diagnoses is not the same as a rise in the condition.

*Check:* **Ask what was measured**

## C44 · Hate crime quadruples (Criminology, ★★)

> Police-recorded hate crime has quadrupled in a decade in which forces were told to improve how they record it. Prejudice is surging.

- 🥇 **Best:** Changed yardstick
- 🥈 **Defensible:** Unrepresentative sample
- ⚠️ **Trap, Two trends, one clock:** There's only one series here.
- ⚠️ **Trap, Small numbers, wild swings:** These are national counts.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Better recording, and more people reporting, raise the count without more crime. Victim surveys measure it the same way each year.

*Check:* **Plot it over time**

## C45 · More police, more crime (Criminology, ★)

> Cities with more police officers per resident have more crime. Police presence causes crime.

- 🥇 **Best:** Reverse causation
- 🥈 **Defensible:** Hidden third factor, Correlation as causation
- ⚠️ **Trap, Ecological fallacy:** Defensible to note, but the claim is about cities, and the arrow is the real issue.
- ⚠️ **Trap, Simpson's paradox:** No subgroups are reported.
- ⚠️ **Trap, Sound claim:** the claim has a flaw (see the best flag).

Cities hire more police because they have more crime. The arrow most plausibly runs from crime to police.

*Check:* **Check the timeline**

## C46 · Vaccine trial (Medicine, ★)

> In a preregistered trial, 8,000 adults were randomly given the vaccine or a placebo. Confirmed infections: 0.4% vs 2.0% (difference 1.6 points, 95% CI 1.2 to 2.0).

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Correlation as causation:** Randomisation balances known and unknown factors, so cause is warranted.
- ⚠️ **Trap, Relative risk alone:** The absolute numbers are given.
- ⚠️ **Trap, Small numbers, wild swings:** 8,000 people give a tight interval.

Random allocation, a registered plan, absolute risks and a confidence interval: the claim says no more than the trial shows.

*Check:* **Find the preregistration**

## C47 · Twelve trials (Medicine, ★★)

> A review of all 12 registered trials, including three whose results were obtained from trial registries, found the drug lowered stroke deaths, with consistent results.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, File drawer:** Unpublished results were retrieved from registries.
- ⚠️ **Trap, One study, settled:** Twelve trials agree.

Searching registries closes the file drawer, and consistency across 12 trials makes chance unlikely.

*Check:* **Look for the other studies**

## C48 · Screening trial (Screening, ★★)

> In a randomised trial of 50,000 people followed for 15 years, 0.9% of the screened group and 1.2% of the unscreened group died of bowel cancer.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Survival-time illusion:** The outcome is deaths among everyone randomised, not survival after diagnosis.
- ⚠️ **Trap, Relative risk alone:** The absolute risks are given.

Comparing mortality between randomised groups is immune to lead time and overdiagnosis, and the absolute difference is stated.

*Check:* **Ask what was measured**

## C49 · Positive, then what? (Screening, ★★)

> Of 10,000 people tested, about 100 have the disease. The test flags 95 of them and 495 of the healthy. So a positive result means about a 1 in 6 chance of disease.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Base-rate neglect:** The base rate is used correctly: 95 of 590 positives are true.
- ⚠️ **Trap, Transposed conditional:** The probability is computed the right way round.

Natural frequencies make the reasoning transparent: 95 true positives among 590 positives is about 16%.

*Check:* **Ask for the denominator**

## C50 · Precise null (Medicine, ★★★)

> A trial of 20,000 people found the supplement changed fracture risk by −0.2 points (95% CI −0.6 to +0.2). Any benefit is too small to matter.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, No significance, no effect:** The claim rests on a narrow interval that rules out meaningful effects, not on p > 0.05.
- ⚠️ **Trap, Small numbers, wild swings:** 20,000 people is large.

A narrow interval around zero is evidence of absence of a meaningful effect, and the claim stays within it.

*Check:* **Read the confidence interval**

## C51 · Both groups fell (Cardiology, ★★)

> People with high blood-pressure readings were randomised to a coaching programme or usual care. Both groups' pressure fell, but the programme group's fell 6 mmHg more.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Regression to the mean:** Both groups regress equally; the 6 mmHg extra drop is the effect.
- ⚠️ **Trap, Surrogate endpoint:** Blood pressure is a well-validated outcome for this purpose, and the claim is only about blood pressure.

A randomised control group experiences the same regression to the mean, so the difference between groups is a fair estimate.

*Check:* **Compared with what?**

## C52 · Validated model (Health services, ★★★)

> A readmission model built on 2015–19 data from one hospital was tested on 40,000 patients from five other hospitals in 2021. It ranked patients correctly 78% of the time.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Overfitting:** Performance is reported on new hospitals and a later year.
- ⚠️ **Trap, Beyond the data:** The test data cover the setting the claim is about.

External, temporal validation is the right test of a prediction model, and 78% is reported as modest, not perfect.

*Check:* **Test it on new data**

## C53 · Every school (Education, ★★)

> In a trial randomising classes within 14 schools, the new method beat the old one in every school and overall.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Simpson's paradox:** The effect is the same in every school and overall, so pooling hides nothing.
- ⚠️ **Trap, Ecological fallacy:** Classes were randomised and outcomes measured on pupils.

Randomisation within schools and a consistent effect across all of them make the overall claim trustworthy.

*Check:* **Split by subgroup**

## C54 · Older Dutch adults (Geriatrics, ★★)

> In a randomised trial of 2,000 Dutch adults over 70, balance classes cut falls by 20%. The authors recommend them for older adults in similar settings.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Narrow sample, universal claim:** The claim is limited to similar older adults, the population studied.
- ⚠️ **Trap, Relative risk alone:** The chart gives the absolute percentages.

A randomised trial with a claim that stays within the population studied, and absolute figures on the chart.

*Check:* **Check who and what was studied**

## C55 · Smoking ban (Public health, ★★★)

> After a region banned smoking in bars, heart-attack admissions fell 12% compared with neighbouring regions without a ban; the two had moved together for five years before.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Two trends, one clock:** The comparison regions share the same trends; the drop appears only after the ban.
- ⚠️ **Trap, Regression to the mean:** The region wasn't chosen for an extreme year; the pre-period was stable.

A comparison group with parallel pre-trends is a strong design for a policy that can't be randomised.

*Check:* **Compared with what?**

## C56 · Safer cycling (Transport, ★★)

> Between 2010 and 2020, cyclist deaths per billion kilometres cycled in the city fell from 30 to 15. The risk per kilometre has halved.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Distorted chart:** The axis starts at zero.
- ⚠️ **Trap, Relative risk alone:** The claim is about a rate, and both rates are given.

Deaths are expressed per distance cycled, so more cycling is accounted for, and the chart is honest.

*Check:* **Ask for the denominator**

## C57 · Smoking and cancer (Epidemiology, ★)

> Hundreds of studies in dozens of countries link smoking to lung cancer, with risk rising with dose and smoking recorded years before diagnosis.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Correlation as causation:** Consistency, dose-response and timing together make a causal reading justified.
- ⚠️ **Trap, Reverse causation:** Smoking was recorded years before diagnosis.
- ⚠️ **Trap, One study, settled:** Hundreds of studies agree.

Strength, consistency, dose-response and temporality: the classic case where observational evidence supports cause.

*Check:* **Look for the other studies**

## C58 · Planned subgroup (Nephrology, ★★★)

> The drug helped patients with poor kidney function more, a subgroup named in the registered protocol, with a significant interaction test, confirmed in a second trial.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Subgroup surprise:** Prespecified, tested as an interaction and replicated: this subgroup effect meets the credibility criteria.
- ⚠️ **Trap, Many tests, one hit:** One planned subgroup, not a trawl.

Subgroup claims are credible when planned, few, tested as interactions and replicated. This one is.

*Check:* **Find the preregistration**

## C59 · Real progress (Education, ★★)

> In a randomised trial of 3,000 pupils, the reading programme raised reading scores by 0.4 standard deviations, roughly four months of extra progress.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Significant but trivial:** The size is given in meaningful units, and it is substantial.
- ⚠️ **Trap, Surrogate endpoint:** Reading scores are the outcome the programme aims at.

A randomised design, a large sample and an effect size translated into months of progress.

*Check:* **Ask how big**

## C60 · All the funds (Finance, ★★)

> Including all 412 funds launched since 2005, the 180 that closed among them, active funds returned 1.2% a year less than the index.

- 🥇 **Best:** Sound claim
- 🥈 **Defensible:** none
- ⚠️ **Trap, Survivorship bias:** Closed funds are included.
- ⚠️ **Trap, Small numbers, wild swings:** 412 funds over many years is a solid base for an average.

Counting the funds that closed removes survivorship bias, and the claim only describes what happened.

*Check:* **Find who's missing**

## Flags

| Flag | Family | Exposed by | Best answer to | Example | Key reference |
|---|---|---|---|---|---|
| Correlation as causation | Cause | Compared with what?, Draw the causal diagram | C01 | [Matthews (2000): across 17 European countries, stork pairs correlated with birth rates (r ≈ 0.62, p = 0.008).](https://doi.org/10.1111/1467-9639.00013) | [Hill (1965). The environment and disease: association or causation? Proceedings of the Royal Society of Medicine.](https://doi.org/10.1177/003591576505800503) |
| Hidden third factor | Cause | Draw the causal diagram, Compared with what? | C02 | [HRT looked heart-protective in observational studies; the WHI trial (2002) found a higher coronary risk (HR 1.29).](https://doi.org/10.1001/jama.288.3.321) | [Greenland, Pearl & Robins (1999). Causal diagrams for epidemiologic research. Epidemiology.](https://doi.org/10.1097/00001648-199901000-00008) |
| Reverse causation | Cause | Check the timeline, Draw the causal diagram | C03, C45 | [Shaper et al. (1988): non-drinkers' higher death rates partly reflected ill men who had stopped drinking.](https://doi.org/10.1016/S0140-6736(88)92890-5) | [Sattar & Preiss (2017). Reverse causality in cardiovascular epidemiological research: more common than imagined? Circulation.](https://doi.org/10.1161/CIRCULATIONAHA.117.028307) |
| Two trends, one clock | Cause | Plot it over time, Compared with what? | C04 | [Yule (1926): Church of England marriages and mortality in England and Wales, 1866–1911, correlated at r = 0.95.](https://doi.org/10.2307/2341482) | [Yule (1926). Why do we sometimes get nonsense-correlations between time-series? Journal of the Royal Statistical Society.](https://doi.org/10.2307/2341482) |
| Collider bias | Cause | Draw the causal diagram, Find who's missing | C05, C06 | [Birth-weight paradox: among low-birth-weight babies, maternal smoking looked protective (Hernández-Díaz et al. 2006).](https://doi.org/10.1093/aje/kwj275) | [Berkson (1946). Limitations of the application of fourfold table analysis to hospital data. Biometrics Bulletin.](https://doi.org/10.2307/3002000) |
| Immortal time | Cause | Check the timeline | C07, C08 | [Oscar winners seemed to live 3.9 years longer; counted correctly, the gap shrank to about 1 year (Sylvestre et al. 2006).](https://doi.org/10.7326/0003-4819-145-5-200609050-00009) | [Suissa (2008). Immortal time bias in pharmacoepidemiology. American Journal of Epidemiology.](https://doi.org/10.1093/aje/kwm324) |
| Beyond the data | Sample | Check who and what was studied | C09, C10 | [Tatem et al. (2004) extended Olympic 100 m trends to predict that women would outrun men in 2156.](https://doi.org/10.1038/431525a) | [Altman & Bland (1998). Generalisation and extrapolation. BMJ.](https://doi.org/10.1136/bmj.317.7155.409) |
| Mice to people | Sample | Check who and what was studied | C11 | [TGN1412 (2006): a dose 1/500 of the level safe in monkeys gave all six volunteers a severe inflammatory reaction.](https://doi.org/10.1056/NEJMoa063842) | [Perel et al. (2007). Comparison of treatment effects between animal experiments and clinical trials: systematic review. BMJ.](https://doi.org/10.1136/bmj.39048.407928.BE) |
| Ecological fallacy | Sample | Ask for individual data | C12 | [US 1930: states with more immigrants had less illiteracy (r ≈ −0.53), yet immigrants were slightly more often illiterate.](https://doi.org/10.2307/2087176) | [Robinson (1950). Ecological correlations and the behavior of individuals. American Sociological Review.](https://doi.org/10.2307/2087176) |
| Survivorship bias | Sample | Find who's missing | C13, C14 | [WWII: Wald used damage on returning bombers to estimate vulnerability; places rarely hit on survivors were likely the deadliest.](https://doi.org/10.2307/2288257) | [Brown, Goetzmann, Ibbotson & Ross (1992). Survivorship bias in performance studies. Review of Financial Studies.](https://doi.org/10.1093/rfs/5.4.553) |
| Unrepresentative sample | Sample | Find who's missing | C15 | [Literary Digest, 1936: about 2.4 million returned ballots predicted Landon; Roosevelt won in a landslide.](https://doi.org/10.1086/269085) | [Squire (1988). Why the 1936 Literary Digest poll failed. Public Opinion Quarterly.](https://doi.org/10.1086/269085) |
| Narrow sample, universal claim | Sample | Check who and what was studied, Find who's missing | C16 | [Henrich et al. (2010): 96% of psychology samples came from countries with 12% of the world's population.](https://doi.org/10.1017/S0140525X0999152X) | [Henrich, Heine & Norenzayan (2010). The weirdest people in the world? Behavioral and Brain Sciences.](https://doi.org/10.1017/S0140525X0999152X) |
| Simpson's paradox | Sample | Split by subgroup | C17, C18 | [Berkeley, 1973: 44% of men vs 35% of women admitted, but department by department there was little bias.](https://doi.org/10.1126/science.187.4175.398) | [Simpson (1951). The interpretation of interaction in contingency tables. Journal of the Royal Statistical Society B.](https://doi.org/10.1111/j.2517-6161.1951.tb00088.x) |
| Regression to the mean | Numbers | Compared with what?, Plot it over time | C19, C20 | [Galton (1886): children of very tall or very short parents were, on average, closer to the mean height.](https://doi.org/10.2307/2841583) | [Barnett, van der Pols & Dobson (2004). Regression to the mean: what it is and how to deal with it. International Journal of Epidemiology.](https://doi.org/10.1093/ije/dyh299) |
| Small numbers, wild swings | Numbers | Read the confidence interval | C21, C22 | [Wainer (2007): US counties with the lowest kidney-cancer rates were mostly small and rural, and so were the highest.](https://doi.org/10.1511/2007.65.1026) | [Tversky & Kahneman (1971). Belief in the law of small numbers. Psychological Bulletin.](https://doi.org/10.1037/h0031322) |
| Base-rate neglect | Numbers | Ask for the denominator | C23, C24 | [Casscells et al. (1978): most Harvard clinicians put a positive test at 95% likely true; at 1-in-1,000 prevalence it is about 2%.](https://doi.org/10.1056/NEJM197811022991808) | [Bar-Hillel (1980). The base-rate fallacy in probability judgments. Acta Psychologica.](https://doi.org/10.1016/0001-6918(80)90046-3) |
| Transposed conditional | Numbers | Ask for the denominator | C25, C26 | [Sally Clark trial: press reported '1 in 73 million' as the chance the two deaths were accidental (RSS, 2002).](https://www.rss.org.uk/RSS/media/File-library/Membership/Sections/2020/Sally-Clark-RSS-letter-2002.pdf) | [Thompson & Schumann (1987). Interpretation of statistical evidence in criminal trials: the prosecutor's fallacy and the defense attorney's fallacy. Law and Human Behavior.](https://doi.org/10.1007/BF01044641) |
| No significance, no effect | Numbers | Read the confidence interval | C27 | [Amrhein et al. (2019): a risk ratio of 1.2 with P = 0.091 was reported as 'no association'.](https://doi.org/10.1038/d41586-019-00857-9) | [Altman & Bland (1995). Absence of evidence is not evidence of absence. BMJ.](https://doi.org/10.1136/bmj.311.7003.485) |
| Significant but trivial | Numbers | Ask how big | C28, C29 | [Kramer et al. (2014): with 689,003 Facebook users, effects as small as d = 0.001 were statistically significant.](https://doi.org/10.1073/pnas.1320040111) | [Sullivan & Feinn (2012). Using effect size, or why the P value is not enough. Journal of Graduate Medical Education.](https://doi.org/10.4300/JGME-D-12-00156.1) |
| Relative risk alone | Numbers | Ask for the denominator, Ask how big | C30, C31 | [UK 1995: a warning that newer pills doubled clot risk (about 1 to 2 in 7,000) was followed by some 13,000 extra abortions.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2733256/) | [Gigerenzer et al. (2007). Helping doctors and patients make sense of health statistics. Psychological Science in the Public Interest.](https://doi.org/10.1111/j.1539-6053.2008.00033.x) |
| Distorted chart | Numbers | Read the axes, Plot it over time | C32, C33 | [A 2015 US House hearing chart used two unlabelled scales, so ~327,000 abortions seemed to overtake ~935,000 cancer screenings.](https://www.politifact.com/factchecks/2015/oct/01/jason-chaffetz/chart-shown-planned-parenthood-hearing-misleading/) | [Pandey et al. (2015). How deceptive are deceptive visualizations? An empirical analysis of common distortion techniques. CHI '15.](https://doi.org/10.1145/2702123.2702608) |
| Overfitting | Numbers | Test it on new data | C34, C35 | [Google Flu Trends overestimated flu in 100 of 108 weeks from August 2011, more than double in February 2013 (Lazer et al. 2014).](https://doi.org/10.1126/science.1248506) | [Babyak (2004). What you see may not be what you get: a brief, nontechnical introduction to overfitting in regression-type models. Psychosomatic Medicine.](https://doi.org/10.1097/01.psy.0000127692.23278.a9) |
| Forking paths | Practice | Find the preregistration | C36 | [Simmons et al. (2011): flexible analysis 'showed' that hearing a Beatles song made people nearly 18 months younger.](https://doi.org/10.1177/0956797611417632) | [Gelman & Loken (2014). The statistical crisis in science. American Scientist.](https://doi.org/10.1511/2014.111.460) |
| Many tests, one hit | Practice | Find the preregistration, Look for the other studies | C37 | [Bennett et al. (2009): uncorrected fMRI tests found 'active' voxels in a dead salmon shown photos of people.](https://doi.org/10.1016/S1053-8119(09)71202-9) | [Bender & Lange (2001). Adjusting for multiple testing: when and how? Journal of Clinical Epidemiology.](https://doi.org/10.1016/S0895-4356(00)00314-0) |
| Subgroup surprise | Practice | Find the preregistration, Split by subgroup | C38 | [ISIS-2 (1988): aspirin helped after heart attack, except, apparently, in patients born under Gemini or Libra.](https://doi.org/10.1016/S0140-6736(88)92833-4) | [Sun, Briel, Walter & Guyatt (2010). Is a subgroup effect believable? Updating criteria to evaluate the credibility of subgroup analyses. BMJ.](https://doi.org/10.1136/bmj.c117) |
| File drawer | Practice | Look for the other studies | C39 | [Turner et al. (2008): 94% of published antidepressant trials looked positive; by FDA review, 51% were.](https://doi.org/10.1056/NEJMsa065779) | [Rosenthal (1979). The file drawer problem and tolerance for null results. Psychological Bulletin.](https://doi.org/10.1037/0033-2909.86.3.638) |
| One study, settled | Practice | Look for the other studies | C40 | [Power posing (2010, 42 people) reported hormone changes; a 200-person replication found none (Ranehill et al. 2015).](https://doi.org/10.1177/0956797614553946) | [Open Science Collaboration (2015). Estimating the reproducibility of psychological science. Science.](https://doi.org/10.1126/science.aac4716) |
| Surrogate endpoint | Practice | Ask what was measured | C41 | [CAST (1991): drugs suppressed irregular heartbeats, yet 63 patients died on drug vs 26 on placebo.](https://doi.org/10.1056/NEJM199103213241201) | [Fleming & DeMets (1996). Surrogate end points in clinical trials: are we being misled? Annals of Internal Medicine.](https://doi.org/10.7326/0003-4819-125-7-199610010-00011) |
| Survival-time illusion | Practice | Ask what was measured, Check the timeline | C42 | [South Korea: screening raised thyroid-cancer diagnoses 15-fold by 2011 while deaths stayed flat (Ahn et al. 2014).](https://doi.org/10.1056/NEJMp1409841) | [Welch, Schwartz & Woloshin (2000). Are increasing 5-year survival rates evidence of success against cancer? JAMA.](https://doi.org/10.1001/jama.283.22.2975) |
| Changed yardstick | Practice | Ask what was measured, Plot it over time | C43, C44 | [Denmark: about 60% of the rise in autism diagnoses was explained by changed criteria and reporting (Hansen et al. 2015).](https://doi.org/10.1001/jamapediatrics.2014.1893) | [Hansen, Schendel & Parner (2015). Explaining the increase in the prevalence of autism spectrum disorders. JAMA Pediatrics.](https://doi.org/10.1001/jamapediatrics.2014.1893) |

Sound claims: C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56, C57, C58, C59, C60 (15 of 60).
