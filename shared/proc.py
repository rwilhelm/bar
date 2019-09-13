#!/usr/bin/env python3.7
# pylint: disable=F0401

import asyncio
import logging
from asyncio import create_subprocess_shell as shell
from asyncio.subprocess import PIPE

import shared.blocks
from shared.blocks import clean
from shared.log import log_stream

FOUT = {}

log = logging.getLogger('bar')


def output(name, block, line=None):
    """Cleanup, format, store and output."""

    # Get custom format function or default
    fmt = getfmt(name, block)

    # Update
    if 'static' in block:
        line = block['static']
    else:
        line = clean(line)

    line = fmt(line, block)

    if FOUT[name] == line:
        return
    else:
        FOUT[name] = line

    # Output
    print("".join(FOUT.values()), flush=True)


async def watch(name, block, stream):
    """Read and deduplicate."""

    last = None
    async for line in stream:

        line = clean(line)

        if last == line:
            continue
        elif last is None:
            last = line
            logging.info("new %s", line)
            output(name, block, line)
        else:
            logging.info("chg %s", line)
            output(name, block, line)
            last = line


def getfmt(name, block):
    """Dynamically load a function to format the block."""

    if 'fmt' in block.keys():
        func_name = block['fmt']
        return getattr(__import__("modules." + name,
                                  fromlist=[func_name]), func_name)

    return shared.blocks.fmt


async def run(name, block):
    """Handles three types of blocks: (1) static blocks which do not change,
    (2) blocks that get their input from a subprocess and (3) blocks that are
    fed by a generator_function that yields strings."""

    # Static blocks
    if 'static' in block.keys():
        output(name, block)

    # Subprocess blocks
    elif 'cmd' in block.keys():
        proc = await shell(block['cmd'], stdout=PIPE, stderr=PIPE)
        await asyncio.gather(watch(name, block, proc.stdout), log_stream(proc.stderr))

    # Generator blocks
    elif 'func' in block.keys():
        func = block['func']
        func = getattr(__import__("modules." + func, fromlist=[func]), func)
        await watch(name, block, func(block))


def init(blocks):
    """By creating the keys in FOUT the order of our blocks is preserved like
    they are configured in config.yml."""

    for block in blocks:
        if 'static' in block:
            FOUT[block] = block['static']
        else:
            FOUT[block] = block  # LOADING...
