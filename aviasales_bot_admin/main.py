from fastapi import FastAPI

from aviasales_bot_admin.bot.views import router


def make_app():
    app = FastAPI()
    app.include_router(router, prefix="/bot")
    return app


app = make_app()


@app.get("/")
async def index():
    return {"hello": "world!"}
