import httpx
from app.core.config import settings

async def get_current_weather(latitude: float, longitude: float) -> dict:
    if not settings.weather_api_key:
        return {"status":"provider_not_configured","message":"Set WEATHER_API_KEY to enable live weather."}
    params={"lat":latitude,"lon":longitude,"appid":settings.weather_api_key,"units":"metric"}
    async with httpx.AsyncClient(timeout=10) as client:
        response=await client.get(settings.weather_base_url,params=params)
        response.raise_for_status()
        data=response.json()
    return {
        "status":"ok",
        "location":data.get("name"),
        "temperature_c":data.get("main",{}).get("temp"),
        "humidity":data.get("main",{}).get("humidity"),
        "pressure_hpa":data.get("main",{}).get("pressure"),
        "weather":data.get("weather",[{}])[0].get("description"),
        "wind_speed_mps":data.get("wind",{}).get("speed"),
    }
