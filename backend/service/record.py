from ninja.errors import ValidationError

from backend.models.record import Record
from backend.responses.record import RecordRequest
from backend.service.game import get_by_id as game_by_id


def create_new(record_request: RecordRequest) -> Record:
    game = game_by_id(id=record_request.game_id)
    if not game:
        raise ValidationError(errors=[{"error": f"Game: {record_request.game_id} is not found."}])

    record = Record(**record_request.model_dump())
    record.save()
    record.refresh_from_db()

    return record
