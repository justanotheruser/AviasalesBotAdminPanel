import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from aviasales_bot_admin.bot.flight_directions_repo import FlightDirectionsRepo
from aviasales_bot_admin.bot.users_repo import UsersRepo


def create_views(app: FastAPI, bot_name: str, database):
    templates = Jinja2Templates(directory=pathlib.Path(__file__).parent / 'templates')
    templates.context_processors = [lambda request: {'bot_name': bot_name}]

    @app.get("/users/", response_class=HTMLResponse)
    async def users_list(request: Request, db=database):
        users_repo = UsersRepo(db)
        users = await users_repo.get_list()
        context = {
            'request': request,
            'users': users,
            'bot_name': 'bot_name placeholder',
        }
        return templates.TemplateResponse('users.html', context=context)

    @app.get("/directions/")
    async def flight_directions_list(db=database):
        flight_directions_repo = FlightDirectionsRepo(db)
        flight_directions = await flight_directions_repo.get_list()
        return flight_directions
