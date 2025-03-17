from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Author
from .forms import AuthorForm


def author_register(request):
    authors = Author.objects.all().order_by("first_name")
    
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor(a) cadastrado(a) com sucesso!')
            return redirect("/authors/")
    else:
        form = AuthorForm()

    return render(request, "authors.html", {"form": form, "authors": authors})

def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            if 'photo-clear' in request.POST:
                author.photo.delete()
            form.save()
            messages.success(request, 'Autor(a) editado(a) com sucesso!')
            return redirect('/authors/')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors.html', {'form': form, 'author': author})