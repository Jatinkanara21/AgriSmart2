from pydantic import Field
from app.schemas.common import APIModel

class FarmCreate(APIModel):
    owner_id: str
    name: str = Field(min_length=2, max_length=150)
    location: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    area_acres: float | None = Field(default=None, gt=0)
    soil_type: str | None = None

class FarmResponse(FarmCreate):
    id: str
