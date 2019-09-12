#!/usr/bin/env python3.7
# pylint: disable=invalid-name

"""Helper functions
"""

import asyncio
import logging
import sys
from asyncio.subprocess import PIPE
from datetime import datetime
from typing import NamedTuple


class Action(NamedTuple):
    """Action objects for bar clicks
    """
    button: int = 1
    command: str = ""


def fmt_actions(text, fg="", bg="", actions=None):
    """Format click actions for lemonbar
    """

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


def now():
    """It's the current year.
    """
    datetime.today().strftime("%Y-%m-%d-%H:%M:%S")


def fmt(line, prefix=""):
    """Format strings for lemonbar.
    """
    print(prefix + line.decode().strip())


async def watch(stream, prefix=""):
    """Deduplicate and forward given readable/stream,
    e.g. from subprocesses or generator functions."""
    last = None
    async for line in stream:
        if last is None:
            last = line
            fmt(line, prefix)
        elif last == line:
            continue
        else:
            fmt(line, prefix)
            last = line


async def run(cmd, prefix=""):
    """Run subprocess.
    """
    proc = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    await asyncio.gather(watch(proc.stdout, prefix), log(proc.stderr, prefix))


async def log(stream, prefix=""):
    """Log to facility.
    """
    logger = logging.getLogger('bar')
    async for line in stream:
        logger.error(prefix + line)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)-12s \
                        %(levelname)-8s %(message)s",
                        datefmt="%m-%d %H:%M:%S",
                        filename=sys.argv[0] + ".log",
                        filemode="w")
