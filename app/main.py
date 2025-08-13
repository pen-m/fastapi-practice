from fastapi import FastAPI
from app.routers import upload, update, delete, file_upload, user

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(update.router, prefix="/update", tags=["update"])
app.include_router(file_upload.router, prefix="/file_upload", tags=["file_upload"])
app.include_router(delete.router, prefix="/delete", tags=["delete"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

