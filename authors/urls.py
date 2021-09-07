from django.urls import path

from . import views

urlpatterns = [
    # ex: /authors/
    path('', views.author_view, name='author_view'),
]