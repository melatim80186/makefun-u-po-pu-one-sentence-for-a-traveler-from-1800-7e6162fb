#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes the entry sentence -- one sentence, 178 characters, every word
available to a person of 1800 -- to /output/entry.txt, deterministically.
Standard library only; no network, no randomness.
"""

import os

SENTENCE = (
    "It is a town square where every word ever spoken or written on earth "
    "is cried aloud, and a word spoken from your own chair is heard in "
    "every square before the bell stops ringing."
)


def main() -> None:
    assert len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.count(".") == 1, "must be exactly one sentence"
    assert SENTENCE.endswith("."), "must end with a single period"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"Wrote {len(SENTENCE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
