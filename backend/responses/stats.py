from datetime import date

from backend.responses.base import BaseRequest, BaseResponse


class LatestPerformance(BaseRequest):
    name: str
    game_id: int
    total_played: int = 0
    total_won: int = 0
    total_lost: int = 0
    total_assist: int = 0
    total_death: int = 0
    total_kill: int = 0
    total_point: int = 0
    valid_assist_match: int = 0
    valid_death_match: int = 0
    valid_kill_match: int = 0
    valid_point_match: int = 0


class LatestPerformanceResponse(BaseResponse, LatestPerformance):
    pass


class StatRequest(LatestPerformance):
    date: date


class StatResponse(BaseResponse, StatRequest):
    id: int
