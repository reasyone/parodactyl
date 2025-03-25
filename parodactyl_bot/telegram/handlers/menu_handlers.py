from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove

from parodactyl_bot.middleware.auth import AuthMiddleware
from parodactyl_bot.services.user import auth_service
from parodactyl_bot.telegram.keyboards import menu_keyboard as mk

start_router = Router()
start_router.message.middleware(AuthMiddleware())


@start_router.message(CommandStart())
async def cmd_start_command(message: Message) -> None:
    await message.answer(
        f"👋",
        reply_markup = ReplyKeyboardRemove()
    )


router = Router()


@router.message(Command("services_menu"))
async def services_menu_handler(message: Message) -> None:
    await message.answer(
        text="🧖",
        reply_markup=mk.services_menu_keyboard
    )
    await message.answer(
        text="Дальнейшее меню недоступно, ведется раработка",
    )
    await message.answer(
        text="❌",
    )


@router.message(Command("profile_menu"))
async def profile_menu_handler(message: Message) -> None:
    user_id = message.from_user.id
    if await auth_service.get_user_role(user_id) == 'admin':
        await message.answer(
            text="🧑‍💻",
            reply_markup=mk.profile_admin_menu_keyboard
        )
    else:
        await message.answer(
            text="🛠",
            reply_markup=mk.profile_user_menu_keyboard
        )
