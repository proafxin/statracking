from backend.models.record import Record
from backend.responses.record import RecordRequest


def create_new(record_request: RecordRequest) -> Record:
    record = Record(**record_request.model_dump())
    record.save()
    record.refresh_from_db()

    return record
