from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {"books": books})


def create(request):
    book_form = BookForm(request.POST or None)
    if book_form.is_valid():
        book_form.save()
        return redirect("Books:index")

    return render(request, "books/create.html", {"form": book_form})


def update(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_form = BookForm(request.POST or None, instance=book)
    if book_form.is_valid():
        book_form.save()
        return redirect("Books:index")

    return render(request, "books/edit.html", {"form": book_form, "book_id": book.pk})


def delete(request, book_id):
    Book.objects.get(pk=book_id).delete()
    return redirect("Books:index")
