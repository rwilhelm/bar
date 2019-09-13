#!/usr/bin/env python3.7

from re import match

from shared.blocks import Action, fmt


def bspwm_fmt(line):
    out = []

    if not line[0] == "W":
        return

    line = line.rstrip()[1:]
    items = line.split(":")

    for item in items:

        actions = []

        t = item[0]   # type  pylint: disable=invalid-name
        v = item[1:]  # value pylint: disable=invalid-name

        if not v:
            continue

        if match("[fFoOuU]", t):
            actions = [
                Action(1, "bspc desktop -f {0}".format(v)),
                Action(3, "bspc node -d {0}".format(v)),
                Action(4, "bspc desktop -f next"),
                Action(5, "bspc desktop -f prev"),
            ]

        # - - - - - - - - - -

        # if t == "m":
        #    # unfocused monitor
        #    out.append(fmt(v))
        # elif t == "M":
        #    # focused monitor
        #    out.append(fmt(v))

        if t == "f":
            # free unfocused desktop
            out.append(fmt(v, {'actions': actions}))
        elif t == "F":
            # free focused desktop
            out.append(fmt(v, {'actions': actions, 'colors': {'fg': 'red'}}))
        elif t == "o":
            # occupied unfocused desktop
            out.append(fmt(v, {'actions': actions, 'colors': {'fg': 'blue'}}))
        elif t == "O":
            # occupied focused desktop
            out.append(fmt(v, {'actions': actions, 'colors': {'fg': 'red'}}))
        elif t == "u":
            # urgent unfocused desktop
            out.append(fmt(v, {'actions': actions, 'colors': {'fg': 'red'}}))
        elif t == "U":
            # urgent focused desktop
            out.append(fmt(v, {'actions': actions, 'colors': {'fg': 'red'}}))

        #if match("[LTG]", t):
        #    pad = ""
        #
        #if t == "L":
        #    # focused desktop layout
        #    out.append(fmt(v, {
        #        'pad': pad,
        #        'actions': [
        #            Action(1, "bspc desktop -l next")
        #        ],
        #        'colors': {
        #            'bg': 'grey',
        #            'fg': 'black'
        #        }
        #    }))

        #if t == "T":
        #    # focused node state
        #    out.append(fmt(v, {
        #        'pad': pad,
        #        'colors': {
        #            'bg': 'grey',
        #            'fg': 'black'
        #        }
        #    }))

        #if t == "G":
        #    # focused node flags
        #    out.append(fmt(v, {
        #        'pad': pad,
        #        'colors': {
        #            'bg': 'red',
        #            'fg': 'black'
        #        }
        #    }))

        # - - - - - - - - - -

    return "".join(out)
