from datetime import datetime

from ninja import Schema


class BaseRequest(Schema):
    pass


class BaseResponse(BaseRequest):
    created_at: datetime
    updated_at: datetime
