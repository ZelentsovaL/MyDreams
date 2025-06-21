from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


from app.database.connector.connector import get_session
from app.database.models.models import User
from app.database.repo.wishes_list_repository import WishesListRepository
from app.security.jwt_provider.jwtmanager import get_current_user
from app.services.wish_list_service import WishListService

wish_lists_router = APIRouter(
    prefix="/wish_lists",
    tags=["Wish Lists"],
)

@wish_lists_router.post("/add_to_list")
async def add_wish_to_list(wish_id: int, list_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishesListRepository(session).add_to_list(wish_id, list_id)

@wish_lists_router.get("/getall")
async def get_wish_lists(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishListService(session).get_all(user.user_id)

@wish_lists_router.post("/create/{list_name}")
async def create_wish_list(list_name: str, desc: str, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishListService(session).create(user.user_id, list_name, desc)

@wish_lists_router.get("/wishes/getall/{list_id}")
async def get_wish_lists(list_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishListService(session).get_wishes(user.user_id, list_id)