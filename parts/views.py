from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Part
from assets.models import Asset
from django.utils import timezone
from .forms import PartForm

# Create your views here.
def parts_all(request):
    parts = Part.objects.all()
    return render(request, 'parts/all.html', {'parts' : parts})

def parts_list(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    query_parts = Part.objects.filter(assigned_asset_id=asset.pk).order_by('created_date')
    return render(request, 'parts/list.html', {'parts' : query_parts, 'asset' : asset})

def parts_detail(request, pk, pk2):
    part = get_object_or_404(Part, pk=pk2)
    asset = get_object_or_404(Asset, id=part.assigned_asset_id)
    return render(request, 'parts/detail.html', {'part' : part, 'asset': asset})

def parts_new(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save()
            return redirect('parts_list', pk)
    else:
        form = PartForm()
    return render(request, 'parts/new.html', {'form' : form, 'asset' : asset})

def parts_edit(request, pk, pk2):
    part = get_object_or_404(Part, pk=pk2)
    asset = get_object_or_404(Asset, id=part.assigned_asset_id)
    if request.method == "POST":
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            part = form.save()
            return redirect('parts_list', asset.pk)
    else:
        form = PartForm(instance=part)
    return render(request, 'parts/edit.html', {'form' : form, 'part' : part})

class parts_delete(DeleteView):
    model = Part
    template_name = "parts/delete.html"

    def get_object(self):
        pk2 = self.kwargs['pk2']
        part = get_object_or_404(Part, pk=pk2)
        return part

    success_url = reverse_lazy('home') 
