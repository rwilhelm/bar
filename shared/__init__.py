from asyncio import sleep

from mpd.asyncio import MPDClient
from shared.config import get_settings
from shared.fmt import fmt
from shared.log import get_logger
from sys import stderr
