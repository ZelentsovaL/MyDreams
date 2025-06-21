from pydantic import BaseModel


class UpdateProfile(BaseModel):
    username: str
    is_private: bool