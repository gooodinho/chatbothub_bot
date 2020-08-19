from aiogram import types

from aiogram.dispatcher import FSMContext
from keyboards.default.main_menu import main_menu
from keyboards.default.bots_page_menu import bots_menu
from utils.notify_admins import question_notify
from loader import dp


@dp.message_handler(text="Для чего нужны чат-боты?👾")
async def get_bots_page(message: types.Message):
    # CHANGE TEXT
    await message.answer("""<b>Что такое чат-бот?</b>

Чат-бот — это программа, отправляющая автоматические ответы пользователям в соцсетях, мессенджерах и на сайтах. 
С помощью чат-ботов можно упрощать коммуникацию с клиентами, используя алгоритмы искусственного интеллекта,
позволяющие имитировать диалог с живым человеком.
Они удерживают пользователя, дают охваты и уменьшают количество рутинной работы.
    """, reply_markup=bots_menu)


@dp.message_handler(text="У меня есть вопрос👁")
async def ask_question(message: types.Message, state: FSMContext):
    await message.answer("Напишите Ваш вопрос, Вам скоро ответят", reply_markup=bots_menu)
    await state.set_state("questions")


@dp.message_handler(state="questions", text="⬅️Назад")
async def finish_questions(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Главное меню", reply_markup=main_menu)


@dp.message_handler(state="questions")
async def send_msg_to_adm(message: types.Message, state: FSMContext):
    await question_notify(dp, text=f"{message.from_user.id}\n"
                            f"{message.from_user.full_name}\n"
                            f"{message.from_user.username}\n"
                            f"Сообщение: {message.text}")


@dp.message_handler(text="⬅️Назад")
async def show_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_menu)
