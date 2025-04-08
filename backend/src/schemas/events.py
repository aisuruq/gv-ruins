from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    datetime: datetime
    met_place: str
    route: str
    guid: str
    cost: int
    max_participants: int
    description: str
    details: str

class Event(EventBase):
    id: int

class CreateEvents(Event):
    ...