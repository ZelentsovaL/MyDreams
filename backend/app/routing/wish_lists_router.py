from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.connector.connector import get_session
from app.database.models.models import User
from app.security.jwt_provider.jwtmanager import get_current_user
from app.services.wish_list_service import WishListService

wish_lists_router = APIRouter(
    prefix="/wish_lists",
    tags=["Wish Lists"],
)


@wish_lists_router.post("/create/{list_name}")
async def create_wish_list(list_name: str, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishListService(session).create(user.user_id, list_name)

@wish_lists_router.get("/wishes/getall/{list_id}")
async def get_wish_lists(list_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishListService(session).get_wishes(user.user_id, list_id)