from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book_register/', views.book_register, name='book_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)