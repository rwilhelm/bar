#!/usr/bin/env python3.7

import asyncio
from re import match

from helpers import Action, block, run


# with Popen(["bspc", "subscribe", "report"], stdout=PIPE, bufsize=1,
#             universal_newlines=True) as p:


def fmt(line):
    # TODO
    red = "#cc475e"
    blue = "#475ecc"

    out = []

    if not line[0] == "W":
        return

    line = line.rstrip()[1:]
    items = line.split(":")

    for item in items:

        actions = []

        t = item[0]   # type  pylint: disable=invalid-name
        v = item[1:]  # value pylint: disable=invalid-name

        if not v:
            continue

        if match("[fFoOuU]", t):
            actions = [
                Action(1, "bspc desktop -f {0}".format(v)),
                Action(3, "bspc node -d {0}".format(v)),
                Action(4, "bspc desktop -f next"),
                Action(5, "bspc desktop -f prev"),
            ]

        # - - - - - - - - - -

        if t == "m":
            # unfocused monitor
            out.append(block(v))
        elif t == "M":
            # focused monitor
            out.append(block(v))

        elif t == "f":
            # free unfocused desktop
            out.append(block(v, actions=actions))
        elif t == "F":
            # free focused desktop
            out.append(block(v, actions=actions, fg=red))
        elif t == "o":
            # occupied unfocused desktop
            out.append(block(v, actions=actions, fg=blue))
        elif t == "O":
            # occupied focused desktop
            out.append(block(v, actions=actions, fg=red))
        elif t == "u":
            # urgent unfocused desktop
            out.append(block(v, actions=actions, fg=red))
        elif t == "U":
            # urgent focused desktop
            out.append(block(v, actions=actions, fg=red))

        elif t == "L":
            # focused desktop layout
            out.append(block(v, actions=[
                Action(1, "bspc desktop -l next")
            ]))

        elif t == "T":
            # focused node state
            out.append(block(v))

        elif t == "G":
            # focused node flags
            out.append(block(v))

        # - - - - - - - - - -

    return "".join(out)


async def desktops():
    yield await run(name="bspwm", cmd="bspc subscribe report", fmt=fmt)

if __name__ == "__main__":
    asyncio.run(desktops())
