from django.db import models
from albums.models import Album
from members.models import Member
from .validators import validate_song_length

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', verbose_name="Album")
    track_number = models.PositiveIntegerField(verbose_name="Track Number", help_text="Must be unique within the album")
    length_in_seconds = models.PositiveIntegerField(validators=[validate_song_length], verbose_name="Length in Seconds", help_text="Length in seconds (e.g. 185 for 3:05)")
    credited_members = models.ManyToManyField(Member, blank=True, related_name='songs', verbose_name="Credited Members",help_text="Tick everyone credited on this song; leave empty if unknown")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        ordering = ['album', 'track_number']
        verbose_name_plural = 'Songs'
        constraints = [
            models.UniqueConstraint(fields=['album', 'track_number'], name='unique_album_track')
        ]

    def __str__(self):
        return f"{self.title} ({self.album.title})"