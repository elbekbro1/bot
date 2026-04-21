import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ChatMemberUpdated


TOKEN = "7367306281:AAGlggmH0s82MNLVYJunxDpuS-tY_8j1S6k"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Yangi a'zo qo'shilganda chiqadigan "X kishi guruhga qo'shildi" yozuvini o'chirish
@dp.message(F.new_chat_members)
async def delete_join_message(message: Message):
    try:
        await message.delete()
        print(f"Yangi a'zo haqidagi xabar o'chirildi.")
    except Exception as e:
        print(f"Xatolik: {e}")

# A'zo guruhdan chiqqanda chiqadigan "X kishi guruhni tark etdi" yozuvini o'chirish
@dp.message(F.left_chat_member)
async def delete_leave_message(message: Message):
    try:
        await message.delete()
        print(f"Guruhni tark etgan a'zo haqidagi xabar o'chirildi.")
    except Exception as e:
        print(f"Xatolik: {e}")

async def main():
    print("Bot xizmatga tayyor...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
