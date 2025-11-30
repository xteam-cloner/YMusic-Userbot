import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

# Impor-impor lainnya
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
# Cukup impor PyTgCalls, jangan lakukan inisialisasi synchronous di sini
from pytgcalls import PyTgCalls 
# Import idle dari pytgcalls jika Anda ingin menggunakannya untuk menjaga bot tetap berjalan
from pytgcalls import idle 

import config

class Call:
    # Hapus PyTgCalls.__init__ karena kita akan menginisialisasi secara custom
    def __init__(self):
        # Menyimpan parameter konfigurasi
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH
        self.session_string = str(config.SESSION_STRING)
        
        # Variabel untuk klien Pyrogram dan PyTgCalls
        self.userbot: Union[Client, None] = None
        self.one: Union[PyTgCalls, None] = None
        
    async def start(self):
        """Metode asinkron untuk menginisialisasi dan memulai klien."""
        
        # 1. Inisialisasi Pyrogram Client (self.userbot)
        self.userbot = Client(
            name="VIPString",
            api_id=self.api_id,
            api_hash=self.api_hash,
            session_string=self.session_string,
            # Tambahkan konfigurasi lain jika perlu
        )
        
        # 2. Inisialisasi PyTgCalls Client (self.one)
        # Baris ini HANYA boleh berjalan di dalam konteks ASINKRON
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
        
# Inisialisasi objek Call, tetapi belum memulai klien PyTgCalls-nya.
VIP = Call()

# Catatan: Karena Anda mungkin memiliki fungsi handler dan dekorator lain
# dalam file-file Anda yang menggunakan VIP.userbot dan VIP.one, 
# pastikan kode tersebut berada DI BAWAH baris `VIP = Call()` dan tidak
# mencoba menggunakan `VIP.one` sebelum `VIP.start()` dipanggil.
