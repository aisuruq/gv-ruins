from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from configuration.settings import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        max_overflow: int = 10,
        pool_size: int = 5,
    ):
        self.engine = create_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_pre_ping=True,
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autocommit=False,
        )

    def dispose(self) -> None:
        self.engine.dispose()

    def session_getter(self) -> Generator[Session, None, None]:
        session = self.session_factory()
        return session


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
)
