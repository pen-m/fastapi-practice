from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import modules here
# from routes import auth, upload, llm, admin
from routes import upload

app = FastAPI(
    title="Three-TEW Care API",
    description="Backend API for supporting document uploads, LLM summaries, and analytics.",
    version="0.1.0",
)

# Allow front-end/mobile app to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with specific domain(s) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (commented until built)
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
# app.include_router(llm.router, prefix="/llm", tags=["LLM"])
# app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Three-TEW Care API"}