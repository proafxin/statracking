from backend.responses.base import BaseRequest, BaseResponse


class GameRequest(BaseRequest):
    name: str


class GameResponse(BaseResponse, GameRequest):
    id: int
