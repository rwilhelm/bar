#!/usr/bin/env python3.7
"""Lemonbar wrapper
"""

import asyncio
import signal
import sys

from helpers import run, watch

from modules.clock import clock


def signal_handler(signum, frame):  # pylint: disable=unused-argument
    """Handle Ctrl-C.
    """
    sys.exit(signum)


async def main():
    """Asynchrounosly run subprocesses and functions.
    """
    await asyncio.gather(
        watch(clock()),
        run("bspc subscribe report"),
        run("xtitle -s", "T"))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main())  # pylint: disable=no-member
