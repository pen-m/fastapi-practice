from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime
from uuid import uuid4
from app.models.common import WithID, Timestamps
from app.core.auth import get_current_user

router = APIRouter()


# ----- Schemas -----
class EmergencyPlanIn(BaseModel):
    user_id: Optional[str] = None #will be provided by authentication
    primary_contact_name: str
    primary_contact_phone: str
    emergency_procedures: Optional[str] = None
    allergies: Optional[str] = None
    medication_list: Optional[str] = None
    additional_notes: Optional[str] = None


class EmergencyPlanOut(EmergencyPlanIn, WithID, Timestamps):
    # all fields are inherited
    pass


# In-memory database, swap for real db later
_DB: Dict[str, EmergencyPlanOut] = {}


# ----- Route -----
@router.post("/emergency_plan", response_model=EmergencyPlanOut, status_code=201)
def upload_emergency_plan(
    payload: EmergencyPlanIn, current_user_id: str = Depends(get_current_user)
):
    
    """
    1. Receives emergency plan from frontend form
    2. Validates user authentication (token -> user id)
    3. Assigns user id to the record
    4. Creates EmergencyPlan with timestamp + unique ID
    5. Stores in-memory db (replace with real db)
    6. Returns created record for confirmation
    """

    payload.user_id = current_user_id

    record = EmergencyPlanOut(**payload.model_dump())
    _DB[record.id] = record

    return record


@router.get("/emergency_plan", response_model=List[EmergencyPlanOut])
def get_emergency_plans():
    return list(_DB.values())
