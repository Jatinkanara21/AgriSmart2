from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from app.api.deps import get_current_user
from app.models import User
from app.services.ml_service import load_yield_model

router = APIRouter(prefix="/yield-prediction", tags=["AI - Yield Prediction"])

class YieldRequest(BaseModel):
    area_acres: float = Field(gt=0)
    rainfall: float = Field(ge=0)
    temperature: float
    soil_ph: float = Field(ge=0, le=14)

@router.post("")
def predict(payload: YieldRequest, current_user: User = Depends(get_current_user)):
    model = load_yield_model()
    if model is None:
        raise HTTPException(status_code=503, detail="Yield prediction model is not trained yet")
    value = float(model.predict([[payload.area_acres, payload.rainfall, payload.temperature, payload.soil_ph]])[0])
    return {"predicted_yield": value, "unit": "dataset_target_unit"}
