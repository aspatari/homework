from pydantic import BaseModel, Field, AnyHttpUrl
from uuid import UUID, uuid4
from datetime import datetime


class PostCreateIn(BaseModel):
    title: str
    author: str
    text: str
    url: AnyHttpUrl


class PostCreate(PostCreateIn):
    user_agent: str


class IndexedPost(PostCreate):
    id: UUID = Field(default_factory=uuid4)
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
