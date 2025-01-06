from fastapi import APIRouter
from app.routing.access_router import access_router

main_router = APIRouter(
    prefix="/v1",
)

main_router.include_router(access_router)
