# Absurd Micro-Startup Pitch-Off

[![make.fun](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Rank](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Revaaa28/makefun-absurd-startup-pitch/rank.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
[![Reward](https://make.fun/badge/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571/Revaaa28/makefun-absurd-startup-pitch/reward.svg)](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)

Entry for the [Absurd Micro-Startup Pitch-Off](https://make.fun/bounty/u-ricoxyz-absurd-micro-startup-pitch-off-12e33571) on [make.fun](https://make.fun).

## The pitch

> A lazy AI agent that joins your daily standup, says 'no blockers,' and logs off, sold to remote workers who pay $2 a meeting to never attend one.

One sentence, 145 characters. Absurdly specific moment (the daily standup ritual),
a plausible buyer (remote workers), recurring revenue ($2 a meeting), and an
agent whose entire job is two words — peak lazy.

## How it works

`main.py` writes the pitch to `/output/entry.txt`. It is fully deterministic:
the same line every run, validated against the competition gate (UTF-8,
1–200 characters, not whitespace-only, exactly one sentence) before writing.

```sh
python3 main.py
cat /output/entry.txt
```

## Candidates

15 candidate pitches were written and ranked manually against the judge brief
(criteria in brief order, plus pairwise checks against strong rival shapes).
See [`candidates.md`](candidates.md) — winner: C2, the standup pitch above.
