#!/usr/bin/env python3.8
# pylint: disable=no-member

from asyncio import sleep
import psutil
from colour import Color
from shared.fmt import fmt
from shared.colors import gradient

async def load():
    while True:
        out = []
        for loadavg in psutil.getloadavg():
            #out.append(fmt(str(loadavg), colors=gradient(loadavg), pad=""))
            out.append(fmt(str(loadavg), pad=""))
        yield " ".join(out)
        await sleep(2)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
