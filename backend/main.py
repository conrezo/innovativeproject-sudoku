from fastapi import FastAPI
from src.auth import connect_to_db
from src.routes.auth import auth_router
from src.routes.game import game_router
from src.routes.lobby import lobby, lobby_router
from src.routes.stats import stats_router

connect_to_db()

app = FastAPI()

app.include_router(auth_router)
app.include_router(lobby_router)
app.include_router(game_router)
app.include_router(stats_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.on_event("startup")
async def startup():
    # Prime the push notification generator
    await lobby.generator.asend(None)
