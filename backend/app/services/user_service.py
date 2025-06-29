
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.user_repository import UserRepository
from app.schema.access import Access
from sqlalchemy.exc import IntegrityError
from app.utils.ext import result
from app.database.models.models import RecomendationWishes
class UserService:

    def __init__(self, session: AsyncSession):
        self._session = session
        self._repo = UserRepository(self._session)

    async def get_recomendations(self):
        query = (
            select(RecomendationWishes)
        )

        result = await self._session.execute(query)
        return result.scalars().all()

    async def is_user_exists(self, email: str) -> bool:
        user = await self._repo.get_by_filter_one(email=email)
        return True if user else False

    async def register(self, access: Access) -> result.Result[dict]:
        
        registered = await self._repo.create(**access.model_dump())
        return result.success(registered.user_id)


        
    async def get_all_wishes(self, user_id: int) -> result.Result[None]:
        return await self._repo.get_all_wishes(user_id)
    
    async def login(self, login, password) -> result.Result[None]:
        user = await self._repo.get_by_login(login)
        if user is None:
            return result.error("Такого пользователя не существует.")
        if user.password != password:
            return result.error("Неверный пароль.")
        return result.success(user)