#!/usr/bin/env python3.8
# pylint: disable=no-member

from asyncio import sleep

import os
import psutil

from shared.fmt import fmt

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

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


async def meta():
    while True:
        pid = os.getpid()
        py = psutil.Process(pid)
        # print(pid)
        mem = py.memory_info()[0]  #/2.**30 memory use in GB...I think
        cpu = py.cpu_percent()
        # print(pid, cpu, mem)

        yield fmt("{}:{}".format(str(cpu), bytes2human(round(mem, 2))), colors={'fg': 'grey'})
        await sleep(2)

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
