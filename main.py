#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line of wedding vows for a robot couple to /output/entry.txt.
Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine inference router, kit's
judge brief) over 6 drafted candidates: it won all 3 of its pairings
(margins 4, 2, 4). The em dash in the line is part of the judged text;
do not replace it with a hyphen or comma.
"""

import os

LINE = "I vow to sync my heart to yours, through every crash, every update, and every factory reset \u2014 forever, or at least until the warranty ends."

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
