from django.db import models

from train_types.models import TrainType
from stations.models import Station


class Train(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название",
    )
    train_type = models.ForeignKey(
        TrainType,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        verbose_name="Тип поезда",
    )
    stations = models.ManyToManyField(
        Station,
        related_name="trains",
        verbose_name="Станции",
    )

    def __str__(self):
        return self.name
