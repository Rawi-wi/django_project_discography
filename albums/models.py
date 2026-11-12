from django.db import models

# Create your models here.

class Album(models.Model):
    ALBUM_TYPES = [
        ('mini', 'Mini Album'),
        ('full', 'Full Album'),
        ('single', 'Single'),
        ('repackage', 'Repackage'),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    release_date = models.DateField(verbose_name="Release Date", help_text="The official release date. It can't be in the future.")
    album_type = models.CharField(max_length=20, choices=ALBUM_TYPES, verbose_name="Album Type")
    cover_url = models.URLField(blank=True, verbose_name="Cover URL", help_text="Optional. A link to an image of the album cover.")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        ordering = ['-release_date']
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.title