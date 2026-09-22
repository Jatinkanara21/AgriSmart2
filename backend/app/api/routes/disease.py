from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from app.api.deps import get_current_user
from app.models import User

router = APIRouter(prefix="/disease-detection", tags=["AI - Disease Detection"])

@router.post("")
async def detect_disease(image: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Upload a valid image file")
    return {"status":"model_pending","filename":image.filename,"message":"Disease model inference will be enabled after a trained image classifier is installed."}
