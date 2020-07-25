#!/usr/bin/env python

import asyncio
import sys
#import tracemalloc
from asyncio import create_subprocess_shell as shell
from asyncio.subprocess import PIPE

from shared.args import getopt
from shared.blocks import stage
from shared.fmt import fmt_block
from shared.helpers import load, print_block, uniq
from shared.log import log_stream
from shared.lemonbar import lemonbar


def stdout(string):
    """Print string to stdout.
    """
    if string:
        try:
            print(string, flush=True)
        except BrokenPipeError:
            sys.exit(32)


async def output(name, block, line):
    final_string = stage(name, fmt_block(name, block, line))
    assert final_string
    if getopt("lemonbar") is True:
        await lemonbar.write(final_string)

    if getopt("print_wrapper") is True:
        stdout(final_string)


async def watch(name, block, stream):
    async for line in uniq(stream):
        if line:
            await output(name, block, line)


async def run(name: str, block: dict):
    """Handles three types of blocks: (1) static blocks which do
    not change, (2) blocks that get their input from a subprocess
    and (3) blocks that are fed by a generator_function that yields
    strings."""

    # Static blocks
    if "static" in block:
        await output(name, block, block["static"])

    # Subprocess blocks
    elif "cmd" in block.keys():
        # print("LOAD subprocess.{} -> {}".format(name, block['cmd']))
        proc = await shell(block["cmd"], stdout=PIPE, stderr=PIPE)
        await asyncio.gather(watch(name, block, proc.stdout), log_stream(proc.stderr))

    # Generator blocks
    elif "func" in block.keys():
        try:
            # print("LOAD modules.{} -> {}".format(name, block['func']))
            func = load(name, block["func"])
            await watch(name, block, func())
        except AttributeError as e:
            raise e


if __name__ == "__main__":
    # Blocks can be run independently from the main
    # loop with `python -m shared.run <blockname>.
    print("A", __name__)
    if len(sys.argv) > 1:
        try:
            asyncio.run(print_block(load(sys.argv[1], sys.argv[1])))
        except KeyboardInterrupt:
            sys.exit(0)
else:
    print("B", __name__)
    #tracemalloc.start()
