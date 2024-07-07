from backend.models.records import Record
from backend.models.stats import Stat
from backend.responses.stats import StatRequest


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
        stat = Stat.objects.get(name=name, game_id=game_id)

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
