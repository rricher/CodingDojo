from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wall', views.wall),
    path('logout', views.logout),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
]