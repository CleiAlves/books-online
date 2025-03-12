from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'home.html', {'books': books})