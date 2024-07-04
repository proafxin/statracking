from ninja import NinjaAPI

from statracking.routers.game import router as game_router
from statracking.routers.track import router as tracking_router

api = NinjaAPI(title="Stats Tracking")
api.add_router(prefix="/track", router=tracking_router)
api.add_router(prefix="/game", router=game_router)


@api.get("/")
async def hello() -> str:
    return "hello"
