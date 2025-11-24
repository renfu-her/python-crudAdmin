from pydantic import BaseModel
from typing import Optional


class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int = 1
    price: float
    product_name: str


class OrderItemUpdate(BaseModel):
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    product_name: Optional[str] = None

