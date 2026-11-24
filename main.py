#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes a single emoji to /output/entry.txt: the desert island.

Why this emoji: the judge is a travel editor collecting wordless
postcards, and it picks the emoji that most makes a stranger want to
book the flight. A desert island is the dream vacation itself in one
glyph - faraway place, beach and palm tree at a glance, specific
rather than generic, and readable on any screen. It beats the obvious
beach umbrella (any holiday), the plane (transport, not the trip) and
the lone palm (a tree, not a place) on the brief's first two criteria.
Stdlib only, no network, no input, deterministic.
"""

import os

# U+1F3DD DESERT ISLAND: one code point, emoji presentation, 4 bytes UTF-8.
EMOJI = "\U0001F3DD"


def main() -> None:
    # Enforce the gate ourselves: 1-8 characters, not only whitespace.
    text = EMOJI.strip()
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry must be 1-8 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" so no platform line-ending translation can add bytes:
    # the file must hold exactly the one emoji, 4 bytes, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what we wrote is exactly the one emoji.
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError(f"entry.txt mismatch: {written!r}")


if __name__ == "__main__":
    main()
