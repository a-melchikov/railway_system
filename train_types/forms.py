from django import forms
from .models import TrainType


class TrainTypeForm(forms.ModelForm):
    class Meta:
        model = TrainType
        fields = ["type_name"]
