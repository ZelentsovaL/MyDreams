

from app.database.repo.wish_repository import WishRepository


from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.wishes.create_wish import CreateWish

class WishService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repo = WishRepository(self._session)

    async def create_wish(self, user_id: str, createWish: CreateWish):
        return await self._repo.create(user_id=user_id, wish=createWish.wish, price=createWish.price, source_url=createWish.source_url)
    
    async def delete_wish(self, user_id: str, wish_id: str):
        return await self._repo.delete_wish(user_id=user_id, wish_id=wish_id)