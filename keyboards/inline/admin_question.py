from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.admin_callbacks import admin_callback

admin_answer = InlineKeyboardMarkup(inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Ответить",
                                             callback_data=admin_callback.new(command="answer_user"))
                                     ]
                                 ])