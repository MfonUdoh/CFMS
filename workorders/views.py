from django.shortcuts import render

# Create your views here.
def workorders_list(request):
    return render(request, 'workorders/workorders_list.html', {})