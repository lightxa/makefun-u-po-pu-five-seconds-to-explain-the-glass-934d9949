"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

Pure Python 3.13 standard library, deterministic, no network.
"""

import os

# The cat's statement: a quality-control inspector's verdict.
# Counted specific (fourth inspection this week) plus one absurd
# detail (the floor signing for delivery); deadpan log voice,
# escalation in the last clause, no apology, no confession.
ENTRY = (
    "That glass failed its fourth water-level inspection this week, "
    "so I stamped it rejected and let the floor sign for delivery."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
