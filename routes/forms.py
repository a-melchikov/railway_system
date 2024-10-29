from django import forms
from .models import Route


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = [
            "owner_station",
            "train",
            "departure_station",
            "arrival_station",
            "departure_time",
            "arrival_time",
            "crew",
        ]
        widgets = {
            "owner_station": forms.Select(attrs={"class": "form-control"}),
            "train": forms.Select(attrs={"class": "form-control"}),
            "departure_station": forms.Select(attrs={"class": "form-control"}),
            "arrival_station": forms.Select(attrs={"class": "form-control"}),
            "departure_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "arrival_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "crew": forms.Select(attrs={"class": "form-control"}),
        }
