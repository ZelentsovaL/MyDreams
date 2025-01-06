from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.schema.access import Access

from app.database.connector.connector import get_session
from app.database.models.models import User, UserProfile

from app.schema.token.access_token import AccessToken
from app.security.jwt_provider.jwtmanager import JWTManager
from app.services.user_service import UserService

from sqlalchemy import (
    select, 
    update, 
    insert, 
    delete
)

from sqlalchemy.ext.asyncio import AsyncSession
access_router = APIRouter()

@access_router.post("/register")
async def register(access: Access, session: AsyncSession = Depends(get_session)):
    registered = await UserService(session).register(access)
    if registered.error:
        raise HTTPException(status_code=400, detail=registered.error)
    return registered.value
    
@access_router.post("/login")
async def login(access: Access, session: Annotated[AsyncSession, Depends(get_session)]):
    user = await UserService(session).login(access)
    if not user.success:
        raise HTTPException(status_code=400, detail=user.error)
    
    token = JWTManager().encode_token({"userId": user.value.user_id})
    return AccessToken(
        access_token=token,
        token_type="Bearer"
    )
    