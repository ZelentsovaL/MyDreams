from sqlalchemy import and_, delete, select
from app.database.abc.repository import AbstractRepository
from app.database.models.models import Subscriptions, User
class SubscribeRepository(AbstractRepository):
    model = Subscriptions

    async def get_subscriptions(self, user_id: int):
        query = (
            select(User.username, User.user_id)
            .select_from(self.model)
            .where(self.model.user_id == user_id)
            .join(User, self.model.subscriber_id == User.user_id)

        )

        result = await self._session.execute(query)
        subscriptions = result.mappings().all()
        return subscriptions


    async def unsubscribe(self, user_id: int, subscriber_id: int) -> None:
        query = (
            delete(self.model)
            .where(and_(
                self.model.user_id == user_id,
                self.model.subscriber_id == subscriber_id
            ))
        )

        result = await self._session.execute(query)
        await self.commit()

        return result.rowcount

    async def get_all_subscribers(self, user_id: int):
        query = (
            select(User.username, User.user_id)
            .select_from(self.model)
            .where(self.model.subscriber_id == user_id)
            .join(User, self.model.user_id == User.user_id)
        )

        result = await self._session.execute(query)
        subscribers = result.mappings().all()
        return subscribers