from pydantic import BaseModel, ConfigDict, Field

class FarmCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    location: str | None = None
    area_acres: float = Field(gt=0)
    soil_type: str | None = None

class FarmResponse(FarmCreate):
    id: str
    owner_id: str
    model_config = ConfigDict(from_attributes=True)
