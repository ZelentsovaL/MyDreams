
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.user_repository import UserRepository
from app.database.repo.wish_repository import WishRepository

class SearchService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repo = UserRepository(session)

    async def search_by_username(self, username: str):
        return await self._repo.search_by_login(username)
    
    async def get_wishes_by_username(self, username: str):
        user = await self._repo.get_by_filter_one(username=username)
        if user is None:
            raise HTTPException(
                status_code=400,
                detail="Пользователь не найден."
            )
        return await WishRepository(self._session).get_by_filter_all(user_id=user.user_id)