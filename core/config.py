from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    #POSTGRES
    db_host: str
    db_port: int
    db_name: str

    postgres_user: str
    postgres_password: str


    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.db_host}:"
            f"{self.db_port}/"
            f"{self.db_name}"
        )