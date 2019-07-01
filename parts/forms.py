from django import forms
from .models import Part
from assets.models import Asset

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name', 'description', 'quantity', 'assigned_asset')
