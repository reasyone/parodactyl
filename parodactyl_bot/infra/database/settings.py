from datetime import timedelta

from common.utils.settings import Settings


class DBSettings(Settings):
    host: str
    password: str
    user: str
    name: str
    app_schema: str = "parodactyl"
    driver: str = "asyncpg"
    port: int = 5432
    start_pool_size: int = 5
    max_pool_size: int = 10
    connection_timeout: timedelta = timedelta(seconds=10)
    statement_timeout: str = "2min"
    echo: bool = False

    @property
    def url(self) -> str:
        schema = f"postgresql+{self.driver}"
        return f"{schema}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    class Config:
        env_prefix = "DB_"
