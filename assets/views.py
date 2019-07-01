from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Asset
from django.utils import timezone
from .forms import AssetForm

# Create your views here.
def assets_list(request):
    query_assets = Asset.objects.order_by('created_date')
    return render(request, 'assets/list.html', {'assets' : query_assets})

def assets_detail(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, 'assets/detail.html', {'asset' : asset})

def assets_new(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save()
            return redirect('assets_detail', pk=asset.pk)
    else:
        form = AssetForm()
    return render(request, 'assets/new.html', {'form' : form})

def assets_edit(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save()
            return redirect('assets_detail', pk=asset.pk)
    else:
        form = AssetForm(instance=asset)
    return render(request, 'assets/edit.html', {'form' : form, 'asset' : asset})

class assets_delete(DeleteView):
    model = Asset
    template_name = "assets/delete.html"
    success_url = reverse_lazy('assets_list')
