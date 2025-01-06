from pydantic import BaseModel

class Access(BaseModel):
    username: str
    password: str