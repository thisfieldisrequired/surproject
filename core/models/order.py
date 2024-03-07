from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


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
