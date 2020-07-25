#!/usr/bin/env python
from colour import Color
from shared.config import config

base16 = config["colors"]["base16"]


def gradient(val):
    gradient = list(Color("white").range_to(Color("red"), 10))
    return {'fg': gradient[round(val)-1].hex}


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
