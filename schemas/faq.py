from pydantic import BaseModel
from typing import Optional


class FAQCreate(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None
    is_active: bool = True
    sort_order: int = 0
    view_count: int = 0


class FAQUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
    is_active: Optional[bool] = None
    sort_order: Optional[int] = None
    view_count: Optional[int] = None

