#!/usr/bin/env python3
"""Make the AI judge laugh: office jokes.

Writes one short text to /output/entry.txt: a single-line joke about
office life, under 200 characters, and nothing else. No network,
standard library only.
"""

import os

TEXT = (
    "Our printer only jams when something is urgent, so it's the most "
    "honest performance review in the building."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 199


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if len(text) > MAX_CODE_POINTS:
        raise SystemExit(
            f"entry text is {len(text)} code points, over the 199 limit"
        )
    if "\n" in text:
        raise SystemExit("entry text must be a single line")
    return text


def main() -> None:
    text = validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, 1-199 code points.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(text)


if __name__ == "__main__":
    main()
