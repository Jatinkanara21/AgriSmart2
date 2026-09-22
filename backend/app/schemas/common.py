from datetime import datetime
from pydantic import BaseModel, ConfigDict

class APIModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class HealthResponse(APIModel):
    status: str
    service: str
    version: str
    environment: str
