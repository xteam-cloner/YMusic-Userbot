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
# HAPUS BARIS INI: from pytgcalls import PyTgCalls <--- (Ini penyebab error!)

import config

class Call:
    def __init__(self):
        # Menyimpan konfigurasi
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH
        self.session_string = str(config.SESSION_STRING)
        
        # Variabel untuk klien
        self.userbot: Union[Client, None] = None
        self.one: Union[object, None] = None # Gunakan 'object' karena PyTgCalls belum diimpor
        
    async def start(self):
        """Menginisialisasi dan memulai klien PYTGCALLS di dalam konteks ASYNCHRONOUS."""
        
        # ⚠️ IMPOR PYTGCALLS DI SINI (DEFERRED IMPORT)
        from pytgcalls import PyTgCalls 
        
        # 1. Inisialisasi Pyrogram Client
        self.userbot = Client(
            name="VIPString",
            api_id=self.api_id,
            api_hash=self.api_hash,
            session_string=self.session_string,
        )
        
        # 2. Inisialisasi PyTgCalls Client
        self.one = PyTgCalls(
            self.userbot,
            cache_duration=100,
        )
        
        # 3. Mulai kedua klien
        print("Memulai klien Pyrogram...")
        await self.userbot.start() 
        print("Memulai klien PyTgCalls...")
        await self.one.start()
        print("Klien VIP telah siap.")
        
    async def stop(self):
        """Metode asinkron untuk menghentikan klien."""
        if self.one:
            await self.one.stop()
        if self.userbot:
            await self.userbot.stop()
        print("Klien VIP telah dihentikan.")
        
# Inisialisasi objek Call yang AMAN
VIP = Call()
