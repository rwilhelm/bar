#!/usr/bin/env python3.7

from asyncio import sleep
from datetime import datetime

from shared.blocks import fmt

async def clock(block):
    clockfmt = block['settings']['clockfmt']
    while True:
        await sleep(1)
        line = datetime.today().strftime(clockfmt)
        yield fmt(line.strip(), block)
