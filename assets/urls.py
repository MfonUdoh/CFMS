from django.urls import path, include
from .views import *
urlpatterns = [
    path('list', assets_list, name ='assets_list'),
    path('<int:pk>', assets_detail, name='assets_detail'),
    path('new', assets_new, name='assets_new'),
    path('<int:pk>/edit', assets_edit, name='assets_edit'),
    path('<int:pk>/delete', assets_delete.as_view(), name='assets_delete'),
    path('<int:pk>/parts/', include('parts.urls')),
]
