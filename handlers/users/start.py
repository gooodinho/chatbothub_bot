import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import AdminFilter

from keyboards.default.main_menu import main_menu
from loader import dp, db


@dp.message_handler(CommandStart(), AdminFilter())
async def bot_start_admin(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    await message.answer(f"Привет Админ", reply_markup=None)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count_users = db.count_users()[0]
    await message.answer(f'Привет, {message.from_user.full_name}! Ты был занесён в базу. В базе <b>{count_users}</b>',
                         reply_markup=main_menu)

