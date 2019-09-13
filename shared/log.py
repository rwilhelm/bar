#!/usr/bin/env python

"""Logging facility
"""

import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)-12s \
                    %(levelname)-8s %(message)s",
                    datefmt="%m-%d %H:%M:%S",
                    filename=sys.argv[0] + ".log",
                    filemode="w")


async def log_stream(stream):
    logger = logging.getLogger('bar')
    async for line in stream:
        logger.error(line)
