from fastapi import FastAPI

from app.board.router import router as board_router
from app.core.config import settings
from app.football.router import router as football_router
from app.users.router import router as users_router

app = FastAPI(title=settings.app_name)

app.include_router(football_router)
app.include_router(board_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"message": "week16 mini board API"}
