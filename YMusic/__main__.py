import importlib
import asyncio
from pytgcalls import idle # OK untuk diimpor di sini, tetapi pastikan PyTgCalls ditunda

from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES

# ⚠️ Variabel Global: Definisikan sebagai None dulu
# Asumsi: Anda juga perlu mengimpor VIPBot untuk bisa menginstansiasinya
from YMusic.core.bot import VIPBot 
from YMusic.core.call import Call # Asumsi VIPBot adalah Bot, dan VIP adalah Call

app = None # Klien Pyrogram (VIPBot)
VIP = None # Klien PyTgCalls (Call/Userbot)

# HAPUS: loop = asyncio.get_event_loop()
# HAPUS: app = VIPBot() # Ini memicu error!

async def init():
    """
    Fungsi inisialisasi utama yang dijalankan di dalam event loop.
    Semua instansiasi klien harus dilakukan di sini.
    """
    global app, VIP # Deklarasikan untuk memodifikasi variabel global

    # 1. Instansiasi Klien (Di dalam loop)
    # Ini aman karena event loop sudah dibuat oleh asyncio.run()
    app = VIPBot()
    VIP = Call()

    # 2. Memulai klien Pyrogram
    await app.start()
    LOGGER("YMusic").info("Account Started Successfully")

    # 3. Mengimpor semua modul plugin secara dinamis
    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"YMusic.plugins.{all_module}")
        except Exception as e:
            LOGGER("YMusic.plugins").error(f"Failed to import module {all_module}: {e}")

    LOGGER("YMusic.plugins").info("Successfully Imported Modules")
    
    # 4. Memulai klien PyTgCalls
    await VIP.start()
    
    # 5. Menjaga loop tetap hidup
    await idle()

# Blok eksekusi utama (Entry Point)
if __name__ == "__main__":
    LOGGER("YMusic").info("Starting YMusic Bot...")
    try:
        # Gunakan asyncio.run() untuk membuat, menjalankan, dan membersihkan loop
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER("YMusic").info("Stopping YMusic Bot! GoodBye")
    except Exception as e:
        LOGGER("YMusic").error(f"Critical error during startup: {e}")
