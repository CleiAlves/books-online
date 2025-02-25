from django.shortcuts import render

def author_register(request):
    return render(request, 'author_register.html')