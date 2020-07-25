#!/usr/bin/env python

import sys


def list_blocks(blocks):
    for block_name, block_values in blocks.items():
        out = [block_name]
        allowed_execs = ['cmd', 'func', 'static']

        out += [item for sublist in
                [*[[k, v] for k, v in
                   list(block_values.items()) if k in
                   allowed_execs]] for item in
                sublist]

        print("{:15} {:10} {}".format(out[0], out[1], " ".join(out[2:])))

    sys.exit(1)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
