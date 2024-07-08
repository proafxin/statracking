from datetime import datetime

from easyocr import Reader
from ninja.errors import ValidationError

from backend.models.records import Record
from backend.models.stats import Stat
from backend.responses.games import GameResponse
from backend.responses.record import RecordRequest, RecordResponse
from backend.responses.stats import LatestPerformanceResponse, StatRequest
from backend.services.games import get_by_name
from backend.services.records import create_new as create_new_record
from image_retrieval.parse import parse_image
from image_retrieval.pubg.calculate import get_stats_from_parsed_labels, parse_labels


def create_request(record: Record) -> StatRequest:
    assist = 0
    death = 0
    kill = 0
    point = 0
    valid_assist_match = 0
    valid_death_match = 0
    valid_kill_match = 0
    valid_point_match = 0
    total_lost = 0
    total_won = 0

    if record.assist >= 0:
        assist = record.assist
        valid_assist_match = 1

    if record.death >= 0:
        death = record.death
        valid_death_match = 1

    if record.kill >= 0:
        kill = record.kill
        valid_kill_match = 1

    if record.point >= 0:
        point = record.point
        valid_point_match = 1

    if record.victory:
        total_won = 1
    else:
        total_lost = 1
    date = record.date

    statistic = StatRequest(
        name=record.name,
        game_id=record.game.id,
        date=date,
        total_played=1,
        total_lost=total_lost,
        total_won=total_won,
        total_assist=assist,
        total_death=death,
        total_kill=kill,
        total_point=point,
        valid_assist_match=valid_assist_match,
        valid_death_match=valid_death_match,
        valid_kill_match=valid_kill_match,
        valid_point_match=valid_point_match,
    )

    return statistic


def get_by_name_game(name: str, game_id: int) -> Stat | None:
    try:
        stat = Stat.objects.filter(name=name, game_id=game_id).latest("created_at")

        return stat
    except Stat.DoesNotExist:
        return None


def update_request(old: Stat, current: StatRequest) -> StatRequest:
    new = StatRequest(
        name=old.name,
        game_id=old.game.id,
        date=current.date,
        total_lost=old.total_lost + current.total_lost,
        total_won=old.total_won + current.total_won,
        total_assist=old.total_assist + current.total_assist,
        total_death=old.total_death + current.total_death,
        total_kill=old.total_kill + current.total_kill,
        total_played=old.total_played + current.total_played,
        total_point=old.total_point + current.total_point,
        valid_assist_match=old.valid_assist_match + current.valid_assist_match,
        valid_death_match=old.valid_death_match + current.valid_death_match,
        valid_kill_match=old.valid_kill_match + current.valid_kill_match,
        valid_point_match=old.valid_point_match + current.valid_point_match,
    )

    return new


def create_new(stat_request: StatRequest) -> Stat:
    stat = Stat(**stat_request.model_dump())
    stat.save()
    stat.refresh_from_db()

    return stat


def get_pubg_stats_from_image(image_path: str, match_date: datetime) -> list[RecordResponse]:
    game_obj = get_by_name(name="PUBG")
    if not game_obj:
        raise ValidationError(errors=[{"error": "PUBG is not a valid game. Create it first."}])

    bounding_boxes = parse_image(image_path=image_path, reader=Reader(lang_list=["en"]))
    parsed_labels, victory = parse_labels(bounding_boxes=bounding_boxes)
    stats = get_stats_from_parsed_labels(parsed_labels=parsed_labels)

    game = GameResponse(**game_obj.__dict__)

    response: list[RecordResponse] = []
    for stat in stats:
        record_request = RecordRequest(
            game_id=game.id,
            victory=victory,
            date=match_date,
            name=str(stat[0]),
            kill=int(stat[1]),
            assist=int(stat[2]),
            death=int(stat[3]),
            point=int(stat[4]),
        )
        record = create_new_record(record_request=record_request)
        response.append(RecordResponse(**record.__dict__))
        stat_request = create_request(record=record)
        old = get_by_name_game(name=record.name, game_id=record.game.id)
        if not old:
            _ = create_new(stat_request=stat_request)
        else:
            new_request = update_request(old=old, current=stat_request)
            _ = create_new(stat_request=new_request)

    return response


def difference(old: Stat, new: Stat) -> LatestPerformanceResponse:
    result = LatestPerformanceResponse(
        name=new.name,
        game_id=new.game.id,
        total_assist=abs(new.total_assist - old.total_assist),
        total_death=abs(new.total_death - old.total_death),
        total_kill=abs(new.total_kill - old.total_kill),
        total_lost=abs(new.total_lost - old.total_lost),
        total_played=abs(new.total_played - old.total_played),
        total_point=abs(new.total_point - old.total_point),
        total_won=abs(new.total_won - old.total_won),
        valid_assist_match=abs(new.valid_assist_match - old.valid_assist_match),
        valid_death_match=abs(new.valid_death_match - old.valid_death_match),
        valid_kill_match=abs(new.valid_kill_match - old.valid_kill_match),
        valid_point_match=abs(new.valid_point_match - old.valid_point_match),
        created_at=new.created_at,
        updated_at=new.updated_at,
    )

    return result


def get_latest_performance(name: str, game: str) -> LatestPerformanceResponse:
    latest = Stat.objects.filter(name=name).latest("date")
    next_latest = Stat.objects.filter(name=name, date__lt=latest.date).order_by("date").first()

    if not next_latest:
        return LatestPerformanceResponse(**latest.__dict__.pop("date"))

    return LatestPerformanceResponse(**difference(old=next_latest, new=latest).model_dump())
