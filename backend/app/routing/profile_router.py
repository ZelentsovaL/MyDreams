import glob
import os
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.database.models.models import User
from app.security.jwt_provider.jwtmanager import get_current_user
from app.database.connector.connector import get_session
from app.database.repo.user_repository import UserRepository
from app.schema.profile.update_profile import UpdateProfile
from app.schema.read_user import ReadUser

profile_router = APIRouter(
    prefix="/profile",
)


@profile_router.post("/update")
async def update_profile(updates: UpdateProfile, user: User = Depends(get_current_user), session = Depends(get_session)):
    update = await UserRepository(session).update_one(user.user_id, **updates.model_dump())
    return update


@profile_router.post("/photo/upload", response_model=ReadUser)
async def upload_photo(avatar: UploadFile = File(...), user: User = Depends(get_current_user), session = Depends(get_session)):
    if not avatar.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail=f"Файл {avatar.filename} не является изображением",
        )
    
    try:
        exists = glob.glob(f"photos/avatar_{user.user_id}.*")
        if exists:
            os.remove(exists[0])
        extension = avatar.filename.split(".")[-1] # jpg, png?
        path = f"photos/avatar_{user.user_id}.{extension}"
        directory = os.path.dirname(path)
        os.makedirs(directory, exist_ok=True)
        with open(f"{path}", "wb") as f:
            f.write(await avatar.read())

        return await UserRepository(session).update_one(user.user_id, photo=path)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Произошла ошибка во время загрузки файла {avatar.filename}: {str(e)}",
        )
