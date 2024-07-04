from os.path import abspath, dirname, join

import pytest
from easyocr import Reader

from image_retrieval.box import BoundingBox, Point
from image_retrieval.parse import get_labels, parse_image
from image_retrieval.pubg.calculate import get_stats_from_parsed_labels, parse_labels

cwd = dirname(abspath(__file__))


@pytest.mark.asyncio
async def test_parse() -> None:
    image_path = join(cwd, "1.jpg")
    reader = Reader(lang_list=["en"])
    bounding_boxes = parse_image(image_path=image_path, reader=reader)

    for bounding_box in bounding_boxes:
        assert isinstance(bounding_box, BoundingBox)
        assert isinstance(bounding_box.left_bottom, Point)
        assert isinstance(bounding_box.left_top, Point)
        assert isinstance(bounding_box.right_bottom, Point)
        assert isinstance(bounding_box.right_top, Point)

    labels = get_labels(bounding_boxes=bounding_boxes)
    assert isinstance(labels, list)
    for label in labels:
        assert isinstance(label, str)

    parsed_labels = parse_labels(bounding_boxes=bounding_boxes)

    assert isinstance(parsed_labels, list)
    for stat in parsed_labels:
        assert isinstance(stat, str) | isinstance(stat, int)

    assert "Score" not in parsed_labels

    stats = get_stats_from_parsed_labels(parsed_labels=parsed_labels)
    assert isinstance(stats, list)
    for stat in stats:  # type: ignore[assignment]
        assert isinstance(stat, list)
        assert len(stat) == 5
        assert isinstance(stat[0], str)
        for x in stat[1:]:
            assert isinstance(x, int)

    image_path = join(cwd, "222.jpg")
    with pytest.raises(FileNotFoundError):
        parse_image(image_path=image_path, reader=reader)
