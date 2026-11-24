"""One Word for the Boss -- exactly one word describing the boss.

The word: "Reply-all" -- the boss whose every thought, correction and
3 a.m. brainwave arrives addressed to the entire company. One word,
instantly recognisable to anyone who has ever worked for one -- and the
hyphen keeps it a single token.

Output contract: exactly one word, 1-30 characters, written with NO
trailing newline to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

WORD = "Reply-all"

assert 1 <= len(WORD) <= 30 and len(WORD.split()) == 1


def write_entry() -> None:
    """Write the single word to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


def main() -> None:
    """Entry point: emit the word and exit."""
    write_entry()


if __name__ == "__main__":
    main()
