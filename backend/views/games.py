from os.path import join

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from ninja import Router
from ninja.files import UploadedFile

from backend.responses.games import GameRequest, GameResponse
from backend.responses.record import RecordResponse
from backend.services.games import create_new, get_pubg_stats_from_image

router = Router()


@router.post("/new", response=GameResponse)
def create(request: WSGIRequest, game_request: GameRequest) -> GameResponse:
    game = create_new(game_request=game_request)
    return GameResponse(**game.__dict__)


@router.post("/pubg/stats", response=list[RecordResponse])
def stats_from_image(request: WSGIRequest, file: UploadedFile) -> list[RecordResponse]:
    tmpfile = join(settings.MEDIA_ROOT, str(file.name))
    with open(file=tmpfile, mode="wb") as f:
        if not file.file:
            raise FileNotFoundError(f"{file.name} does not have any contents.")

        f.write(file.file.read())

    return get_pubg_stats_from_image(image_path=tmpfile)
