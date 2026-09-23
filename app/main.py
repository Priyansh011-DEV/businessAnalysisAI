from fastapi import FastAPI

app = FastAPI(
    title="Business Analysis Suite",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Business Analysis API is running"
    }