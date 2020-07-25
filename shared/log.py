#!/usr/bin/env python

import logging
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    filename=sys.argv[0] + ".log",
    filemode="w",
)


def debug(*args):
    logger = logging.getLogger("debug")
    logger.debug(*args)


def get_logger(name=None):
    if not name:
        # pylint: disable=protected-access
        name = sys._getframe(1).f_code.co_name
    return logging.getLogger(name)


async def log_stream(stream, name=None):
    if not name:
        name = sys._getframe(1).f_code.co_name
    logger = logging.getLogger(name)
    async for line in stream:
        logger.error(line)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
