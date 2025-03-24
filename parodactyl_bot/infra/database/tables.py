from typing import ClassVar

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from parodactyl_bot.infra.database.base_model import TableModel, Identifiable


class Users(TableModel, Identifiable):
    __tablename__: ClassVar[str] = "users"

    role_id: Mapped[int] = mapped_column(Integer)
    username: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String)
    city: Mapped[str] = mapped_column(String)

class UserRoles(TableModel, Identifiable):
    __tablename__: str = "user_roles"

    role_name: Mapped[str] = mapped_column(String)
