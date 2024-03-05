from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from core.models.post import Post
    from core.models.profile import Profile


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(30), unique=True)
    post: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
