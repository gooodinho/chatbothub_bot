from aiogram import types

from aiogram.dispatcher import FSMContext
from keyboards.default.main_menu import main_menu
from keyboards.default.bots_page_menu import bots_menu
from keyboards.default.question_menu import question_menu
from keyboards.default.order_menu import order_menu
from utils.notify_admins import question_notify
from utils.misc import rate_limit
from loader import dp


@rate_limit(1, "Для чего нужны чат-боты?👾")
@dp.message_handler(text="Для чего нужны чат-боты?👾")
async def get_bots_page(message: types.Message):
    await message.answer("""<b>Что такое чат-бот?</b>

Чат-бот — это программа, отправляющая автоматические ответы пользователям в соцсетях, мессенджерах и на сайтах. 
С помощью чат-ботов можно упрощать коммуникацию с клиентами, используя алгоритмы искусственного интеллекта,
позволяющие имитировать диалог с живым человеком.
Они удерживают пользователя, дают охваты и уменьшают количество рутинной работы.
    """, reply_markup=bots_menu)


@rate_limit(1, "У меня есть вопрос👁")
@dp.message_handler(text="У меня есть вопрос👁")
async def ask_question(message: types.Message, state: FSMContext):
    await message.answer("Напишите Ваш вопрос, Вам скоро ответят", reply_markup=question_menu)
    await state.set_state("questions")


@rate_limit(1, "⬅️Назад")
@dp.message_handler(state="questions", text="⬅️Назад")
async def finish_questions(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Главное меню", reply_markup=main_menu)


@rate_limit(1)
@dp.message_handler(state="questions")
async def send_msg_to_adm(message: types.Message, state: FSMContext):
    await question_notify(dp, text="--------------------------------"
                                   f"<b>ID</b>{message.from_user.id}\n"
                                   "--------------------------------"
                                   f"<b>Full_name: </b>{message.from_user.full_name}\n"
                                   "--------------------------------"
                                   f"<b>Username: </b>{message.from_user.username}\n"
                                   "--------------------------------"
                                   f"<b>Сообщение: </b> {message.text}"
                                   "--------------------------------")

    await message.answer("В ближайшее время Вам прийдёт ответ в этом чате")


@rate_limit(1, "Хочу заказать 😈")
@dp.message_handler(text="Хочу заказать 😈")
async def order_func(message: types.Message):
    await message.answer("Выберите предпочтительный вариант связи", reply_markup=order_menu)


@rate_limit(1, "⬅️Назад")
@dp.message_handler(text="⬅️Назад")
async def show_main_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=main_menu)
