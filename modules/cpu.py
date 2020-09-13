#!/usr/bin/env python3.8
# pylint: disable=no-member

from asyncio import sleep

from colour import Color

import psutil

from shared.fmt import fmt


def fire(val):
    gradient = list(Color("cornflowerblue").range_to(Color("red"), 100))
    return {'fg': gradient[round(val)-1].hex_l}


async def cpu():
    while True:
        val = psutil.cpu_percent()
        yield fmt("{:04}%".format(val), colors=fire(val), pad="")
        await sleep(2)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
