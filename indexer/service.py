from indexer import schemas, utils, index


def create_post(post: schemas.PostCreate):
    structured_post = utils.post_to_indexed_post(post)

    index.index_post(structured_post)


def search_post(search_params: schemas.PostSearch) -> list[schemas.IndexedPost]:
    return index.search_posts(params=search_params)


def get_post_by_id(post_id: schemas.POST_ID) -> schemas.IndexedPost | None:
    return index.post_retrieve(post_id=post_id)
