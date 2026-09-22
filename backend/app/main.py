from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="2.0.0",
    debug=settings.debug,
)

@app.get("/health", tags=["system"])
def health_check():
    return {
        "status": "ok",
        "service": "AgriSmart API",
        "version": "2.0.0",
    }
