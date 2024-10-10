from django.db import models

from train_types.models import TrainType


class Train(models.Model):
    name = models.CharField(max_length=255, unique=True)
    train_type = models.ForeignKey(TrainType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
