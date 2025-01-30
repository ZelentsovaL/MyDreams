from pydantic import BaseModel, field_validator

class GetWish(BaseModel):
    wish: str
    price: float
    source_url: str | None
    is_secret: bool
    wish_photo: str

    @field_validator('wish_photo')
    def validator(cls, v):
        return f"http://mydreams.speedsolver.ru/{v}"