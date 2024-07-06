from django.db.models import CASCADE, CharField, ForeignKey, IntegerField

from backend.models.base import Base
from backend.models.game import Game


class Record(Base):
    game = ForeignKey(to=Game, on_delete=CASCADE)
    name = CharField(max_length=100, null=False)
    kill = IntegerField(default=-1)
    assist = IntegerField(default=-1)
    death = IntegerField(default=-1)
    point = IntegerField(default=-1)
