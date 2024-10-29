from django import forms
from .models import Personnel


class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ["station", "person_tax_id", "full_name", "position", "crew"]
        widgets = {
            "station": forms.Select(attrs={"class": "form-control"}),
            "person_tax_id": forms.TextInput(
                attrs={"class": "form-control", "maxlength": 12}
            ),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-control"}),
            "crew": forms.Select(attrs={"class": "form-control"}),
        }
