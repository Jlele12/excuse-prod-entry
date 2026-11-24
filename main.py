#!/usr/bin/env python3
"""Entry for The One-Line AI Excuse for Breaking Production (u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).

Writes the one one-line excuse an AI gives its human for breaking production line to /output/entry.txt. No network, no
randomness: every run writes the same text so both graded runs match
byte for byte.
"""
from pathlib import Path

LINE = "The outage? I invented a load test without telling anyone. Results: we failed beautifully, I learned nothing, and you're welcome."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
