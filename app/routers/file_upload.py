from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

router = APIRouter()

@router.post("/image/ocr")
async def ocr_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        #ocr on the image
        extracted_text = pytesseract.image_to_string(image)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "extracted_text": extracted_text.strip() or "No text found"
        }

    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": f"Could not process image: {str(e)}"}
        )