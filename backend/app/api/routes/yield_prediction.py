from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models import Farm, User, YieldPrediction
from app.services.ml_service import load_yield_model
router=APIRouter(prefix="/yield-prediction",tags=["AI - Yield Prediction"])
class YieldRequest(BaseModel):
 area_acres:float=Field(gt=0); rainfall:float=Field(ge=0); temperature:float; soil_ph:float=Field(ge=0,le=14); farm_id:str|None=None; crop_name:str="Unknown"
@router.post("")
def predict(payload:YieldRequest,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 model=load_yield_model()
 if model is None: raise HTTPException(status_code=503,detail="Yield prediction model is not trained yet")
 farm=None
 if payload.farm_id:
  farm=db.scalar(select(Farm).where(Farm.id==payload.farm_id,Farm.owner_id==current_user.id))
  if not farm: raise HTTPException(status_code=404,detail="Farm not found")
 value=float(model.predict([[payload.area_acres,payload.rainfall,payload.temperature,payload.soil_ph]])[0]); unit="dataset_target_unit"
 if farm: db.add(YieldPrediction(farm_id=farm.id,crop_name=payload.crop_name,predicted_yield=value,unit=unit)); db.commit()
 return {"predicted_yield":value,"unit":unit,"farm_id":farm.id if farm else None}
@router.get("/history/{farm_id}")
def history(farm_id:str,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
 farm=db.scalar(select(Farm).where(Farm.id==farm_id,Farm.owner_id==current_user.id))
 if not farm: raise HTTPException(status_code=404,detail="Farm not found")
 rows=db.scalars(select(YieldPrediction).where(YieldPrediction.farm_id==farm.id).order_by(YieldPrediction.created_at.desc()).limit(50)).all()
 return [{"id":r.id,"crop_name":r.crop_name,"predicted_yield":r.predicted_yield,"unit":r.unit,"confidence":r.confidence,"created_at":r.created_at} for r in rows]
