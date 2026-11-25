"""One-Liner Marathon entry (v2).

Writes a single deadpan one-line joke to /output/entry.txt.

The text is fixed, so every run produces the exact same output: the
gate reads the file, and the judge compares it head to head with the
other entries. Nothing here reads the network, the git history, or any
file outside this repository; the joke is written in this file, below.
"""

import os

# A fitness tracker mistakes financial anxiety for exercise. The setup
# sounds like a health brag, the punchline reframes it as a bank-balance
# panic: the twist lands on the last words, and every word before them
# earns its place. "I'd only been" keeps the confession flat and deadpan
# instead of explaining it.
JOKE = (
    "My smartwatch congratulated me on burning 400 calories \u2014 "
    "I'd only been anxiously refreshing my bank balance."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The gate accepts UTF-8 text of 1 to 280 characters, a single line,
# not only white space.
MAX_CHARS = 280


def validate(text: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, limit is {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if text.strip() == "":
        raise ValueError("joke must not be only white space")
    # The file must be valid UTF-8; encoding it here catches a bad
    # character before anything is written.
    text.encode("utf-8")


def write_entry(text: str) -> str:
    """Write the joke to /output/entry.txt and leave it world-readable.

    The grader collects /output as another user than the one the
    program runs as, so the file is chmodded 0644 after writing.
    """
    validate(text)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_FILE, 0o644)
    return OUTPUT_FILE


def main() -> None:
    path = write_entry(JOKE)
    print(JOKE)
    print(f"characters: {len(JOKE)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
