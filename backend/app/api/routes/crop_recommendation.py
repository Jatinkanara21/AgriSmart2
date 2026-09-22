from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.ml_service import load_crop_model

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
    model = load_crop_model()
    if model is None:
        raise HTTPException(status_code=503, detail="Crop recommendation model is not trained yet.")
    values = [[payload.nitrogen, payload.phosphorus, payload.potassium,
               payload.temperature, payload.humidity, payload.ph, payload.rainfall]]
    prediction = model.predict(values)[0]
    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(max(model.predict_proba(values)[0]))
    return {"crop": str(prediction), "confidence": confidence}
