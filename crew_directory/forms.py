from django import forms
from .models import CrewDirectory


class CrewDirectoryForm(forms.ModelForm):
    class Meta:
        model = CrewDirectory
        fields = ["crew_name"]
