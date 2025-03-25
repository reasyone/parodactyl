from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy import Sequence, RowMapping, select, update
from sqlalchemy.orm import Session

from parodactyl_bot.infra.database.tables import Users, UserRoles

class UserRepository:
    def __init__(self, session: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session = session

    async def get_user_by_id(self, user_id: int) -> Sequence[RowMapping] | None:
        async with self.session() as session:
            query = select(Users).where(Users.id == user_id)
            result = await session.execute(query)
            return result.mappings().all()

    async def get_user_role(self, user_id: int) -> str:
        async with self.session() as session:
            query = select(UserRoles.role_name).join(Users, UserRoles.id == Users.role_id).where(Users.id == user_id)
            result = await session.execute(query)
            user_role = result.scalar()
            return user_role

    async def create_user(self, user_id: int, phone_number: str, username: str, full_name: str):
        async with self.session() as session:
            user = Users(
                id=user_id,
                role_id=1,
                phone_number=phone_number,
                username=username,
                full_name=full_name,
                city='None'
            )
            session.add(user)
            await session.commit()

    async def add_users_city(self, user_id: int, city: str) -> None:
        async with self.session() as session:
            query = update(Users).where(Users.id == user_id).values(city=city)
            await session.execute(query)
            await session.commit()

    async def update_users_role(self, user_id: int, role: str) -> None:
        async with self.session() as session:
            query = select(UserRoles).where(UserRoles.role_name == role)
            result = await session.execute(query)
            role_info = result.scalar()

            query = update(Users).where(Users.id == user_id).values(role_id=role_info.id)
            await session.execute(query)
            await session.commit()

    async def update_user_name(self, user_id: int, name: str) -> None:
        async with self.session() as session:
            query = update(Users).where(Users.id == user_id).values(full_name=name)
            await session.execute(query)
            await session.commit()

    async def update_user_city(self, user_id: int, city: str) -> None:
        async with self.session() as session:
            query = update(Users).where(Users.id == user_id).values(city=city)
            await session.execute(query)
            await session.commit()

    async def update_user_phone_number(self, user_id: int, phone_number: str) -> None:
        async with self.session() as session:
            query = update(Users).where(Users.id == user_id).values(phone_number=phone_number)
            await session.execute(query)
            await session.commit()
