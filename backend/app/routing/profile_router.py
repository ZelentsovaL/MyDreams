from fastapi import APIRouter, Depends

from app.database.models.models import User
from app.security.jwt_provider.jwtmanager import get_current_user

profile_router = APIRouter(
    prefix="/profile",
)


@profile_router.post("/update")
async def update_profile(user: User = Depends(get_current_user)):
    return user