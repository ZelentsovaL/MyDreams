from sqlalchemy import and_, delete, insert, select, update
from app.database.abc.repository import AbstractRepository
from app.database.models.models import CompletedWishes, Wish


class WishRepository(AbstractRepository):
    model = Wish
    
    async def complete_wish(self, wish_id: str, user_id: str):
        query = (
            select(self.model)
            .where(
                and_(
                    self.model.wish_id == wish_id,
                    self.model.user_id == user_id
                )
            )
        )

        result = await self._session.execute(query)
        wish = result.scalars().first()

        insert_query = (
            insert(CompletedWishes)
            .values(
                user_id=user_id,
                wish_id=wish_id,
            )
        )

        await self._session.execute(insert_query)
        await self._session.commit()

        return wish

    async def update_one(self, wish_id: int, **kwargs):
        
        query = update(self.model).where(self.model.wish_id == wish_id).values(**kwargs).returning(self.model)
        result = await self._session.execute(query)
        await self._session.commit()
        return result.scalars().first()

    async def delete_wish(self, user_id: int, wish_id: int):
        result = await self._session.execute(
            delete(self.model).where(and_(self.model.user_id == user_id, self.model.wish_id == wish_id))
        )
        await self._session.commit()

        return result.rowcount
    
    async def update_wish(self,
                          user_id: int,
                          wish_id: int,
                          new_name: str,
                          new_price: float,
                          new_source_url: str,
                          is_secret: bool
                          ):
        query = (
            select(self.model)
            .where(
                and_(
                    self.model.user_id == user_id,
                    self.model.wish_id == wish_id
                )
            )
        )

        result = await self._session.execute(query)
        wish = result.scalars().first()

        update_query = (
            update(self.model)
            .where(self.model.wish_id == wish_id)
            .values(
                wish = new_name if new_name else wish.wish,
                price = new_price if new_price else wish.price,
                source_url = new_source_url if new_source_url else wish.source_url,
                is_secret = is_secret
            ).returning(self.model)
                
        )

        upd = await self._session.execute(update_query)
        await self.commit()
        return upd.scalars().first()

        