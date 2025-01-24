from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
    declarative_base
)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()

    email: Mapped[str] = mapped_column(nullable=True)

    user_profile: Mapped["UserProfile"] = relationship("UserProfile", back_populates="user")\

    wishes: Mapped[List["Wish"]] = relationship("Wish", back_populates="user")

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    user_profile_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    
    surname: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    patronymic: Mapped[str] = mapped_column()
    photo: Mapped[str] = mapped_column(nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="user_profile")

class Wish(Base):
    __tablename__ = "users_wishes"

    wish_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    wish: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
    source_url: Mapped[str] = mapped_column()
    is_secret: Mapped[bool] = mapped_column()
    user: Mapped["User"] = relationship("User", back_populates="wishes")


