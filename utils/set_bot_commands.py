from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Перезапусить бота"),
        types.BotCommand("email", "Сохранить/Изменить почту"),
        types.BotCommand("phone", "Сохранить/Изменить номер телефона")
    ])