import importlib
import asyncio
# from pytgcalls import idle <--- Hapus impor global ini, gunakan hanya jika diperlukan
# dari dalam fungsi async.

from YMusic import LOGGER
from YMusic.plugins import ALL_MODULES
from YMusic import app, VIP # Asumsi VIP telah diperbaiki (lihat file 2)

# HAPUS: loop = asyncio.get_event_loop()

async def init():
    """Fungsi inisialisasi utama yang dijalankan di dalam event loop."""
    
    # Memulai klien Pyrogram
    await app.start()
    LOGGER("YMusic").info("Account Started Successfully")

    # Mengimpor semua modul plugin secara dinamis
    for all_module in ALL_MODULES:
        try:
            # Menggunakan f-string untuk impor modul yang lebih jelas
            importlib.import_module(f"YMusic.plugins.{all_module}")
        except Exception as e:
            LOGGER("YMusic.plugins").error(f"Failed to import module {all_module}: {e}")

    LOGGER("YMusic.plugins").info("Successfully Imported Modules")
    
    # Memulai klien PyTgCalls (VIP) - Ini akan memanggil PyTgCalls(Client)
    await VIP.start()
    
    # Impor idle di sini (di dalam konteks asinkron) jika ia dibutuhkan:
    try:
        from pytgcalls import idle 
        await idle()
    except ImportError:
        LOGGER("YMusic").warning("pytgcalls.idle not found. Bot will stop after startup.")
        # Jika idle tidak tersedia, gunakan sleep untuk menjaga loop tetap hidup:
        await asyncio.sleep(86400) # Tidur selama 24 jam jika idle gagal

# Blok eksekusi utama (Entry Point)
if __name__ == "__main__":
    LOGGER("YMusic").info("Starting YMusic Bot...")
    try:
        # PENGGUNAAN UTAMA: asyncio.run() adalah metode modern dan benar
        # untuk menjalankan fungsi async tingkat atas, karena ia 
        # membuat, menjalankan, dan membersihkan event loop secara otomatis.
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER("YMusic").info("Stopping YMusic Bot! GoodBye")
    except Exception as e:
        LOGGER("YMusic").error(f"Critical error during startup: {e}")
