from api.router import router
from indexer import service
from indexer.schemas import PostSearch, PostSearchOut


@router.get("/posts", response_model=PostSearchOut)
def post_search(search_params: PostSearch):
    results = service.search_post(search_params=search_params)
    return results
