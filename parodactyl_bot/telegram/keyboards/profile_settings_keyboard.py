from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_changes_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить имя"),
            KeyboardButton(text="Изменить город"),
        ],
        [KeyboardButton(text="Изменить номер телефона")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выбери вариант",
)
