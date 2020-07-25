
from asyncio import sleep
import os
import errno
from shared.config import get_settings
from shared.log import get_logger
from shared.fifo import mkfifo

async def crash():
    while True:
        yield
        await sleep(3)
        print("EXCEPTION ___ bla")
        raise Exception

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    logger = get_logger('fifo')
    config = get_settings('fifo')
