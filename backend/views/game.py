from django.core.handlers.wsgi import WSGIRequest
from ninja import Router

from backend.responses.game import GameRequest, GameResponse
from backend.service.game import create_new

router = Router()


@router.post("/new", response=GameResponse)
def create(request: WSGIRequest, game_request: GameRequest) -> GameResponse:
    game = create_new(game_request=game_request)
    return GameResponse(**game.__dict__)
