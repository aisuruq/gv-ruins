from fastapi import FastAPI
from configuration.routes_path import __routes__


class Server:

    __app: FastAPI

    def __init__(self, app: FastAPI):

        self.__app = app
        self.__register_routes(app)

    def get_app(self) -> FastAPI:
        return self.__app

    @staticmethod
    def __register_routes(app):

        __routes__.register_routes(app)
