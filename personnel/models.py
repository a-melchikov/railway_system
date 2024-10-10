from django.db import models

from stations.models import Station
from positions.models import Position
from crew_directory.models import CrewDirectory

class Personnel(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    person_tax_id = models.CharField(max_length=12, primary_key=True)
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    crew = models.ForeignKey(CrewDirectory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name