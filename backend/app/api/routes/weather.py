from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.api.deps import get_current_user
from app.models import User
from app.services.weather_service import get_current_weather

router=APIRouter(prefix="/weather",tags=["Weather"])

class WeatherRequest(BaseModel):
    latitude: float
    longitude: float

@router.post("")
async def weather(payload:WeatherRequest,current_user:User=Depends(get_current_user)):
    try:
        return await get_current_weather(payload.latitude,payload.longitude)
    except Exception as exc:
        raise HTTPException(status_code=502,detail="Weather provider request failed") from exc
