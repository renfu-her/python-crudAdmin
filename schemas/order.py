from pydantic import BaseModel
from typing import Optional


class OrderCreate(BaseModel):
    user_id: int
    order_number: str
    status: str = "pending"
    total_amount: float
    shipping_address: str
    shipping_name: str
    shipping_phone: Optional[str] = None
    notes: Optional[str] = None


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    order_number: Optional[str] = None
    status: Optional[str] = None
    total_amount: Optional[float] = None
    shipping_address: Optional[str] = None
    shipping_name: Optional[str] = None
    shipping_phone: Optional[str] = None
    notes: Optional[str] = None

