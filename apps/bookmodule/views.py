from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Q
from .models import Publisher, Book

def index(request):
    return render(request, "bookmodule/index.html")


def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html", {"bookId": bookId})


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def lab9_task6(request): # Lab9-Task 6
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/publisherFilteredBooks.html', {'publishers': publishers})