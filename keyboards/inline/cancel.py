from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_menu = InlineKeyboardMarkup(inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Отмена",
                                             callback_data="cancel_action"
                                         )
                                     ]
                                 ])