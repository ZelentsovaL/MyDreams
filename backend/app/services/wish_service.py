

from app.database.repo.wish_repository import WishRepository


from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.wishes.create_wish import CreateWish
from app.schema.wishes.update_wish import UpdateWish

class WishService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repo = WishRepository(self._session)

    async def create_wish(self, user_id: str, createWish: CreateWish):
        return await self._repo.create(user_id=user_id, wish=createWish.wish, price=createWish.price, source_url=createWish.source_url, is_secret=createWish.is_secret)
    
    async def delete_wish(self, user_id: str, wish_id: str):
        return await self._repo.delete_wish(user_id=user_id, wish_id=wish_id)
    
    async def update_wish(self, user_id: str, wish_id: str, update_wish: UpdateWish):
        return await self._repo.update_wish(
            user_id,
            wish_id,
            update_wish.new_title,
            update_wish.new_price,
            update_wish.new_source_url,
            update_wish.is_secret
        )