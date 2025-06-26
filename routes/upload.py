from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from models.document import UploadMetadata
from services.extract import extract_text_from_pdf
from services.logger import log_upload_event

router = APIRouter()

@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...),
    user_id: str = Form(...),
    document_type: str = Form(...),
    notes: str = Form(None)
):
    # Read and extract text from PDF
    contents = await file.read()
    try:
        extracted_text = extract_text_from_pdf(contents)
        log_upload_event(
            user_id=user_id,
            document_type=document_type,
            filename=file.filename,
            text_length=len(extracted_text),
         notes=notes or ""
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    # Store the file and metadata
    return {
        "filename": file.filename,
        "document_type": document_type,
        "user_id": user_id,
        "text_preview": extracted_text[:200]  # just to confirm processing
    }