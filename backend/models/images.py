from django.db.models import CharField

from backend.models.base import Base


class ImagePath(Base):
    path = CharField(max_length=300, unique=True)
