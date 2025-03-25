from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="services_menu", description="Меню поиска услуг"),
        BotCommand(command="profile_menu", description="Меню профиля"),
        BotCommand(command="help", description="Меню помощи"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

