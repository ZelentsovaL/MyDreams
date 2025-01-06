from fastapi import APIRouter

profile_router = APIRouter(
    prefix="/profile",
)


@profile_router.post("/update")
async def update_profile():
    ...