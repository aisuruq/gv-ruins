from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base
from src.models.utils import IdIntPkMixin


class Participant(IdIntPkMixin, Base):
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    phone: Mapped[str]
    tg_username: Mapped[str]

    comment: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    event = relationship("Event", back_populates="participants")
    payment: Mapped[int]
    prepayment: Mapped[float] = mapped_column(default=0.0)
    people_count: Mapped[int] = mapped_column(default=0)
    
    # balance_of_payment: Mapped[Float] = mapped_column(default=0.0)
