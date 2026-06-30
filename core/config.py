from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    #FROM DOCKER
    db_host: str
    db_port: int
    postgres_db: str

    postgres_user: str
    postgres_password: str

    #postgres
    driver: str = "postgresql+asyncpg"


    # RabbitMQ
    rabbit_host: str
    rabbit_port: int
    rabbit_user: str
    rabbit_password: str

    @property
    def database_url(self) -> str:
        return (
            f"{self.driver}://{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.postgres_db}"
        )

    @property
    def rabbit_url(self) -> str:
        return (
            f"amqp://{self.rabbit_user}:{self.rabbit_password}"
            f"@{self.rabbit_host}:{self.rabbit_port}/"
        )

_settings = Settings()

@lru_cache
def get_settings() -> Settings:
    return _settings