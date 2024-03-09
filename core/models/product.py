from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.order import Order


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    price: Mapped[int]
    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_association",
        back_populates="products",
    )
