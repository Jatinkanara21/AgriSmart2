from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.db.session import get_db
from app.models import User
bearer=HTTPBearer(auto_error=False)
def get_current_user(credentials:HTTPAuthorizationCredentials|None=Depends(bearer),db:Session=Depends(get_db))->User:
 if not credentials: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Authentication required")
 try: user_id=str(decode_access_token(credentials.credentials)["sub"])
 except Exception as exc: raise HTTPException(status_code=401,detail="Invalid or expired token") from exc
 user=db.get(User,user_id)
 if not user or not user.is_active: raise HTTPException(status_code=401,detail="User is inactive or not found")
 return user
def get_current_admin(current_user:User=Depends(get_current_user))->User:
 if not current_user.is_admin: raise HTTPException(status_code=403,detail="Admin access required")
 return current_user
