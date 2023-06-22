import threading
from collections import defaultdict
from sortedcontainers import SortedList
from indexer import schemas, utils

lock = threading.Lock()
posts = dict()
sorted_posts = SortedList()

author_index = defaultdict(list)
title_index = defaultdict(list)


def index_post(post: schemas.IndexedPost):
    with lock:
        post_author_hash = utils.string_to_md5(post.author.lower())
        lower_case_title = post.title.lower().split()
        posts[post.id] = post
        sorted_posts.add(post)
        author_index[post_author_hash].append(post.id)

        for word in lower_case_title:
            title_index[word].append(post.id)


def post_retrieve(post_id: schemas.POST_ID) -> schemas.IndexedPost | None:
    return posts.get(post_id, None)


def search_posts(params: schemas.PostSearch) -> list[schemas.IndexedPost]:
    with lock:
        relevant_post_ids = set(posts.keys())
        if params.author:
            post_author_hash = utils.string_to_md5(params.author.lower())
            author_math_ids = author_index[post_author_hash]

            relevant_post_ids = set(author_math_ids)

        if params.title:
            title_lowercase_tokens = params.title.lower().split()
            title_match_ids = set()
            for word in title_lowercase_tokens:
                word_match_ids = title_index.get(word, set())

                title_match_ids.update(word_match_ids)

            if title_match_ids:
                relevant_post_ids = relevant_post_ids.intersection(title_match_ids)

        match_posts = []

        for post in sorted_posts:
            if post.id in relevant_post_ids:
                match_posts.append(post)
            if len(match_posts) == params.count:
                break
        return match_posts
