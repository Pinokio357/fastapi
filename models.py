import databases
import sqlalchemy
from datetime import datetime
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(..., max_length=128)


class OrderIn(BaseModel):
    product_id: int = Field(...)
    user_id: int = Field(...)
    order_status: bool = Field(...)
    date: datetime = Field(default=datetime.now())


class Order(BaseModel):
    id: int
    product_id: int = Field(...)
    user_id: int = Field(...)
    order_status: bool = Field(...)
    date: datetime = Field(default=datetime.now())


class ProductIn(BaseModel):
    name: str = Field(..., max_length=32)
    description: str = Field(max_length=128)
    price: float = Field(..., gt=0)


class Product(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    description: str = Field(max_length=128)
    price: float = Field(..., gt=0)
