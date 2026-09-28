from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Business Analysis Suite",
    version="1.0.0"
)
app.include_router(auth_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Business Analysis API is running"
    }