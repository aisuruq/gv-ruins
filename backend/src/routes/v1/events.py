from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configuration.db_helper import db_helper
from src.sheets.events import events_sheet
from src.repositories.events_repository import sync_events_with_db
from src.models.events import Event as events_db
from src.schemas.events import Event as event_sh
from typing import List

router = APIRouter()


@router.get("/upcoming_sheets")
def get_upcoming_events():
    return events_sheet.get_upcoming_events()


@router.post("/sync-events")
def sync_events(session: Session = Depends(db_helper.session_getter)):
    return sync_events_with_db(session)


@router.get("/list", response_model=List[event_sh])
def get_events(session: Session = Depends(db_helper.session_getter)):
    events = session.query(events_db).all()
    return events
