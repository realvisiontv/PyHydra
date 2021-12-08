from fastapi import APIRouter

from app.api.routes import sink_kafka

router = APIRouter()
router.include_router(sink_kafka.router, tags=["sink"], prefix="/sink/kafka")
