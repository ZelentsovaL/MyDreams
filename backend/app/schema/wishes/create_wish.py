from pydantic import BaseModel


class CreateWish(BaseModel):
    wish: str
    price: float
    source_url: str