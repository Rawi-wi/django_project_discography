from django.core.exceptions import ValidationError

MIN_SONG_LENGTH = 1
MAX_SONG_LENGTH = 600

def validate_song_length(value):
    if value < MIN_SONG_LENGTH or value > MAX_SONG_LENGTH:
        raise ValidationError(
            f"Song length must be between {MIN_SONG_LENGTH} and {MAX_SONG_LENGTH} seconds.",
            code="invalid_length",
        )