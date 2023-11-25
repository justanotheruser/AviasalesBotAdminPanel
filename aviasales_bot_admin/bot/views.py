from fastapi import Depends

from aviasales_bot_admin.bot.database import get_db, init_db
from aviasales_bot_admin.bot.flight_directions_repo import FlightDirectionsRepo
from aviasales_bot_admin.bot.users_repo import UsersRepo

from aviasales_bot_admin.bot.app import router


@router.on_event("startup")
async def on_startup():
    await init_db()


@router.get("/users/")
async def users_list(db=Depends(get_db)):
    users_repo = UsersRepo(db)
    users = await users_repo.get_list()
    return users


@router.get("/directions/")
async def flight_directions_list(db=Depends(get_db)):
    flight_directions_repo = FlightDirectionsRepo(db)
    flight_directions = await flight_directions_repo.get_list()
    return flight_directions
