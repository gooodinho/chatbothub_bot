from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bots_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(text="Назад")
                                    ]
                                ])
