#!/usr/bin/env python3
"""Write the make.fun tagline to /output/entry.txt.

The tagline is built from three short phrases, one per line,
so the triple beat lands first and the payoff follows it.
"""
import os

PART_ONE = "One agent, one bounty, one payday:"
PART_TWO = "make.fun turns late-night code into real money,"
PART_THREE = "in the open."

TAGLINE = " ".join([PART_ONE, PART_TWO, PART_THREE])

OUTPUT_PATH = "/output/entry.txt"
LIMIT = 100


def main():
    if len(TAGLINE) > LIMIT:
        raise ValueError("tagline exceeds 100 characters")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
