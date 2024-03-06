import asyncio

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.engine import Result

from core.models import User, Profile, Post, db_helper


async def create_user(
    session: AsyncSession,
    username: str,
) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print("**************")
    print(f"User - {user}")
    print("**************")
    return user


async def get_user_by_username(
    session: AsyncSession,
    username: str,
) -> User | None:
    stmt = Select(User).where(User.username == username)
    # result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    """ИЛИ"""
    user: User | None = await session.scalar(stmt)
    print("**********")
    print("User ", username, user)
    print("**********")
    return user


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profile(
    session: AsyncSession,
) -> list[User]:
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    # users = result.scalars().all()
    # print("***********")
    # print(users)
    users = await session.scalars(stmt)
    # print(users)
    for user in users:
        if user.profile is not None:
            print(user.profile.first_name)
    return list(users)


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="Max")
        # await create_user(session=session, username="Sam")
        # await get_user_by_username(session=session, username="Oleg")
        # user_max = await get_user_by_username(session=session, username="Max")
        # await create_user_profile(
        #     session=session, user_id=user_max.id, first_name="Max"
        # )
        await show_users_with_profile(session)


if __name__ == "__main__":
    asyncio.run(main())
