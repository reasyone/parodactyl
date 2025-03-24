from aiogram.types import User

from parodactyl_bot.infra.database.engine import session_factory
from parodactyl_bot.repository.auth import UserRepository


class AuthService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def check_auth(self, user_id: int) -> bool:
        if not await self.user_repository.get_user_by_id(user_id):
            return False
        return True

    async def initial_add_user(self, user_id: int, phone_number: str, username: str, full_name: str) -> None:
        await self.user_repository.create_user(user_id, phone_number, username, full_name)

    async def add_users_city(self, user_id: int, city: str) -> None:
        await self.user_repository.add_users_city(user_id, city)

    async def update_users_role(self, user_id: int, role: str) -> None:
        await self.user_repository.update_users_role(user_id, role)

auth_service = AuthService(UserRepository(session=session_factory()))
