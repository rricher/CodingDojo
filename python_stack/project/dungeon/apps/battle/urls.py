from django.conf.urls import url
from .views import Intro, Battle, Attack, Attacked, Cleared, Death

urlpatterns = [
    url(r'^$', Battle.as_view()),
    url(r'^intro/', Intro.as_view()),
    url(r'^attack/', Attack.as_view()),
    url(r'^attacked/', Attacked.as_view()),
    url(r'^cleared/', Cleared.as_view()),
    url(r'^death/', Death.as_view()),
]