from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Farm
from app.schemas.farm import FarmCreate, FarmResponse

router = APIRouter(prefix="/farms", tags=["farms"])

@router.post("", response_model=FarmResponse, status_code=201)
def create_farm(payload: FarmCreate, db: Session = Depends(get_db)):
    farm = Farm(**payload.model_dump())
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm

@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm(farm_id: str, db: Session = Depends(get_db)):
    from fastapi import HTTPException
    farm = db.get(Farm, farm_id)
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm
