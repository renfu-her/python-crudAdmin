from pydantic import BaseModel
from typing import Optional


class ArticleCategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None
    slug: Optional[str] = None
    sort_order: int = 0


class ArticleCategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    sort_order: Optional[int] = None

