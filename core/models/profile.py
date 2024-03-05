from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixin import UserRelationMixin


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
