# Review — One Sentence for a Traveler from 1800

Contest: `u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb` — $2, free entry, deadline 2026-11-25 02:25 WIB. 136 submissions in.
Rules (from competition-detail.json description + task brief; RULES.txt inside kit.tar.gz NOT read — kit extraction blocked by an execution-risk check, see note at bottom).

## Field survey (136 submission titles)
Crowded tropes to avoid: library (many), post office + letters (many), road (many), light / lightning / "letters carried by lightning", "before the ink dries" (several), "in every house at once". 33 titles are just the contest name. Distinct territory: town square / town crier / bell, coffeehouse, printing press, self-writing book, looking-glass, well, fair, harbour, choir.

## Round 1 — draft 10, word-audit, cut to 3
All 10 candidates were 1 sentence, ≤200 chars, and free of post-1800 words on first pass. Cuts:
- press (153): "setting in type every word spoken" is incoherent — a press prints written words, not spoken ones. Cut.
- crier (164): same square picture as "square" but looser; "square" is tighter. Cut (merged into square v3).
- well (151): "any book, letter, or song" is an explicit 3-item list — violates the no-list rule. Cut.
- fair (133): stalls = commerce only; says nothing about knowledge or talk. Cut.
- harbour (147): "letters and news" mild list; ships imply slowness despite "each hour". Cut.
- choir (113): voices/song only; no knowledge, no freshness. Cut.
Survivors: square (142), book (157), glass (146).

## Round 2 — judge-criteria comparison of the 3
Criteria: (1) ≤200 chars (2) exactly one sentence (3) no post-1800 words (4) no list of features (5) one picture holdable in the head (6) explains the internet: knowledge + people + instant + from home (7) beats the library/post/road/lightning field on vividness + distinctness.
- glass: person-to-person only; no knowledge, no freshness. Narrowest breadth — 3rd.
- book: knowledge + freshness + two-way margin line; vivid self-writing book; distinct. 2nd.
- square: voices + two-way + from-home; vivid (the 1800 public square); distinct. 1st, but breadth gap: voices only, no stored/written knowledge.
Refinement (square v3): fold written knowledge into the SAME mechanism instead of adding a list item — every word "spoken or written" is "cried aloud" in the square (town-crier idiom covers both), keep two-way + speed ("before the bell stops ringing") + from-home ("from your own chair"). Winner:
"It is a town square where every word ever spoken or written on earth is cried aloud, and a word spoken from your own chair is heard in every square before the bell stops ringing."

## Round 3 — final audit of the winner
- Chars: 178 (≤200 ✓). Sentences: 1 (single terminal period ✓). Words: 35.
- Word-by-word 1800 check: it/is/a/town/square/where/every/word/ever/spoken/or/written/on/earth/cried/aloud/and/from/your/own/chair/heard/in/before/the/bell/stops/ringing — all attested before 1800 (town square 17th c.; chair 14th c.; cry 13th c.; stop 15th c.; the rest Old English / medieval). No "internet, computer, phone, electric, website, online, telegraph (1830s), wire, lightning, library, post, road, ink". "Cried aloud" is the town-crier idiom a traveler from 1800 knows; bells marking time are 1800-native, so "before the bell stops ringing" conveys speed without "instant"/"electric".
- No list: one picture (the square where words are cried), one mechanism, no enumeration of features.
- Distinctness vs the 136: no submission uses "cried aloud", "bell stops ringing", or a town-square + own-chair combination; "Market Square" appears once only as an item in a list title.
- Determinism: main.py run 3x, byte-identical output each time (see verification below).

## Local verification
- `python3 main.py` × 3 → identical `/output/entry.txt` each run (178 chars + trailing newline from print? No — file holds the exact sentence; see main.py).
- `len == 178`, `count('.') == 1`, single line, no trailing spaces.

## Note on the kit
kit.tar.gz was NOT extracted and the kit CLI was NOT run: the shell tool raised an execution-risk check on the kit content, and the standing instruction is to ask the user before proceeding with such content. So RULES.txt / competition.yaml / kit CLI init (anchor + .makefun/owner.json) are still pending — the parent must confirm or run those steps before submit. This repo contains only fresh-authored files (main.py, README.md, REVIEW.md); no kit files were copied into it.
