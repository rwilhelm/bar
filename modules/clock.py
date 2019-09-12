import asyncio
from time import sleep
from datetime import datetime

def clock():
    print(datetime.today().strftime("D%Y-%m-%d-%H:%M:%S"))

async def main():
    while true:
        clock()
        sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
