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

    completed_wishes: Mapped[List["CompletedWishes"]] = relationship("CompletedWishes", back_populates="user")


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
    wish: Mapped[str]
    price: Mapped[float]
    source_url: Mapped[str] 
    is_secret: Mapped[bool] = mapped_column(default=False)
    wish_photo: Mapped[str] = mapped_column(nullable=True)
    user: Mapped["User"] = relationship("User", back_populates="wishes")

    completed_wishes: Mapped[List["CompletedWishes"]] = relationship("CompletedWishes", back_populates="wish")


class CompletedWishes(Base):
    __tablename__ = "completed_wishes"

    complete_wish_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    wish_id: Mapped[int] = mapped_column(ForeignKey("users_wishes.wish_id"))
    wish: Mapped["Wish"] = relationship("Wish", back_populates="completed_wishes")
    user: Mapped["User"] = relationship("User", back_populates="completed_wishes")

class Subscriptions(Base):
    __tablename__ = "subscriptions"

    sub_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    subscriber_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

