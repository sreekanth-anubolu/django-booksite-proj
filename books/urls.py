from django.urls import path

from . import views

urlpatterns = [
    # ex: /books/
    path('', views.books_view, name="books-list-view"),
    path('create/', views.books_create),
    path('create-book/', views.books_create_post),
]