from fastapi import APIRouter

from configuration.settings import settings
from src.routes.v1 import events
from src.routes.v1 import participants

router_api_v1 = APIRouter()

router_api_v1.include_router(events.router, prefix=settings.api.version.events)
router_api_v1.include_router(
    participants.router, prefix=settings.api.version.participants
)
