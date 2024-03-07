import asyncio

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
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


async def create_posts(
    session: AsyncSession,
    user_id: int,
    *posts_titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in posts_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_users_with_posts(
    session: AsyncSession,
) -> list[User]:
    """"""
    """ если работать со .scalars() обязательно .unique()"""
    # stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    # users = await session.scalars(stmt)
    # for user in users.unique():  # обязательно .unique()
    #     print("___________________")
    #     print(user)
    #     for post in user.posts:
    #         print(f"Post - {post}")
    """если работать с Result обязательно .unique()"""
    # stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    # users = result.unique().scalars()  # обязательно .unique()
    # for user in users:
    #     print("___________________")
    #     print(user)
    #     for post in user.posts:
    #         print(f"Post - {post}")
    """если работать с selectinload load, для того чтобы посты подгружались с пользователем
    выполняется 2 запроса в БД"""
    stmt = select(User).options(selectinload(User.posts)).order_by(User.id)
    # result: Result = await session.execute(stmt)
    # users = result.scalars()
    users = await session.scalars(stmt)
    for user in users:
        print("___________________")
        print(user)
        for post in user.posts:
            print(f"Post - {post}")
    return list(users)


async def get_users_with_posts_and_profiles(
    session: AsyncSession,
) -> list[User]:
    stmt = (
        select(User)
        .options(
            joinedload(User.profile),
            selectinload(User.posts),
        )
        .order_by(User.id)
    )
    users = await session.scalars(stmt)
    for user in users:
        print("___________________")
        if user.profile is not None:
            print(user.profile.first_name)
        print(user, user.profile and user.profile.first_name)
        for post in user.posts:
            print(f"Post - {post}")
    return list(users)


async def get_posts_with_authors(
    session: AsyncSession,
) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.user)).order_by(Post.id)
    posts = await session.scalars(stmt)
    for post in posts:
        print(f"Post - {post}")
        print(f"Authors - {post.user}")
    return list(posts)


async def get_profiles_with_users_and_users_with_posts(
    session: AsyncSession,
):
    stmt = (
        select(Profile)
        .join(Profile.user)
        .options(joinedload(Profile.user).selectinload(User.posts))
        .where(User.username == "Max")
        .order_by(Profile.id)
    )

    profiles = await session.scalars(stmt)
    for profile in profiles:
        print(profile.first_name, profile.user)
        print(profile.user.posts)


async def main_relations(session: AsyncSession):
    async with db_helper.session_factory() as session:
        # user_max = await create_user(session=session, username="Max")
        # await create_user(session=session, username="Sam")
        # await get_user_by_username(session=session, username="Oleg")
        # user_max = await get_user_by_username(session=session, username="Max")
        # # await create_user_profile(
        # #     session=session, user_id=user_max.id, first_name="Max"
        # # )
        # # await show_users_with_profile(session)
        # await create_posts(
        #     session,
        #     user_max.id,
        #     "first post",
        #     "second post",
        # )
        # await get_users_with_posts(session=session)
        # await get_posts_with_authors(session=session)
        # await get_users_with_posts_and_profiles(session=session)
        await get_profiles_with_users_and_users_with_posts(session=session)


async def main():
    async with db_helper.session_factory() as session:
        pass


if __name__ == "__main__":
    asyncio.run(main())
