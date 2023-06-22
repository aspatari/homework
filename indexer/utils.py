from indexer import schemas
from datetime import datetime
from hashlib import md5
from indexer.schemas import IndexedPost


def post_to_indexed_post(post: schemas.PostCreate) -> schemas.IndexedPost:
    indexed_post = IndexedPost(
        created_at=datetime.now(),
        title_md5=md5(post.title.encode()).hexdigest(),
        text_md5=md5(post.text.encode()).hexdigest(),
        title_len_ch=len(post.title),
        text_len_ch=len(post.text),
        title_len_words=len(post.title.split()),
        text_len_words=len(post.text.split()),
        url_hostname=post.url.host,
        url_scheme=post.url.scheme,
        **post.dict()
    )
    return indexed_post
