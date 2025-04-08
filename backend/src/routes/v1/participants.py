from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, HTTPException, status
from configuration.db_helper import db_helper
from src.repositories.participants_repository import register_participant
from src.schemas.participants import CreateParticipants
from src.sheets.participants import participants_sheet

router = APIRouter()


@router.get("/list", response_model=List[dict])
def get_events():
    return participants_sheet.get_all_participants()


@router.post("/register")
def register_to_event(participants: CreateParticipants):
    try:
        session = db_helper.session_getter()
        register_participant(session, participants)
        return {"status": "success", "message": "Регистрация прошла успешно"}
    except Exception as e:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Ошибка валидации данных. Пожалуйста, проверьте правильность заполнения формы {e}.",
        )
