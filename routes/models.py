from django.db import models
from django.utils import timezone

from stations.models import Station
from trains.models import Train
from crew_directory.models import CrewDirectory


class Route(models.Model):
    owner_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="owned_routes",
        db_index=True,
        verbose_name="Станция-владелец",
    )
    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Поезд",
    )
    departure_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="departing_routes",
        db_index=True,
        verbose_name="Станция отправления",
    )
    arrival_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="arriving_routes",
        db_index=True,
        verbose_name="Станция прибытия",
    )
    departure_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время отправления",
    )
    arrival_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время прибытия",
    )
    crew = models.ForeignKey(
        CrewDirectory,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="Бригада",
    )

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"

    def __str__(self):
        return f"{self.train.name} - {self.departure_station.name} to {self.arrival_station.name}"
