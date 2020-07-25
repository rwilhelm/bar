from shared.args import getopt
from shared.config import config
from shared.log import get_logger
from typing import NamedTuple

logger = get_logger('blocks2')

class Action(NamedTuple):
    button: int = 1
    command: str = ""


class Block:
    def __init__(self, name: str, block: dict):
        self.name = name
        self.line = ""

        if "cmd" in block:
            self.type = "cmd"
        elif "func" in block:
            self.type = "func"
        elif "static" in block:
            self.type = "static"
        else:
            raise Exception

        self.actions = block.get("actions", None)
        self.colors = block.get("colors", None)
        self.pad = block.get("pad", None)

    def fmt(self, line: str, **kwargs):
        """Format the output string (ie a block) to be parsed by lemonbar."""

        actions = kwargs.get("actions", [])
        colors = kwargs.get("colors", {})
        pad = kwargs.get("pad", None)
        pfx = kwargs.get("pfx", [])
        sfx = kwargs.get("sfx", [])

        def add_actions(actions):
            for action in actions:

                if not isinstance(action, Action):
                    if getopt("debug"):
                        logger.debug("Action created: %s", action)
                    action = Action(action, actions[action])

                if action.button < 1 or action.button > 7:
                    raise ValueError(
                        "Invalid button assignment for action: {0}".format(
                            actions[action]
                        )
                    )

                pfx.append("%{{A{0}:{1}:}}".format(action.button, action.command))
                sfx.append("%{A}")

        def add_colors(fg=None, bg=None, rev=False):
            theme = get_colors("terminal")

            if getopt("debug"):
                logger.debug("Theme: %s", theme)
                logger.debug("Adding colors: fg=%s bg=%s rev=%s", fg, bg, rev)

            if fg:
                c = fg if fg[0] == "#" else theme[fg]
                pfx.append("%{{F{0}}}".format(c))
                sfx.append("%{F-}")

            if bg:
                c = bg if not bg[0] == "#" else theme[bg]
                pfx.append("%{{B{0}}}".format(theme[c]))
                sfx.append("%{B-}")

            if rev:
                pfx.append("%{R}")
                sfx.append("%{R-}")

        add_actions(actions)
        add_colors(**colors)

        if sfx:
            sfx.reverse()

        try:
            if pad:
                fmt_out = "".join(pfx + [pad + str(line) + pad] + sfx)
            else:
                fmt_out = "".join(pfx + [str(line)] + sfx)
            if getopt("debug"):
                logger.debug('Fmt out: "%s" (%s)', fmt_out, len(fmt_out))
            return fmt_out
        except TypeError as e:
            raise e

    def fmt_block(self):
        """Figure out the formatting function, call it with the given line and the
        parameters found in the given block. It will return a formatted string,
        parsable by lemonbar. This is called from run.py -> output -> stage."""

        if "fmt" in block.keys():
            func_name = block["fmt"]
            fmt_func = getattr(
                __import__("modules." + name, fromlist=[func_name]), func_name
            )
        else:
            fmt_func = fmt

        return fmt_func(line, **block)

    def stage(self, name: str, line: str) -> str:
        def build() -> str:
            last = None
            stage_out = []
            for name, block in BLOCKS.items():
                cur = config["blocks"][name]
                if (
                    name == "left"
                    or name == "leftc"
                    or name == "right"
                    or last
                    and "static" in last.keys()
                ):
                    stage_out.append(block)
                else:
                    stage_out.append(" ")
                    stage_out.append(block)

                last = cur

            stage_out = "".join(stage_out)
            return stage_out

        if not BLOCKS[name] == line:
            BLOCKS[name] = line

        return build()
