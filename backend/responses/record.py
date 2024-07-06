from backend.responses.base import BaseRequest, BaseResponse


class RecordRequest(BaseRequest):
    game_id: int
    victory: bool
    name: str
    kill: int = -1
    assist: int = -1
    death: int = -1
    point: int = -1


class RecordResponse(BaseResponse, RecordRequest):
    id: int
