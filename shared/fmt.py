#!/usr/bin/env python


def strfmt(s):
    if s == " ":
        return s
    try:
        return s.decode().strip()
    except (UnicodeDecodeError, AttributeError):
        return s.strip()
