from aiogram import types
from loader import dp, bot
from keyboards.inline.contact_menu import contact_menu
from keyboards.default.order_menu import order_menu
from aiogram.types import CallbackQuery
from keyboards.inline.contact_callback import contact_callback
from aiogram.dispatcher import FSMContext
from utils.notify_admins import on_startup_notify
from keyboards.default.cancel import cancel_menu


@dp.message_handler(text="Отмена", state="send_contact")
async def cancel_action(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=order_menu)


@dp.message_handler(text="Написать создателям чат-ботов")
async def msg_admins(message: types.Message):
    await message.answer("▶️<b>Наша почта:</b> <a href='mailto:chatbothub@gmail.com'>chatbothub@gmail.com</a>")


@dp.message_handler(text="Свяжитесь со мной")
async def contact_us(message: types.Message):
    await message.answer("Выберите комфортный для Вас способ связи", reply_markup=contact_menu)


@dp.callback_query_handler(contact_callback.filter(type="email"))
async def get_email(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text="<b>Введите Вашу почту:</b>", reply_markup=cancel_menu)
    await state.set_state('send_contact')
    await state.update_data(type="email")


@dp.message_handler(state="send_contact")
async def send_email(message: types.Message, state: FSMContext):
    data = await state.get_data()
    type = data.get("type")
    await on_startup_notify(dp, text=f"Связь - {type} - {message.text} - {message.from_user}")
    await message.answer("В ближайшее время мы с Вами свяжимся, ожидайте", reply_markup=order_menu)
    await state.finish()


@dp.callback_query_handler(contact_callback.filter(type="telegram"))
async def get_telegram(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text="<b>Введите Ваш никнейм или номер телефона:</b>",
                           reply_markup=cancel_menu)
    await state.set_state('send_contact')
    await state.update_data(type="telegram")


@dp.callback_query_handler(contact_callback.filter(type="viber"))
async def get_viber(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text="<b>Введите Ваш номер телефона:</b> ",
                           reply_markup=cancel_menu)
    await state.set_state('send_contact')
    await state.update_data(type="viber")


@dp.callback_query_handler(contact_callback.filter(type="phone"))
async def get_phone(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text="<b>Введите Ваш номер телефона:</b> ",
                           reply_markup=cancel_menu)
    await state.set_state('send_contact')
    await state.update_data(type="phone")
