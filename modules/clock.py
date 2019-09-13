#!/usr/bin/env python3.7

from asyncio import sleep
from datetime import datetime

from shared.blocks import block


def fmt(line):
    print(line)


async def clock():
    while True:
        await sleep(1)
        yield block(datetime.today().strftime("%Y-%m-%d-%H:%M:%S").encode())
