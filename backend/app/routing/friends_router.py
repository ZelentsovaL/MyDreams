from typing import Annotated
from fastapi import APIRouter, Depends

from app.database.connector.connector import get_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.search_service import SearchService

friends_router = APIRouter(
    prefix="/friends",
    tags=["Friends"]
)

@friends_router.get("/search/username")
async def search_by_username(username: str, session: Annotated[AsyncSession, Depends(get_session)]):
    return await SearchService(session).search_by_username(username)