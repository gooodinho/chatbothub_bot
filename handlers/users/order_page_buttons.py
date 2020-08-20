from aiogram import types
from loader import dp, bot
from keyboards.inline.contact_menu import contact_menu
from aiogram.types import CallbackQuery
from keyboards.inline.contact_callback import contact_callback
from aiogram.dispatcher import FSMContext
from utils.notify_admins import order_notify
from keyboards.inline.cancel import cancel_menu


@dp.callback_query_handler(text="cancel_action", state="send_contact")
async def cancel_action(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=10)
    await state.finish()
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text="Действие отменено")


@dp.message_handler(text="Написать создателям чат-ботов")
async def msg_admins(message: types.Message):
    await message.answer("▶️<b>Наша почта:</b> <a href='mailto:chatbothub@gmail.com'>chatbothub@gmail.com</a>")


@dp.message_handler(text="Свяжитесь со мной")
async def contact_us(message: types.Message):
    await message.answer("Выберите комфортный для Вас способ связи", reply_markup=contact_menu)


@dp.callback_query_handler(contact_callback.filter(type="email"))
async def get_email(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=10)
    await call.message.edit_text("<b>Введите Вашу почту:</b> ")
    await call.message.edit_reply_markup(cancel_menu)
    await state.set_state('send_contact')
    msg = call.message
    await state.update_data(msg=msg)


@dp.message_handler(state="send_contact")
async def send_email(message: types.Message, state: FSMContext):
    await order_notify(dp, text=f"Связь - {state} - {message.text}")
    data = await state.get_data()
    msg = data.get("msg")
    await msg.delete()
    await message.answer("В ближайшее время мы с Вами свяжимся, ожидайте")
    await state.finish()


@dp.callback_query_handler(contact_callback.filter(type="telegram"))
async def get_telegram(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.edit_text("<b>Введите Ваш никнейм или номер телефона:</b> ")
    await call.message.edit_reply_markup(cancel_menu)
    await state.set_state('send_contact')
    msg = call.message
    await state.update_data(msg=msg)


@dp.callback_query_handler(contact_callback.filter(type="viber"))
async def get_viber(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.edit_text("<b>Введите Ваш номер телефона:</b> ")
    await call.message.edit_reply_markup(cancel_menu)
    await state.set_state('send_contact')
    msg = call.message
    await state.update_data(msg=msg)


@dp.callback_query_handler(contact_callback.filter(type="phone"))
async def get_phone(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.edit_text("<b>Введите Ваш номер телефона:</b> ")
    await call.message.edit_reply_markup(cancel_menu)
    await state.set_state('send_contact')
    msg = call.message
    await state.update_data(msg=msg)
