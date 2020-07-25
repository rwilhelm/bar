import asyncio
from asyncio.subprocess import STDOUT, PIPE
import os
import subprocess

def run(args):
    cmd = subprocess.Popen(args,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)
    output, errors = cmd.communicate()
    #print(args, cmd.wait())
    return output.rstrip()

def above():
    run(["xdo", "above", "-t",
          run(["xdo", "id", "-n", "root"]),
          run(["xdo", "id", "-n", "lemonbar"])])
    #print("lemonbar above root")

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
