from django.core.handlers.asgi import ASGIRequest
from ninja import Router

from statracking.responses.record import Record

router = Router()


@router.post("/new")
async def create(request: ASGIRequest, record: Record) -> str:
    return record.name
