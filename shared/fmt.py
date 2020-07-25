#!/usr/bin/env python3.7

from typing import NamedTuple

from shared.args import getopt
from shared.config import get_colors
from shared.log import get_logger


class Action(NamedTuple):
    button: int = 1
    command: str = ""


# class Fmt(NamedTuple):
#     line: str
#     pad: str
#     pfx: list
#     sfx: list


def fmt_block(name: str, block: dict, line: str):
    """Figure out the formatting function, call it with the given line and the
    parameters found in the given block. It will return a formatted string,
    parsable by lemonbar. This is called from run.py -> output -> stage."""

    if "fmt" in block.keys():
        func_name = block["fmt"]
        fmt_func = getattr(
            __import__("modules." + name, fromlist=[func_name]), func_name
        )
    else:
        fmt_func = fmt

    return fmt_func(line, **block)


def fmt(line: str, **kwargs):
    """Format the output string (ie a block) to be parsed by lemonbar."""

    actions = kwargs.get("actions", [])
    colors = kwargs.get("colors", {})
    pad = kwargs.get("pad", None)
    pfx = kwargs.get("pfx", [])
    sfx = kwargs.get("sfx", [])

    def add_actions(actions):
        for action in actions:

            if not isinstance(action, Action):
                if getopt("debug"):
                    logger.debug("Action created: %s", action)
                action = Action(action, actions[action])

            if action.button < 1 or action.button > 7:
                raise ValueError(
                    "Invalid button assignment for action: {0}".format(actions[action])
                )

            pfx.append("%{{A{0}:{1}:}}".format(action.button, action.command))
            sfx.append("%{A}")

    def add_colors(fg=None, bg=None, rev=False):
        theme = get_colors("terminal")

        if getopt("debug"):
            logger.debug("Theme: %s", theme)
            logger.debug("Adding colors: fg=%s bg=%s rev=%s", fg, bg, rev)

        if fg:
            c = fg if fg[0] == "#" else theme[fg]
            pfx.append("%{{F{0}}}".format(c))
            sfx.append("%{F-}")

        if bg:
            c = bg if not bg[0] == "#" else theme[bg]
            pfx.append("%{{B{0}}}".format(theme[c]))
            sfx.append("%{B-}")

        if rev:
            pfx.append("%{R}")
            sfx.append("%{R-}")

    add_actions(actions)
    add_colors(**colors)

    if sfx:
        sfx.reverse()

    try:
        if pad:
            fmt_out = "".join(pfx + [pad + str(line) + pad] + sfx)
        else:
            fmt_out = "".join(pfx + [str(line)] + sfx)
        if getopt("debug"):
            logger.debug('Fmt out: "%s" (%s)', fmt_out, len(fmt_out))
        return fmt_out
    except TypeError as e:
        raise e


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    logger = get_logger("fmt")
