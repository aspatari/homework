from typing import TypeAlias

from pydantic import BaseModel, Field, AnyHttpUrl
from uuid import UUID, uuid4
from datetime import datetime

POST_ID: TypeAlias = UUID


class Post(BaseModel):
    title: str
    author: str
    text: str
    url: AnyHttpUrl


class PostCreateIn(Post):
    ...


class PostCreate(PostCreateIn):
    user_agent: str


class IndexedPost(PostCreate):
    id: POST_ID = Field(default_factory=uuid4)
    created_at: datetime
    title_md5: str
    text_md5: str
    title_len_ch: int
    text_len_ch: int
    title_len_words: int
    text_len_words: int
    url_hostname: str
    url_scheme: str
    user_agent: str

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.created_at > other.created_at


class PostSearch(BaseModel):
    title: str | None
    author: str | None
    count: int = 50


class PostSearchOut(BaseModel):
    id: POST_ID
    title: str
    author: str
    text: str
    created_at: datetime
