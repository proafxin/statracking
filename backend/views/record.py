from django.core.handlers.wsgi import WSGIRequest
from ninja import Router

from backend.responses.record import RecordRequest, RecordResponse
from backend.service.record import create_new

router = Router()


@router.post("/new", response=RecordResponse)
def create(request: WSGIRequest, record_request: RecordRequest) -> RecordResponse:
    record = create_new(record_request=record_request)
    return RecordResponse(**record.__dict__)
