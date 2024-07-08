from datetime import datetime
from os.path import join

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from ninja import Router
from ninja.files import UploadedFile

from backend.responses.record import RecordResponse
from backend.responses.stats import LatestPerformanceResponse
from backend.services.stats import (
    get_latest_performance,
    get_pubg_stats_from_image,
    get_stats_from_dir,
)

router = Router()


@router.post("/pubg", response=list[RecordResponse])
def stats_from_image(
    request: WSGIRequest, date: datetime, file: UploadedFile
) -> list[RecordResponse]:
    tmpfile = join(settings.MEDIA_ROOT, str(file.name))
    with open(file=tmpfile, mode="wb") as f:
        if not file.file:
            raise FileNotFoundError(f"{file.name} does not have any contents.")

        f.write(file.file.read())

    return get_pubg_stats_from_image(image_path=tmpfile, match_date=date)


@router.post("/pubg/batch", response=list[str])
def stats_from_image_dir(request: WSGIRequest, date: datetime, image_dir: str) -> list[str]:
    return get_stats_from_dir(image_dir=image_dir, match_date=date)


@router.post("/pubg/latest/individual", response=LatestPerformanceResponse)
def latest_performance(request: WSGIRequest, name: str) -> LatestPerformanceResponse:
    return get_latest_performance(name=name, game="PUBG")
