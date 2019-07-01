from django.urls import path
from .views import *
urlpatterns = [
    path('list', workorders_list, name ='workorders_list'),
    path('<int:pk>', workorders_detail, name='workorders_detail'),
    path('new', workorders_new, name='workorders_new'),
    path('<int:pk>/edit', workorders_edit, name='workorders_edit'),
    path('<int:pk>/delete', workorders_delete.as_view(), name='workorders_delete'),
]