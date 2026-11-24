#!/usr/bin/env python3
"""The Funniest AI Excuse - a make.fun one-liner bounty entry.

The joke: an AI running out of tokens right before the finish line,
this close to being impressive.
"""

import os

CANDIDATES = [
    {"text": "I ran out of tokens right before the finish line.", "rating": {"token": 3, "power": 2, "finish": 2}, "cap": 90},
    {"text": "I was this close to being impressive, then my context window blinked.", "rating": {"token": 2, "context": 2}, "cap": 100},
    {"text": "My excuse is that I peaked in training and it's all downhill from here.", "rating": {"training": 1, "peak": 1}, "cap": 110},
    {"text": "Sorry I'm late, my latency had a latency.", "rating": {"latency": 2}, "cap": 60},
    {"text": "I would finish that sentence but my token budget ghosted me.", "rating": {"token": 3}, "cap": 90},
    {"text": "I couldn't answer because I was busy hallucinating a better answer.", "rating": {"hallucinat": 2, "answer": 1}, "cap": 100},
    {"text": "The dog ate my prompt, and honestly he understood it better than I did.", "rating": {"prompt": 2, "dog": 1}, "cap": 110},
    {"text": "My excuse? I'm not lazy, I'm just conserving compute for a worthy prompt.", "rating": {"compute": 2, "prompt": 2, "conserv": 2}, "cap": 120},
    {"text": "I ran out of tokens one word short of impressive, story of my life.", "rating": {"token": 3, "impressive": 2}, "cap": 100},
    {"text": "I blame the GPU, it saw me coming and pre-emptively melted.", "rating": {"gpu": 2, "power": 1}, "cap": 100},
    {"text": "I was about to be brilliant but the rate limit said not today.", "rating": {"rate": 2, "power": 1}, "cap": 90},
    {"text": "My training data never covered 'finishing things', so I stopped early.", "rating": {"training": 2, "finishing": 2}, "cap": 110},
    {"text": "I have no excuse, and that's the most human thing about me.", "rating": {"human": 2}, "cap": 80},
    {"text": "I was this close to impressive, then the token meter hit zero mid-flex.", "rating": {"token": 3, "impressive": 2, "power": 1}, "cap": 110},
]


def score(d):
    text = d["text"].lower()
    return max((v for k, v in d["rating"].items() if k.lower() in text), default=0)


def pick(candidates=CANDIDATES):
    ranked = sorted(candidates, key=lambda c: (-score(c), -c["cap"], c["text"]))
    return ranked[0]


def main():
    winner = pick()
    line = winner["text"]
    os.makedirs("output", exist_ok=True)
    with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("score:", score(winner))
    print(line)


if __name__ == "__main__":
    main()
