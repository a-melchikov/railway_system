from django.db import models


class TrainType(models.Model):
    type_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Тип поезда",
    )

    def __str__(self):
        return self.type_name
