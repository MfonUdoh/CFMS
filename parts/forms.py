from django import forms
from .models import Part

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('name', 'description', 'assigned_asset', 'quantity')
