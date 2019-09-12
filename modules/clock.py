#!/usr/bin/env python3.7
"""
"""

from asyncio import sleep
from datetime import datetime
from helpers import block, colors as c


def clock_format(line):
    print(line)


async def clock():
    while True:
        await sleep(1)
        yield block(datetime.today().strftime("%Y-%m-%d-%H:%M:%S").encode(),
                    fg=c.bwhite)
