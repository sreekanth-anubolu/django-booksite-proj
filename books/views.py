from authors.models import Author
from django.shortcuts import render, redirect

# Create your views here.

from . import models
from . import forms

def books_view(request):
    # Retriving the data from Authors Model/tables
    books = models.Books.objects.all()
    # Connected to DB
    # performed select operation on the authors_author table
    # Retrived records
    context = {
        "books": books
    }
    return render(request, "books_view.html", context)



def books_create(request):
    books_form = forms.BooksForm()
    context = {
        "form": books_form
    }
    return render(request, "create_book.html", context)


def books_create_post(request):
    data = request.POST
    title = data.get("title")
    author = data.get("author")
    stock = data.get("stock")
    desc = data.get("desc")
    book = models.Books()
    author = Author.objects.get(id=int(author))
    book.author = author
    book.stock = stock
    book.title = title
    book.desc = desc
    book.save()
    return redirect("books-list-view")
