from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AgriSmart API"
    app_env: str = "development"
    debug: bool = True
    database_url: str = "postgresql+psycopg://agrismart:agrismart@localhost:5432/agrismart"
    api_v1_prefix: str = "/api/v1"
    jwt_secret: str = "change-this-secret-in-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
settings = Settings()
