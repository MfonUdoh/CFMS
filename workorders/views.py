from django.shortcuts import render, get_object_or_404
from .models import WorkOrder
from django.utils import timezone
from .forms import WorkOrderForm

# Create your views here.
def workorders_list(request):
    query_orders = WorkOrder.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'workorders/workorders_list.html', {'orders' : query_orders})

def workorders_detail(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    return render(request, 'workorders/workorders_detail.html', {'order' : order})

def workorders_new(request):
    form = WorkOrderForm()
    return render(request, 'workorders/workorders_new.html', {'form' : form})

def workorders_delete(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    return render(request, 'workorders/workorders_delete.html', {'order':order})

def workorders_edit(request, pk):
    order = get_object_or_404(WorkOrder, pk=pk)
    return render(request, 'workorders/workorders_edit.html', {'order' : order})