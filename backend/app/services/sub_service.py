from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.repo.subscribe_repository import SubscribeRepository


class SubscribeService:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._repo = SubscribeRepository(session)

    async def get_subscriptions(self, user_id: int):
        return await self._repo.get_subscriptions(user_id)

    async def unsubscribe(self, user_id: int, subscriber_id: int) -> None:
        return await self._repo.unsubscribe(user_id, subscriber_id)

    async def subscribe(self, user_id: int, subscriber_id: int) -> None:
        if await self._repo.get_by_filter_one(user_id=user_id, subscriber_id=subscriber_id) is not None:
            raise HTTPException(status_code=400, detail="Вы уже подписаны на этого пользователя.")
        return await self._repo.create(user_id=user_id, subscriber_id=subscriber_id)

    async def get_subscribers(self, user_id: int):
        return await self._repo.get_all_subscribers(user_id)