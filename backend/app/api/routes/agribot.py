from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/agribot", tags=["AI - AgriBot"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)

@router.post("/chat")
def chat(payload: ChatRequest):
    return {
        "status": "provider_pending",
        "reply": "AgriBot AI provider will be connected in the next stage.",
        "message": payload.message,
    }
