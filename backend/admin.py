from django.contrib import admin

from backend.models.games import Game
from backend.models.records import Record

admin.site.register(Game)
admin.site.register(Record)
