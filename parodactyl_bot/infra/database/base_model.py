from typing import ClassVar

from sqlalchemy import MetaData, Table, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column
from typing_extensions import no_type_check

from parodactyl_bot.infra.database.settings import DBSettings


class TableModel(DeclarativeBase):

    COLUMN_KEY: ClassVar[str] = "sa"

    __abstract__: ClassVar[bool] = True
    __allow_unmapped__ = True

    metadata = MetaData(schema=DBSettings.get_settings().app_schema)

    @classmethod
    @property
    @no_type_check
    def table(cls) -> Table:
        return cls.__table__


class Identifiable(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    __abstract__: ClassVar[bool] = True
