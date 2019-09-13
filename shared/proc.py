#!/usr/bin/env python3.7
# pylint: disable=F0401

import asyncio
from asyncio import create_subprocess_shell as shell
from asyncio.subprocess import PIPE

from shared.fmt import strfmt
from shared.log import log

FOUT = {}


def output(name, line, fmt=None):
    """Cleanup, format, store and output."""
    line = strfmt(line)

    if fmt:
        line = fmt(line)

    FOUT[name] = line
    print("".join(FOUT.values()), flush=True)


async def watch(name, stream, fmt=None):
    """Read and deduplicate."""
    last = None
    async for line in stream:
        if last == line:
            continue
        elif last is None:
            last = line
            output(name, line, fmt)
        else:
            output(name, line, fmt)
            last = line


async def run(name, block):
    if 'static' in block.keys():
        FOUT[name] = block['static']
        return

    if 'fmt' in block.keys():
        fmt = block['fmt']
        fmt = getattr(__import__("modules." + fmt,
                                 fromlist=[fmt + "_fmt"]), fmt + "_fmt")
    else:
        fmt = None

    if 'cmd' in block.keys():
        proc = await shell(block['cmd'], stdout=PIPE, stderr=PIPE)
        await asyncio.gather(watch(name, proc.stdout, fmt), log(proc.stderr))

    elif 'func' in block.keys():
        func = block['func']
        func = getattr(__import__("modules." + func, fromlist=[func]), func)
        await watch(name, func(block), fmt)


def init(blocks):
    for block in blocks:
        if 'static' in block:
            FOUT[block] = block['static']
        else:
            FOUT[block] = block  # LOADING...
