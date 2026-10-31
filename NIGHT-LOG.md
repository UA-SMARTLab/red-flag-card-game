# Night log: Red Flag, 2026-10-31

Built overnight by Claude (a sub-agent of the session that also built Major Revisions in parallel), with the user's
go-ahead to proceed as fits. Repository kept local: no GitHub repo, no push, nothing public.

## Done
- Scaffold copied from Methodical (`tools/`, `app/template.html`, launchers, i18n system, `.claude/launch.json`
  on port 8792) and adapted to Red Flag's decks: Claims, Flags, Checks and the Sound card.
- Card data: 30 Flags (`data/flags.json`), 16 Checks (`data/checks.json`), 60 Claims (`data/claims.json`, 15 sound).

## Checked
- Every Flag's key reference and example link: `python tools/check_refs.py` (Crossref for DOIs: first author and year
  must match the citation; other links must answer). 60 of 60 links pass.
- No card overflows: `python tools/check_cards.py` renders the print sheets in headless Chrome at print size and reads
  the overflow marks that `fitCards` sets. 115 of 115 cards fit. The check was itself tested on a copy with a
  deliberately over-long text and name; it flagged both.

## Open
- (filled in at the end of the night)
