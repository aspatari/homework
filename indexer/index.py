import threading
from indexer import schemas

lock = threading.Lock()
posts = []


def index_post(post: schemas.IndexedPost):
    with lock:
        posts.append(post)

    print(len(posts))
