from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/status", tags=["system"])
def api_status():
    return {"status": "ok", "api": "v1"}
