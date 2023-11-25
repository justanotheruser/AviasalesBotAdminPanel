from fastapi import FastAPI

from aviasales_bot_admin.bot.app import BotInfoAPI
from aviasales_bot_admin.config import config


def make_app():
    app = FastAPI()
    for bot_name, bot_config in config.bots.items():
        bot_info_api = BotInfoAPI(bot_config)
        app.mount(f'/{bot_name}', bot_info_api.app)
    return app


app = make_app()


@app.get("/")
async def index():
    return {"hello": "world!"}
