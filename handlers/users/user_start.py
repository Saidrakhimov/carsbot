from aiogram import types

from loader import dp


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    pass
