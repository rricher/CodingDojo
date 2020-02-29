from django.conf.urls import url
from apps.user.views import Index, Login, Register, Logout
urlpatterns = [
    url(r'^$', Index.as_view()),
    url(r'^login/$', Login.as_view()),
    url(r'^register/$', Register.as_view()),
    url(r'^logout/', Logout.as_view()),
]
