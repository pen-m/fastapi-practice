from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime
from uuid import uuid4
from app.models.common import WithID, Timestamps

router = APIRouter()

# ----- Schemas -----
class EmergencyPlanIn(BaseModel):
    user_id: str
    primary_contact_name: str
    primary_contact_phone: str
    emergency_procedures: Optional[str] = None
    allergies: Optional[str] = None
    medication_list: Optional[str] = None
    additional_notes: Optional[str] = None

class EmergencyPlanOut(EmergencyPlanIn, WithID, Timestamps):
    #all fields are inherited
    pass

# In-memory database, swap for real db later
_DB: Dict[str, EmergencyPlanOut] = {}

# ----- Route -----
@router.post("/emergency_plan", response_model=EmergencyPlanOut, status_code=201)
def upload_emergency_plan(payload: EmergencyPlanIn):
    record = EmergencyPlanOut(**payload.model_dump())
    _DB[record.id] = record
    return record

@router.get("/emergency_plan", response_model=List[EmergencyPlanOut])
def get_emergency_plans():
    return list(_DB.values())

