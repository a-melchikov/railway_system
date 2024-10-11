from django.db import models

from train_types.models import TrainType
from stations.models import Station


class Train(models.Model):
    name = models.CharField(max_length=255, unique=True)
    train_type = models.ForeignKey(
        TrainType, on_delete=models.SET_NULL, null=True, db_index=True
    )
    stations = models.ManyToManyField(Station, related_name="trains")

    def __str__(self):
        return self.name
