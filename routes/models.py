from django.db import models

from stations.models import Station
from trains.models import Train
from crew_directory.models import CrewDirectory


class Route(models.Model):
    owner_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="owned_routes", db_index=True
    )
    train = models.ForeignKey(Train, on_delete=models.CASCADE, db_index=True)
    departure_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="departing_routes",
        db_index=True,
    )
    arrival_station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="arriving_routes", db_index=True
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ForeignKey(CrewDirectory, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f"{self.train.name} - {self.departure_station.name} to {self.arrival_station.name}"
