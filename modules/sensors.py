from asyncio import sleep
from colour import Color
from shared.fmt import fmt

def fire(val, threshold):
    gradient = list(Color("darkseagreen").range_to(Color("dodgerblue"), threshold))
    return {'fg': gradient[round(val)-1].hex_l}

def colorize(val, high=80, crit=100):
    if val > crit:
        return {'bg': 'red', 'fg': 'white'}
    elif val > high:
        return {'fg': 'red', 'bg': 'white'}
    else:
        return fire(val, high)


async def sensors():
    t = [0.0, 0.0]
    while True:
        with open('/sys/class/hwmon/hwmon0/temp1_input', 'r', encoding="utf-8") as p:
            t[0] = float(p.read())/1000 # mainboard temperature?

        with open('/sys/class/hwmon/hwmon1/temp1_input', 'r', encoding="utf-8") as p:
            t[1] = float(p.read())/1000 # overall cpu temperature?

        yield fmt("{} {}".format(fmt(t[0], colors=colorize(t[0])), fmt(t[1], colors=colorize(t[1]))))
        await sleep(2)
