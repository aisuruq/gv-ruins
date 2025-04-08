from fastapi import APIRouter

from configuration.settings import settings
from src.routes.v1 import events
from src.routes.v1 import participants
from src.routes.v1 import yokassa

router_api_v1 = APIRouter()

router_api_v1.include_router(events.router, prefix=settings.api.version.events)
router_api_v1.include_router(
    participants.router, prefix=settings.api.version.participants
)
router_api_v1.include_router(yokassa.router, prefix=settings.api.version.payments)
