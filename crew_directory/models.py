from django.db import models


class CrewDirectory(models.Model):
    crew_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.crew_name
