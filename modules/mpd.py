#!/usr/bin/env python3.7

from asyncio import sleep

from mpd import MPDClient

from shared.blocks import fmt


async def mpd(block={}):
    client = MPDClient()
    client.connect("localhost", 6600)
    client.password("blub")
    while True:
        await sleep(1)
        yield fmt(client.currentsong()['title'], block)
