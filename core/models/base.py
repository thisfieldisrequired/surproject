from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    @declarative_attr.directive
    def __tablename__(cls) -> str:
        return f"{str.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primery_key=True)