from django.db.models import CharField, Index

from backend.models.base import Base


class Game(Base):
    name = CharField(max_length=100, null=False, unique=True)

    class Meta:
        indexes = [Index(fields=["name", "created_at", "updated_at"])]
