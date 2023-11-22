from fastapi import APIRouter, Depends

from aviasales_bot_admin.bot.database import get_db, init_db
from aviasales_bot_admin.bot.users_repo import UsersRepo

router = APIRouter()


@router.on_event("startup")
async def on_startup():
    await init_db()


@router.get("/users/")
async def users_list(db=Depends(get_db)):
    users_repo = UsersRepo(db)
    users = await users_repo.get_list()
    return users
