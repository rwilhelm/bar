#!/usr/bin/env python

from datetime import datetime


def now():
    datetime.today().strftime("%Y-%m-%d-%H:%M:%S")


def strfmt(s):
    try:
        return s.decode().strip()
    except (UnicodeDecodeError, AttributeError):
        return s.strip()
