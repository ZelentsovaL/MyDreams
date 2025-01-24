from fastapi import APIRouter

from app.routing.access_router import access_router
from app.routing.profile_router import profile_router
from app.routing.wish_router import wish_router
from app.routing.friends_router import friends_router

main_router = APIRouter(
    prefix="/v1",
)

main_router.include_router(access_router)
main_router.include_router(profile_router)
main_router.include_router(wish_router)
main_router.include_router(friends_router)