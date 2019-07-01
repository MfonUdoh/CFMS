from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Part, Asset
from django.utils import timezone
from .forms import PartForm

# Create your views here.
def parts_list(request, pk):
    asset = Asset.objects.get_object_or_404(pk=pk)
    query_parts = Part.objects.filter(assigned_asset=asset.name).order_by('created_date')
    return render(request, 'parts/list.html', {'parts' : query_parts, 'asset' : asset})

def parts_detail(request, pk2):
    part = get_object_or_404(Part, pk=pk2)
    asset = Asset.objects.get_object_or_404(assigned_asset=part.assigned_asset.name)
    return render(request, 'parts/detail.html', {'part' : part, 'asset': asset})

def parts_new(request):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save()
            asset = Asset.objects.get_object_or_404(assigned_asset=part.assigned_asset.name)
            return redirect('parts_detail', pk=part.pk)
    else:
        form = PartForm()
    return render(request, 'parts/new.html', {'form' : form})

def parts_edit(request, pk2):
    part = get_object_or_404(Part, pk=pk2)
    if request.method == "POST":
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            part = form.save()
            return redirect('parts_detail', pk=part.pk)
    else:
        form = PartForm(instance=part)
    return render(request, 'parts/edit.html', {'form' : form, 'part' : part})

class parts_delete(DeleteView):
    model = Part
    template_name = "parts/delete.html"
    pk2 = self.kwargs['pk']
    success_url = reverse_lazy('parts_list', pk=pk2)
