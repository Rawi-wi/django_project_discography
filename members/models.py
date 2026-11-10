from django.db import models

# Create your models here.

from django.db import models

class Member(models.Model):
    stage_name = models.CharField(max_length=100, unique=True, verbose_name="Stage Name", help_text="Unique stage name.")
    birth_name = models.CharField(max_length=100, verbose_name="Birth Name")
    position = models.CharField(max_length=100, blank=True, verbose_name="Position", help_text="e.g., Leader, Dancer, Vocalist")
    birthday = models.DateField(verbose_name="Birthday")
    image_url = models.URLField(blank=True, verbose_name="Image URL")
    bio = models.TextField(blank=True, verbose_name="Bio")

    class Meta:
        ordering = ['stage_name']
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.stage_name
