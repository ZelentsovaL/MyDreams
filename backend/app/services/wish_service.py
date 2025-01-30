

import aiofiles
from fastapi import UploadFile
from sqlalchemy import UUID
from app.database.models.models import User, Wish
from app.database.repo.user_repository import UserRepository
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
    
    async def upload_photo(self, wish_id: int, file: UploadFile):
        file_path = f"photos/{wish_id}.{file.filename.split('.')[-1]}"
        wish: Wish = await WishRepository(self._session).update_one(wish_id, wish_photo=file_path)
        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write

        return wish