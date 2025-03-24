from contextlib import asynccontextmanager
from functools import lru_cache
from typing import AsyncIterator

from sqlalchemy import Executable, text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncConnection, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from parodactyl_bot.infra.database.settings import DBSettings

@lru_cache(maxsize=1, typed=True)
def get_engine_singleton() -> AsyncEngine:
    config = DBSettings.get_settings()

    engine: AsyncEngine = create_async_engine(
        url=config.url,
        pool_size=config.start_pool_size,
        max_overflow=config.max_pool_size,
        pool_timeout=config.connection_timeout.seconds,
        echo=config.echo,
    )
    return engine


@asynccontextmanager
async def get_connection_ctx() -> AsyncIterator[AsyncConnection]:
    config = DBSettings.get_settings()
    engine = get_engine_singleton()

    async with engine.begin() as conn:
        await conn.execute(await _get_set_search_path_query(config.app_schema))
        await conn.execute(text(f"SET statement_timeout = '{config.statement_timeout}'"))
        yield conn

@lru_cache(maxsize=1, typed=True)
def session_factory() -> async_sessionmaker:
    return async_sessionmaker(
        get_engine_singleton(),
        class_=AsyncSession,
        expire_on_commit=False,
    )

async def _get_set_search_path_query(schema: str) -> Executable:
    return text(f"SET search_path TO {schema}")
