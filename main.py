#!/usr/bin/env python3.7

import asyncio
import signal
import sys

from shared.proc import init, run


import yaml


def signal_handler(signum, frame):  # pylint: disable=unused-argument
    sys.exit(signum)


async def main():
    config = yaml.safe_load(open("config.yaml"))

    # creates keys in output dictionary to have them properly ordered (creation
    # order seems to be maintained in dicts)
    init(config['blocks'])

    # pass all configured blocks async to the run method
    await asyncio.gather(*map(lambda x: run(x, config['blocks'][x]),
                              config['blocks']))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    asyncio.run(main())  # pylint: disable=no-member
