from django import forms
from .models import RouteDetail


class RouteDetailForm(forms.ModelForm):
    class Meta:
        model = RouteDetail
        fields = [
            "route",
            "stop_number",
            "stop_station",
            "arrival_time",
            "departure_time",
        ]
        widgets = {
            "route": forms.Select(attrs={"class": "form-control"}),
            "stop_number": forms.NumberInput(attrs={"class": "form-control"}),
            "stop_station": forms.Select(attrs={"class": "form-control"}),
            "arrival_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "departure_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
        }
