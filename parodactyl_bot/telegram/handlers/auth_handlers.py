from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from common.states import WaitingStates
from common.utils.enums import Cities
from common.utils.nominatim import get_city_by_coordinates
from parodactyl_bot.services.auth import auth_service
from parodactyl_bot.telegram.keyboards.auth_keyboard import request_location_keyboard, approve_keyboard, \
    manual_choose_city_keyboard

router = Router()


@router.message(
    F.contact,
    WaitingStates.waiting_for_phone,
)
async def contact_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    username = message.from_user.username
    full_name = message.from_user.first_name
    await auth_service.initial_add_user(user_id, phone_number, username, full_name)
    await state.set_state(WaitingStates.waiting_for_location)
    await message.bot.send_message(
        chat_id=user_id,
        text="Продолжим знакомство, отправьте мне вашу геолокацию.",
        reply_markup=request_location_keyboard
    )


@router.message(
    F.location.is_not(None),
    WaitingStates.waiting_for_location,
)
async def location_handler(message: Message, state: FSMContext):
    await state.clear()
    location = message.location
    city = get_city_by_coordinates(lat=location.latitude, lon=location.longitude)
    await state.set_state(WaitingStates.waiting_approve_city)
    await state.update_data(city=city)
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text=f"Ваш город {city}?",
        reply_markup=approve_keyboard
    )

@router.message(
    F.text.in_(("Выберу город из списка", "Нет")),
    WaitingStates.waiting_approve_city,
    )
async def manual_choose_city_handler(message: Message) -> None:
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="К нам подключены такие города: ",
        reply_markup=manual_choose_city_keyboard
    )

@router.message(
    F.text == "Да",
    WaitingStates.waiting_approve_city,
)
async def approve_city_handler(message: Message, state: FSMContext) -> None:
    state_data = await state.get_data()
    city = state_data.get('city')
    await state.clear()
    await auth_service.add_users_city(message.from_user.id, city)
    await state.set_state(WaitingStates.waiting_role_state)
    await answer_role(message)

@router.message(
    F.text.in_((Cities.MOSCOW.value, Cities.TULA.value)),
    WaitingStates.waiting_approve_city,
)
async def manual_choose_city_handler(message: Message, state: FSMContext) -> None:
    city = message.text
    await state.clear()
    await auth_service.add_users_city(message.from_user.id, city)
    await state.set_state(WaitingStates.waiting_role_state)
    await answer_role(message)

async def answer_role(message: Message) -> None:
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Ты пармастер?",
        reply_markup=approve_keyboard
    )

@router.message(
    F.text == "Да",
    WaitingStates.waiting_role_state,
)
async def approve_stream_master(message: Message, state: FSMContext) -> None:
    await state.clear()
    await auth_service.update_users_role(message.from_user.id, "admin")
    await message.bot.send_message(
        chat_id=message.from_user.id,
        text="Спасибо за предоставленную информацию!\n"
             "Для администрирования своего профиля услуг или продолжения использования бота вызови команду /menu",
        reply_markup=ReplyKeyboardRemove()
    )

