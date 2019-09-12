#!/usr/bin/python3

from re import match
from subprocess import Popen, PIPE

from shared.colors import red, blue
from shared.helpers import pp, Action

def bspc_report():
    with Popen(["bspc", "subscribe", "report"], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        for line in p.stdout:
            if line[0] == "W":

                out = []
                line = line.rstrip()[1:]
                items = line.split(":")

                for item in items:

                    t = item[0] # type
                    v = item[1:] # value
                    actions = []

                    if len(v) == 0:
                        continue

                    if match("[fFoOuU]", t):
                        actions = [
                            Action(1, "bspc desktop -f {0}".format(v)),
                            Action(3, "bspc node -d {0}".format(v)),
                            Action(4, "bspc desktop -f next".format(v)),
                            Action(5, "bspc desktop -f prev".format(v)),
                        ]

                    # - - - - - - - - - -

                    if t == "m":
                        # unfocused monitor
                        continue
                    elif t == "M":
                        # focused monitor
                        continue

                    elif t == "f":
                        # free unfocused desktop
                        out.append(pp(v, actions=actions))
                    elif t == "F":
                        # free focused desktop
                        out.append(pp(v, fg=red, actions=actions))
                    elif t == "o":
                        # occupied unfocused desktop
                        out.append(pp(v, fg=blue, actions=actions))
                    elif t == "O":
                        # occupied focused desktop
                        out.append(pp(v, fg=red, actions=actions))
                    elif t == "u":
                        # urgent unfocused desktop
                        out.append(pp(v, bg=red, actions=actions))
                    elif t == "U":
                        # urgent focused desktop
                        out.append(pp(v, bg=red, actions=actions))

                    elif t == "L":
                        # focused desktop layout
                        continue

                    elif t == "T":
                        # focused node state
                        continue

                    elif t == "G":
                        # focused node flags
                        continue

                    # - - - - - - - - - -

                #return "".join(out)
                print("".join(out), flush=True)
