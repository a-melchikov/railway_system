from django.db import models

from stations.models import Station
from trains.models import Train
from crew_directory.models import CrewDirectory


class Route(models.Model):
    owner_station = models.ForeignKey(
        Station, related_name="owner_station", on_delete=models.SET_NULL, null=True
    )
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    departure_station = models.ForeignKey(
        Station, related_name="departure_station", on_delete=models.SET_NULL, null=True
    )
    arrival_station = models.ForeignKey(
        Station, related_name="arrival_station", on_delete=models.SET_NULL, null=True
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ForeignKey(CrewDirectory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.departure_station} to {self.arrival_station}"
