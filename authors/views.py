from django.shortcuts import render
from .models import Author


def author_register(request):
    if request.method == 'GET':
        authors = Author.objects.all().order_by('first_name')
        return render(request, 'authors.html', {'authors': authors})
