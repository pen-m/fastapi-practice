from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.routers.upload import _DB, EmergencyPlanOut
from app.models.common import WithID, UserOwned, apply_partial_update

router = APIRouter()

class EmergencyPlanUpdate(UserOwned, WithID):
    #inherits id, user_id
    primary_contact_name: Optional[str] = None
    primary_contact_phone: Optional[str] = None
    emergency_procedures: Optional[str] = None
    allergies: Optional[str] = None
    medication_list: Optional[str] = None
    additional_notes: Optional[str] = None

@router.put("/emergency_plan", response_model=EmergencyPlanOut)
def update_emergency_plan(update: EmergencyPlanUpdate):
    if update.id not in _DB:
        raise HTTPException(status_code=404, detail="Record not found")
    
    existing = _DB[update.id]

    if update.user_id != existing.user_id:
        raise HTTPException(status_code=403, detail="Verification mismatch: user not authorized to updated this record")
    
    #update only the given fields
    updated_data = apply_partial_update(existing, update)

    #preserve original creation timestamp
    updated_data["created_at"]=existing.created_at
    updated_data["updated_at"] = datetime.utcnow()

    updated_record = EmergencyPlanOut(**updated_data)
    _DB[update.id] = updated_record

    return updated_record