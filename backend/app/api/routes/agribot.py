from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models import ChatMessage, ChatSession, User

router = APIRouter(prefix="/agribot", tags=["AgriBot"])

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    session_id: str | None = None

def local_reply(message: str) -> str:
    text = message.lower()
    if "irrig" in text or "water" in text:
        return "Check soil moisture before irrigation. If moisture is low, irrigate according to your crop and local soil conditions."
    if "disease" in text or "leaf" in text:
        return "Upload a clear leaf image in Disease Detection for model-based analysis when the disease model is installed."
    if "weather" in text or "rain" in text:
        return "Use the Weather module with your farm coordinates to review current weather conditions."
    if "crop" in text or "plant" in text:
        return "Use Crop Recommendation with soil N-P-K, pH, temperature, humidity and rainfall data."
    return "I can help with crops, irrigation, soil, weather and plant disease workflows. Add your farm conditions for a more specific recommendation."

@router.post("/chat")
def chat(payload: ChatRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    session = None
    if payload.session_id:
        session = db.scalar(select(ChatSession).where(ChatSession.id == payload.session_id, ChatSession.user_id == current_user.id))
    if session is None:
        session = ChatSession(user_id=current_user.id, title=payload.message[:80])
        db.add(session)
        db.flush()
    reply = local_reply(payload.message)
    db.add(ChatMessage(session_id=session.id, role="user", content=payload.message))
    db.add(ChatMessage(session_id=session.id, role="assistant", content=reply))
    db.commit()
    return {"status": "local_fallback", "reply": reply, "message": payload.message, "session_id": session.id}
