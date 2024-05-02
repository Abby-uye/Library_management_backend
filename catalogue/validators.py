
from django.core.validators import ValidationError


def validate_file_size(file):
    max_size = 100
    if file.size > max_size * 1024:
        raise ValidationError(f"image size must be less than{max_size} kb")
