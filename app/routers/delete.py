from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from app.routers.upload import _DB, EmergencyPlanOut

router = APIRouter()


class DeleteRequest(BaseModel):
    user_id: str


@router.delete("/emergency_plan/{id}", status_code=204)
def delete_emergency_plan(id: str = Path(...), payload: DeleteRequest = None):
    if id not in _DB:
        raise HTTPException(status_code=404, detail="Record not found")

    record = _DB[id]
    if payload.user_id != record.user_id:
        raise HTTPException(
            status_code=403,
            detail="Verification mismatch: user not authorized to delete this record",
        )

    del _DB[id]
    return
