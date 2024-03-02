from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    price: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductUpdatePartial(ProductBase):
    name: str | None = None
    price: int | None = None


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
