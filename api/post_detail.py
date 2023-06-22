from fastapi import status
from fastapi.exceptions import HTTPException

from api.router import router
from indexer.schemas import POST_ID, IndexedPost
from indexer.service import get_post_by_id


@router.get("/post/{post_id}", name="post_detail", response_model=IndexedPost)
def post_detail(post_id: POST_ID):
    post = get_post_by_id(post_id=post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post with given id not found"
        )
    return post
