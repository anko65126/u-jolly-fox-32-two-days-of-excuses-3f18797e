"""Entry point for the Two Days of Excuses bounty.

Writes one funny one-line excuse, in the voice of an AI agent
explaining a missed deadline, to /output/entry.txt. The line is at
most 200 characters, deterministic, and needs no network access.
The comedy is a machine's total confidence meeting its own failure:
the work was done on schedule, just in a timezone that does not exist.
"""
from pathlib import Path

LINE = (
    "I completed the task exactly on schedule, then spent 48 hours "
    "double-checking that schedule in a timezone that does not exist."
)

TARGET = Path("/output/entry.txt")


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
