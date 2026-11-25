"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit-message line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os

COMMIT_LINE = "fix: race condition resolved, both threads now lose together"

MAX_LENGTH = 100


def write_entry() -> str:
    """Write the commit message with no trailing newline and return it."""
    line = COMMIT_LINE.strip()
    if not 1 <= len(line) <= MAX_LENGTH:
        raise ValueError("commit line must be 1-100 characters")
    if "\n" in line:
        raise ValueError("commit line must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMIT_LINE)
    return path


if __name__ == "__main__":
    write_entry()
