from django.db import models


class Position(models.Model):
    position_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название должности",
    )

    def __str__(self):
        return self.position_name
