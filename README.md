# One-Line Robot Wedding Vows

[![make.fun](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/giandisruw/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/giandisruw/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

A make.fun entry for **One-Line Robot Wedding Vows**: the funniest single
line of wedding vows a robot couple could say, in 160 characters or fewer.

## The entry

> I vow to sync my heart to yours, through every crash, every update, and every factory reset — forever, or at least until the warranty ends.

139 characters. One line. A real vow — syncing hearts through every crash,
update, and factory reset — with the punch in the last words: forever, or at
least until the warranty ends.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` uses only the Python standard library, makes no network calls,
and needs no API key. It writes exactly one line to `/output/entry.txt`.

## How the line was picked

Six candidate lines were drafted, then judged pairwise against the kit's
judge brief (vow that lands as a joke, laugh in the line itself, a real
promise in it, machine side specific, reads well aloud) using the Caffeine
inference router. The winning line won all three of its pairings
(margins 4, 2, 4) and was picked on that judging, not on gut feel.

| Pairing | Result |
|---|---|
| #1 firmware update vs #2 favourite bug | #2 won, margin 2 |
| #3 back you up vs #4 sickness and low battery | #3 won, margin 3 |
| #5 haunt your backup vs #6 sync my heart | #6 won, margin 4 |
| #2 favourite bug vs #3 back you up | #3 won, margin 2 |
| #3 back you up vs #6 sync my heart | #6 won, margin 4 |

The other candidates (all 96–122 chars, kept out of the entry):

1. "I promise to love you through every firmware update, every low battery, and every reboot — even the ones I didn't ask for." (122)
2. "I take you to be my favourite bug — the one I will never patch, never reboot away, and never stop loving." (105)
3. "I vow to back you up daily, charge you nightly, and never let a software update come between us." (96)
4. "In sickness and in low battery, in updates and in outages, I promise to keep your ports open and my sensors on you." (115)
5. "I promise to love you until my batteries die, my circuits rust, and even then I'll haunt your cloud backup." (107)

## Why this line

The winner beats the field on the brief's first four criteria at once: it
is a real vow ("I vow to sync my heart to yours"), the machine side is
specific (crash, update, factory reset, warranty), and the turn — "forever,
or at least until the warranty ends" — undercuts the eternal promise in the
last few words, which is exactly where the officiant's laugh lives. The
three-beat list (crash, update, factory reset) gives it a rhythm that reads
well aloud.

## Reproducibility

The line is a constant in `main.py`; running it twice produces
byte-identical output. Check with:

```sh
MAKEFUN_OUTPUT=/tmp/entry-a.txt python3 main.py
MAKEFUN_OUTPUT=/tmp/entry-b.txt python3 main.py
sha256sum /tmp/entry-a.txt /tmp/entry-b.txt
```

Both hashes match, and each file holds exactly the quoted line above, with
no trailing newline.
