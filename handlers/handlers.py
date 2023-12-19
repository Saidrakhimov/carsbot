from aiogram import types

from keyboards.default.deault_keyboards import *
from loader import dp


# from aiogram.dispatcher import FSMContext
# from states.user import RegisterState


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "salom!"
    await message.answer(text=text, reply_markup=main_menu)


# @dp.message_handler(text="Problems🔧")
# async def start_handler(message: types.Message):
#     text = "write to me if there is a problem https://t.me/Saidrakhimov_99"
#     await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text="Choose Cars")
async def start_handler(message: types.Message):
    text = "ok"
    await message.answer(text=text, reply_markup=cars_co)


@dp.message_handler(text="Germany 🇩🇪")
async def start_handler(message: types.Message):
    text = "German cars good choose"
    await message.answer(text=text, reply_markup=German)


@dp.message_handler(text="BMW")
async def start_handler(message: types.Message):
    text = "good choose"
    await message.answer(text=text, reply_markup=bmw)


@dp.message_handler(text="AUDI")
async def start_handler(message: types.Message):
    text = "German cars good choose"
    await message.answer(text=text, reply_markup=German)


@dp.message_handler(text="PORSCHE")
async def start_handler(message: types.Message):
    text = "good choose"
    await message.answer(text=text, reply_markup=German)


@dp.message_handler(text="🔚 Main menu")
async def start_handler(message: types.Message):
    text = "good choose"
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text="⬅️ Back")
async def start_handler(message: types.Message):
    text = "good choose"
    await message.answer(text=text, reply_markup=cars_co)


@dp.message_handler(text="Britan 🇬🇧 ")
async def start_handler(message: types.Message):
    text = "Save cars"
    await message.answer(text=text, reply_markup=Britain)


@dp.message_handler(text="American 🇺🇸")
async def start_handler(message: types.Message):
    text = "Save cars"
    await message.answer(text=text, reply_markup=us)
