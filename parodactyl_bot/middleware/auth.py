from typing import Callable, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from common.states import WaitingStates
from parodactyl_bot.services.auth import auth_service
from parodactyl_bot.telegram.keyboards.auth_keyboard import request_phone_keyboard, request_location_keyboard


class AuthMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        result = await handler(event, data)
        user_id = event.from_user.id
        if not await auth_service.check_auth(user_id):
            await data['state'].set_state(WaitingStates.waiting_for_phone)
            await event.bot.send_message(
                chat_id=user_id,
                text="К сожалению, мы не знакомы. Пожалуйста, отправьте ваш номер телефона.",
                reply_markup=request_phone_keyboard
            )
            return
        return result
