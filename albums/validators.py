from datetime import date
from django.core.exceptions import ValidationError


def validate_release_date_not_in_future(value):
    if value > date.today():
        raise ValidationError('The release date cannot be in the future.')


def validate_title_length(value):
    if len(value.strip()) < 2:
        raise ValidationError('The title must be at least 2 characters long.')


def validate_cover_url_is_image(value):
    if not value.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
        raise ValidationError(
            'The URL should point to an image (.jpg, .jpeg, .png, .webp or .gif).'
        )