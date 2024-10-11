from django import forms
from .models import Station, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["country", "city", "street", "house", "apartment"]


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ["name", "tax_id"]
