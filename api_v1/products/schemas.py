from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
