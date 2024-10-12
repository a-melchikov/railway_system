from django import forms
from .models import Train


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ["name", "train_type", "stations"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "train_type": forms.Select(attrs={"class": "form-control"}),
            "stations": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
