from configuration.settings import settings
from configuration.routes import Routes
from src.http.v1 import router_api_v1

__routes__ = Routes(routers=(
    (router_api_v1, settings.api.v1),
))