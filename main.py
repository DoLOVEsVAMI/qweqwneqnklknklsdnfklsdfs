
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import aiogram.dispatcher.filters as filters
from credits import token
import random


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("✅ Пока", "Амогус")
    keyboard.add("уцирцу", "йцйуцс")

    await message.answer("Привет!",reply_markup=keyboard, )


@dp.message_handler(commands=["random"])
async def number(message: types.Message):
    await message.answer(f'{random.randint(1,9)}')

@dp.message_handler(lambda message: message.text.lower() == "ещё")
async def qweqwe(message: types.Message):
    await message.answer(f'{random.randint(1,9)}')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)