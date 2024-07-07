from backend.models.records import Record
from backend.responses.record import RecordRequest


def create_new(record_request: RecordRequest) -> Record:
    record = Record(**record_request.model_dump())
    if not record.date:
        record.date = record.created_at
    record.save()
    record.refresh_from_db()

    return record
