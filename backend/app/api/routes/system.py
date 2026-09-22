from fastapi import APIRouter
from app.core.config import settings
from app.schemas.common import HealthResponse

router = APIRouter(tags=["system"])

@router.get("/status")
def api_status():
    return {"status": "ok", "api": "v1", "version": "2.0.0"}

@router.get("/health", response_model=HealthResponse)
def api_health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": "2.0.0",
        "environment": settings.app_env,
    }
