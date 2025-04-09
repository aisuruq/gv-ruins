from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseModel):
    host: str
    user: str
    password: str
    name: str
    echo: bool = False
    max_overflow: int = 20
    pool_size: int = 50
    key_sheets: Path

    @property
    def url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.name}"
        )

    @property
    def url_alembic(self) -> str:
        return f"postgresql+psycopg2://{self.user}:{self.password}@localhost:5433/{self.name}"

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    events: str = "/events"
    participants: str = "/participants"
    payments: str = "/payments"


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
    db: DatabaseSettings


settings = Settings()
