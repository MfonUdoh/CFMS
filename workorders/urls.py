from django.urls import path
from . import views
urlpatterns = [
    path('list', views.workorders_list, name ='workorders_list'),
    path('<int:pk>', views.workorders_detail, name='workorders_detail'),
]