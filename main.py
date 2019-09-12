#!/usr/bin/env python3.7


from asyncio.subprocess import PIPE
from datetime import datetime
from typing import List, Dict, Coroutine, Union
import asyncio
import signal
import sys
import logging

from modules.clock import clock


def signal_handler(signum, frame):
    sys.exit(0)


async def watch(stream, prefix=""):
    last = None
    async for line in stream:
        if last == None:
            last = line
            print(prefix + line.decode().strip())
        elif last == line:
            continue
        else:
            print(prefix + line.decode().strip())
            last = line


async def log(stream, prefix=""):
    async for line in stream:
        logger.error(line)


async def run(cmd, prefix=""):
    p = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    await asyncio.gather(watch(p.stdout, prefix), log(p.stderr, prefix))


async def main():
    await asyncio.gather(
        run("bspc subscribe report"),
        run("xtitle -s", "T"))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
                        datefmt="%m-%d %H:%M:%S",
                        filename="exec.log",
                        filemode="w")

    logger = logging.getLogger('bar')

    asyncio.run(main())
