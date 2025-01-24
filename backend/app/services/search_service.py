
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.user_repository import UserRepository

class SearchService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repo = UserRepository(session)

    async def search_by_username(self, username: str):
        return await self._repo.search_by_login(username)