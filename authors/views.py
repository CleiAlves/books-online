from django.shortcuts import render, redirect
from .models import Author
from django.contrib import messages


def author_register(request):
    if request.method == 'GET':
        authors = Author.objects.all().order_by('first_name')
        return render(request, 'authors.html', {'authors': authors})
    elif request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        photo = request.FILES.get('photo')
        author = Author(first_name=first_name, last_name=last_name, photo=photo)
        author.save()
        messages.success(request, 'Autor(a) cadastrado com sucesso!')
        return redirect("/authors/")
