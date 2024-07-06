from django.db.models import CharField

from backend.models.base import Base


class Game(Base):
    name = CharField(max_length=100, null=False, unique=True)
