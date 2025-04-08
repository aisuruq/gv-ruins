from datetime import datetime
from sqlalchemy import Float, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.utils import IdIntPkMixin


class Event(IdIntPkMixin, Base):

    name: Mapped[str]
    datetime: Mapped[datetime]
    met_place: Mapped[str]
    route: Mapped[str | None]
    guid: Mapped[str] = mapped_column(unique=False)
    cost: Mapped[float] = mapped_column(Float, nullable=True)
    max_participants: Mapped[int]
    description: Mapped[str] = mapped_column(Text, nullable=False)
    details: Mapped[str] = mapped_column(Text, nullable=True)

    participants = relationship("Participant", back_populates="event", cascade="all, delete-orphan")
