from django.shortcuts import render, redirect

# Create your views here.
from reader.epub_info import get_epub_info
from reader.forms import BookForm
from reader.models import Book, Author


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


def epub_read(request, book_id):
    context = {
        'book': Book.objects.get(pk=book_id),
    }

    return render(request, 'read.html', context)


def book_upload_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            metadata = get_epub_info(book.document)
            book.title = metadata.get('title')
            author = metadata.get('creator')
            author = str(author).split()
            book.author = Author.objects.create(first_name=author[0], last_name=author[1])
            book.description = metadata.get('description')
            if metadata.get('date') is not 'none':
                if len(str(metadata.get('date'))) > 10:
                    book.pub_date = metadata.get('date')
            book.save()
            return redirect('homepage')
    else:
        form = BookForm()
    return render(request, 'simple_upload.html', {
        'form': form
    })
