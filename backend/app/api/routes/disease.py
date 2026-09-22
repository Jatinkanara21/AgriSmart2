from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/disease-detection", tags=["AI - Disease Detection"])

@router.post("")
async def detect_disease(image: UploadFile = File(...)):
    return {
        "status": "model_pending",
        "filename": image.filename,
        "message": "Plant disease model will be connected after dataset training.",
    }
