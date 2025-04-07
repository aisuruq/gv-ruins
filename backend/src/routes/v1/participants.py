from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, HTTPException, status
from src.schemas.participants import CreateParticipants
from src.sheets.participants import participants_sheet

router = APIRouter()


@router.get("/list", response_model=List[dict])
def get_events():
    return participants_sheet.get_all_participants()


@router.post("/register")
def register_to_event(participants: CreateParticipants):
    try:
        participants_sheet.register(
            participants.name,
            participants.surname,
            participants.patronymic,
            participants.phone,
            participants.tg_username,
            participants.event_id,
            participants.comment,
            participants.payment,
            participants.prepayment,
        )
        return {"status": "success", "message": "Регистрация прошла успешно"}
    except Exception as e:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Ошибка валидации данных. Пожалуйста, проверьте правильность заполнения формы.",
        )
