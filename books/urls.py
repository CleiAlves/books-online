from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
    path('book_register/', views.book_register, name='book_register'),
    path('book_details/<int:id>/', views.book_details, name='book_details'),
    path('book_edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book_delete/<int:book_id>/', views.delete_book, name='book_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)