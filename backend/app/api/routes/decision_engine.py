from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.api.deps import get_current_user
from app.models import User

router=APIRouter(prefix="/decision-engine",tags=["Smart Farming Decision Engine"])

class DecisionRequest(BaseModel):
    temperature: float
    humidity: float=Field(ge=0,le=100)
    rainfall: float=Field(ge=0)
    soil_moisture: float=Field(ge=0,le=100)
    soil_ph: float=Field(ge=0,le=14)

@router.post("/analyze")
def analyze(payload:DecisionRequest,current_user:User=Depends(get_current_user)):
    recommendations=[]
    if payload.soil_moisture < 30: recommendations.append("Consider irrigation; soil moisture is low.")
    if payload.rainfall > 80: recommendations.append("Monitor drainage because rainfall is high.")
    if payload.soil_ph < 5.5: recommendations.append("Consider a soil-management plan for acidic soil.")
    if payload.soil_ph > 7.5: recommendations.append("Consider a soil-management plan for alkaline soil.")
    if payload.temperature > 38: recommendations.append("Monitor heat stress because temperature is high.")
    if payload.humidity > 90: recommendations.append("Monitor fungal-risk conditions because humidity is high.")
    if not recommendations: recommendations.append("No basic risk rule was triggered by the supplied values.")
    return {"recommendations":recommendations,"rules_version":"1.1"}
