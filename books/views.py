from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book
from .forms import BookForm
from authors.models import Author


def home(request):
    books = Book.objects.all().order_by('title')
    authors = Author.objects.all().order_by('first_name')
    return render(request, 'home.html', {'books': books, 'authors': authors})


def book_register(request):
    books = Book.objects.all()

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect("/")
    else:
        form = BookForm()

    return render(request, "book_register.html", {"form": form, "books": books})


def book_details(request, id):
    book = Book.objects.get(id=id)
    authors = Author.objects.all().order_by('first_name')
    return render(request, "book_details.html", {"book": book, "authors": authors})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            if 'cover_image-clear' in request.POST:
                book.cover_image.delete()
            form.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect(f'/book_details/{book_id}/')
    else:
        form = BookForm(instance=book)
    authors = Author.objects.all()
    return render(request, 'book_details.html', {'form': form, 'book': book, 'authors': authors})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Livro deletado com sucesso!')
        return redirect('/')
    return render(request, 'book_details.html', {'book': book})
