#!/usr/bin/env python3.7

import asyncio
import signal
import sys

import shared.config as config
from shared.proc import init, run
from shared.lemonbar import lemonbar


# pylint: disable=unused-argument
def signal_handler(signum, frame):
    sys.exit(signum)


async def main():

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(tcp_echo_client(message, loop))
    # loop.close()

    # blocks are configured in config.yaml
    print(config)
    blocks = config.config['blocks']

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
    asyncio.run(main())
