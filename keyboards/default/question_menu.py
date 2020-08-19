from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

question_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [
                                            KeyboardButton(text="⬅️Назад")
                                        ]
                                    ])
