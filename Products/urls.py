from django.urls import path, include
from .views import index, prod_detail

urlpatterns = [
    path('', index),
    path('<str:slug>', prod_detail, name='prod_detail')
]