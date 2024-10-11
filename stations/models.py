from django.db import models
from addresses.models import Address


class Station(models.Model):
    name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=12, unique=True, db_index=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
