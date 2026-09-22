from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/crop-recommendation", tags=["AI - Crop Recommendation"])

class CropRecommendationRequest(BaseModel):
    nitrogen: float = Field(ge=0)
    phosphorus: float = Field(ge=0)
    potassium: float = Field(ge=0)
    temperature: float
    humidity: float = Field(ge=0, le=100)
    ph: float = Field(ge=0, le=14)
    rainfall: float = Field(ge=0)

@router.post("")
def recommend_crop(payload: CropRecommendationRequest):
    # Placeholder until the trained model is loaded.
    return {
        "status": "model_pending",
        "message": "Crop recommendation model will be connected after dataset training.",
        "input": payload.model_dump(),
    }
