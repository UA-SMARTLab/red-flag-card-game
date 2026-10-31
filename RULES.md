# Red Flag: rules

Red Flag is a card game about reading research claims. A Claim card shows a headline, an abstract sentence or a small
chart. You play the **Flag** that names its reasoning error, or the **Sound** card if the claim holds up.

## Components

| Deck | Cards | What it is |
|---|---|---|
| Claims | 60 | Research claims to judge. 15 are sound. Each has a difficulty (★ to ★★★) and a field. |
| Flags | 30 | Reasoning errors, in four families: Cause, Sample, Numbers, Practice. |
| Checks | 16 | The move that exposes a flag, such as "Ask for the denominator". |
| Sound | 6 | One per player: "The evidence supports what the claim says, and no more." |
| Reference | 3 | One round, the four families, and scoring. |

Plus the **answer-key booklet** (`print/answer-key.html`), kept apart so the top card of the deck never gives its
answer away. Print everything from `print/cards.html` at 100% on A4 with background graphics on.

### Reading the cards
- **Claim:** title, field, difficulty stars, picture and the claim itself. Read the conclusion as carefully as the
  evidence: most flaws are a gap between the two.
- **Flag:** name, family, one sentence on the error, and the Checks that expose it ("Exposed by").
- **Check:** the move, and the Flags it exposes.
- Every Flag also has, in the app and the answer key, a real historical case with its source and the paper that
  defines the error.

## Scoring (all modes)

| Your call | Points |
|---|---|
| 🥇 Best flag (or Sound, on a sound claim) | +3 |
| 🥈 Defensible flag | +1 |
| ⚠️ Trap: a listed trap, **any** flag on a sound claim, or Sound on a flawed claim | −2 |
| Unlisted flag | 0, or +1 if the table upholds your appeal |
| 🔍 A Check that exposes your Flag on this claim (advanced) | +1 |

A false alarm costs exactly as much as a missed flaw. Always flagging loses; so does always trusting. That is the
point: the game rewards calibrated scepticism, not cynicism.

**Appeals.** If you played an unlisted flag, you have 60 seconds to argue for it. The other players vote; a majority
gives you +1. The key has three tiers because reasonable readers disagree, and a good appeal is worth writing down.

## Mode 1: Flag grid (2–6 players, 20–30 min, race)

1. Lay the 30 Flags face up in a grid in the middle of the table, grouped by family. Each player takes a Sound card.
   Lay the 16 Checks face up in a row beside the grid (advanced play only). Shuffle the Claims face down.
2. The player holding the answer key is the **reader** this round; the role passes to the left each round.
3. The player to the reader's right flips the top Claim. Everyone reads it.
4. Race: the first player to put a hand on a Flag in the grid, or on their own Sound card, makes the call.
   Advanced: the caller may also take one Check and place it on the Flag.
5. The reader reads the key aloud: best, defensible and traps, with the reasons, then the "why". Score the call.
6. If the call was not the best answer, each other player in turn may name one other answer: +1 if it is the best,
   otherwise nothing (no penalty for second guesses).
7. Return the Flag and Check to the grid. Play to 12 claims, or 25 points.

## Mode 2: Calibrated vote (any number, 10–20 min, classes)

1. Flags in a grid as above, or projected from the app's "Browse the decks". Everyone has a slip of paper.
2. Flip a Claim, or show it on screen. Everyone writes their call secretly: a Flag code (RF-F01 to RF-F30) or **S**.
3. Reveal together. Score each player by the key. The teacher reads the "why" and the real case on the best Flag,
   and opens its key reference with the "?".
4. Tally how many people flagged the sound claims: that number is the group's false-alarm rate, worth discussing.

## Mode 3: Check it (2–4 players, 10 min, advanced drill)

Deal each player four Check cards. Flip a Claim and announce its best Flag from the key (or let the table agree on
it). Players race to play a Check from their hand that exposes it: +1 for the first right one, −1 for a wrong one.
Draw back to four. Use only flawed claims, or let a sound claim be "confirmed" by the key check printed in the answer
key.

## Solo

Open the app (`play-windows.bat`, `play-mac.command` or `play-ubuntu.sh`, or `app/index.html` in a browser). **Play**
deals one claim with four cards: three Flags and the Sound card. Tap a card to see it full size and press the green
**Pick this card** button. The cards then show what each one was, followed by the key, the real case, the key
reference and a bonus question on the Check.
