#!/usr/bin/env python3.7

import asyncio
from asyncio.subprocess import PIPE
from datetime import datetime
import logging
import signal
import sys
from typing import List, Dict, Coroutine, Union

import format
from helpers import run, watch
from modules.bspwm import report
from modules.clock import clock

def signal_handler(signum, frame):
    sys.exit(0)


async def main():
    await asyncio.gather(
        watch(clock()),
        run("bspc subscribe report"),
        run("xtitle -s", "T"))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main())
