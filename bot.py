# Qo'shimcha va kerakli modullar
import asyncio
import logging
from ai_chat import chatting

# Asosiy modul
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# 1- usul .env faylidan kalit olish
from dotenv import get_key
TOKEN_1 = get_key(r"C:\Users\miuceo\PycharmProjects\telegram_bots\fn34_bot\.env","TOKEN")

# 2-usul .env faylidan kalit olish
from environs import Env
env = Env()
env.read_env()

TOKEN_2 = env.str("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    await message.reply(f"Assalomu alaykum {user.first_name}.\n\nGemini 2.0-flash yordamida quvvatlangan telegram botga xush kelibsiz!")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply("Yordam uchun @muhammadibrohimovceo ga murojaat qiling!")

@dp.message()
async def chat(message: Message):
    request = message.text
    responce = chatting(request)
    await message.answer(responce)


async def main():
    bot = Bot(token=TOKEN_2)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Exit")