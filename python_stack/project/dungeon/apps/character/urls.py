from django.conf.urls import url
from .views import CharacterSelect, CharacterCreate

urlpatterns = [
    url(r'^select/', CharacterSelect.as_view()),
    url(r'^create/', CharacterCreate.as_view())
]