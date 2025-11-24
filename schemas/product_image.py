from pydantic import BaseModel
from typing import Optional


class ProductImageCreate(BaseModel):
    product_id: int
    image_url: str
    alt_text: Optional[str] = None
    sort_order: int = 0


class ProductImageUpdate(BaseModel):
    product_id: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    sort_order: Optional[int] = None

