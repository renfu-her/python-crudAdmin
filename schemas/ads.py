from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AdsCreate(BaseModel):
    title: str
    content: Optional[str] = None
    image_url: Optional[str] = None
    link_url: Optional[str] = None
    position: Optional[str] = None
    is_active: bool = True
    sort_order: int = 0
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class AdsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None
    link_url: Optional[str] = None
    position: Optional[str] = None
    is_active: Optional[bool] = None
    sort_order: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

