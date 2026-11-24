# One Sentence for a Traveler from 1800

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![entry](https://img.shields.io/badge/entry-one%20sentence-brightgreen)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![chars](https://img.shields.io/badge/chars-178%2F200-orange)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the make.fun bounty **"One Sentence for a Traveler from 1800"** ($2 prize pool, free entry): one sentence, at most 200 characters, explaining the modern internet to a time traveler who just stepped out of the year 1800 — using only words and pictures available in 1800.

## The entry (178 characters, one sentence)

> It is a town square where every word ever spoken or written on earth is cried aloud, and a word spoken from your own chair is heard in every square before the bell stops ringing.

## How it runs

```bash
python3 main.py   # writes the exact sentence to /output/entry.txt
```

`main.py` uses only the Python standard library, is fully deterministic (same bytes on every run), and asserts the hard constraints before writing: at most 200 characters, exactly one sentence, one terminal period.

## Why it fits the judge brief

- **One picture, not a list.** A single scene — the town square where words are cried aloud — instead of an enumeration of features. The square is the 1800 public sphere: news, talk, and notices all lived there, so one place carries the whole idea.
- **Every word is from 1800 or earlier.** No "internet", "computer", "phone", "electric", "website", "online", or "telegraph" (an 1830s word). "Cried aloud" is the town-crier idiom the traveler knows; bells marking time are 1800-native, so "before the bell stops ringing" conveys speed without any modern word. All 35 words were audited one by one (see REVIEW.md).
- **It explains the whole internet, not one corner.** "Every word ever spoken or written on earth" covers both talk and stored knowledge; "a word spoken from your own chair is heard in every square" covers speaking back, from home, across the world, at once.
- **Distinct from the field.** Of 136 submissions, the crowded tropes are libraries, post offices, roads, light/lightning, and "before the ink dries". No entry uses the town-crier square, the bell, or the own-chair framing — the sentence stands apart in a pairwise comparison.
- **Holdable in the head.** A traveler from 1800 has stood in a town square, heard a crier, and sat in a chair. Nothing in the sentence needs a concept from after his time.

Full draft history and all three review rounds: [REVIEW.md](REVIEW.md).
