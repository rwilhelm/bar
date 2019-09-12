#!/usr/bin/env python3.7

from helpers import run

async def report():
    await run("bspc subscribe report")

if __name__ == "__main__":
    asyncio.run(main())

