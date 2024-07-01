import os

from easyocr import Reader


async def parse_image(
    image_path: str, reader: Reader
) -> list[list[list[int | float] | str | float]]:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"{image_path} does not exist.")

    result: list[list[list[int | float] | str | float]] = reader.readtext(
        image=image_path
    )

    return result
