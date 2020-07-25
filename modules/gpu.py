#!/usr/bin/env python3.7
# pylint: disable=no-member

from asyncio import sleep
from colour import Color
from py3nvml.py3nvml import *

from shared.fmt import fmt

def fire(val, threshold):
    gradient = list(Color("white").range_to(Color("red"), threshold))
    return {'fg': gradient[round(val)-1].hex_l}


async def gpu():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)

    while True:
        temperature = nvmlDeviceGetTemperature(handle, 0)
        threshold = nvmlDeviceGetTemperatureThreshold(handle, 0)
        gpu = nvmlDeviceGetUtilizationRates(handle).gpu
        mem = nvmlDeviceGetUtilizationRates(handle).memory
        yield fmt("{:02}C {:02}% {:02}%".format(temperature, gpu, mem),
                  colors=fire(temperature, threshold), pad="")
        await sleep(1)

    nvmlShutdown() # FIXME


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
