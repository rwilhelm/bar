#!/usr/bin/env python3.7
# pylint: disable=no-member

from asyncio import sleep
from colour import Color
import psutil

from shared.fmt import fmt


def fire(val):
    gradient = list(Color("cornflowerblue").range_to(Color("red"), 100))
    return {'fg': gradient[round(val)-1].hex_l}


async def mem():
    while True:
        val = psutil.virtual_memory()[2] # used ram %
        yield fmt("{}%".format(val), colors=fire(val))
        await sleep(2)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
