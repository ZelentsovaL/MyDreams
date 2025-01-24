from sqlalchemy import RowMapping, and_, insert, select
from app.database.abc.repository import AbstractRepository

from app.database.models.models import User, UserProfile, Wish

class UserRepository(AbstractRepository):
    model = User

    async def get_all_wishes(self, userId: str):
        query = (
            select(Wish)
            .select_from(Wish)
            .where(Wish.user_id == userId)

        )
        result = await self._session.execute(query)
        wishes = result.scalars().all()
        return wishes


    async def create(self, **kwargs):
        
        query = insert(self.model).values(**kwargs).returning(self.model)
        result = await self._session.execute(query)
        await self.commit()
        return result.scalars().first()
    

    async def search_by_login(self, login: str):
        query = (
            select(self.model.username)
            .where(self.model.username.contains(login))
        )

        result = await self._session.execute(query)
        return result.mappings().all()

    async def get_by_login(self, username: str):
        query = (
            select(self.model)
            .where(self.model.username == username)
        )

        query_result = await self._session.execute(query)
        return query_result.scalars().one_or_none()