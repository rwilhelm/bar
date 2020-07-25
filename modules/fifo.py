
from asyncio import sleep
import os
import errno
from shared.config import get_settings
from shared.log import get_logger
from shared.fifo import mkfifo
FIFO = 'fifo'

async def fifo():
    try:
        os.mkfifo(FIFO)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise

    with open(FIFO) as fifo_in:
        while True:
            data = fifo_in.read().strip()
            if len(data) > 0:
                yield data
                await sleep(5)
                yield ""

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    logger = get_logger('fifo')
    config = get_settings('fifo')
