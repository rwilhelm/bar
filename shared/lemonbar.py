#!/usr/bin/env python3.7

from shared.config import config
from shared.proc import Proc


class Lemonbar(Proc):
    def __init__(self, bar: str = "lemonbar"):
        super(Lemonbar, self).__init__()
        cfg = config[bar]
        self.args = [
            "-g",
            "{}x{}+{}+{}".format(
                cfg.get("width", ""),
                cfg.get("height", ""),
                cfg.get("x", ""),
                cfg.get("y", ""),
            ),
        ]

        if "colors" in cfg:
            if "fg" in cfg["colors"]:
                theme, color = cfg["colors"]["fg"].split(".")
                self.args += ["-F", config["colors"][theme][color]]
            if "bg" in cfg["colors"]:
                theme, color = cfg["colors"]["bg"].split(".")
                self.args += ["-B", config["colors"][theme][color]]

        if "fonts" in cfg:
            if "font1" in cfg["fonts"]:
                self.args += ["-f", cfg["fonts"]["font1"]]

            if "font2" in cfg["fonts"]:
                self.args += ["-f", cfg["fonts"]["font2"]]

        if "regions" in cfg:
            self.args += ["-a", cfg["regions"]]

        if "offset" in cfg:
            self.args += ["-o", cfg["offset"]]

        if "name" in cfg:
            self.args += ["-n", cfg["name"]]

        if "hover" in cfg:
            self.args.append("-H")

        if "bottom" in cfg:
            self.args.append("-b")

        if "permanent" in cfg:
            self.args.append("-p")

        if "docking" in cfg:
            self.args.append("-d")


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    lemonbar = Lemonbar()
