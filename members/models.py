from django.db import models

from members.validators import validate_birthday_not_in_future, validate_stage_name


# Create your models here.

class Member(models.Model):
    stage_name = models.CharField(
        validators=[validate_stage_name],
        max_length=100,
        unique=True,
        verbose_name="Stage Name",
        help_text="Unique stage name."
    )
    birth_name = models.CharField(
        max_length=100,
        verbose_name="Birth Name"
    )
    position = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Position",
        help_text="e.g., Leader, Dancer, Vocalist"
    )
    birthday = models.DateField(
        validators=[validate_birthday_not_in_future],
        verbose_name="Birthday"
    )
    image_url = models.URLField(
        blank=True,
        verbose_name="Image URL"
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Bio"
    )

    class Meta:
        ordering = ['stage_name']

    def __str__(self):
        return self.stage_name
