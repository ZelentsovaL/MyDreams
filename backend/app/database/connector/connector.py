from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import ( 
    AsyncSession, 
    AsyncEngine,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from contextlib import asynccontextmanager

from app.settings.settings import settings

engine = create_async_engine(str(settings.db_url))
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()