from django.db import models
from django.utils import timezone

from routes.models import Route
from stations.models import Station


class RouteDetail(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_number = models.IntegerField()
    stop_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(default=timezone.now)
    departure_time = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("route", "stop_number")
