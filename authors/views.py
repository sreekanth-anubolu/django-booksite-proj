from django.shortcuts import render

from . import models
from . import forms

# Create your views here.


def author_view(request):
    # Retriving the data from Authors Model/tables
    authors = models.Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "authors_view.html", context)



def create_author(request):
    auth_form = forms.AuthorForm()
    context = {
        "form": auth_form
    }
    return render(request, "create_author.html", context)


def create_author_post(request):
    data = request.POST

    fn = data.get("first_name")
    ln = data.get("last_name")

    author = models.Author()
    author.first_name = fn
    author.last_name = ln
    author.save()

    auth_form = forms.AuthorForm()
    context = {
        "form": auth_form
    }
    return render(request, "create_author.html", context)

