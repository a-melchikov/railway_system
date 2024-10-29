from django.db import models
from django.utils import timezone

from routes.models import Route
from stations.models import Station


class RouteDetail(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        verbose_name="Маршрут",
    )
    stop_number = models.IntegerField(
        verbose_name="Номер остановки",
    )
    stop_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        verbose_name="Станция остановки",
    )
    arrival_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время прибытия",
    )
    departure_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Время отправления",
    )

    class Meta:
        unique_together = ("route", "stop_number")
        verbose_name = "Деталь маршрута"
        verbose_name_plural = "Детали маршрутов"

    def __str__(self):
        return f"Деталь маршрута {self.route.train.name}: Остановка {self.stop_number} на {self.stop_station.name}"
