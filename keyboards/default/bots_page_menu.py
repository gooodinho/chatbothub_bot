from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bots_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(text="Что такое чат-боты ?")
                                    ],
                                    [
                                        KeyboardButton(text="Как чат-бот поможет мне прямо сейчас ?")
                                    ],
                                    [
                                        KeyboardButton(text="Какие бывают чат-боты ?")
                                    ],
                                    [
                                        KeyboardButton(text="⬅️Назад")
                                    ]
                                ])
