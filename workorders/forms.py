from django import forms
from .models import WorkOrder
from assets.models import Asset

class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('title', 'text', 'urgent', 'targetuser', 'assigned_asset')
