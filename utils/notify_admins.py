import logging

from aiogram import Dispatcher
from keyboards.inline.admin_question import admin_answer
from keyboards.inline.admin_callbacks import admin_callback
from data.config import admins


async def on_startup_notify(dp: Dispatcher, text):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, text)

        except Exception as err:
            logging.exception(err)


async def question_notify(dp: Dispatcher, text):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, text, reply_markup=admin_answer)

        except Exception as err:
            logging.exception(err)


async def order_notify(dp: Dispatcher, text):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, text)

        except Exception as err:
            logging.exception(err)
