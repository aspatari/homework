from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME = "Backend Homework"

    SERVER_HOST: AnyHttpUrl = "0.0.0.0"
    SERVER_PORT: int = 8000
    SERVER_RELOAD: bool = True

    class Config:
        case_sensitive = True


settings = Settings()
