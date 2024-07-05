from django.db.models import DateTimeField, Model
from django.utils import timezone


class AutoDateTimeField(DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Base(Model):
    created_at: DateTimeField = DateTimeField(editable=False, default=timezone.now)
    updated_at: DateTimeField = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True
