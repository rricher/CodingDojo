from django.conf.urls import url
from apps.user.views import Index, Login, Register
urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^register/$', Register.as_view(), name="register"),
]
