from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps import get_current_user
from app.models import User

router=APIRouter(prefix="/weather",tags=["Weather"])

class WeatherRequest(BaseModel):
    latitude: float
    longitude: float

@router.post("")
def weather(payload:WeatherRequest,current_user:User=Depends(get_current_user)):
    return {
        "status":"provider_pending",
        "latitude":payload.latitude,
        "longitude":payload.longitude,
        "message":"Connect a weather provider in the service layer before using live weather data."
    }
