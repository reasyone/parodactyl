from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove

import parodactyl_bot.telegram.keyboards.telegram_keyboard as kb
from parodactyl_bot.middleware.auth import AuthMiddleware

router = Router()
router.message.middleware(AuthMiddleware())


@router.message(CommandStart())
async def cmd_start_command(message: Message) -> None:
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        "Я Пародактиль.",
        reply_markup = ReplyKeyboardRemove()
    )

@router.message(F.text == "... отдыха")
async def cmd_start_relax(message: Message) -> None:
    await message.answer("Давай посмотрим, что у нас есть...", reply_markup=kb.relax_keyboard)

@router.message(F.text == "... управления админкой")
async def cmd_start_relax(message: Message) -> None:
    await message.answer("Что будем делать, босс...", reply_markup=kb.admin_keyboard)

@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer("Меню помощи.")
