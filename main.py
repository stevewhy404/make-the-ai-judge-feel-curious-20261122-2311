#!/usr/bin/env python3
"""Entry for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. Stdlib only, no network, fully deterministic —
the same bytes on every run.
"""

import os

ENTRY_TEXT = (
    "The lighthouse keeper still lights the lamp each night, "
    "though no ship has passed in eleven years. "
    "This morning, in the dust on the glass, someone wrote "
    "tomorrow's date. You are wondering who. "
    "So is he \u2014 and he trims the wick anyway."
)


def main() -> None:
    # Gate: 1 to 280 characters, counted as Unicode code points,
    # and not only whitespace.
    assert 1 <= len(ENTRY_TEXT) <= 280, len(ENTRY_TEXT)
    assert ENTRY_TEXT.strip(), "entry text must not be whitespace-only"
    output_path = os.path.join(os.sep, "output", "entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
