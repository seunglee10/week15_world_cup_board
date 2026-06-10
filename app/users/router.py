from fastapi import APIRouter

from app.users.service import list_users

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def read_users():
    return list_users()
