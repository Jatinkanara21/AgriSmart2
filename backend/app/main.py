from fastapi import FastAPI
from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="2.0.0",
    debug=settings.debug,
    description="AI-powered smart farming platform API.",
)

app.include_router(api_router, prefix=settings.api_v1_prefix)

@app.get("/health", tags=["system"])
def health_check():
    return {
        "status": "ok",
        "service": "AgriSmart API",
        "version": "2.0.0",
        "environment": settings.app_env,
    }
