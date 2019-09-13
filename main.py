#!/usr/bin/env python3.7

import asyncio
import signal
import sys

from shared.config import config
from shared.proc import init, run


def signal_handler(signum, frame):  # pylint: disable=unused-argument
    sys.exit(signum)


async def main():

    # blocks are configured in config.yaml
    blocks = config()['blocks']

    if not blocks:
        print("No blocks configured")
        sys.exit(1)

    # creates keys in output dictionary to have them properly ordered (creation
    # order seems to be maintained in dicts)
    init(blocks)

    # pass all configured blocks async to the run method
    await asyncio.gather(*map(lambda x: run(x, blocks[x]), blocks))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main())  # pylint: disable=no-member
