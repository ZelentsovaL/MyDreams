from sqlalchemy import RowMapping, and_, insert, select, update
from app.database.abc.repository import AbstractRepository

from app.database.models.models import Wish, WishesList

class WishesListRepository(AbstractRepository):
    model = WishesList


    async def get_all_wishes(self, user_id: int, list_id: int):
        query = (
            select(Wish)
            .select_from(self.model)
            .where(and_(
                self.model.user_id == user_id,
                self.model.wishes_list_id == list_id
            ))
            .join(Wish, self.model.wish_id == Wish.wish_id)
        )

        result = await self._session.execute(query)
        wishes = result.mappings().all()
        return wishes
    

