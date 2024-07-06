from datetime import datetime
from typing import Any

from django.db.models import DateTimeField, Model
from django.utils import timezone


class AutoDateTimeField(DateTimeField):  # type: ignore[type-arg]
    def pre_save(self, model_instance: Model, add: Any) -> datetime:
        return timezone.now()


class Base(Model):
    created_at = DateTimeField(editable=False, default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True
