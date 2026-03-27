from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class Category(str, Enum):
    BURRITO = "Burrito"
    TACO = "Taco"
    BEBIDA = "Bebida"

class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    price: float = Field(..., gt=0)
    category: Category

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]

class OrderItemResponse(BaseModel):
    menu_item: MenuItem
    quantity: int
    subtotal: float

class OrderResponse(BaseModel):
    id: int
    items: List[OrderItemResponse]
    total: float
    status: str = "Recibido"