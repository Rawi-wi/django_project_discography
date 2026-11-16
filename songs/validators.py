from django.core.exceptions import ValidationError

MIN_SONG_LENGTH = 1
MAX_SONG_LENGTH = 1200

MIN_TRACK_NUMBER = 1
MAX_TRACK_NUMBER = 100

MIN_SEARCH_LENGTH = 2


def validate_song_length(value):
    if value < MIN_SONG_LENGTH or value > MAX_SONG_LENGTH:
        raise ValidationError(
            f"Song length must be between {MIN_SONG_LENGTH} and {MAX_SONG_LENGTH} seconds.",
            code="invalid_length",
        )


def validate_track_numbers(value):
    if value < MIN_TRACK_NUMBER or value > MAX_TRACK_NUMBER:
        raise ValidationError(
            f"Track number must be between {MIN_TRACK_NUMBER} and {MAX_TRACK_NUMBER}.",
            code="invalid_number",
        )


def validate_search_length(value):
    if len(value) < MIN_SEARCH_LENGTH:
        raise ValidationError(
            f"Please enter at least {MIN_SEARCH_LENGTH} characters to search.",
            code="invalid_search",
        )
