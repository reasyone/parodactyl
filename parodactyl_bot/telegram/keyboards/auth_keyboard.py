from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

request_phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить номер телефона", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

request_location_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поделись геолокацией (доступно с телефона)", request_location=True)],
        [KeyboardButton(text="Выберу город из доступного списка")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="... отдыха"),
         KeyboardButton(text="... управления админкой")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

approve_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

manual_choose_city_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Москва"), KeyboardButton(text="Тула")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
