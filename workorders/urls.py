from django.urls import path
from . import views
urlpatterns = [
    path('list', views.workorders_list, name ='workorders_list'),
    path('<int:pk>', views.workorders_detail, name='workorders_detail'),
    path('new', views.workorders_new, name='workorders_new'),
    path('<int:pk>/edit', views.workorders_edit, name='workorders_edit'),
    path('<int:pk>/delete', views.workorders_delete, name='workorders_delete'),
]