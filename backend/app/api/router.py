from fastapi import APIRouter
from app.api.routes import system, auth, farms, crop_recommendation, disease, yield_prediction, agribot, weather, decision_engine

api_router=APIRouter()
api_router.include_router(system.router)
api_router.include_router(auth.router)
api_router.include_router(farms.router)
api_router.include_router(crop_recommendation.router)
api_router.include_router(disease.router)
api_router.include_router(yield_prediction.router)
api_router.include_router(agribot.router)
api_router.include_router(weather.router)
api_router.include_router(decision_engine.router)
