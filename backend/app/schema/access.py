from pydantic import BaseModel, EmailStr

class Access(BaseModel):
    email: EmailStr
    username: str
    password: str