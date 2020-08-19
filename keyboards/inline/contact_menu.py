from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.contact_callback import contact_callback

contact_menu = InlineKeyboardMarkup(inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Почта📩",
                                             callback_data=contact_callback.new(type="email")
                                         )
                                     ],
                                    [
                                        InlineKeyboardButton(
                                            text="Telegram📨",
                                            callback_data=contact_callback.new(type="telegram")
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="Viber♈️",
                                            callback_data=contact_callback.new(type="viber")
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="Номер для звонка📞",
                                            callback_data=contact_callback.new(type="phone")
                                        )
                                    ]
                                 ])