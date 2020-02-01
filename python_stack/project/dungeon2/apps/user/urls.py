from django.conf.urls import url
from .views import Index, Login, Register, Logout, CreateDB

urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^register/', Register.as_view()),
    url(r'^logout/', Logout.as_view()),
    url(r'^createdb/', CreateDB.as_view()),
]