from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import parodactyl_bot.keyboards.telegram_keyboard as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n"
        f"Я Пародактиль.\n"
        f"Попаримся?"
    )
    await message.answer("Так вот...", reply_markup=kb.main_keyboard)


@router.message(Command('help'))
async def cmd_help(message: Message) -> None:
    await message.answer("Меню помощи.")


@router.message(F.text == "Ищу где отдохнуть")
async def cmd_relax (message: Message) -> None:
    await message.answer("Давай посмотрим, что у нас есть...", reply_markup=kb.relax_keyboard)


@router.message(F.text == "Я босс")
async def cmd_relax (message: Message) -> None:
    await message.answer("Что будем делать, босс...", reply_markup=kb.admin_keyboard)
