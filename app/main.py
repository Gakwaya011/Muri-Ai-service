from fastapi import FastAPI

from app.api.chat import router as chat_router


app = FastAPI(
    title="MURI AI Service",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "service": "MURI AI Service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(
    chat_router,
    prefix="/api"
)