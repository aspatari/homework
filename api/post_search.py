from fastapi import Query

from api.router import router
from indexer import service, schemas


@router.get("/posts", response_model=list[schemas.PostSearchOut])
def post_search(
    title: str | None = Query(None),
    author: str | None = Query(None),
    size: int = Query(50),
):
    results = service.search_post(
        search_params=schemas.PostSearch(title=title, author=author, count=size)
    )
    return results
