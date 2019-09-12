#!/usr/bin/env python3.7

import asyncio
import logging
import sys
from asyncio import create_subprocess_shell as shell
from asyncio.subprocess import PIPE
from datetime import datetime
from typing import NamedTuple

FOUT = {}

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)-12s \
                    %(levelname)-8s %(message)s",
                    datefmt="%m-%d %H:%M:%S",
                    filename=sys.argv[0] + ".log",
                    filemode="w")


class Action(NamedTuple):
    button: int = 1
    command: str = ""


class Colors(NamedTuple):
    black: str = "#16130f"     # base00, gray50
    red: str = "#cc475e"       # 350|65|80 red
    green: str = "#5ecc47"     # 110|65|80 green
    yellow: str = "#ccb647"    # 050|65|80 yellow
    blue: str = "#475ecc"      # 230|65|80 blue
    magenta: str = "#7447cc"   # 290|65|80 magenta
    cyan: str = "#47a0cc"      # 170|65|80 cyan
    white: str = "#beb6ae"     # base06, gray90
    grey: str = "#8C8A81"      # base01 black, bright
    bred: str = "#ff5975"      # 350|65|80 red
    bgreen: str = "#75ff59"    # 110|65|80 green
    byellow: str = "#ffe359"   # 050|65|80 yellow
    bblue: str = "#5975ff"     # 230|65|80 blue
    bmagenta: str = "#e359ff"  # 290|65|80 magenta
    bcyan: str = "#59c8ff"     # 170|65|80 cyan, light blue
    bwhite: str = "#f1f0ee"    # base07 white


colors = Colors()


def strfmt(s):
    try:
        return s.decode().strip()
    except (UnicodeDecodeError, AttributeError):
        return s.strip()


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


def now():
    datetime.today().strftime("%Y-%m-%d-%H:%M:%S")


def collect(block):
    pass


def output(name, line, fmt=None):
    line = strfmt(line)

    if fmt:
        line = fmt(line)

    FOUT[name] = line

    try:
        print("%{{l}}{bspwm} {xtitle}%{{r}}{clock}".format(
            bspwm=FOUT['bspwm'],
            xtitle=FOUT['xtitle'],
            clock=FOUT['clock'],
        ), flush=True)
    except KeyError as e:
        print("%{{c}}LOADING {}".format(e), flush=True)
        FOUT[e] = e
        pass


async def watch(name, stream, fmt=None):
    """Deduplicate and forward given readable/stream,
    e.g. from subprocesses or generator functions."""
    last = None
    async for line in stream:
        if last == line:
            continue
        elif last is None:
            last = line
            output(name, line, fmt)
        else:
            output(name, line, fmt)
            last = line


async def run(name, cmd, fmt=None):
    if isinstance(cmd, str):
        proc = await shell(cmd, stdout=PIPE, stderr=PIPE)
        await asyncio.gather(watch(name, proc.stdout, fmt), log(proc.stderr))
    else:
        await watch(name, cmd, fmt)


async def log(stream):
    logger = logging.getLogger('bar')
    async for line in stream:
        logger.error(line)


# if __name__ == "__main__":
