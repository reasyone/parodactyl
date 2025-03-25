import logging

import asyncio

from parodactyl_bot.bot_client import dispatcher, bot
from parodactyl_bot.telegram.bot_commands import set_bot_commands
from parodactyl_bot.telegram.handlers.menu_handlers import start_router
from parodactyl_bot.telegram.handlers.menu_handlers import router as menu_router
from parodactyl_bot.telegram.handlers.auth_handlers import router as user_router
from parodactyl_bot.telegram.handlers.profile_settings_handlers import router as profile_settings_router


dispatcher.include_router(start_router)
dispatcher.include_router(user_router)
dispatcher.include_router(menu_router)
dispatcher.include_router(profile_settings_router)

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    await set_bot_commands(bot)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
