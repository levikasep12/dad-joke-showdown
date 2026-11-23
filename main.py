#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry.

Writes one dad joke to /output/entry.txt. Deterministic: the same
bytes on every run. The joke is a constant in this file; nothing is
read from the working directory, so the program does not depend on
process.cwd().
"""

import os

LINE = "I named my dog Five Miles so I can tell people I walk Five Miles every single day."
# 82 characters: one joke, inside the 200-character gate.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
