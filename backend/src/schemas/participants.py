import re
from pydantic import BaseModel, field_validator
from typing import Optional


class CreateParticipants(BaseModel):
    name: str
    surname: str
    patronymic: str
    phone: str
    tg_username: str
    event_id: int
    comment: Optional[str]
    payment: int
    prepayment: int

    @field_validator("phone")
    def validate_phone(cls, v):
        if not re.fullmatch(r"\+7\d{10}", v):
            raise ValueError("Номер телефона должен быть в формате +7XXXXXXXXXX")
        return v

    @field_validator("prepayment")
    def validate_prepayment(cls, v, values):
        payment = values.get("payment")
        if payment is not None and v > payment:
            raise ValueError("Предоплата не может быть больше общей суммы")
        return v
