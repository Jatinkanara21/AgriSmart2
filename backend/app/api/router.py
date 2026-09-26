from fastapi import APIRouter
from app.api.routes import system, auth, farms, crop_recommendation, disease, yield_prediction, agribot, weather, decision_engine, admin
api_router=APIRouter()
for router in [system.router,auth.router,farms.router,crop_recommendation.router,disease.router,yield_prediction.router,agribot.router,weather.router,decision_engine.router,admin.router]: api_router.include_router(router)
