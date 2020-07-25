from functools import wraps
from typing import NamedTuple

from shared.config import config
from shared.fmt import fmt_block


class Block(NamedTuple):
    name: str
    block: dict
    line: str


def clean(string: str) -> str:
    """Decodes the string and removes newlines, usually required for
    subprocess output."""
    try:
        return string.decode().strip()
    except AttributeError:
        try:
            return string.strip()
        except AttributeError:
            return string
    except UnicodeDecodeError:
        return string.strip()


# deduplicate generators
async def uniq(generator):
    last = None
    async for data in generator:
        if last == data:
            continue
        else:
            last = data
            yield clean(data)


async def print_block(func):
    async for data in yield_block(func):
        print(data)


# run -> yield_block -> uniq -> fmt -,
#        print <---------------------`
async def yield_block(func):
    async for line in uniq(func()):
        name = func.__name__
        block = config['blocks'][func.__name__]
        yield fmt_block(name, block, line)


def load(name: str, module: str):
    # -> from modules.<name> import <module>
    return getattr(__import__(
        "modules." + name, fromlist=[module]), module)


def iterate(iterable):
    iterator = iter(iterable)
    item = iterator.next()

    for next_item in iterator:
        yield item, next_item
        item = next_item

    yield item, None


def debug(func):
    @wraps(func)
    def wrapper(name: str, block: dict, line: str):
        # do something here
        func(name, block, line)
        # do something here
    return wrapper


def flatten(forest):
    # [leaf for tree in forest for leaf in tree]
    return [leaf for tree in forest if isinstance(tree, list) for leaf in tree]


def remove_null_string(lst: list) -> list:
    return [x for x in lst if x != '']
    # return [v for i, v in enumerate(lst) if i == 0 or v != lst[i-1]]


def pairwise(iterable):
    it = iter(iterable)
    #a = next(it, None)
    a = next(it)  # pylint: disable=stop-iteration-return
    for b in it:
        yield (a, b)
        a = b


def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
