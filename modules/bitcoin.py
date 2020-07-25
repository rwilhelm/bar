#!/usr/bin/env python3.7
# pylint: disable=no-member

from asyncio import sleep

from shared.fmt import fmt
from shared.http import get_request

url = "https://blockchain.info/ticker"


def colorize(val):
    if val > 10000:
        c = {'fg': 'red', 'rev': True}
    elif val < 9000:
        c = {'fg': 'bmagenta'}
    elif val < 8000:
        c = {'fg': 'bred'}
    else:
        c = {'fg': 'white'}
    return c


async def bitcoin():
    while True:
        res = await get_request(url)
        if res:
            val = res['EUR']['15m']
            yield fmt(val, colors=colorize(val))
            await sleep(900)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
