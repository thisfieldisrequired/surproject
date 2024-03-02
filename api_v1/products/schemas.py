from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int


class Product(ProductBase):
    id: int
