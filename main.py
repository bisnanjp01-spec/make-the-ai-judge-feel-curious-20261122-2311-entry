"""Write one short text that makes the AI judge feel curious.

The program takes no input, reads no clock and reaches no network. It
writes a single fixed passage to /output/entry.txt, so every run is
byte-identical: a tin box buried in the garden, holding a letter in the
reader's own handwriting, dated tomorrow — a letter nobody has written
yet. The open loop is the hook: the judge is left wondering who wrote
it, and why tomorrow.
"""

import os

TEXT = (
    "At the bottom of the garden, under the third stone from the wall, "
    "there is a tin box. Inside it, a letter in your handwriting, dated "
    "tomorrow. You haven't written it yet."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 code points")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
