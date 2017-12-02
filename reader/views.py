from django.shortcuts import render

# Create your views here.
from reader.models import Book


def homepage(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'base.html', context)


def book_details(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id),
    }
    return render(request, 'detail.html', context)
