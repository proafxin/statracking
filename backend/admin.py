from django.contrib import admin

from backend.models.game import Game
from backend.models.record import Record

admin.site.register(Game)
admin.site.register(Record)
