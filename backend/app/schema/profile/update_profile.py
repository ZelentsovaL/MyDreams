from pydantic import BaseModel


class UpdateProfile(BaseModel):
    surname: str
    name: str
    patronymic: str