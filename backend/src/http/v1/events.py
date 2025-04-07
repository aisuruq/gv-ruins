from fastapi import APIRouter
from src.sheets.events import events_sheet
from typing import List

router = APIRouter()

@router.get("/list", response_model=List[dict])
def get_events():
    return events_sheet.get_all_events()

@router.get("/upcoming")
def get_upcoming_events():
    return events_sheet.get_upcoming_events()
