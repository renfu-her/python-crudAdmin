from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ArticleCreate(BaseModel):
    title: str
    content: Optional[str] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None
    author: Optional[str] = None
    category_id: Optional[int] = None
    is_active: bool = True
    view_count: int = 0
    published_at: Optional[datetime] = None


class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None
    author: Optional[str] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None
    view_count: Optional[int] = None
    published_at: Optional[datetime] = None

