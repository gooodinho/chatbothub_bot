from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command("email"))
async def add_email(message: types.Message, state: FSMContext):
    await message.answer("Пришлите Ваш email")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_email(email=email, id=message.from_user.id)
    await message.answer(f"Почта была сохранена -> {email}")
    await state.finish()


@dp.message_handler(Command("phone"))
async def add_email(message: types.Message, state: FSMContext):
    await message.answer("Пришлите Ваш номер телефона")
    await state.set_state("add_phone")


@dp.message_handler(state="add_phone")
async def enter_email(message: types.Message, state: FSMContext):
    phone = message.text
    db.update_phone(phone=phone, id=message.from_user.id)
    await message.answer(f"Номер телефона сохранён -> {phone}")
    await state.finish()
