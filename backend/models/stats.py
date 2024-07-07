from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    ForeignKey,
    Index,
    IntegerField,
    Manager,
)

from backend.models.base import Base
from backend.models.games import Game


class Stat(Base):
    name = CharField(max_length=100, null=False)
    game = ForeignKey(to=Game, on_delete=CASCADE)
    date = DateField()
    total_played = IntegerField(default=0)
    total_won = IntegerField(default=0)
    total_lost = IntegerField(default=0)
    total_assist = IntegerField(default=0)
    total_death = IntegerField(default=0)
    total_kill = IntegerField(default=0)
    total_point = IntegerField(default=0)
    valid_assist_match = IntegerField(default=0)
    valid_death_match = IntegerField(default=0)
    valid_kill_match = IntegerField(default=0)
    valid_point_match = IntegerField(default=0)

    class Meta:
        indexes = [
            Index(fields=["name"]),
            Index(fields=["date"]),
            Index(fields=["name", "game_id"]),
            Index(fields=["created_at"]),
            Index(fields=["updated_at"]),
        ]
        objects: Manager["Stat"]
