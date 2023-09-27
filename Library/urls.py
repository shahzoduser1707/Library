from django.urls import path
from .views import *

urlpatterns = [
    path('category/all/', CategoryApiView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('update_category/<int:id>/', CategoryUpdateView.as_view()),
    path('author/all/', AuthorApiView.as_view()),
    path('author/create/', AuthorCreateApi.as_view()),
    path('update_author/<int:id>/', AuthorUpdateApi.as_view()),
    path('genre/all/', GenreApiView.as_view()),
    path('genre/create/', GenreCreateApi.as_view()),
    path('update_genre/<int:id>/', GenreUpdateApi.as_view()),
    path('book/all/', BookApiView.as_view()),
    path('book/create/', BookCreateApi.as_view()),
    path('book/<int:id>/', BookUpdateApi.as_view())
]