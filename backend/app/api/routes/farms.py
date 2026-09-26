from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models import Farm, User
from app.schemas.farm import FarmCreate, FarmResponse

router = APIRouter(prefix="/farms", tags=["farms"])

@router.post("", response_model=FarmResponse, status_code=status.HTTP_201_CREATED)
def create_farm(payload: FarmCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    farm = Farm(owner_id=current_user.id, **payload.model_dump())
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return farm

@router.get("", response_model=list[FarmResponse])
def list_farms(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return list(db.scalars(select(Farm).where(Farm.owner_id == current_user.id).order_by(Farm.created_at.desc())).all())

@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm(farm_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    farm = db.scalar(select(Farm).where(Farm.id == farm_id, Farm.owner_id == current_user.id))
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm

@router.delete("/{farm_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_farm(farm_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    farm = db.scalar(select(Farm).where(Farm.id == farm_id, Farm.owner_id == current_user.id))
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    db.delete(farm)
    db.commit()
