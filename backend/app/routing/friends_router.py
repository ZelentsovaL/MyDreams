from typing import Annotated
from fastapi import APIRouter, Depends

from app.database.connector.connector import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.models import User
from app.security.jwt_provider.jwtmanager import get_current_user
from app.services.search_service import SearchService
from app.services.sub_service import SubscribeService
from app.services.user_service import UserService

friends_router = APIRouter(
    prefix="/friends",
    tags=["Friends"]
)

@friends_router.get("/search/username")
async def search_by_username(username: str, session: Annotated[AsyncSession, Depends(get_session)]):
    return await SearchService(session).search_by_username(username)

@friends_router.post("/subscribe/{user_id}")
async def subscribe(user_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await SubscribeService(session).subscribe(user.user_id, user_id)
    
@friends_router.post("/unsubscribe/{user_id}")
async def unsubscribe(user_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await SubscribeService(session).unsubscribe(user.user_id, user_id)

@friends_router.get("/subscriptions")
async def get_subscriptions(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await SubscribeService(session).get_subscriptions(user.user_id)

@friends_router.get("/subscribers/")
async def get_subscribers(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await SubscribeService(session).get_subscribers(user.user_id)

@friends_router.get("/wishes/{username}")
async def search_by_username(username: str, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await SearchService(session).get_wishes_by_username(username)
