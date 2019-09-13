#!/usr/bin/env python3.7

from re import match

from shared.blocks import Action, clean, fmt


def bspwm_fmt(line, block=None):
    """Custom format-functions should have a signature like
    func(line, block=None)."""

    line = clean(line)

    out = []

    if not line[0] == "W":
        raise ValueError("bspc report prefix unknown")

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

        if block['settings']['show_monitor']:
            if t == "m":
                # unfocused monitor
                out.append(fmt(v))
            elif t == "M":
                # focused monitor
                out.append(fmt(v))

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

        if match("[LTG]", t):
            pad = ""
            colors = {
                'bg': 'grey',
                'fg': 'black'
            }

        if block['settings']['show_desktop_layout']:
            if t == "L":
                # desktop layout
                out.append(fmt(v, {
                    'pad': pad,
                    'colors': colors,
                    'actions': [
                        Action(1, "bspc desktop -l next")
                    ],
                }))

        if block['settings']['show_node_state']:
            if t == "T":
                # node state
                out.append(fmt(v, {
                    'pad': pad,
                    'colors': colors
                }))

        if block['settings']['show_node_flags']:
            if t == "G":
                # node flags
                out.append(fmt(v, {
                    'pad': pad,
                    'colors': colors
                }))

        # - - - - - - - - - -

    return "".join(out)
