#!/usr/bin/env python

import sys
from typing import NamedTuple

from shared.config import config
from shared.fmt import strfmt


class Action(NamedTuple):
    button: int = 1
    command: str = ""


def fmt(string, block=None):
    """Format click actions for lemonbar
    """

    string = strfmt(string)

    pfx = []
    sfx = []
    pad = " "

    if block:
        if 'actions' in block:
            actions = block['actions']

            for action in actions:
                if not isinstance(action, Action):
                    action = Action(action, actions[action])
                if action.button < 1 or action.button > 7:
                    sys.stderr.write(
                        "Invalid button assignment for action: {0}"
                        .format(actions[action]))

                pfx.append("%{{A{0}:{1}:}}".format(action.button, action.command))
                sfx.append("%{A}")

        if 'colors' in block:
            c = config()['colors']['terminal']
            if 'fg' in block['colors']:
                color = c[block['colors']['fg']]
                pfx.append("%{{F{0}}}".format(color))
                sfx.append("%{F-}")

            if 'bg' in block['colors']:
                color = c[block['colors']['bg']]
                pfx.append("%{{B{0}}}".format(color))
                sfx.append("%{B-}")

        if 'static' in block:
            pad = ""
        elif 'pad' in block:
            pad = block['pad']

    return "".join(pfx + [pad, string, pad] + sfx)
