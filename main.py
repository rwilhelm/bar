#!/usr/bin/env python3.7

import asyncio
import signal
import sys

from helpers import run

import modules.bspwm as bspwm
from modules.clock import clock


def signal_handler(signum, frame):  # pylint: disable=unused-argument
    sys.exit(signum)


async def main():
    await asyncio.gather(
        run("bspc", bspwm.desktops(), bspwm.fmt),
        run("xtitle", "xtitle -s"),
        run("clock", clock()))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main())  # pylint: disable=no-member
