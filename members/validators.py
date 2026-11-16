from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_birthday_not_in_future(value):
    if value > timezone.localdate():
        raise ValidationError('Birthday cannot be in the future.')


def validate_stage_name(value):
    if all(char.isspace() or char.isdigit() for char in value):
        raise ValidationError('The stage name cannot consist only of spaces or digits.')
