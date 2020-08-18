from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                keyboard=[
                                    [
                                        KeyboardButton(
                                            text="Для чего нужны чат-боты?👾"
                                        )
                                    ],
                                    [
                                        KeyboardButton(
                                            text="Хочу заказать 😈"
                                        )
                                    ],
                                    [
                                        KeyboardButton(
                                            text="У меня есть вопрос👁"
                                        )
                                    ]
                                ])
