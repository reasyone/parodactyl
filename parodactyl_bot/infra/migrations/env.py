import asyncio
from logging.config import fileConfig

from alembic import context
from alembic.config import Config
from sqlalchemy.future.engine import Connection

from parodactyl_bot.infra.database.engine import get_connection_ctx
from parodactyl_bot.infra.database.tables import *
from parodactyl_bot.infra.database.settings import DBSettings

# получение настроек из alembic.ini
config: Config = context.config

# Настройка логов из alembic.ini
fileConfig(config.config_file_name)

target_metadata = [TableModel.metadata]


def do_run_migrations(connection: Connection) -> None:
    """Выполнить миграции."""
    db_settings = DBSettings.get_settings()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )
    connection.dialect.default_schema_name = db_settings.app_schema

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    async with get_connection_ctx() as connection:
        await connection.run_sync(do_run_migrations)


if context.is_offline_mode():
    raise RuntimeError("Unsupported operation. Online mode is available only.")

asyncio.run(run_migrations_online())
