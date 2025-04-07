from pydantic import BaseModel
from typing import Optional


class CreateParticipants(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str] = None
    tg_username: str
    event_id: int
    # comment: Optional[str] = None

