# bar

> My lemonbar helper :)

## How to add stuff

A block must have a key of `[func, cmd, static]`, where the value of `func`
must match the base filename of a python script in `modules/`. If the module
`bla` could not be found at `modules/bla.py` you'll see `ModuleNotFoundError:
No module named 'modules.bla'`. It sounds probably more complicated that it is.

## How to format stuff

Formatting specified in modules have priority over definitions in the yaml
config file.

## Prefixes and suffixes

In config.yaml `pfx` and `sfx` must be given as arrays. Additinally `prefix`
and `suffix` can be given, which will always be colored like ...

## What's not so great

* Uses quite a lot of RAM, like 120 Mb iirc.
* Building a thing like this around a rarely maintained or updated bar may be a
  little bit stupid. This should probably all be written in Rust.

## Dependencies

* https://git.suckless.org/dmenu
* https://git.suckless.org/slock
* https://git.suckless.org/st
* https://git.suckless.org/tabbed
* https://github,com/baskerville/Z
* https://github,com/baskerville/sxhkd
* https://github,com/baskerville/xtitle
* https://github.com/baskerville/bspwm
* https://github.com/krypt-n/bar
