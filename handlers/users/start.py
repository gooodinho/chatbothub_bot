import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from utils.misc import rate_limit
from filters import AdminFilter
from utils.notify_admins import on_startup_notify
from keyboards.default.main_menu import main_menu
from loader import dp, db


@rate_limit(3, 'start')
@dp.message_handler(CommandStart(), AdminFilter())
async def bot_start_admin(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    await message.answer(f"Добро пожаловать, <b>Администратор - {name}!</b>", reply_markup=ReplyKeyboardRemove())


@rate_limit(3, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
        count_users = db.count_users()[0]
        await on_startup_notify(dp, "Новый пользователь: \n"
                                f"<b>ID:</b> {message.from_user.id}\n"
                                f"<b>Name:</b> {message.from_user.full_name}\n"
                                f"<b>Username:</b> {message.from_user.username}"
                                f"<b>Всего на Базе:</b> {count_users}")
    except sqlite3.IntegrityError as err:
        print(err)
    # CHANGE TEXT
    await message.answer(f'Привет, {message.from_user.full_name}!',
                         reply_markup=main_menu)

