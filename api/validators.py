from django.core.exceptions import ValidationError


def GreaterThanZeroValidator(value):

    if value <= 0:
        raise ValidationError("The value must be > 0!")
