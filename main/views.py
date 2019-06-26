from django.shortcuts import render

def homeview(request):
    return render(request, 'home.html')

def aboutview(request):
    return render(request, 'about.html')