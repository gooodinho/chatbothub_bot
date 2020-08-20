from aiogram.types import CallbackQuery

from keyboards.inline.admin_menu import admin_menu
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin_callbacks import admin_callback
from loader import dp, db, bot
from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import AdminFilter


@dp.message_handler(Command("admin"), AdminFilter())
async def show_admin_cmd(message: types.Message):
    await message.answer("Приветствую на Базе, Господин!", reply_markup=admin_menu)


@dp.callback_query_handler(admin_callback.filter(command="all_users"), AdminFilter())
async def show_all_users(call: CallbackQuery):
    all_users = db.select_all_users()
    for user in all_users:
        await bot.send_message(chat_id=call.message.chat.id,
                               text=f"<b>User_id</b>: {user[0]}"
                               f"\n<b>User name: {user[1]}</b>"
                               f"\n<b>User email: {user[2]}</b>"
                               f"\n<b>User phone: {user[3]}</b>")


@dp.callback_query_handler(admin_callback.filter(command="answer_user"))
async def answer_user(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=2)
    user_id = call.message.text.partition('\n')[0]
    print(user_id)
    await state.set_state('question_answer')
    await state.update_data(user_id=user_id)
    await bot.send_message(chat_id=call.message.chat.id, text=f"Ответить пользователю {user_id}:")


@dp.message_handler(state="question_answer")
async def answer_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(chat_id=data.get("user_id"), text=message.text)
    await state.finish()
