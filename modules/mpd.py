#!/usr/bin/env python3.7

from asyncio import run, sleep

from mpd import MPDClient

from shared.helpers import get_config, print_block, yield_block


async def mpd():
    c = get_config()
    client = MPDClient()
    client.connect(c['settings']['host'], c['settings']['port'])
    client.password(c['settings']['password'])

    while True:
        yield client.currentsong()['title']
        await sleep(1)


async def main():
    await yield_block(mpd)

if __name__ == "__main__":
    run(print_block(mpd))
