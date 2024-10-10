from django.db import models

from routes.models import Route
from stations.models import Station


class RouteDetail(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop_number = models.IntegerField()
    stop_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    class Meta:
        unique_together = ("route", "stop_number")
