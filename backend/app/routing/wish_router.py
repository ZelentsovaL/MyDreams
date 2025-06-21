import random
from typing import List
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.database.connector.connector import get_session
from app.database.models.models import User
from app.schema.wishes.create_wish import CreateWish
from app.schema.wishes.get_wish import GetCompletedWish, GetWish
from app.schema.wishes.update_wish import UpdateWish
from app.security.jwt_provider.jwtmanager import get_current_user

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user_service import UserService
from app.services.wish_service import WishService



wish_router = APIRouter(
    prefix="/wishes",
    tags=["Wishes"],
)

@wish_router.get("/recomendations", response_model=List[GetWish])
async def get_recomendations(session: AsyncSession = Depends(get_session)):
    wishes = await UserService(session).get_recomendations()
    return random.sample(wishes, 15)

@wish_router.get("/getall", response_model=list[GetWish])
async def get_wishes(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    all_wishes = await UserService(session).get_all_wishes(user.user_id)
    return all_wishes

@wish_router.post("/armored/create/{wish_id}", response_model=GetWish)
async def armor_wish(wish_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).armor_wish(user.user_id, wish_id)

@wish_router.get("/armored/getall/{user_id}", response_model=list[GetWish])
async def get_armored_wishes(user_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).get_armored_wishes(user_id)

@wish_router.get("/armoder/my/all", response_model=list[GetWish])
async def get_armored_wishes(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).get_armored_wishes(user.user_id)

@wish_router.post("/create")
async def create_wish(create_wish: CreateWish, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).create_wish(user.user_id, create_wish)

@wish_router.get("/completed/getall", response_model=list[GetCompletedWish])
async def get_completed_wishes(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).get_completed_wishes(user.user_id)

@wish_router.post("/photo/create/{wish_id}", response_model=GetWish)
async def create_wish_photo(wish_id: int, photo: UploadFile = File(...), user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).upload_photo(wish_id, photo)

@wish_router.post("/complete/{wish_id}", response_model=GetWish)
async def complete_wish(wish_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).complete_wish(user.user_id, wish_id)

@wish_router.delete("/delete/{wish_id}")
async def delete_wish(wish_id: int, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    deleted_rows = await WishService(session).delete_wish(user.user_id, wish_id)
    if (deleted_rows == 0):
        raise HTTPException(
            status_code=400,
            detail="Wish not found",
        )
    
    return deleted_rows

@wish_router.put("/update/{wish_id}")
async def update_wish(wish_id: int, update_wish: UpdateWish, user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    return await WishService(session).update_wish(user.user_id, wish_id, update_wish)