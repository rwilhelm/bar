import json

from asyncio import sleep
import httpx
from h2.exceptions import StreamClosedError

from shared.log import get_logger
logger = get_logger('httpx')


#async with httpx.AsyncClient() as client:
#    r = await client.get('https://www.example.com/')
#r


async def get_request(url: str, oksleep=90, errsleep=180):

    async with httpx.AsyncClient() as client:

        try:
            res = await client.get(url)
            return json.loads(res.read())

        # httpx exceptions
        except httpx._exceptions.ConnectTimeout as e:
            logger.debug(e)
            await sleep(errsleep)
        except httpx._exceptions.ReadTimeout as e:
            logger.debug(e)
            await sleep(errsleep)
        except httpx._exceptions.WriteTimeout as e:
            logger.debug(e)
            await sleep(errsleep)
        except httpx._exceptions.PoolTimeout as e:
            logger.debug(e)
            await sleep(errsleep)

        except ConnectionResetError as e:
            logger.debug(e)
            await sleep(errsleep)

        except StreamClosedError as e:
            logger.debug(e)
            await sleep(oksleep)



        #response = await client.get('https://www.example.com/')
        #print(response)


    #timeout = httpx.TimeoutConfig(connect_timeout=5, read_timeout=5 * 60 write_timeout=5)
    #client = httpx.AsyncClient()

#    except httpx.exceptions.ConnectTimeout as e:
#        logger.debug(e)
#        await sleep(errsleep)


if __name__ == "__main__":
    print("A", __name__)
else:
    print("B", __name__)
