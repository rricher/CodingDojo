from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:building>', views.process_money),
]

