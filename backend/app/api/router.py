from fastapi import APIRouter
from app.api.routes import agribot, crop_recommendation, disease, farms, system, yield_prediction

api_router = APIRouter()
api_router.include_router(system.router)
api_router.include_router(farms.router)
api_router.include_router(crop_recommendation.router)
api_router.include_router(disease.router)
api_router.include_router(yield_prediction.router)
api_router.include_router(agribot.router)
