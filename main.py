"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke to /output/entry.txt.
Deterministic: no network, no randomness, no external input.
The joke is a fixed string; the program always writes the same bytes.
"""

import os

JOKE = "I emailed the whole office begging them to stop replying all \u2014 47 people replied-all to agree."


def main() -> None:
    assert 1 <= len(JOKE) <= 199, "entry must be 1-199 characters"
    assert "\n" not in JOKE and JOKE.strip(), "entry must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
