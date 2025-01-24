from sqlalchemy import and_, delete
from app.database.abc.repository import AbstractRepository
from app.database.models.models import Wish


class WishRepository(AbstractRepository):
    model = Wish
    
    async def delete_wish(self, user_id: int, wish_id: int):
        result = await self._session.execute(
            delete(self.model).where(and_(self.model.user_id == user_id, self.model.wish_id == wish_id))
        )

        return result.rowcount