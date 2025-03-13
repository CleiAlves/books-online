from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'home.html', {'books': books})

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
    return render(request, "book_details.html", {"book": book})