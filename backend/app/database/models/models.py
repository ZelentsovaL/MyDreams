from typing import List, Optional
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

    is_private: Mapped[Optional[bool]] = mapped_column(default=False)
    email: Mapped[str] = mapped_column(nullable=True)

    user_profile: Mapped["UserProfile"] = relationship("UserProfile", back_populates="user")\

    wishes: Mapped[List["Wish"]] = relationship("Wish", back_populates="user")

    completed_wishes: Mapped[List["CompletedWishes"]] = relationship("CompletedWishes", back_populates="user")

    armored_wishes: Mapped[List["ArmoredWishes"]] = relationship("ArmoredWishes", back_populates="user")

class ArmoredWishes(Base):
    __tablename__ = 'armored_wishes'

    armored_wish_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    wish_id: Mapped[int] = mapped_column(ForeignKey("users_wishes.wish_id"))
    user: Mapped["User"] = relationship("User", back_populates="armored_wishes")
    wish: Mapped["Wish"] = relationship("Wish", back_populates="armored_wishes")


class WishesList(Base):
    __tablename__ = 'wishes_lists'

    wishes_list_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    list_name: Mapped[str]
    wishes_in_list: Mapped[List["WishesInList"]] = relationship("WishesInList", back_populates="list")

class WishesInList(Base):
    __tablename__ = 'wishes_in_list'

    wishes_in_list_id: Mapped[int] = mapped_column(primary_key=True)
    wish_id: Mapped[int] = mapped_column(ForeignKey("users_wishes.wish_id"))
    list_id: Mapped[int] = mapped_column(ForeignKey("wishes_lists.wishes_list_id"))
    wish: Mapped["Wish"] = relationship("Wish", back_populates="wishes_in_list")
    list: Mapped["WishesList"] = relationship("WishesList", back_populates="wishes_in_list")

    
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



    armored_wishes: Mapped[List["ArmoredWishes"]] = relationship("ArmoredWishes", back_populates="wish")

    wishes_in_list: Mapped[List["WishesInList"]] = relationship("WishesInList", back_populates="wish")

class CompletedWishes(Base):
    __tablename__ = "completed_wishes"

    complete_wish_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    wish_title: Mapped[str]
    wish_price: Mapped[float]
    wish_source_url: Mapped[str | None]
    wish_photo: Mapped[str | None]
    user: Mapped["User"] = relationship("User", back_populates="completed_wishes")

class Subscriptions(Base):
    __tablename__ = "subscriptions"

    sub_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    subscriber_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))

