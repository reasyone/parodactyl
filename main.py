import logging

import asyncio

from aiogram import Dispatcher, Bot

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from parodactyl_bot.telegram.handlers.telegram_handlers import router as telegram_routers
from parodactyl_bot.telegram.handlers.auth_handlers import router as user_routers

# @click.group()
# def main() -> None:
#     """ Управление приложением """
#
# main.add_command(run)


TOKEN = "7685179558:AAGaLC89TIClZLJ17moTE4YGP55nCDjUV_w"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dispatcher = Dispatcher()
dispatcher.include_router(telegram_routers)
dispatcher.include_router(user_routers)

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
