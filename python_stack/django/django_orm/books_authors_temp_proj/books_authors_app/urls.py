from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('authors', views.authors),
    path('books/<int:id>', views.show_book),
    path('authors/<int:id>', views.show_author),
]
