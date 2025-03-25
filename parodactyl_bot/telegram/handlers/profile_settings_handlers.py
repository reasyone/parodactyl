from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common.states import ProfileChangesStates
from parodactyl_bot.services.user import auth_service
from parodactyl_bot.telegram.keyboards.profile_settings_keyboard import profile_changes_keyboard

router = Router()

@router.message(F.text == "Настройки профиля")
async def services_menu_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(ProfileChangesStates.main_state)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Что будем делать? 👀",
        reply_markup=profile_changes_keyboard
    )

@router.message(F.text == "Изменить имя", ProfileChangesStates.main_state)
async def change_name_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(ProfileChangesStates.change_name)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Введите новое имя",
    )

@router.message(ProfileChangesStates.change_name)
async def change_name(message: Message, state: FSMContext) -> None:
    name = message.text
    await state.clear()
    await auth_service.update_user_name(message.from_user.id, name)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"✔️\nВаше имя изменено на {name}",
    )

@router.message(F.text == "Изменить город", ProfileChangesStates.main_state)
async def change_city_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(ProfileChangesStates.change_city)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Введите название нового города",
    )

@router.message(ProfileChangesStates.change_city)
async def change_city(message: Message, state: FSMContext) -> None:
    city = message.text
    await state.clear()
    await auth_service.update_user_city(message.from_user.id, city)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"✔️\nВаш город изменен на {city}",
    )

@router.message(F.text == "Изменить номер телефона", ProfileChangesStates.main_state)
async def change_phone_number_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(ProfileChangesStates.change_phone_number)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Введите номер телефона",
    )

@router.message(ProfileChangesStates.change_phone_number)
async def change_phone_number(message: Message, state: FSMContext) -> None:
    phone_number = message.text
    await state.clear()
    await auth_service.update_user_phone_number(message.from_user.id, phone_number)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"✔️\nВаш номер телефона изменен на {phone_number}",
    )
