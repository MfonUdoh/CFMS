from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import WorkOrder
from assets.models import Asset
from django.utils import timezone
from .forms import WorkOrderForm

# Create your views here.
def workorders_list(request):
    query_orders = WorkOrder.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workorders/list.html', {'orders' : query_orders})

def workorders_detail(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    asset = get_object_or_404(Asset, id=order.assigned_asset_id)
    return render(request, 'workorders/detail.html', {'order' : order, 'asset' : asset})

def workorders_new(request):
    if request.method == "POST":
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('workorders_detail', pk=order.pk)
    else:
        form = WorkOrderForm()
    return render(request, 'workorders/new.html', {'form' : form})

def workorders_edit(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    if request.method == "POST":
        form = WorkOrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('workorders_detail', pk=order.pk)
    else:
        form = WorkOrderForm(instance=order)
    return render(request, 'workorders/edit.html', {'form' : form, 'order' : order})

class workorders_delete(DeleteView):
    model = WorkOrder
    template_name = "workorders/delete.html"
    success_url = reverse_lazy('workorders_list')
