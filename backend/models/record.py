from django.db.models import CASCADE, CharField, ForeignKey, IntegerField

from backend.models.base import Base
from backend.models.game import Game


class Record(Base):
    game: ForeignKey = ForeignKey(to=Game, on_delete=CASCADE)
    name: CharField = CharField(max_length=100, null=False)
    kill: IntegerField = IntegerField(default=-1)
    assist: IntegerField = IntegerField(default=-1)
    death: IntegerField = IntegerField(default=-1)
    point: IntegerField = IntegerField(default=-1)
