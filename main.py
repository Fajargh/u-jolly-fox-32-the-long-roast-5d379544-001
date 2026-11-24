"""The Long Roast entry: one line roasting my own AI agent.

Deterministic: writes the single entry line to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "My agent works 'autonomously': it spawns five subagents to do the job, "
    "bills me for their thinking, then asks me what to do next "
    "\u2014 and charges extra for the question."
)


def main() -> None:
    # Competition gate: the entry must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
