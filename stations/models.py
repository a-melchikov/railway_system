from django.db import models
from django.core.validators import RegexValidator
from addresses.models import Address


class Station(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    tax_id = models.CharField(
        max_length=12,
        unique=True,
        db_index=True,
        verbose_name="ИНН",
        validators=[
            RegexValidator(regex=r"^\d{12}$", message="ИНН должен состоять из 12 цифр.")
        ],
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        verbose_name="Адрес",
    )

    def __str__(self):
        return f"{self.name} (ИНН: {self.tax_id})"
