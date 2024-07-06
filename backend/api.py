from ninja import NinjaAPI

from backend.views.games import router as game_router

api = NinjaAPI(title="Stats Tracking", csrf=True)
api.add_router(prefix="/game", router=game_router)
