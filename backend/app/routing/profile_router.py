from fastapi import APIRouter, Depends

from app.database.models.models import User
from app.security.jwt_provider.jwtmanager import get_current_user
from backend.app.database.connector.connector import get_session
from backend.app.database.repo.user_repository import UserRepository
from backend.app.schema.profile.update_profile import UpdateProfile

profile_router = APIRouter(
    prefix="/profile",
)


@profile_router.post("/update")
async def update_profile(updates: UpdateProfile, user: User = Depends(get_current_user), session = Depends(get_session)):
    update = await UserRepository(session).update_one(user.user_id, **updates.model_dump())
    return update