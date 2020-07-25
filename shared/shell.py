#!/usr/bin/env python3.7

from shared.config import config
from shared.proc import Proc

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    shell = Proc(config["wrapper"]["shell"])
