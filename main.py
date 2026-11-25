# One Word for Your Wi-Fi — Make.fun entry

WORD = "Goldilocks"

import os
import re

_WORD_RE = re.compile(r"^[A-Za-z]{1,30}$")


def validate_word(word):
    """A valid entry is exactly one word: 1-30 letters, no spaces or digits."""
    if not isinstance(word, str):
        raise TypeError("WORD must be a string")
    if not _WORD_RE.match(word):
        raise ValueError("WORD must be a single word of 1-30 letters")
    return True


def word_count(text):
    """Count words in text (entry must contain exactly one)."""
    return len(text.split())

def main():
    """Write the chosen word to /output/entry.txt, then verify it."""
    validate_word(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read-back check: the file must be byte-identical to WORD, one word only.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "read-back mismatch"
    assert word_count(written) == 1, "entry must be exactly one word"
    print("Wrote entry: %s" % written)

if __name__ == "__main__":
    main()
