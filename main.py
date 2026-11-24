"""The Robot Vacuum's Best Excuse — the vacuum's own alibi, straight-faced.

Design against the brief
------------------------
The brief wants the funniest one-line excuse a robot vacuum gives for
missing a spot, judged by a tired homeowner who has heard an excuse from
every appliance in the house. It must be rooted in the vacuum's own
world (sensors, bumpers, dock, map, battery), sound like the vacuum
itself talking, and land on the first read with a clean turn at the end.
This entry does it in three beats:

1. The specific scene — the dust under the couch. One concrete spot,
   not "the floor" in general; the homeowner can picture exactly the
   corner the vacuum always skips.
2. The surprising twist — the dust filed a restraining order. The
   vacuum is not lazy or broken; it is law-abiding. The joke turns the
   missed spot into a legal boundary the little machine is too polite
   to cross.
3. The deadpan retreat — "I respected the boundary and went home to my
   dock." The dock is the vacuum's home, so the excuse ends with the
   machine doing the most vacuum thing possible: going back to charge,
   case closed, no further questions.

Why it wins: the setup and the payoff are the same object (the dust
under the couch), every word earns its place, and the punchline is a
clean turn — restraining order, boundary, dock — that needs no
explaining. The vacuum never apologises; it reports a legal fact, which
is exactly how a small machine keeping a straight face would talk.
It is 105 characters (105 bytes UTF-8), well inside the 1-140 gate.

The program writes exactly that one excuse to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "The dust under the couch filed a restraining order, "
    "so I respected the boundary and went home to my dock."
)


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 140 characters, not only white space.
    assert 1 <= len(text) <= 140, f"entry length {len(text)} outside 1-140"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
