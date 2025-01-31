


from app.database.repo.wishes_list_repository import WishesListRepository



class WishListService:

    def __init__(self, session):
        self._session = session
        self._repo = WishesListRepository(self._session)

    async def create(self, user_id: int, list_name: str):
        return await self._repo.create(
            user_id=user_id,
            list_name=list_name
        )
    
    async def get_wishes(self, user_id: int, list_id: int):
        return await self._repo.get_all_wishes(user_id, list_id)