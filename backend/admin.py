from django.contrib import admin

from backend.models.games import Game
from backend.models.images import ImagePath
from backend.models.records import Record
from backend.models.stats import Stat

admin.site.register(Game)
admin.site.register(Record)
admin.site.register(Stat)
admin.site.register(ImagePath)
