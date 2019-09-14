import sys

import config

from shared.blocks import fmt


def get_config():
    return config.config['blocks'][sys._getframe(1).f_code.co_name]


async def print_block(func):
    async for data in yield_block(func):
        print(data)


async def yield_block(func):
    async for data in uniq(func):
        yield fmt(data, config.config['blocks'][func.__name__])


async def uniq(generator):
    last = None
    async for data in generator():
        if last == data:
            continue
        else:
            last = data
            yield data
