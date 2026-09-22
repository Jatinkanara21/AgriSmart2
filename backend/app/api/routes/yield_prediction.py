from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.ml_service import load_yield_model

router = APIRouter(prefix="/yield-prediction", tags=["AI - Yield Prediction"])

class YieldPredictionRequest(BaseModel):
    crop_name: str
    area_acres: float = Field(gt=0)
    rainfall: float = Field(ge=0)
    temperature: float
    soil_ph: float = Field(ge=0, le=14)

@router.post("")
def predict_yield(payload: YieldPredictionRequest):
    model = load_yield_model()
    if model is None:
        raise HTTPException(status_code=503, detail="Yield prediction model is not trained yet.")
    values = [[payload.area_acres, payload.rainfall, payload.temperature, payload.soil_ph]]
    prediction = float(model.predict(values)[0])
    return {"crop": payload.crop_name, "predicted_yield": prediction, "unit": "tonnes"}
