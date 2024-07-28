from pydantic import BaseModel, computed_field


class Point(BaseModel):
    x: float
    y: float


class Row(Point):
    label: str
    confidence: float


class BoundingBox(BaseModel):
    points: list[Point]
    label: str
    confidence: float
    center: Point

    @computed_field  # type: ignore[prop-decorator]
    @property
    def left_bottom(self) -> Point:
        return self.points[0]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def left_top(self) -> Point:
        return self.points[1]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def right_bottom(self) -> Point:
        return self.points[2]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def right_top(self) -> Point:
        return self.points[3]

    def rows(self) -> list[Row]:
        return [Row(x=self.center.x, y=self.center.y, label=self.label, confidence=self.confidence)]
