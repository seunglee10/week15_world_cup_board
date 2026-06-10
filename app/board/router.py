from pydantic import BaseModel
from fastapi import APIRouter

from app.board.service import create_post, list_posts

router = APIRouter(prefix="/board", tags=["board"])


class PostCreate(BaseModel):
    title: str
    content: str


@router.get("/posts")
def read_posts():
    return list_posts()


@router.post("/posts")
def write_post(post: PostCreate):
    return create_post(title=post.title, content=post.content)
