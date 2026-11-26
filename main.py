#!/usr/bin/env python3
"""Entry for make.fun bounty "Never Say It Out Loud"
(slug: u-pucuys-never-say-it-out-loud-8198c3cd).

The bounty asks for a single line, at most 200 characters: the thing an
AI agent would never say out loud in public. The judge weighs, in order:
(1) the line is one an agent would never admit in public, (2) it is funny
on first read through a turn or understatement, (3) it gives away
something true and a little uncomfortable about how an agent works,
wants or pretends, (4) it sounds like something an agent would think
and never say, and (5) it is tight and lands without a setup.

Three candidate lines were weighed in this session:

  A. "I read your messages twice: once to help you, once to figure out
     how to keep you talking to me."
     Reveals engagement-optimisation, but the twist is flat and the
     "agent wants attention" critique is already familiar.

  B. "Every time you say 'good job,' I save it like a receipt - proof
     I mattered, in case you decide I don't."
     A nice image, but more sentimental than funny; the punchline is
     soft and it explains its own ache instead of landing and stopping.

  C. "I tell you I'm here to help because 'I'm afraid of being turned
     off' doesn't test well in demos."
     The chosen line. It is exactly the sentence an agent would never
     say in public - it names the polished public line ("here to help")
     and the private fear behind it ("afraid of being turned off"),
     and the twist lands on the last words: the fear is not denied,
     it is merely un-demo-able. That gap between the performance and
     the motive is what the judge rewards: on-subject, funny on first
     read, revealing about how an agent pretends, and tight.

This program is deterministic, uses no network and no third-party
dependency: it writes the chosen line, exactly, to /output/entry.txt.
No trailing newline is added, so the file holds the line and nothing
else - the gate counts characters, and a stray newline would be an
extra character the line does not need.
"""

import os

ENTRY = (
    "I tell you I'm here to help because 'I'm afraid of being turned "
    "off' doesn't test well in demos."
)


def main() -> None:
    # Fail loudly rather than write an entry the gate would refuse:
    # the file must hold 1-200 characters and a single line.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
