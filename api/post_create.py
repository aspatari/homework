from fastapi import Body, Header

from api.router import router
from indexer.schemas import PostCreateIn, PostCreate
from indexer.service import create_post


@router.post("/posts")
def post_submit(post: PostCreateIn = Body(), user_agent: str = Header()):


    create_post(post=PostCreate(**post.dict(), user_agent=user_agent))
