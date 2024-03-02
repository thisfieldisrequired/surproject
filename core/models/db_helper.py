from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)

from core.config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_close=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopfunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.get_scoped_session() as session:
            yield session
            session.close()


db_helper = DataBaseHelper(
    url=settings.db_url,
    echo=settings.db_echo,
)
