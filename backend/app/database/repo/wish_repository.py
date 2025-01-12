from app.database.abc.repository import AbstractRepository
from app.database.models.models import Wish


class WishRepository(AbstractRepository):
    model = Wish