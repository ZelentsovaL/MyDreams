import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routing.main_router import main_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/photos", StaticFiles(directory=f"{os.path.dirname(__file__)}/photos"), name="photos")


app.include_router(main_router)