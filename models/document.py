from pydantic import BaseModel, Field
from typing import Optional

class UploadMetadata(BaseModel):
    user_id: str = Field(..., description="Unique user identifier")
    document_type: str = Field(..., description="Type of uploaded document (e.g. 'insurance', 'medication')")
    notes: Optional[str] = Field(None, description="Optional user-provided context or label")