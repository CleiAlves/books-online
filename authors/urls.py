from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('register/', views.author_register, name='author_register'),
]