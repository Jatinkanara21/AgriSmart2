from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.api.deps import get_current_user
from app.models import User

router=APIRouter(prefix="/agribot",tags=["AgriBot"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1,max_length=4000)

@router.post("/chat")
def chat(payload:ChatRequest,current_user:User=Depends(get_current_user)):
    return {
        "status":"provider_pending",
        "reply":"AgriBot AI provider is not configured yet. Your message was received successfully.",
        "message":payload.message
    }
