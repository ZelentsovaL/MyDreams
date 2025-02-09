

import aiofiles
from fastapi import UploadFile
from sqlalchemy import UUID, insert, select
from app.database.models.models import ArmoredWishes, User, Wish
from app.database.repo.user_repository import UserRepository
from app.database.repo.wish_repository import WishRepository


from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.wishes.create_wish import CreateWish
from app.schema.wishes.update_wish import UpdateWish

class WishService:
    def __init__(self, session: AsyncSession) -> None:
        
        self._session = session
        self._repo = WishRepository(self._session)

    async def get_armored_wishes(self, user_id: int):
        return await self._repo.get_my_armored_wishes(user_id)

    async def armor_wish(self, user_id: int, wish_id: str):
        query = insert(ArmoredWishes).values(user_id=user_id, wish_id=wish_id).returning(ArmoredWishes)
        result = await self._session.execute(query)
        await self._session.commit()
        inserted: ArmoredWishes = result.scalars().first()
        armored_wish = await self._repo.get_by_filter_one(wish_id=inserted.wish_id)

        return armored_wish

    async def complete_wish(self, user_id: int, wish_id: str):
        return await self._repo.complete_wish(wish_id, user_id)

    async def create_wish(self, user_id: int, createWish: CreateWish):
        return await self._repo.create(user_id=user_id, wish=createWish.wish, price=createWish.price, source_url=createWish.source_url, is_secret=createWish.is_secret)
    
    async def delete_wish(self, user_id: int, wish_id: str):
        return await self._repo.delete_wish(user_id=user_id, wish_id=wish_id)
    
    async def get_completed_wishes(self, user_id: int):
        return await WishRepository(self._session).get_completed_wishes(user_id)

    async def update_wish(self, user_id: str, wish_id: str, update_wish: UpdateWish):
        return await self._repo.update_wish(
            user_id,
            wish_id,
            update_wish.new_title,
            update_wish.new_price,
            update_wish.new_source_url,
            update_wish.is_secret
        )
    
    async def upload_photo(self, wish_id: int, file: UploadFile):
        file_path = f"photos/{wish_id}.{file.filename.split('.')[-1]}"
        wish: Wish = await WishRepository(self._session).update_one(wish_id, wish_photo=file_path)
        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write

        return wish