from django.conf.urls import url
from .views import CharacterSelect, CharacterCreate, SelectClass

urlpatterns = [
    url(r'^select/', CharacterSelect.as_view()),
    url(r'^create/', CharacterCreate.as_view()),
    url(r'^class', SelectClass.as_view())
]