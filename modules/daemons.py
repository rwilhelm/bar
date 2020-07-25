import psutil
from asyncio import sleep

async def daemons():
    p = psutil.Process()

    while True:
        await sleep(2)
        process = [proc for proc in psutil.process_iter() if proc.name == "YourProcess.exe"]
        yield process


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
