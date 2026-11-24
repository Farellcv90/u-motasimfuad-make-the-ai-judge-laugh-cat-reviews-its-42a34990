#!/usr/bin/env python3
"""One-star cat review of its human.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR)
and prints it. Deterministic, no network, no secrets.
"""

import os

LINE = (
    "One star. He greets me every morning with 'who's a good boy?' "
    "I am a girl. I have corrected him for six years. "
    "He has not listened once."
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-200 chars, one line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
