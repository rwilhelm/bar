#!/usr/bin/env python3.7

import logging
from asyncio.subprocess import PIPE
import asyncio

from typing import NamedTuple

class Action(NamedTuple):
    button: int = 1
    command: str = ""

def pp(s, fg="", bg="", actions=[]):

    pre = []
    suf = []

    if len(actions) > 0:
        for action in actions[::-1]:

            if action.button < 1 or action.button > 7:
                sys.stderr.write("Invalid button assignment for action: {0}".format(action.command))
                return

            pre.append("%{{A{0}:{1}:}}".format(action.button, action.command))
            suf.append("%{A}")

    if fg:
        pre.append("%{{F{0}}}".format(fg))
        suf.append("%{F-}")

    if bg:
        pre.append("%{{B{0}}}".format(bg))
        suf.append("%{B-}")

    return "".join(pre + [" " , s, " "] + suf)


def now():
    datetime.today().strftime("%Y-%m-%d-%H:%M:%S")



def format(line, prefix=""):
    print(prefix + line.decode().strip())


async def watch(stream, prefix=""):
    last = None
    async for line in stream:
        if last == None:
            last = line
            format(line, prefix)
        elif last == line:
            continue
        else:
            format(line, prefix)
            last = line


async def run(cmd, prefix=""):
    p = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    await asyncio.gather(watch(p.stdout, prefix), log(p.stderr, prefix))


async def log(stream, prefix=""):
    async for line in stream:
        logger.error(line)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                        datefmt="%m-%d %H:%M:%S",
                        filename="exec.log",
                        filemode="w")

    logger = logging.getLogger('bar')

    asyncio.run(main())
