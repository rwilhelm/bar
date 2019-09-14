#!/usr/bin/env python3.7

from asyncio import run, sleep
from datetime import datetime

from shared.helpers import get_config as c, print_block, yield_block


async def clock():
    clockfmt = c()['settings']['clockfmt']
    while True:
        yield datetime.today().strftime(clockfmt).strip()
        await sleep(1)


async def main():
    await yield_block(clock)

if __name__ == "__main__":
    run(print_block(clock))
