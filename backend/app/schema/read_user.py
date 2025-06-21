from pydantic import BaseModel, field_validator

class ReadUser(BaseModel):
    username: str
    email: str
    is_private: bool
    photo: str

    @field_validator('photo')
    def validate_photo(cls, v):
        return f"https://mydreams.speedsolver.ru/{v}"