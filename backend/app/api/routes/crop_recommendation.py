from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models import CropRecommendation, Farm, User
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
    farm_id: str | None = None

@router.post("")
def recommend_crop(payload: CropRecommendationRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    model = load_crop_model()
    if model is None:
        raise HTTPException(status_code=503, detail="Crop recommendation model is not trained yet.")
    farm = None
    if payload.farm_id:
        farm = db.scalar(select(Farm).where(Farm.id == payload.farm_id, Farm.owner_id == current_user.id))
        if not farm:
            raise HTTPException(status_code=404, detail="Farm not found")
    values = [[payload.nitrogen, payload.phosphorus, payload.potassium, payload.temperature, payload.humidity, payload.ph, payload.rainfall]]
    prediction = model.predict(values)[0]
    confidence = float(max(model.predict_proba(values)[0])) if hasattr(model, "predict_proba") else None
    if farm:
        db.add(CropRecommendation(farm_id=farm.id, crop_name=str(prediction), confidence=confidence, reason="ML crop recommendation"))
        db.commit()
    return {"crop": str(prediction), "confidence": confidence, "farm_id": farm.id if farm else None}
