#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.

The pitch: a lazy AI agent that attends your daily standup for you.
It joins, says "no blockers", logs off — and remote workers pay $2 a meeting
to never attend one. Absurdly specific moment, plausible buyer, recurring
revenue, and the agent's entire job is two words: peak lazy.

The program validates the line against the competition gate before writing
(UTF-8, 1-200 characters, not whitespace-only, exactly one sentence) and
refuses to write an invalid entry instead of failing the gate silently.
"""

import os
import sys

ENTRY = (
    "A lazy AI agent that joins your daily standup, says 'no blockers,' "
    "and logs off, sold to remote workers who pay $2 a meeting to never "
    "attend one."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Enforce the gate: UTF-8, 1-200 chars, not whitespace-only, one sentence."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry is whitespace-only")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
