from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AgriSmart API"
    app_env: str = "development"
    debug: bool = True
    database_url: str = "postgresql+psycopg://agrismart:agrismart@localhost:5432/agrismart"
    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()
