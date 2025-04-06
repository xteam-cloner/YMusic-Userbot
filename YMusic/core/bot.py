from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from ..logging import LOGGER

class YMusicBot(Client):
    def __init__(self):
        self.one = Client(
            name="YMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.SESSION_STRING),
            no_updates=True,
        )
        YMusicUser = PyTgCalls(YMusicBot)
