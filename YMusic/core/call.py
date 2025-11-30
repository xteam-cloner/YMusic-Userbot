import asyncio
from typing import Union

# Import-impor Pyrogram tetap di atas
from pyrogram import Client 

# HAPUS BARIS INI: from pytgcalls import PyTgCalls 
# Jika baris ini ada di sini, kesalahan akan muncul saat file ini diimpor!

import config

class Call:
    """Kelas untuk mengelola klien Pyrogram dan PyTgCalls."""

    def __init__(self):
        # Menyimpan konfigurasi
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH
        self.session_string = str(config.SESSION_STRING)
        
        # Inisialisasi klien sebagai None
        self.userbot: Union[Client, None] = None
        self.one: Union[object, None] = None
        
    async def start(self):
        """Metode asinkron untuk menginisialisasi dan memulai klien PyTgCalls."""
        
        # ⚠️ SOLUSI UTAMA: Impor PyTgCalls DI SINI (Deferred Import)
        # Baris ini HANYA dieksekusi setelah event loop dibuat dan berjalan.
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
            # Karena PyTgCalls diimpor saat runtime, kita perlu memastikan 
            # ia ada sebelum mencoba menghentikannya.
            try:
                await self.one.stop()
            except AttributeError:
                pass # Klien mungkin belum berhasil dimulai
        if self.userbot:
            await self.userbot.stop()
        print("Klien VIP telah dihentikan.")
        
# Inisialisasi objek Call yang aman di tingkat modul
VIP = Call()
