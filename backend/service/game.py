from backend.models.game import Game
from backend.responses.game import GameRequest


def create_new(game_request: GameRequest) -> Game:
    game = Game(**game_request.model_dump())
    game.save()
    game.refresh_from_db()

    return game


def get_by_id(id: int) -> Game | None:
    try:
        game = Game.objects.get(pk=id)
        return game

    except Game.DoesNotExist:
        return None
