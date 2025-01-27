from sqlalchemy import select
from app.database.abc.repository import AbstractRepository
from app.database.models.models import Subscriptions, User
class SubscribeRepository(AbstractRepository):
    model = Subscriptions


    async def get_all_subscribers(self, user_id: int):
        query = (
            select(User)
            .select_from(self.model)
            .where(self.model.subscriber_id == user_id)
            .join(User, self.model.user_id == User.user_id)
        )

        result = await self._session.execute(query)
        subscribers = result.scalars().all()
        return subscribers