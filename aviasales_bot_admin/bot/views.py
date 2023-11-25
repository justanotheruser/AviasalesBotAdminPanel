from fastapi import FastAPI

from aviasales_bot_admin.bot.flight_directions_repo import FlightDirectionsRepo
from aviasales_bot_admin.bot.users_repo import UsersRepo


def create_views(app: FastAPI, database):
    @app.get("/users/")
    async def users_list(db=database):
        users_repo = UsersRepo(db)
        users = await users_repo.get_list()
        return users

    @app.get("/directions/")
    async def flight_directions_list(db=database):
        flight_directions_repo = FlightDirectionsRepo(db)
        flight_directions = await flight_directions_repo.get_list()
        return flight_directions
