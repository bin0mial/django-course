from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


@login_required
@permission_required(['books.view_book'])
def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {"books": books})


@login_required
@permission_required(['books.add_book'])
def create(request):
    book_form = BookForm(request.POST or None)
    if book_form.is_valid():
        book_form.save()
        return redirect("Books:index")

    return render(request, "books/create.html", {"form": book_form})


@login_required
@permission_required(['books.change_book'])
def update(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_form = BookForm(request.POST or None, instance=book)
    if book_form.is_valid():
        book_form.save()
        return redirect("Books:index")

    return render(request, "books/edit.html", {"form": book_form, "book_id": book.pk})


@login_required
@permission_required(['books.delete_book'])
def delete(request, book_id):
    Book.objects.get(pk=book_id).delete()
    return redirect("Books:index")
