from fastapi import APIRouter, Depends

from app.database.connector.connector import get_session
from app.database.models.models import User
from app.schema.wishes.create_wish import CreateWish
from app.security.jwt_provider.jwtmanager import get_current_user

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from app.services.wish_service import WishService



wish_router = APIRouter(
    prefix="/wishes",
    tags=["Wishes"],
)

@wish_router.get("/getall")
async def get_wishes(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    all_wishes = await UserService(session).get_all_wishes(user.user_id)
    return all_wishes

@wish_router.post("/create")
async def create_wish(create_wish: CreateWish, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).create_wish(user.user_id, create_wish)