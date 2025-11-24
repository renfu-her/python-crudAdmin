from pydantic import BaseModel
from typing import Optional


class CartCreate(BaseModel):
    user_id: int


class CartUpdate(BaseModel):
    user_id: Optional[int] = None

