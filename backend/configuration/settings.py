from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    events: str = "/events"
    participants: str = "/participants"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    version: ApiV1Prefix = ApiV1Prefix()

    @property
    def v1(self) -> str:
        return f"{self.prefix}{self.version.prefix}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="XAK__",
    )
    api: ApiPrefix = ApiPrefix()


settings = Settings()
