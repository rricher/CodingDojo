from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<int:id>', views.show_id),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/delete', views.delete),
]
