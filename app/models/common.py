from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4

# start from BaseSchema instead of BaseModel
class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

#For user-linked records
class UserOwned(BaseSchema):
    user_id: str

#For auto-generated IDs
class WithID(BaseSchema):
    id: str = Field(default_factory=lambda: uuid4().hex)

#For timestamps - created and (optional) updated
class Timestamps(BaseSchema):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime | None = None

def apply_partial_update(existing: BaseModel, update_obj: BaseModel, protected_fields: set = {"id", "user_id"}) -> dict:
    updated = existing.model_dump()

    for field, value in update_obj.model_dump(exclude_unset=True).items():
        if field not in protected_fields and value is not None:
            updated[field] = value
    
    return updated