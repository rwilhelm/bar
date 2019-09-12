#!/usr/bin/python3

from typing import NamedTuple

class Action(NamedTuple):
    button: int = 1
    command: str = ""


def pp(s, fg="", bg="", actions=[]):

    pre = []
    suf = []

    if len(actions) > 0:
        for action in actions[::-1]:

            if action.button < 1 or action.button > 7:
                sys.stderr.write("Invalid button assignment for action: {0}".format(action.command))
                return

            pre.append("%{{A{0}:{1}:}}".format(action.button, action.command))
            suf.append("%{A}")

    if fg:
        pre.append("%{{F{0}}}".format(fg))
        suf.append("%{F-}")

    if bg:
        pre.append("%{{B{0}}}".format(bg))
        suf.append("%{B-}")

    return "".join(pre + [" " , s, " "] + suf)


def now():
    datetime.today().strftime("%Y-%m-%d-%H:%M:%S")

