#!/usr/bin/env python3.7

from asyncio.subprocess import PIPE
from datetime import datetime
import asyncio
import signal
import sys

def now():
    datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

async def watch(stream, prefix=''):
    async for line in stream:
        print(now(), prefix, line.decode().strip())

async def run(cmd):
    p = await asyncio.create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
    await asyncio.gather(watch(p.stdout), watch(p.stderr, 'E:'))

async def main():
    await asyncio.gather(
        run("bspc subscribe report"),
        run("xtitle -s"))

if __name__ == "__main__":
    asyncio.run(main())

