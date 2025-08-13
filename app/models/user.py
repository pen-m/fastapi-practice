from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from app.models.common import WithID, Timestamps

class UserIn(BaseModel):
    name: str
    email: EmailStr
    role: str = "caregiver" #or ... ?patient? family member? define roles

class UserOut(UserIn, WithID, Timestamps):
    #inherits all fields
    pass