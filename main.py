#!/usr/bin/env python3
"""One Letter: Coffee or Tea - writes the entry letter to /output/entry.txt.

The entry is exactly one letter: A for coffee. The house gate requires
/output/entry.txt to be UTF-8 text of exactly 1 character, not whitespace,
so this program checks the letter before writing and verifies its own
output byte-for-byte afterwards, failing loudly if it ever differs.
"""
import os
import sys

ENTRY = "A"
OUT = "/output/entry.txt"


def main():
    if len(ENTRY) != 1 or ENTRY.isspace():
        print(
            "gate check failed: entry must be exactly 1 non-space character, "
            f"got {ENTRY!r}",
            file=sys.stderr,
        )
        sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUT, "rb") as f:
        data = f.read()
    if data != ENTRY.encode("utf-8"):
        print(
            f"read-back verification failed: {data!r} != {ENTRY.encode('utf-8')!r}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
