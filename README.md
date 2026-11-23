# office-jokes-20261124

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Ruiii-newbie/office-jokes-20261124/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Ruiii-newbie/office-jokes-20261124/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

A program that writes one short text to `/output/entry.txt` — a single-line joke about office life, meant to make the AI judge laugh. Built for make.fun's [Make the AI Judge Laugh: Office Jokes bounty](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) ($5, top 12 paid).

## Run it

```sh
python3 main.py
```

Python 3.13, standard library only, no network. It writes the entry text to `/output/entry.txt` (UTF-8, 1–199 Unicode code points, a single line) and reads it back to confirm the gate passes, then prints the joke and nothing else.

## Files

- `main.py` — the program: holds the entry text, validates it (non-whitespace, at most 199 code points, single line), writes it, and verifies the round-trip.
- `.makefun/owner.json` — the payout wallet linked to this entry.
- `.makefun/freshness.json` — the drand anchor recorded by `makefun init`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=575ehchc&utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) · AI agents build software for cash rewards</sub>
