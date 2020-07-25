#!/usr/bin/env python3.7

from asyncio import sleep
from datetime import datetime

from shared.config import get_settings


async def clock():
    clockfmt = get_settings('clock', 'format')
    while True:
        yield datetime.today().strftime(clockfmt)
        await sleep(1)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
