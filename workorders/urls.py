from django.urls import path
from . import views
urlpatterns = [
    path('', views.workorders_list, name ='workorders_list'),
]