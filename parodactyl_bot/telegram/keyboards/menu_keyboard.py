from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


services_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ищу баню"),
            KeyboardButton(text="Ищу пармастера"),
        ],
        [KeyboardButton(text="Ищу мероприятие")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выбери вариант",
)

profile_user_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Настройки профиля"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

profile_admin_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Личный кабинет"),
            KeyboardButton(text="Настройки профиля"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выбери вариант",
)
