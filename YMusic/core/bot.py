# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, <https://github.com/THE-VIP-BOY-OP>.
# This file is part of <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC> project,
# and is released under the "GNU v3.0 License Agreement".
# Please see <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE>
# All rights reserved.

import asyncio
import threading

import uvloop
from flask import Flask
from pyrogram import Client, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

import config

from ..logging import LOGGER

uvloop.install()

# Flask app initialize
app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running"


def run():
    app.run(host="0.0.0.0", port=8000, debug=False)


# VIPBot Class
class VIPBot(Client):
    def __init__(self):
        LOGGER(__name__).info("Starting Bot")
        super().__init__(
            "VIPMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = get_me.first_name + " " + (get_me.last_name or "")
        self.mention = get_me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )
        
async def anony_boot():
    bot = VIPBot()
    await bot.start()
    await idle()


if __name__ == "__main__":
    LOGGER(__name__).info("Starting Flask server...")

    # Start Flask server in a new thread
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    LOGGER(__name__).info("Starting VIPBot...")

    # Run the bot
    asyncio.run(anony_boot())

    LOGGER(__name__).info("Stopping VIPBot...")
