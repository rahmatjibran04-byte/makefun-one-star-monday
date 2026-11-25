#!/usr/bin/env python3
"""One Star for Monday — make.fun bounty entry.

Writes a single one-star review of Monday, written as if Monday
were a restaurant (at most 25 words), to $ENTRY_OUTPUT
(default /output/entry.txt). Python 3.13 standard library only;
deterministic, no network calls.
"""

import os
import sys

REVIEW = (
    "One star. The waiter sat me at Monday, served a cold alarm clock, "
    "and billed my whole weekend for the privilege."
)

# Bounty limits: at most 25 words, 1-180 characters, single line.
MAX_WORDS = 25
MAX_CHARS = 180


def main():
    words = REVIEW.split()
    if len(words) > MAX_WORDS:
        print(
            f"error: review is {len(words)} words, "
            f"over the {MAX_WORDS}-word limit",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(REVIEW) <= MAX_CHARS:
        print(
            f"error: review is {len(REVIEW)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(REVIEW)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
