#!/usr/bin/env python3.7

import asyncio
from asyncio import create_subprocess_shell as shell
from asyncio.subprocess import PIPE

from shared.log import log_stream


async def lemonbar():

    args = ["lemonbar",
            "-g", "x35++",
            "-f", """Envy Code R:pixelsize = 22:style = Regular:antialias =
            true:autohint = true""",
            "-f", """Wuncon Siji:pixelsize = 22:style = Regular:antialias =
            true:autohint = true""",
            "-B", "#16130f",
            "-F", "#dbd6d1",
            "-n", "bar",
            "-H",
            "-a", "30",
            "-o", "-4"]

    proc = await shell(" ".join(args), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    await asyncio.gather(log_stream(proc.stdout), log_stream(proc.stderr))

if __name__ == "__main__":
    asyncio.run(lemonbar())
