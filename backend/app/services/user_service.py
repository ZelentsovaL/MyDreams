from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.user_repository import UserRepository
from app.schema.access import Access
from sqlalchemy.exc import IntegrityError
from app.utils.ext import result
class UserService:

    def __init__(self, session: AsyncSession):
        self._session = session
        self._repo = UserRepository(self._session)


    async def register(self, access: Access) -> result.Result[dict]:
        try:
            registered = await self._repo.create(**access.model_dump())
            return result.success(registered.user_id)
        except IntegrityError:
            return result.error("Такой пользователь уже есть.")

        
    async def get_all_wishes(self, user_id: int) -> result.Result[None]:
        return await self._repo.get_all_wishes(user_id)
    
    async def login(self, login, password) -> result.Result[None]:
        user = await self._repo.get_by_login(login)
        if user is None:
            return result.error("Такого пользователя не существует.")
        if user.password != password:
            return result.error("Неверный пароль.")
        return result.success(user)