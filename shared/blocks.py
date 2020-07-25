from shared.args import getopt
from shared.config import config

BLOCKS = {}


def stage(name: str, line: str) -> str:
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


def init():
    """Initialize the global BLOCKS dict by creating the dict and the
     keys according to the blocks configured. The values of static
     blocks are immediately stored. For non-static blocks the block
     name will be stored, which acts as a placeholder until the
     value of the block is updated. By creating the keys the order
     of the blocks is preserved in the order they are configured."""

    blocks = {}

    opts = getopt()
    if opts.blocks:
        for name in opts.blocks:
            try:
                blocks[name] = config["blocks"][name]
            except KeyError:
                print("Block not found: {}".format(name))
    else:
        blocks = config["blocks"]

    for name, block in blocks.items():
        if "static" in block:
            BLOCKS[name] = block["static"]
        else:
            # displayed as long as the module has not produced any output
            BLOCKS[name] = name  # LOADING...

    return blocks
