from django.db import models

# Create your models here.

from django.db import models
from albums.models import Album
from members.models import Member

class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', verbose_name="Album")
    track_number = models.PositiveIntegerField(verbose_name="Track Number")
    length_in_seconds = models.PositiveIntegerField(verbose_name="Length in Seconds")
    credited_members = models.ManyToManyField(Member, related_name='songs', verbose_name="Credited Members")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        ordering = ['album', 'track_number']
        verbose_name_plural = 'Songs'
        constraints = [
            models.UniqueConstraint(fields=['album', 'track_number'], name='unique_album_track')
        ]

    def __str__(self):
        return f"{self.title} ({self.album.title})"