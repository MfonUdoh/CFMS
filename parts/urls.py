from django.urls import path
from .views import *
urlpatterns = [
    path('list', parts_list, name ='parts_list'),
    path('<int:pk2>', parts_detail, name='parts_detail'),
    path('new', parts_new, name='parts_new'),
    path('<int:pk2>/edit', parts_edit, name='parts_edit'),
    path('<int:pk2>/delete', parts_delete.as_view(), name='parts_delete'),
]
