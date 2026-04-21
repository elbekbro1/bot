import asyncio
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

# --- 1. SOZLAMALAR ---
TOKEN = "7367306281:AAGlggmH0s82MNLVYJunxDpuS-tY_8j1S6k"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- 2. RENDER UCHUN SOXTA SERVER (PORT XATOLIGINI OLDINI OLISH) ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running...")

def run_health_check():
    # Render beradigan portni oladi (default 10000)
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    print(f"Health check server {port}-portda ishlamoqda...")
    server.serve_forever()

# --- 3. BOT FUNKSIYALARI ---

# Start komandasi
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! Men guruhdagi kirdi-chiqdi xabarlarini tozalovchi botman.")

# Yangi a'zo qo'shilganda xabarni o'chirish
@dp.message(F.new_chat_members)
async def delete_join_message(message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Xatolik (yangi a'zo): {e}")

# A'zo tark etganda xabarni o'chirish
@dp.message(F.left_chat_member)
async def delete_leave_message(message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Xatolik (tark etgan): {e}")

# --- 4. ASOSIY ISHGA TUSHIRISH ---
async def main():
    # Render portni topishi uchun serverni alohida oqimda yoqamiz
    threading.Thread(target=run_health_check, daemon=True).start()
    
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi")
