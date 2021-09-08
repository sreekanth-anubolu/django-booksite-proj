from django.urls import path

from . import views

urlpatterns = [
    # ex: /authors/
    path('', views.author_view),
    path('create/', views.create_author),
    path('create-author/', views.create_author_post),
]