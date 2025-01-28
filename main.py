
import click
import asyncio

from aiogram import Dispatcher, Bot

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from parodactyl_bot.cli.start import run
from parodactyl_bot.handlers.telegram_handlers import router

# @click.group()
# def main() -> None:
#     """ Управление приложением """
#
# main.add_command(run)


TOKEN = "7685179558:AAGaLC89TIClZLJ17moTE4YGP55nCDjUV_w"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dispatcher = Dispatcher()
dispatcher.include_router(router)


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
