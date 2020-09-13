#!/usr/bin/env python3.8
# pylint: disable=no-member

import sys
from asyncio import sleep

from mpd.asyncio import MPDClient
#import tracemalloc

from shared.config import get_settings
from shared.fmt import fmt
from shared.log import get_logger


async def mpd():
    try:
        await client.connect(config["host"], config["port"])
        await client.password(config["password"])

        # >>>>>
        status = await client.status()
        if status["state"] == "play":
            colors = {'fg': 'green'}
        elif status["state"] == "pause":
            colors = {'fg': 'grey'}
        elif status["state"] == "stop":
            colors = {'fg': 'grey'}

        currentsong = await client.currentsong()
        if "title" in currentsong:
            title = currentsong["title"]
        else:
            title = ""

        yield fmt("{}".format(title), colors=colors, pad="")
        # <<<<<

    except Exception as e:
        print("MPD Connection failed: {}".format(e), file=sys.stderr)
        raise e

    while True:
        try:
            async for x in client.idle():
                logger.info(x)
                if "player" in x: # ['player', 'mixer']
                    try:
                        #await sleep(1)

                        # >>>>>
                        status = await client.status()
                        if status["state"] == "play":
                            colors = {'fg': 'green'}
                        elif status["state"] == "pause":
                            colors = {'fg': 'grey'}
                        elif status["state"] == "stop":
                            colors = {'fg': 'grey'}

                        currentsong = await client.currentsong()
                        if "title" in currentsong:
                            title = currentsong["title"]

                        yield fmt("{}".format(title), colors=colors)
                        # <<<<<

                    except Exception as e:
                        raise e
        except Exception as e:
            raise e



if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
    logger = get_logger("mpd")
    config = get_settings("mpd")
    client = MPDClient()
    #tracemalloc.start()
