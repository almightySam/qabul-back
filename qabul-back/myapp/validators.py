from django.core.exceptions import ValidationError


def validate_non_negative(value):
    """Kvota manfiy bo‘lishini oldini oladi."""
    if value < 0:
        raise ValidationError("Kvota manfiy bo‘lishi mumkin emas!")
