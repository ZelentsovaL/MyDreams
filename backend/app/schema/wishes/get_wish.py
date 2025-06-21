from pydantic import BaseModel, field_validator

class GetWish(BaseModel):
    wish_id: int
    wish: str
    price: float
    source_url: str | None
    is_secret: bool
    wish_photo: str | None

    @field_validator('wish_photo')
    def validator(cls, v):
        return f"https://mydreams.speedsolver.ru/{v}" if (v is not None) else None
    

class GetRecomendationWishes(BaseModel):
    name: str
    price: float
    photo: str
    description: str
    source_url: str

class GetCompletedWish(BaseModel):
    wish_title: str
    wish_price: float
    wish_source_url: str | None
    wish_photo: str | None

    @field_validator('wish_photo')
    def validator(cls, v):
        return f"https://mydreams.speedsolver.ru/{v}" if (v is not None) else None