

from fastapi import Depends, HTTPException
from app.database.connector.connector import get_session
from app.database.repo.user_repository import UserRepository
from app.security.jwt_provider.jwttype import JWTType
from app.utils.ext.result import Result, error, success
from app.security.oauth import oauth_scheme
from sqlalchemy.ext.asyncio import AsyncSession

from jwt import decode, encode
from app.settings.settings import settings

from datetime import datetime, timedelta

async def get_current_user(token: str = Depends(oauth_scheme), session: AsyncSession = Depends(get_session)):

    payload = JWTManager().decode_token(token)
    if payload.error:
        return error(payload.error)
    
    username: str = payload.value.get("userId")
    if username is None:
        raise HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    user = await UserRepository(session).get_by_filter_one(userId=username)
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

class JWTManager:

    def __init__(self):
        self.SECRET_KEY = settings.JWT_SECRET_KEY
        self.ALGORITHM = settings.JWT_ALGORITHM
        self.ACCESS_TOKEN_LIFETIME = settings.JWT_ACCESS_TOKEN_LIFETIME_HOURS

    def encode_token(self, payload, token_type: JWTType = JWTType.ACCESS):
        jwt_payload = payload.copy()

        current_time = datetime.utcnow()
        expire = timedelta(hours=self.ACCESS_TOKEN_LIFETIME)
        jwt_payload.update({"exp": current_time + expire})
        return encode(jwt_payload, self.SECRET_KEY, algorithm=self.ALGORITHM)
    
    def decode_token(self, token: str) -> Result[dict]:
        try:
            return success(decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM]))
        except:
            return error("Invalid token")
    