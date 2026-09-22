from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/yield-prediction", tags=["AI - Yield Prediction"])

class YieldPredictionRequest(BaseModel):
    crop_name: str
    area_acres: float = Field(gt=0)
    rainfall: float = Field(ge=0)
    temperature: float
    soil_ph: float = Field(ge=0, le=14)

@router.post("")
def predict_yield(payload: YieldPredictionRequest):
    return {
        "status": "model_pending",
        "message": "Yield prediction model will be connected after dataset training.",
        "input": payload.model_dump(),
    }
