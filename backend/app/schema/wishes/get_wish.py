from pydantic import BaseModel, field_validator

class GetWish(BaseModel):
    wish: str
    price: float
    source_url: str | None
    is_secret: bool
    wish_photo: str | None

    @field_validator('wish_photo')
    def validator(cls, v):
        return f"https://mydreams.speedsolver.ru/{v}" if (v is not None) else None