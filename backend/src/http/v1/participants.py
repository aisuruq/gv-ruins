from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, HTTPException
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
            participants.tg_username,
            participants.event_id,
        )
        return {"status": "success", "message": "Регистрация прошла успешно"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))