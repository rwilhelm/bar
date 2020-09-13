#!/usr/bin/env python3.8
# pylint: disable=no-member

from asyncio import sleep

from colour import Color

import psutil

from shared.fmt import fmt


def colorize(val):
    if val > 3500:
        c = {'fg': 'red', 'rev': True}
    elif val > 1000:
        c = {'fg': 'red'}
    elif val > 500:
        c = {'fg': 'cyan'}
    elif val > 250:
        c = {'fg': 'green'}
    else:
        c = {'fg': 'grey'}
    return c


async def traffic():
    rx = 0
    tx = 0
    rxd = 0
    txd = 0
    rxdc = {}
    txdc = {}
    rxdf = 'rx'
    txdf = 'tx'
    while True:
        data = psutil.net_io_counters()

        if rx:
            rxd = round((data.bytes_recv - rx) / 1024, 2)
            rxdf = "{:07}".format(rxd)
            rxdc = colorize(rxd)

        if tx:
            txd = round((data.bytes_sent - tx) / 1024, 2)
            txdf = "{:06}".format(txd)
            txdc = colorize(txd)

        rx = data.bytes_recv
        tx = data.bytes_sent

        yield fmt("{} {}".format(fmt(rxdf, colors=rxdc), fmt(txdf, colors=txdc)))
        await sleep(2)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
