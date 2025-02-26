from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Author
from .forms import AuthorForm


def author_register(request):
    authors = Author.objects.all()
    
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor(a) cadastrado(a) com sucesso!')
            return redirect("/authors/")
    else:
        form = AuthorForm()

    return render(request, "authors.html", {"form": form, "authors": authors})