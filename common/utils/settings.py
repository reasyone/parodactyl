from functools import lru_cache
from pathlib import Path
from typing import TypeVar, Type, Literal

from pydantic import Extra
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

from common.utils.base_directory import PROJECT_DIR

T = TypeVar("T", bound="Settings")

ENV_FILE: Path = PROJECT_DIR / ".env"
ENV_FILE_ENCODING: Literal["utf-8"] = "utf-8"


class Settings(BaseSettings):
    """Базовый класс для чтения конфигов из переменных окружения и env-файла"""

    class Config:
        extra = Extra.ignore

    @classmethod
    def settings_customise_sources(
        cls: Type[T],
        settings_cls: Type[T],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return env_settings, dotenv_settings, file_secret_settings, init_settings

    @classmethod
    @lru_cache(typed=True)
    def get_settings(cls: Type[T]) -> T:
        """Создать/вернуть синглтон класса настроек"""
        return cls(_env_file=ENV_FILE, _env_file_encoding=ENV_FILE_ENCODING)
