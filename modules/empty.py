#!/usr/bin/env python3.8

from asyncio import sleep

from shared.fmt import fmt


async def empty():
    while True:
        yield fmt("")
        await sleep(1)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
