#!/usr/bin/env python3.7

from asyncio import sleep
from datetime import datetime

from shared.blocks import fmt


async def clock(block):
    clockfmt = block['settings']['clockfmt']
    while True:
        await sleep(1)
        string = datetime.today().strftime(clockfmt).encode()
        yield fmt(string, block)
