import asyncio
import sys

from shared.args import getopt
from shared.helpers import clean

class Proc:
    def __init__(self, cmd: str = "lemonbar"):
        super(Proc, self).__init__()
        self.args = []
        self.cmd = cmd
        self.proc = None

    async def init(self):
        self.proc = await asyncio.create_subprocess_exec(
            self.cmd,
            *map(str, self.args),
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

    async def write(self, string: str):
        try:
            self.proc.stdin.write(bytes(string, "utf-8"))
            await self.proc.stdin.drain()
        except AttributeError as e:
            raise e
        except ConnectionResetError as e:
            print("Connection reset", file=sys.stderr)
            sys.exit(0) # exit old process
            #pass
            #raise e

    async def consume(self, generator: asyncio.streams.StreamReader):
        async for bstring in generator:
            try:
                self.proc.stdin.write(bstring)
                await self.proc.stdin.drain()
            except AttributeError as e:
                raise e

            if getopt("print_actions"):
                print(clean(bstring))
