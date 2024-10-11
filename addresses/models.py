from django.db import models


class Address(models.Model):
    country = models.CharField(
        max_length=100,
        verbose_name="Страна",
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
    )
    street = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Улица",
    )
    house = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Дом",
    )
    apartment = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Квартира",
    )

    def __str__(self):
        return f"{self.street or ''} {self.house or ''}, {self.city}, {self.country}"
