from ninja import NinjaAPI

from backend.views.game import router as game_router
from backend.views.record import router as record_router

api = NinjaAPI(title="Stats Tracking", csrf=True)
api.add_router(prefix="/game", router=game_router)
api.add_router(prefix="/record", router=record_router)
