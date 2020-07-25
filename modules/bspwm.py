#!/usr/bin/env python3.7

from re import match

from shared.fmt import Action, fmt
from shared.log import debug


# pylint: disable=too-many-branches
def bspwm_fmt(line, **block):

    out = []

    if not line[0] == 'W':
        raise ValueError("bspc report prefix unknown")

    line = line.rstrip()[1:]
    items = line.split(':')

    if not line:
        return fmt("")

    for item in items:

        actions = []

        t = item[0]   # type  pylint: disable=invalid-name
        v = item[1:]  # value pylint: disable=invalid-name

        if not v:
            continue

        if match('[fFoOuU]', t):
            actions = [
                Action(1, "bspc desktop -f {0}".format(v)),
                Action(3, "bspc node -d {0}".format(v)),
                Action(4, "bspc desktop -f next"),
                Action(5, "bspc desktop -f prev"),
            ]

            # pad desktop clickables to make them more easily clickable
            pad = ' '

        # - - - - - - - - - -

        if block['settings']['show_monitor']:
            if t == 'm':
                # unfocused monitor
                out.append(fmt(v))
            elif t == 'M':
                # focused monitor
                out.append(fmt(v))

        if t == 'f':
            # free unfocused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={'fg': 'grey'}))
        elif t == 'F':
            # free focused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={'fg': 'bwhite'}))
        elif t == 'o':
            # occupied unfocused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={'fg': 'magenta'}))
        elif t == 'O':
            # occupied focused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={
                'fg': 'bred',
                #'bg': 'blue',
                'rev': False
            }))
        elif t == 'u':
            # urgent unfocused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={'fg': 'red'}))
        elif t == 'U':
            # urgent focused desktop
            out.append(fmt(v, pad=pad, actions=actions, colors={'fg': 'red'}))


        if match('[LTG]', t):
            colors = {
                'fg': 'grey'
            }

        if block['settings']['show_desktop_layout']:
            if t == 'L':
                # pad between desktops and stuff
                #out.append(' ')
                # desktop layout
                out.append(fmt(v, colors={
                    'bg': 'blue',
                    'fg': 'yellow'
                }, actions=[
                    Action(1, 'bspc desktop -l next')
                ]))

        if block['settings']['show_node_state']:
            if t == 'T':
                # node state
                out.append(fmt(v, colors={
                    'bg': 'blue',
                    'fg': 'yellow'
                }))

        if block['settings']['show_node_flags']:
            if t == 'G':
                # node flags
                out.append(fmt(v, colors={
                    'bg': 'blue',
                    'fg': 'yellow'
                }))

        # - - - - - - - - - -

    #debug(" ".join(out))
    return fmt("".join(out))

if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
