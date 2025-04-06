import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from ntgcalls import TelegramServerError
from pyrogram import Client
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    FloodWait,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls
from pytgcalls.exceptions import AlreadyJoinedError, NoActiveGroupCall
from pytgcalls.types import (
    JoinedGroupCallParticipant,
    LeftGroupCallParticipant,
    MediaStream,
    Update,
)
from pytgcalls.types.stream import StreamAudioEnded

import config

class Call(PyTgCalls):
    def __init__(self):
        self.userbot = Client(
            name="VIPString",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.SESSION_STRING),
        )
        self.one = PyTgCalls(
            self.userbot,
            cache_duration=100,
        )
