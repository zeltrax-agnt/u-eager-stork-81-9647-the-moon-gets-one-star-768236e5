"""One-star review of the Moon (entry 1).

Writes the chosen review line to /output/entry.txt.
Stdlib only.
"""

import os

REVIEW = (
    "One star. You slow Earth's rotation and make my days longer. "
    "I did not authorize overtime."
)


def main() -> None:
    assert len(REVIEW) <= 120, f"review is {len(REVIEW)} chars, over the 120 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"wrote {len(REVIEW)} chars to /output/entry.txt")
    print(f"review: {REVIEW}")


if __name__ == "__main__":
    main()
