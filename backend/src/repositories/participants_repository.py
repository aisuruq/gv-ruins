from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from src.models.events import Event
from src.models import Participant
from src.schemas.participants import CreateParticipants
from src.sheets.participants import participants_sheet


def register_participant(session: Session, data: CreateParticipants) -> dict:
    event = session.scalar(select(Event).where(Event.id == data.event_id))
    if not event:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Мероприятие не найдено")

    participant = Participant(**data.model_dump(exclude={"event_name"}))

    participant.event_name = event.name

    session.add(participant)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при сохранении в базу данных",
        )

    participants_sheet.register(
        name=data.name,
        surname=data.surname,
        patronymic=data.patronymic,
        phone=data.phone,
        tg_username=data.tg_username,
        event_id=data.event_id,
        event_name=data.event_name,
        comment=data.comment or "",
        payment=data.payment,
        prepayment=data.prepayment,
        people_count=data.people_count,
    )

    return {"status": "success", "message": "Участник успешно зарегистрирован"}
