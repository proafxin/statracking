from ninja import Field, Schema


class Record(Schema):
    name: str
    kill: int = Field(default=-1)
    assist: int = Field(default=-1)
    death: int = Field(default=-1)
    point: int = Field(default=-1)
