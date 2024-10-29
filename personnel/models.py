from django.db import models
from stations.models import Station
from positions.models import Position
from crew_directory.models import CrewDirectory


class Personnel(models.Model):
    station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Вокзал",
    )
    person_tax_id = models.CharField(
        max_length=12,
        primary_key=True,
        db_index=True,
        verbose_name="Идентификационный номер",
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name="Полное имя",
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        verbose_name="Должность",
    )
    crew = models.ForeignKey(
        CrewDirectory,
        on_delete=models.SET_NULL,
        null=True,
        db_index=True,
        verbose_name="Бригада",
    )

    def __str__(self):
        return self.full_name
