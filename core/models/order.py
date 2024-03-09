from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.product import Product


class Order(Base):
    promocode: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        default=datetime.now,
    )
    products: Mapped[list["Product"]] = relationship(
        secondary="order_product_association",
        back_populates="orders",
    )
