from django.db import IntegrityError

from backend.models.images import ImagePath


def is_duplicate(image_path: str) -> bool:
    try:
        ImagePath.objects.get(path=image_path)
        return True
    except ImagePath.DoesNotExist:
        return False


def create(image_path: str) -> ImagePath:
    image_path_obj = ImagePath(path=image_path)
    try:
        image_path_obj.save()
        image_path_obj.refresh_from_db()

        return image_path_obj
    except IntegrityError:
        raise
