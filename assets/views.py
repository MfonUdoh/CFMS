from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Asset
from django.utils import timezone
from .forms import AssetForm

# Create your views here.
def workorders_list(request):
    query_orders = WorkOrder.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workorders/workorders_list.html', {'orders' : query_orders})

def workorders_detail(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    return render(request, 'workorders/workorders_detail.html', {'order' : order})

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
    return render(request, 'workorders/workorders_new.html', {'form' : form})

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
    return render(request, 'workorders/workorders_edit.html', {'form' : form, 'order' : order})
 
class workorders_delete(DeleteView):
    model = WorkOrder
    template_name = "workorders/workorders_delete.html"
    success_url = reverse_lazy('workorders_list')