from sqlalchemy import RowMapping, and_, insert, select, update
from app.database.abc.repository import AbstractRepository
from sqlalchemy.orm import selectinload
from app.database.models.models import Wish, WishesInList, WishesList

class WishesListRepository(AbstractRepository):
    model = WishesList


    async def get_all_wishes(self, user_id: int, list_id: int):
        query = (
            select(self.model)
            .options(
                selectinload(self.model.wishes_in_list).selectinload(WishesInList.wish)
            )
        )

        result = await self._session.execute(query)
        wishes = result.mappings().all()
        return wishes
    

