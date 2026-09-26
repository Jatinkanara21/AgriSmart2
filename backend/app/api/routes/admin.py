from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from app.api.deps import get_current_admin
from app.db.session import get_db
from app.models import CropRecommendation, DiseasePrediction, Farm, User, YieldPrediction
router=APIRouter(prefix="/admin",tags=["Admin"])
@router.get("/stats")
def stats(db:Session=Depends(get_db),admin:User=Depends(get_current_admin)):
 return {"users":db.scalar(select(func.count()).select_from(User)) or 0,"farms":db.scalar(select(func.count()).select_from(Farm)) or 0,"crop_recommendations":db.scalar(select(func.count()).select_from(CropRecommendation)) or 0,"disease_predictions":db.scalar(select(func.count()).select_from(DiseasePrediction)) or 0,"yield_predictions":db.scalar(select(func.count()).select_from(YieldPrediction)) or 0}
@router.get("/users")
def users(db:Session=Depends(get_db),admin:User=Depends(get_current_admin)):
 rows=db.scalars(select(User).order_by(User.created_at.desc()).limit(100)).all()
 return [{"id":u.id,"full_name":u.full_name,"email":u.email,"is_active":u.is_active,"is_admin":u.is_admin,"created_at":u.created_at} for u in rows]
@router.get("/farms")
def farms(db:Session=Depends(get_db),admin:User=Depends(get_current_admin)):
 rows=db.execute(select(Farm,User).join(User,User.id==Farm.owner_id).order_by(Farm.created_at.desc()).limit(100)).all()
 return [{"id":f.id,"name":f.name,"owner_name":u.full_name,"owner_email":u.email,"location":f.location,"area_acres":f.area_acres,"soil_type":f.soil_type} for f,u in rows]
