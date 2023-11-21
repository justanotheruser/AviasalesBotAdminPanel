from fastapi import FastAPI


def make_app():
    app = FastAPI()
    return app


app = make_app()


@app.get("/")
async def index():
    return {"hello": "world!"}