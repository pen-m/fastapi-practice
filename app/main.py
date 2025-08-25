from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.models import APIKey, APIKeyIn, SecuritySchemeType
from app.routers import upload, update, delete, file_upload, user

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(update.router, prefix="/update", tags=["update"])
app.include_router(file_upload.router, prefix="/file_upload", tags=["file_upload"])
app.include_router(delete.router, prefix="/delete", tags=["delete"])
app.include_router(user.router, prefix="/user", tags=["user"])


# Add OpenAPI schema for bearer auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="3-2 Care API",
        version="1.0.0",
        description="Caregiver app API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    # Set security globally
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
