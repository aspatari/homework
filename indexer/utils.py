from indexer import schemas
from datetime import datetime
from hashlib import md5
from indexer.schemas import IndexedPost


def string_to_md5(input_str: str) -> str:
    return md5(input_str.encode()).hexdigest()


def count_words(input_str: str) -> int:
    return len(input_str.split())


def post_to_indexed_post(post: schemas.PostCreate) -> schemas.IndexedPost:
    indexed_post = IndexedPost(
        created_at=datetime.now(),
        title_md5=string_to_md5(post.title),
        text_md5=string_to_md5(post.text),
        title_len_ch=len(post.title),
        text_len_ch=len(post.text),
        title_len_words=count_words(post.title),
        text_len_words=count_words(post.text),
        url_hostname=post.url.host,
        url_scheme=post.url.scheme,
        **post.dict()
    )
    return indexed_post
