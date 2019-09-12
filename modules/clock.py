from datetime import datetime
from asyncio import sleep

async def clock():
    while True:
        await sleep(1)
        yield datetime.today().strftime("D%Y-%m-%d-%H:%M").encode()

