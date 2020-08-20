from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.admin_callbacks import admin_callback


admin_menu = InlineKeyboardMarkup(inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Все пользователи",
                                             callback_data=admin_callback.new(command="all_users"))
                                     ],
                                    [
                                        InlineKeyboardButton(
                                            text="Рассылка",
                                            callback_data=admin_callback.new(command="message_all")
                                        )
                                    ]
                                 ])