from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsCreate(BaseModel):
    title: str
    content: Optional[str] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None
    author: Optional[str] = None
    is_active: bool = True
    view_count: int = 0
    published_at: Optional[datetime] = None


class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    image_url: Optional[str] = None
    author: Optional[str] = None
    is_active: Optional[bool] = None
    view_count: Optional[int] = None
    published_at: Optional[datetime] = None

