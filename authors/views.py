from django.shortcuts import render

# Create your views here.


def author_view(request):
    return render(request, "authors_view.html")
