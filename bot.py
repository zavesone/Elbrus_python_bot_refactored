import time
import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

TOKEN = "7732949922:AAERQbyil4x2XhRjtGeEJiWwwZ9q1RHJceQ"
MSG = "Did you program today, {}?"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=}, {time.asctime()}')
    await message.reply(f"Howdy, {user_name}!")

    for i in range(10):
        await asyncio.sleep(2)
        await bot.send_message(user_id, MSG.format(user_name))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())