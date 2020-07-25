#!/usr/bin/env python3.7

import asyncio
import signal
import sys
import tracemalloc
import os

from shared.above import above
from shared.args import getopt
from shared.blocks import init
from shared.lemonbar import lemonbar
from shared.run import run
from shared.shell import shell

# pylint: disable=unused-argument
def signal_handler(signum, frame):
    sys.exit(signum)

async def main():
    blocks = init()
    procs = list(map(lambda x: run(x, blocks[x]), blocks))

    if getopt("lemonbar"):
        await lemonbar.init()
        await shell.init()
        procs.append(shell.consume(lemonbar.proc.stdout))
        await asyncio.sleep(.02)
        above()

    await asyncio.gather(*procs)


if __name__ == "__main__":
    print("A {}".format(__name__), file=sys.stderr)

    #tracemalloc.start()

    if getopt("daemon"):
        fpid = os.fork() # fork to 0
        if fpid != 0:
            sys.exit(0) # exit old process

    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main()) # loops forever

else:
    print("B {}".format(__name__), file=sys.stderr)
