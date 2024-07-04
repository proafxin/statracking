from django.core.handlers.asgi import ASGIRequest
from ninja import Router

from statracking.responses.game import Game

router = Router()


@router.post("/new")
async def add(request: ASGIRequest, game: Game) -> str:
    print(request.user)
    return game.name
