import os

import numpy as np
from easyocr import Reader

from image_retrieval.box import BoundingBox, Point


def parse_image(image_path: str, reader: Reader) -> list[BoundingBox]:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"{image_path} does not exist.")

    result = reader.readtext(image=image_path)

    bounding_boxes: list[BoundingBox] = []

    for corners, label, confidence in result:
        center = np.mean(corners, axis=0)
        points: list[Point] = []
        for corner in corners:
            point = Point(x=float(corner[0]), y=float(corner[1]))
            points.append(point)

        bounding_box = BoundingBox(
            points=points,
            confidence=confidence,
            label=label,
            center=Point(x=center[0], y=center[1]),
        )
        bounding_boxes.append(bounding_box)

    return bounding_boxes


def get_labels(bounding_boxes: list[BoundingBox]) -> list[str]:
    return [bounding_box.label for bounding_box in bounding_boxes]
