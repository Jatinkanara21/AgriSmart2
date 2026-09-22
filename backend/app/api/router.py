from fastapi import APIRouter
from app.api.routes import farms, system

api_router = APIRouter()
api_router.include_router(system.router)
api_router.include_router(farms.router)
