from pydantic import BaseModel

class UpdateWish(BaseModel):
    new_title: str
    new_price: float
    new_source_url: str
    is_secret: bool