from indexer import schemas, utils, index


def create_post(post: schemas.PostCreate):
    structured_post = utils.post_to_indexed_post(post)

    index.index_post(structured_post)


def search_post(search_params: schemas.PostSearch) -> schemas.PostSearchOut:
    return []


def get_post_by_id(post_id: schemas.POST_ID):
    ...
