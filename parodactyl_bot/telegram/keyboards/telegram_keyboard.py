from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ищу где отдохнуть"),
         KeyboardButton(text="Я босс")],
        [KeyboardButton(text="О нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню...",
)

relax_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ищу баню", callback_data="searching_bathhouse")],
        [InlineKeyboardButton(text="Ищу пармастера", callback_data="searching_stream_master")],
        [InlineKeyboardButton(text="Ищу мероприятие", callback_data="searching_event")],
    ],
)

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Мои бани", callback_data="my_bathhouse"),
         InlineKeyboardButton(text="Мои мероприятия", callback_data="my_events")],
        [InlineKeyboardButton(text="Личный кабинет", callback_data="personal_account"),
         InlineKeyboardButton(text="Настройки профиля", callback_data="profile_settings")],
    ],
)


role_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="... отдыха"),
         KeyboardButton(text="... управления админкой")],
    ],
    resize_keyboard=True,
)
