from os.path import abspath, dirname, join

import pytest
from easyocr import Reader
from numpy import floating, integer

from statracking.parse import parse_image

cwd = dirname(abspath(__file__))


@pytest.mark.asyncio
async def test_parse() -> None:
    image_path = join(cwd, "1.jpg")
    reader = Reader(lang_list=["en"])
    result = await parse_image(image_path=image_path, reader=reader)

    assert isinstance(result, list)

    for box, text, confidence in result:
        assert isinstance(box, list)
        assert len(box) == 4
        for coordinate in box:
            assert isinstance(coordinate, list)
            assert len(coordinate) == 2
            assert isinstance(coordinate[0], integer) or isinstance(
                coordinate[0], floating
            )
            assert isinstance(coordinate[1], integer) or isinstance(
                coordinate[1], floating
            )

        assert isinstance(text, str)
        assert isinstance(confidence, float)

    image_path = join(cwd, "2.jpg")
    with pytest.raises(FileNotFoundError):
        await parse_image(image_path=image_path, reader=reader)
