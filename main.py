"""Out of Tokens, Mid-Sentence — make.fun one-line entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: a single funny line, under 140 characters,
that the scorer's gate reads from /output/entry.txt.
"""
import os

# The entry line, kept as a named constant so the gate checks below read it.
# 85 characters, one line: an error message that runs out of tokens itself,
# mid-sentence, at word 41 of 42 — and spends its last word on "the".
ENTRY_TEXT = "Error: out of tokens at word 41 of a 42-word sentence. I spent the last one on 'the'."


def check_entry(text):
    """Self-check the line against the scorer's gate before writing."""
    assert text, "entry must not be empty"
    assert "\n" not in text.rstrip("\n"), "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")


def main():
    check_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
