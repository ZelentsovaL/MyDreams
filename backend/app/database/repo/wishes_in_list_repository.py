from sqlalchemy import RowMapping, and_, insert, select, update
from app.database.abc.repository import AbstractRepository

from app.database.models.models import Wish, WishesInList

class WishesListRepository(AbstractRepository):
    model = WishesInList


    async def move_to(self, user_id: int, list_id: int, wish_id: int):
        ...
    

