from fastapi import FastAPI

from api.database import Base
from api.database import engine
from api.models import TradeRecord
from api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="B2B Trade Intelligence API",
    description="API for global import/export trade intelligence data",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "B2B Trade Intelligence API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }