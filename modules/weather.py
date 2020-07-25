#!/usr/bin/env python3.7
# pylint: disable=no-member

from asyncio import sleep

from shared.config import get_settings
from shared.fmt import fmt
from shared.http import get_request
from shared.log import get_logger

from json.decoder import JSONDecodeError

logger = get_logger("weather")
settings = get_settings("weather")

async def openweathermap():
    URL = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric".format(
        settings["city_id"], settings["openweathermap_api_key"]
    )

    while True:
        try:
            data = await get_request(URL)
        except JSONDecodeError as e:
            print(e)

        if data:
            try:
                temperature = data["main"]["temp"]
                summary = data["weather"][0]["description"].title()
            except (NameError, KeyError) as e:
                yield fmt("ERROR:{}".format(e))
                print(e)
                await sleep(90)
                continue

            yield fmt("{} {}".format(summary, temperature))

        await sleep(90)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
