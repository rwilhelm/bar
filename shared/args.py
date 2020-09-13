#!/usr/bin/env python3.8

import argparse


def getopt(opt=None):
    parser = argparse.ArgumentParser(description="Lemonbar wrapper")
    _add_arguments(parser)
    args = parser.parse_args()
    if opt:
        if opt not in args:
            raise ValueError("Opt {} not found in args {}.".format(opt, args))
        return vars(args)[opt]
    return parser.parse_args()


def _add_arguments(parser):
    parser.add_argument(
        "-b",
        action="store_false",
        dest="lemonbar",
        default=True,
        help="Do not pipe wrapper output to lemonbar",
    )

    parser.add_argument(
        "-o",
        action="store_true",
        dest="print_wrapper",
        default=False,
        help="Print wrapper output to stdout",
    )

    parser.add_argument(
        "-a",
        action="store_true",
        dest="print_actions",
        default=False,
        help="Print actions stdout",
    )

    parser.add_argument(
        "-l",
        action="store_true",
        dest="debug",
        default=False,
        help="Log debug output",
    )

    parser.add_argument(
        "-d",
        action="store_true",
        dest="daemon",
        default=False,
        help="Fork to background",
    )

    parser.add_argument("blocks", nargs=argparse.REMAINDER)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    opts = getopt()
