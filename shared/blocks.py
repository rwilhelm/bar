#!/usr/bin/env python

import sys
from typing import NamedTuple

from shared.fmt import strfmt


class Action(NamedTuple):
    button: int = 1
    command: str = ""


def block(text, fg="", bg="", actions=None):
    """Format click actions for lemonbar
    """

    text = strfmt(text)

    pfx = []
    sfx = []

    if actions:
        for action in actions[::-1]:
            if action.button < 1 or action.button > 7:
                sys.stderr.write(
                    "Invalid button assignment for action: {0}"
                    .format(action.command))

            pfx.append("%{{A{0}:{1}:}}".format(action.button, action.command))
            sfx.append("%{A}")

    if fg:
        pfx.append("%{{F{0}}}".format(fg))
        sfx.append("%{F-}")

    if bg:
        pfx.append("%{{B{0}}}".format(bg))
        sfx.append("%{B-}")

    return "".join(pfx + [" ", text, " "] + sfx)
