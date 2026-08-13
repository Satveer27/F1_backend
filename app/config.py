import os
from pydantic_settings import BaseSettings, SettingsConfigDict


environment = os.getenv("APP_ENV", "dev")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=f".env.{environment}", extra="ignore")
    db_url: str
    log_sql: bool
    environment: str = environment

settings = Settings()