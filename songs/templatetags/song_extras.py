from django import template
from django.db.models import Sum
from songs.models import Song

register = template.Library()


@register.filter
def duration(value):
    try:
        total_seconds = int(value)
    except (TypeError, ValueError):
        return "-"

    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes}:{seconds:02d}"


@register.simple_tag
def album_total_duration(album):
    total = Song.objects.filter(album=album).aggregate(total=Sum('length_in_seconds'))['total']
    return duration(total or 0)
