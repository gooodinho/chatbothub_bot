from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

order_menu = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [
                                         KeyboardButton(text="Написать создателям чат-ботов")
                                     ],
                                     [
                                         KeyboardButton(text="Свяжитесь со мной")
                                     ],
                                     [
                                         KeyboardButton(text="⬅️Назад")
                                     ]
                                 ])
