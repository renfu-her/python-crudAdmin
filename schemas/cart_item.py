from pydantic import BaseModel
from typing import Optional


class CartItemCreate(BaseModel):
    cart_id: int
    product_id: int
    quantity: int = 1


class CartItemUpdate(BaseModel):
    cart_id: Optional[int] = None
    product_id: Optional[int] = None
    quantity: Optional[int] = None

